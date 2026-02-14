#1
class Parent:
    def show(self):
        print("This is parent method")

class Child(Parent):
    def show(self):
        print("This is child method")

p = Parent()
c = Child()

p.show()
c.show()

# This is parent method
# This is child method

#2
class Parent:
    def show(self):
        print("Parent says hi")

class Child(Parent):
    def show(self):
        super().show()
        print("Child says hello")

c = Child()
c.show()
# Parent says hi
# Child says hello

#3
class Parent:
    def greet(self, name):
        print("Hello,", name)

class Child(Parent):
    def greet(self, name):
        print("Hi,", name)

p = Parent()
c = Child()

p.greet("Jan")
c.greet("Jan")
# Hello, Jan
# Hi, Jan

#4
class Parent:
    def calculate(self, a, b):
        return a + b

class Child(Parent):
    def calculate(self, a, b):
        return a * b

p = Parent()
c = Child()

print(p.calculate(2, 3))
print(c.calculate(2, 3))
# 5
# 6

#5
class Parent:
    def get_value(self):
        return 10

class Child(Parent):
    def get_value(self):
        return 20

p = Parent()
c = Child()

print(p.get_value())
print(c.get_value())
# 10
# 20
