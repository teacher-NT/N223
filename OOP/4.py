import os
os.system("cls")

class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def celebrate(self):
        print("Happy birth day from B")

class C(B):
    pass

c1 = C()
c1.celebrate()
c1.hello()
