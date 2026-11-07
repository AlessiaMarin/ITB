import hashlib
from itertools import permutations

cypher = input("Introdu cifru: ").strip()

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn0123456789"

for combinatie in permutations(charset, 5):
    word = "".join(combinatie)
    word_cyphered = hashlib.sha256(word.encode()).hexdigest()

    if word_cyphered == cypher:
        print(word)
        break