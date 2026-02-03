#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # apple banana cherry

#2
for x in "banana":
  print(x) # b a n a n a

#3
for i in range(5):
    print(i)
# 0 1 2 3 4

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# apple cherry

#5
for i in range(0, 10, 2):  # start 0, stop 10, step 2
    print(i)
# 0 2 4 6 8