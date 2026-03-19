import os

file_path = "example_file.txt"

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("This is line one.\nThis is line two.\nPython is fun!\nWe can read and write files.\nEnd of the example.\n")

# Example 1: Overwrite the file
with open(file_path, "w") as f:
    f.write("Overwriting the file.\nThis is new content.")
# "w" mode overwrites any existing content or creates a new file

# Example 2: Append a line to the file
with open(file_path, "a") as f:
    f.write("\nAppending this line at the end.")
# "a" mode adds content to the end without removing existing content

# Example 3: Write multiple lines
lines = ["Line one\n", "Line two\n", "Line three\n"]
with open(file_path, "w") as f:
    f.writelines(lines)
# writelines() writes a list of strings; newlines must be added manually

# Example 4: Append multiple lines
more_lines = ["Line four\n", "Line five\n"]
with open(file_path, "a") as f:
    f.writelines(more_lines)
# Appending multiple lines keeps previous content intact

# Example 5: Write and then immediately read
with open(file_path, "w") as f:
    f.write("Fresh start.\nReading it now.")
with open(file_path, "r") as f:
    print(f.read())
# After writing, you can reopen the file to read its content