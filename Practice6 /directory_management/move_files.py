import os
import shutil

# Base directory
base_dir = "move_files_test"

# Example 1: Create source and destination folders
source_dir = os.path.join(base_dir, "source")
destination_dir = os.path.join(base_dir, "destination")

os.makedirs(source_dir, exist_ok=True)
os.makedirs(destination_dir, exist_ok=True)

print("Source and destination folders created.")
# os.makedirs() creates directories if they don't exist


# Example 2: Create sample files in source directory
for i in range(3):
    file_path = os.path.join(source_dir, f"file{i}.txt")
    with open(file_path, "w") as f:
        f.write(f"This is file {i}\n")

print("Sample files created in source folder.")
# Creates 3 text files inside source folder


# Example 3: Move one file to destination folder
file_to_move = os.path.join(source_dir, "file0.txt")
new_location = os.path.join(destination_dir, "file0.txt")

shutil.move(file_to_move, new_location)

print(f"Moved file: {new_location}")
# shutil.move() moves a file from one place to another


# Example 4: Move all remaining .txt files
for file in os.listdir(source_dir):
    if file.endswith(".txt"):
        src_path = os.path.join(source_dir, file)
        dst_path = os.path.join(destination_dir, file)
        shutil.move(src_path, dst_path)

print("All remaining .txt files moved.")
# Moves all text files from source to destination


# Example 5: List files in destination folder
if os.path.exists(destination_dir):
    print("Files in destination folder:")
    print(os.listdir(destination_dir))
# os.listdir() shows all files in destination
