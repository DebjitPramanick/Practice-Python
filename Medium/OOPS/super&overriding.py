class A:
    classVar1 = "I am class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classVar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classVar1 = "I am in class B"
    def __init__(self):
        super().__init__() # >> It will call constructor of super class
        print(super().classVar1)
        self.var1 = "I am inside class B's constructor"

a = A()
b = B()

print(b.var1)
print(b.special)