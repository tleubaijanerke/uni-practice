#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#[('Tobias', 22), ('Emil', 25), ('Linus', 28)]

#2
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
#['pie', 'apple', 'banana', 'cherry']

#3
words = ["apple", "banana", "cat"]
result = sorted(words, key=lambda x: x[-1])
print(result)
# ['banana', 'apple', 'cat']

#4
numbers = [-10, 5, -3, 2]
result = sorted(numbers, key=lambda x: abs(x))
print(result)
# [2, -3, 5, -10]

#5
words = ["apple", "hi", "banana"]
result = sorted(words, key=lambda x: len(x), reverse=True)
print(result)
# ['banana', 'apple', 'hi']

