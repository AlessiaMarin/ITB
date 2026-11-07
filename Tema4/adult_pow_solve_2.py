import hashlib
from itertools import permutations
from multiprocessing import Pool

charset = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn0123456789"


def cauta(args):
    primul, target = args
    rest = charset.replace(bytes([primul]), b"")
    sha256 = hashlib.sha256

    for combinatie in permutations(rest, 4):
        word = bytes((primul, *combinatie))
        if sha256(word).digest() == target:
            return word.decode()

    return None


if __name__ == "__main__":
    cypher = input("Introdu cifru: ").strip()
    target = bytes.fromhex(cypher)
    sarcini = [(c, target) for c in charset]

    with Pool() as pool:
        for rezultat in pool.imap_unordered(cauta, sarcini):
            if rezultat:
                print(rezultat)
                pool.terminate()
                break