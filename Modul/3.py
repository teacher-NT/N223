import os
os.system("cls")

import random as rd

print(rd.randint(1, 100))

ismlar = ['Iftixor', 'Javohir', 'SHahboz', 'Oybek', 'Zayniddin']

# n = rd.choice(ismlar)
# print(n)

# m = rd.choices(ismlar, k=3)
# print(m)

# w  = rd.sample(ismlar, k=3)
# print(w)

rd.shuffle(ismlar)
print(ismlar)