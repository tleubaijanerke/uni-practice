#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # apple cherry

#2
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue
    print(num)
# 1 2 4 5

#3
for letter in "banana":
    if letter == "a":
        continue
    print(letter)
# b n n

#4
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
# 1 3 5

#5
for i in range(5):
    if i < 3:
        continue
    print(i)
# 3 4
