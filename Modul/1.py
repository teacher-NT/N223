import os
os.system("cls")

try:
    a = int(input("a = "))
    b = int(input("b = "))
    print(a / b)
except ValueError:
    print("Faqat butun son kiritish kerak!")
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas!")
else:
    print("Dastur xatosiz ishladi!")
finally:
    print("Chiqish")
    
# a = int(input("a = "))
# b = int(input("b = "))
# print(a / b)