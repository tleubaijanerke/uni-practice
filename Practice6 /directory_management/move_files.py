import os

# Base directory
base_dir = "Practice6_test"

# Example 1: Create a nested directory
nested_dir = os.path.join(base_dir, "folder1", "subfolder1")
os.makedirs(nested_dir, exist_ok=True)
print(f"Nested directory created: {nested_dir}")
# os.makedirs() creates all intermediate directories; exist_ok=True avoids errors

# Example 2: Create another nested directory
nested_dir2 = os.path.join(base_dir, "folder2", "subfolder2")
os.makedirs(nested_dir2, exist_ok=True)
print(f"Nested directory created: {nested_dir2}")
# You can create multiple levels of directories at once

# Example 3: List files and folders in base_dir
if os.path.exists(base_dir):
    print("Listing files and folders in base_dir:")
    print(os.listdir(base_dir))
# os.listdir() returns all files and folders in a directory

# Example 4: Find files by extension in base_dir (e.g., .txt)
txt_files = [f for f in os.listdir(base_dir) if f.endswith(".txt")]
print("Text files in base_dir:", txt_files)
# List comprehension can filter files by extension

# Example 5: Create a new text file inside nested directory
file_path = os.path.join(nested_dir, "example_file.txt")
with open(file_path, "a") as f:
    f.write("This is a test file for directory exercises.\n")
print(f"File created or appended: {file_path}")
# "a" mode creates the file if it doesn't exist, appends otherwise