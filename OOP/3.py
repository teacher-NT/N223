import os
os.system("cls")

class Plane:
    def fly(self):
        print("Flying...")

class Boat:
    def swim(self):
        print("Swimming...")

    def fly(self):
        print("Boat can fly")


class Duck(Plane, Boat):
    def swim(self):
        print("Duck is swimming")

duck1 = Duck()
duck1.fly()
duck1.swim()
