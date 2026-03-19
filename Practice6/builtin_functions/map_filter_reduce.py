from functools import reduce

# Example 1: Using map() to square numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)
# map() applies a function to each element of a list

# Example 2: Using filter() to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)
# filter() selects elements that meet a condition

# Example 3: Using reduce() to sum numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total)
# reduce() applies a function cumulatively to items of a list

# Example 4: Using map() with type conversion
str_numbers = list(map(str, numbers))
print("Numbers as strings:", str_numbers)
# map() can also convert types, e.g., int to str

# Example 5: Using filter() with strings
words = ["apple", "banana", "pear", "kiwi"]
long_words = list(filter(lambda w: len(w) > 4, words))
print("Long words:", long_words)
# filter() works on any iterable, not just numbers