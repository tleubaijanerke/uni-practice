import os

# Common file for all examples
file_path = "example_file.txt"

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("This is line one.\nThis is line two.\nPython is fun!\nWe can read and write files.\nEnd of the example.\n")

# Example 1: Read the entire file
with open(file_path, "r") as f:
    content = f.read()
    print(content)
# read() returns the whole content of the file

# Example 2: Read the first 10 characters
with open(file_path, "r") as f:
    part = f.read(10)
    print(part)
# read(n) reads the first n characters

# Example 3: Read the first line
with open(file_path, "r") as f:
    line1 = f.readline()
    print(line1)
# readline() returns one line at a time

# Example 4: Read all lines into a list
with open(file_path, "r") as f:
    lines = f.readlines()
    print(lines)
# readlines() returns a list of lines

# Example 5: Loop through the file line by line
with open(file_path, "r") as f:
    for line in f:
        print(line.strip())
# Iterating over a file reads it line by line; strip() removes newline characters