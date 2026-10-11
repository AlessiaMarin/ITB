#Task 1
#"Blockchain" 625da44e4eaf58d61cf048d168aa6f5e492dea166d8bb54ec06c30de07db57e1
# Alessia.Marin.<SHA256("Blockchain") b4ddd7019075af438febabc41437d792658d90cc8e17060a000617954a346664

#Task 2 - chainybaby*2791

import hashlib
password = "8ec47631827329eb114714a20d9b3eeb8a9a4293bd5d6823af0632e8d4f30dfa"
def find(target):
    with open("../rockyou.txt", "rb") as f:
        for line in f:
            for word in line.split():
                if hashlib.sha256(word).hexdigest() == target:
                    return word.decode("utf-8", errors="replace")
    return None

print(find(password))


