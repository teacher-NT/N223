import os
os.system("cls")

file = open("myfile.txt", "w")

# text = input("Matn kiriting: ")
# file.write(text)
# print("Fayl yozildi")

ismlar = ['ali', 'vali', 'hasan', 'husan']
ismlar = list(map(lambda n: n+"\n", ismlar))
file.writelines(ismlar)
print("faylga yozildi")