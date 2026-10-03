import os
os.system("cls")


class Person:
    def __init__(self, i, y, m):
        self.ism = i
        self.yosh = y
        self.manzil = m
    def __str__(self):
        return f"{self.ism} {self.yosh} {self.manzil}"

    def __gt__(self, n):
        return self.yosh > n

    def __lt__(self, n):
        return self.yosh < n



class Employee:
    def __init__(self, i, y, m, s):
        self.ism = i
        self.yosh = y
        self.manzil = m
        self.maosh = s
    def __str__(self):
        return f"{self.ism} {self.yosh} {self.manzil}"

    def __gt__(self, n):
        return self.maosh > n
        # if self.maosh > n:
        #     print(f"{self.ism} ning maoshi {n}dan katta")
        # else:
        #     print(f"Maosh {n} dan kichik")

    def __lt__(self, n):
        return self.maosh < n

p1 = Person("Ali", 32, 'Toshkent')
e1 = Employee('Vali', 32, 'Navoiy', 500)

print(p1 > 50) # p1.yosh > 50
print(e1 > 50) # e1.maosh > 50

print(p1 < 50)
print(e1 < 50)