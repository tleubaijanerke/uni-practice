#1
class MyClass:
  x = 5
print(MyClass)
#<class '__main__.MyClass'>

#2
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
#5

#3
class MyClass:
  x = 5
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)
#5
#5
#5

#4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Jan", 17)
p1.age = 18
print(p1.age)
# 18

#5
class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b
calc = Calculator()
print(calc.add(3, 5))
print(calc.multiply(4, 6))
# 8
# 24


