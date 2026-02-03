#1
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # 1 2 4 5 6

#2
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)  # 1 3 4 5

#3
i = 1
while i <= 6:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1  # 1 2 4 5 7 

#4
i = 5
while i > 0:
    if i == 3:
        i -= 1
        continue
    print(i)
    i -= 1  # 5 4 2 1

#5
letters = ["a", "b", "c", "d"]
index = 0
while index < len(letters):
    index += 1
    if letters[index-1] == "b":
        continue
    print(letters[index-1])  # a c d

