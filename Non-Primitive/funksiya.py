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

def func1(a,b):
    """
    Bu funksiya 2 ta sonni yig'indi, ko'paytma, ayirma va
    bo'linmasini qaytaradi.
    """
    return a+b, a*b, a-b, a/b

print(func1(4,5))
