import os
os.system("cls")

names = ['Ali', 'Vali', 'Hasan', 'Husan']
name = 'Alisher Navoiy'
data = {
    "brand": "BYD",
    "model": "Chazor",
    "probeg": 50000,
    "narx": 20000
}

print(len(names))
print(len(name))
print(len(data))

class Book:
    def __init__(self, n, m, s, y):
        self.nom = n
        self.muallif = m
        self.sahifalar = s
        self.yil = y

    def __len__(self):
        return self.sahifalar

b1 = Book('Urush va Tinchlik', 'Lev Tolstoy', 750, 1745)
print(len(b1))