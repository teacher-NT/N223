import os
os.system("cls")

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def kick(self):
        pass

    @abstractmethod
    def jump(self):
        pass

class Ironman(Player):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} is running...")

    def kick(self):
        print(f"{self.name} is kicking...")

    def jump(self):
        print(f"{self.name} is jumping...")

iron1 = Ironman("Tony Stark", 41)
