#1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)
#Emil
#36

#2
class Person:
  pass
p1 = Person()
p1.name = "Tobias"
p1.age = 25
print(p1.name)
print(p1.age)
#Tobias
#25

#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Linus", 28)
print(p1.name)
print(p1.age)
#Linus
#28

#4
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)
print(p2.name, p2.age)
#Emil 18
#Tobias 25

#5
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country
p1 = Person("Linus", 30, "Oslo", "Norway")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
#Linus
#30
#Oslo
#Norway
