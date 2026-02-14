#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#Mike Olsen

#2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
#2019

#3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
#2019

#4
class Animal:
    def speak(self):
        print("I am an animal")

class Dog(Animal):
    def speak(self):
        super().speak()  
        print("Woof!")

d = Dog()
d.speak()
# I am an animal
# Woof!

#5
class Animal:
    def __init__(self, name="Unknown"):
        self.name = name

class Dog(Animal):
    def __init__(self, name="Buddy", breed="Unknown"):
        super().__init__(name)
        self.breed = breed

d = Dog()
print(d.name)
print(d.breed)
# Buddy
# Unknown
