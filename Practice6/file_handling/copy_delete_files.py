import os
import shutil

file_path = "example_file.txt"

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("This is line one.\nThis is line two.\nPython is fun!\nWe can read and write files.\nEnd of the example.\n")

# Example 1: Copy a file
shutil.copy(file_path, "example_file_copy.txt")
print("File copied to example_file_copy.txt")
#shutil.copy() copies the content to a new file

# Example 2: Move (rename) the copied file
shutil.move("example_file_copy.txt", "example_file_moved.txt")
print("example_file_copy.txt moved to example_file_moved.txt")
# shutil.move() moves or renames a file

# Example 3: Delete a file safely
if os.path.exists("example_file_moved.txt"):
    os.remove("example_file_moved.txt")
    print("example_file_moved.txt deleted")
else:
    print("example_file_moved.txt does not exist")
# os.remove() deletes a file; check existence to avoid errors

# Example 4: Delete a folder safely (must be empty)
os.makedirs("temp_folder", exist_ok=True)
if os.path.exists("temp_folder"):
    os.rmdir("temp_folder")
    print("temp_folder deleted")
# os.rmdir() deletes an empty folder

# Example 5: Copy and then append content
shutil.copy(file_path, "example_file_backup.txt")
with open("example_file_backup.txt", "a") as f:
    f.write("\nBackup line added.")
print("example_file_backup.txt created and appended")
# You can copy a file and then modify the copy without affecting the original