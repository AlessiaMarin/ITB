#Task 4
#euler totient - suma tututor numerelor pana la n care nu au niciun factor comun >1 cu n, gen pentru numere prime este exact n-1
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
et=(p-1)*(q-1)
print(et)
cheie=pow(e, -1, et)
print(cheie)