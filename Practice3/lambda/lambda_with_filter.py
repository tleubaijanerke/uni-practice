#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
#[1, 3, 5, 7]

#2
numbers = [5, 12, 8, 20, 3]
result = list(filter(lambda x: x > 10, numbers))
print(result)
# [12, 20]

#3
words = ["hi", "apple", "cat", "banana"]
result = list(filter(lambda word: len(word) > 3, words))
print(result)
# ['apple', 'banana']

#4
numbers = [-5, 3, -1, 8, -2]
result = list(filter(lambda x: x < 0, numbers))
print(result)
# [-5, -1, -2]

#5
names = ["Jan", "Ali", "Jamal", "Mira"]
result = list(filter(lambda name: name.startswith("J"), names))
print(result)
# ['Jan', 'Jamal']
