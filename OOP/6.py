import os
os.system("cls")

class A:
    def hello(self):
        print("I'm A")

class B:
    def hello(self):
        print("I'm B")

class C(A):
    pass

class F(A):
    pass

class D( B):
    pass

class E(F, D, C):
    pass

e1 = E()
e1.hello()
