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
    
    def __add__(self, n):
        self.yosh += n

    def __sub__(self, n):
        self.yosh -= n


p1 = Person('Abdulla', 21, 'Buxoro shaxri')
print(p1)
print(p1 > 30)
print(p1 < 30)
# p1 + 2
# p1 - 10
print(p1)
# print(4 > 3)