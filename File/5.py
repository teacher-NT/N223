import os
os.system("cls")

with open("N223/image.jpg", "rb") as image:
    baytlar = image.read()
    # for i in list(baytlar):
    #     print(i, end=" ")
    print(len(list(baytlar)))

with open("N223/panda.jpg", "wb") as image:
    image.write(baytlar)
    print("Rasm nusxalandi")