import os
os.system("cls")

class BankAccount:
    def __init__(self, name, balans):
        self.name = name
        self.__balans = balans

    def show_balans(self, parol):
        if parol == "qwerty":
            print(f"{self.name} ning balansi: {self.__balans}")
        else:
            print("Parol xato!")

    def change_balans(self, new, parol):
        if parol == 'qwerty':
            self.__balans += new
            print("Balans o'zgardi...")
        else:
            print("Parol xato!")

b1 = BankAccount("Bobur", 1000)
b1.name = 'Murod'
print(b1.name)
# print(b1.__balans)
b1.change_balans(500, "qwerty")
b1.show_balans("qwerty")