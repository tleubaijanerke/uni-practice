#1
class Person:
    species = "Human" 

    def __init__(self, name, age):
        self.name = name 
        self.age = age    
p1 = Person("Jan", 17)
p2 = Person("Ali", 20)
print(p1.species)
print(p2.species)
# Human
# Human

#2
class Person:
    species = "Human"
p1 = Person()
p2 = Person()
Person.species = "Homo sapiens"
print(p1.species)
print(p2.species)
# Homo sapiens
# Homo sapiens

#3
class Person:
    species = "Human"
    def __init__(self, name):
        self.name = name  # instance variable
p1 = Person("Jan")
p2 = Person("Ali")
p1.name = "Mira"
print(p1.name)
print(p2.name)
# Mira
# Ali

#4
class Person:
    species = "Human"
p1 = Person()
p1.species = "Alien"  
print(p1.species)  # instance variable
print(Person.species)  # class variable
# Alien
# Human

#5
class Person:
    count = 0  # class variable
    def __init__(self, name):
        self.name = name
        Person.count += 1
p1 = Person("Jan")
p2 = Person("Ali")
p3 = Person("Mira")
print(Person.count)
# 3
