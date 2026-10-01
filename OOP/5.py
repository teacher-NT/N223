import os
os.system("cls")

class Animal:
    def eat(self):
        print("Animal is eating.")
    
    def walk(self):
        print("Animal is walking")

class Dog(Animal):
    def eat(self):
        print("Dog is eating")

class Cat(Animal):
    def walk(self):
        print("Cat is walking")

dog1 = Dog()
dog1.walk()
dog1.eat()

cat1 = Cat()
cat1.walk()
cat1.eat()