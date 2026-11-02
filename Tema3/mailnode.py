import argparse
import smtplib
import socketserver
from email.message import EmailMessage
from pathlib import Path

MAILBOX = Path("mailbox")


class SMTPHandler(socketserver.StreamRequestHandler):
    def reply(self, text):
        print("S:", text)
        self.wfile.write(f"{text}\r\n".encode())

    def read_line(self):
        return self.rfile.readline().decode().strip()

    def handle(self):
        sender = ""
        recipients = []
        self.reply("220 mailnode ready")
        while True:
            line = self.read_line()
            print("C:", line)
            command = line[:4].upper()
            if command in ("HELO", "EHLO"):
                self.reply("250 Hello")
            elif command == "MAIL":
                sender = line.split(":", 1)[1].split()[0].strip("<>")
                self.reply("250 OK")
            elif command == "RCPT":
                recipients.append(line.split(":", 1)[1].strip().strip("<>"))
                self.reply("250 OK")
            elif command == "DATA":
                self.reply("354 End data with <CRLF>.<CRLF>")
                self.save(sender, recipients)
                recipients = []
                self.reply("250 Message saved")
            elif command == "QUIT":
                self.reply("221 Bye")
                return
            else:
                self.reply("500 Unknown command")

    def save(self, sender, recipients):
        lines = []
        while True:
            line = self.read_line()
            if line == ".":
                break
            lines.append(line)
        MAILBOX.mkdir(exist_ok=True)
        number = len(list(MAILBOX.glob("*.txt"))) + 1
        path = MAILBOX / f"{number}.txt"
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Saved email from {sender} to {recipients} in {path}")


def serve(args):
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("0.0.0.0", args.port), SMTPHandler) as server:
        print(f"SMTP server running on port {args.port}")
        server.serve_forever()


def send(args):
    message = EmailMessage()
    message["From"] = args.sender
    message["To"] = args.recipient
    message["Subject"] = args.subject
    message.set_content(args.body)
    with smtplib.SMTP(args.host, args.port) as client:
        client.send_message(message)
    print("Email sent")


def inbox(args):
    for path in sorted(MAILBOX.glob("*.txt"), key=lambda p: int(p.stem)):
        print(f"--- Email {path.stem} ---")
        print(path.read_text(encoding="utf-8"))


parser = argparse.ArgumentParser()
commands = parser.add_subparsers(required=True)

serve_parser = commands.add_parser("serve")
serve_parser.add_argument("--port", type=int, default=2525)
serve_parser.set_defaults(run=serve)

send_parser = commands.add_parser("send")
send_parser.add_argument("--host", required=True)
send_parser.add_argument("--port", type=int, default=2525)
send_parser.add_argument("--from", dest="sender", required=True)
send_parser.add_argument("--to", dest="recipient", required=True)
send_parser.add_argument("--subject", required=True)
send_parser.add_argument("--body", required=True)
send_parser.set_defaults(run=send)

inbox_parser = commands.add_parser("inbox")
inbox_parser.set_defaults(run=inbox)

args = parser.parse_args()
args.run(args)