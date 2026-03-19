#1
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#The youngest child is Linus

#2
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_function("Emil", "Tobias", "Linus")
#Type: <class 'tuple'>
#First argument: Emil
#Second argument: Tobias
#All arguments: ('Emil', 'Tobias', 'Linus')

#3
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")
#Hello Emil
#Hello Tobias
#Hello Linus

#4
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen")
#Type: <class 'dict'>
#Name: Tobias
#Age: 30
#All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}

#5
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#Title: User Info
#Positional arguments: ('Emil', 'Tobias')
#Keyword arguments: {'age': 25, 'city': 'Oslo'}
