import os
os.system("cls")

class Student:
    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.grade = g

    def info(self):
        print(f"Student: {self.name}, age: {self.age}, grade: {self.grade}")



s1 = Student('Azizbek', 22, 4)
s1.info()


s2 = Student('Javohir', 19, 4)
s2.info()



# a = 5
# b = 4.5
# c = "SAlom"
# d = True
# l = [1,2,3]

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(l))
# print(type(s1))