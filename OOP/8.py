import os
os.system('cls')

# lst = [1,2,3]
# matn = 'salom'
# n = 3
# print(lst*2)
# print(matn*2)
# print(n*2)


class Transport:
    def run(self):
        print("Transport yurmoqda...")

class Velosiped(Transport):
    # pass
    def run(self):
        print("Velosiped yurmoqda...")

t1  = Transport()
v1 = Velosiped()
t1.run()
v1.run()