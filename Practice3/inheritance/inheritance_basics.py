#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
#John Doe

#2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
#Mike Olsen

#3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#Mike Olsen

#4
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("I am an animal")
class Dog(Animal):
    pass  
d = Dog("Buddy")
d.speak()
print(d.name)
# I am an animal
# Buddy

#5
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed
d = Dog("Buddy", "Golden Retriever")
print(d.name)
print(d.breed)
# Buddy
# Golden Retriever
