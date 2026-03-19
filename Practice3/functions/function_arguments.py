#1
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#Emil Refsnes
#Tobias Refsnes
#Linus Refsnes

#2
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
#Emil Refsnes

#3
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Hello Emil
#Hello Tobias
#Hello friend
#Hello Linus

#4
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#I am from Sweden
#I am from India
#I am from Norway
#I am from Brazil

#5
def my_function(name): 
  print("Hello", name)

my_function("Emil") 

#Hello, Emil
