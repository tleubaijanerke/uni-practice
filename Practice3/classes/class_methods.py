#1
class Person:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()
#Hello, my name is Emil

#2
class Calculator:
  def add(self, a, b):
    return a + b
  def multiply(self, a, b):
    return a * b
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
#8
#28

#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def get_info(self):
    return f"{self.name} is {self.age} years old"
p1 = Person("Tobias", 28)
print(p1.get_info())
#Tobias is 28 years old

#4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 36)
print(p1)
#<__main__.Person object at 0x15039e602100>

#5
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")
p1 = Person("Emil")
del Person.greet
p1.greet()  # This will cause an error
