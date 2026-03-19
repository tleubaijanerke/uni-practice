#1
class A:
    def show(self):
        print("A's method")

class B:
    def show(self):
        print("B's method")

class C(A, B):
    pass

c = C()
c.show()
# A's method

#2
class A:
    def show(self):
        print("A's method")

class B:
    def show(self):
        print("B's method")

class C(A, B):
    def show(self):
        print("C's method")

c = C()
c.show()
# C's method

#3
class A:
    def show(self):
        print("A's method")

class B:
    def show(self):
        print("B's method")

class C(A, B):
    def show(self):
        super().show()
        print("C's method")

c = C()
c.show()
# A's method
# C's method

#4
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

#5
class A:
    def feature(self):
        print("Feature from A")

class B:
    def tool(self):
        print("Tool from B")

class C(A, B):
    pass

c = C()
c.feature()
c.tool()
# Feature from A
# Tool from B

