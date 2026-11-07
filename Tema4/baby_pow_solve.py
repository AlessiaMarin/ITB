import hashlib
import random
import string
import os
hash_funcs = {
    "sha256": hashlib.sha256,
    "md5": hashlib.md5,
    "keccak": hashlib.sha3_256,
}
algoritm = input("Introdu algoritmul: ").strip()
cypher=input("Introdu cifru: ")
sequence=input("Introdu secventa: ")
length=20-len(sequence)
print(length)

hash_func = hash_funcs[algoritm]
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for char in sequence:
    charset=charset.replace(char,"")
word_cyphered=""
while word_cyphered != cypher:
    word = "".join(random.sample(charset, length))
    word_cyphered = hash_func((word + sequence).encode()).hexdigest()
print(word)





