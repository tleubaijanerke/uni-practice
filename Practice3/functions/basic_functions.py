#1
def my_function():
  print("Hello from a function")
my_function()  #Hello from a function

#2
def greet():
    print("Hello!")
greet()
# Hello!

#3
def greet(name):
    print("Hello,", name)
greet("Zhanerke")
# Hello, Zhanerke

#4
def add(a, b):
    return a + b
result = add(3, 5)
print(result)
# 8

#5
def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
check_number(0)
# Zero
