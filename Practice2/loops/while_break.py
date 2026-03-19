#1
i = 1
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1 # 1 2 3

#2
number = 0
while True:
    number += 2
    print(number)
    if number >= 8:
        break
# 2 4 6 8

#3
letters = ['a', 'b', 'c', 'd']
index = 0
while index < len(letters):
    print(letters[index])
    if letters[index] == 'c':
        break
    index += 1
# a b c

#4
i = 1
while i < 10:
    print("Number:", i)
    if i == 4:
        break
    i += 2
# Number: 1
# Number: 3
# Number: 5
# Number: 7
# Number: 9 

#5
while True:
    color = input("Type a color (or 'red' to stop): ")
    if color == "red":
        break
    print("You typed:", color)