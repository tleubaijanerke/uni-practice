#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break 
# apple banana

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# apple

#3
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
# 1 2

#4
for letter in "banana":
    if letter == "n":
        break
    print(letter)
# b a

#5
for i in range(10):
    if i == 5:
        break
    print(i)
# 0 1 2 3 4
