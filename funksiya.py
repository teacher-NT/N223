import os
os.system("cls")

# def say_hello():
#     print("Hello everyone!")

# say_hello()
# say_hello()
# say_hello()


# def func1():
#     pass


# def add_two_nums(a:int, b:int):
#     print(a + b)

# add_two_nums(4, 5)
# add_two_nums("Salom ", "Dunyo")


# def add_three_nums(a,b,c=0):
#     print(a+b+c)
# add_three_nums(3,4,5)
# add_three_nums(3,4)


# def avg(a,b,c) -> int:
#     d = (a+b+c)/3
#     return d

# n = avg(5,10,20)
# print(n)
# print(avg(2,4,7))

# def func1(a,b):
#     """
#     Bu funksiya 2 ta sonni yig'indi, ko'paytma, ayirma va
#     bo'linmasini qaytaradi.
#     """
#     return a+b, a*b, a-b, a/b

# print(func1(4,5))


# def sonlar(*a):
#     print(sum(a)/len(a))
#     n = 1
#     for i in a:
#         n *= i
#     print(n)
#     print(a)

# sonlar(2,3,4,5,6,7,8,9,1)


# def info(**talaba):
#     print(talaba)
#     print(talaba['ism'])

# info(ism='Ali', familya='Valiev', yosh=21)


# def add1(a,b):
#     return a+b
# print(add1(3,4))

# add2 = lambda a,b: a+b
# print(add2(4,5))


# names = ['Javohir', 'Muhammadrizo', 'Iftixor', 'SHahboz', 'SHahboz', 'Zayniddin', 'Azizbek']
# names2 = []
# for i in names:
#     if len(i) > 7:
#         names2.append(i)
# print(names2)

# def check(n):
#     return len(n) > 7
# names3 = list(filter(check, names))
# print(names3)

# names4 = list(filter(lambda n: len(n)>7, names))
# print(names4)


# names = ['javoHIR', 'MuhammadRIZO', 'IFTIxor', 'shaHBoz', 'ShaHbOz', 'zaYNiddin', 'aZizBEk']
# names2 = []
# for i in names:
#     k = i.title()
#     names2.append(k)
# print(names2)

# names3 = list(map(lambda i: i.title(), names))
# print(names3)