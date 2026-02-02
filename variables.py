#1
x = 5
y = "John"
print(x)
print(y)

#2
x = 4       # integer
x = "Sally" # now string
print(x)

#3
a = str(3)    # '3'
b = int(3)    # 3
c = float(3)  # 3.0
print(a, b, c)

#4
x = y = z = "Orange"
print(x, y, z)

#5
x = "awesome"  # global variable

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)  # prints local/global modified

myfunc()
print("Python is " + x)      # prints modified global variable
