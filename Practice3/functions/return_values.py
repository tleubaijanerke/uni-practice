#1
def add(a, b):
    return a + b
result = add(3, 4)
print(result)
# 7

#2
def square(x):
    return x * x
print(square(5))
print(square(2) + 3)
# 25
# 7

#3
def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(4))
print(check_even(7))
# Even
# Odd

#4
def example():
    return "Hello"
    print("This will not run")
print(example())
# Hello

#5
def operations(a, b):
    return a + b, a - b
x, y = operations(10, 5)
print(x)
print(y)
# 15
# 5
