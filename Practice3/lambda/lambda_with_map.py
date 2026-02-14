#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#[2, 4, 6, 8, 10]

#2
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 10, numbers))
print(result)
# [10, 20, 30, 40]

#3
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)
# [5, 7, 9]

#4
words = ["apple", "hi", "banana"]
result = list(map(lambda word: len(word), words))
print(result)
# [5, 2, 6]

#5
names = ["jan", "ali", "mira"]
result = list(map(lambda name: name.upper(), names))
print(result)
# ['JAN', 'ALI', 'MIRA']
