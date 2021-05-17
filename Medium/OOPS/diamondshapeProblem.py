# Multiple inhertiance
'''
    A
  /   \
 B     C
  \   /
    D
'''


class A:
    def met(self):
        print("This is a metho of class A.")

class B(A):
    def met(self):
        print("This is a metho of class B.")

class C(A):
    pass

class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()

d.met()