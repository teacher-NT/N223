import os
os.system("cls")

class Animal:
    def eat(self):
        print("Animal is eating")
    
    def walk(self):
        print("Animal is walking")


class Dog(Animal):
    def run(self):
        print("Dog is running")

    def eat(self):
        print("Dog is eating a meat")

dog1 = Dog()
dog1.eat()
dog1.walk()
dog1.run()