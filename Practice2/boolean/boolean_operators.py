#1
x = 5
print(x > 0 and x < 10)  # True

#2
x = 5
print(x < 5 or x > 10)  # False

#3
x = 5
print(not(x > 3 and x < 10))  # False

#4
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # True
print(x is y) # False
print(x == y) # True

#5
x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y) # True