from random import choice
import os
os.system("cls")

def bosh_doska_hosil_qil():
    doska = [
        1,2,3,
        4,5,6,
        7,8,9
    ]
    return doska
    
def doskani_korsat(doska):
    print("+-----------+")
    for i in range(len(doska)):
        print("|", doska[i], end= " ")
        if i in [2,5,8]:
            print("|\n+-----------+")

def bosh_maydonlar(doska):
    res = []
    for i in range(1,10):
        if i in doska:
            res.append(i)
    return res    
   
def foydalanuvchi_tanlasin(doska):
    if not bosh_maydonlar(doska):
        return
    n = int(input("Katak tanlang: "))
    if n not in doska:
        print("Iltimos faqat bo'sh katak tanlang!")
        foydalanuvchi_tanlasin(doska)
    else:
        doska[n-1] = "O"
 
def golib_bormi(doska, belgi):
    if doska[0]==doska[1]==doska[2]==belgi:
        return True
    elif doska[3]==doska[4]==doska[5]==belgi:
        return True
    elif doska[6]==doska[7]==doska[8]==belgi:
        return True
    elif doska[0]==doska[3]==doska[6]==belgi:
        return True
    elif doska[1]==doska[4]==doska[7]==belgi:
        return True
    elif doska[2]==doska[5]==doska[8]==belgi:
        return True
    elif doska[0]==doska[4]==doska[8]==belgi:
        return True
    elif doska[2]==doska[4]==doska[6]==belgi:
        return True
    return False
    
def kompyuter_tanlasin(doska):
    free = bosh_maydonlar(doska)
    if not free:
        return
    tanlov = choice(free)
    doska[tanlov-1] = "X"

doska = bosh_doska_hosil_qil()

while bosh_maydonlar(doska):
    os.system("cls")
    kompyuter_tanlasin(doska)
    doskani_korsat(doska)
    if golib_bormi(doska, "X"):
        os.system("cls")
        doskani_korsat(doska)
        print("Kompyuter yutdi!")
        break

    foydalanuvchi_tanlasin(doska)
    if golib_bormi(doska,  "O"):
        os.system("cls")
        doskani_korsat(doska)
        print("Siz yutdingiz!")
        break
else:
    print("Durrang!")