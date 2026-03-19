# Example 1: Using enumerate() on a list
fruits = ["apple", "banana", "pear"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# enumerate() gives index and value

# Example 2: Using enumerate() with start index
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
# start parameter changes the starting index

# Example 3: Using zip() to pair two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
# zip() pairs elements from multiple lists

# Example 4: Using zip() to create a dictionary
name_age_dict = dict(zip(names, ages))
print(name_age_dict)
# zip() can be used to make key-value pairs

# Example 5: Type checking and conversion
x = "123"
print("Type before:", type(x))
y = int(x)
print("Type after:", type(y))
# type() checks type; int(), str(), float() convert types