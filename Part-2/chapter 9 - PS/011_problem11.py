import os

# Specify the current file name and the new file name
current_name = "chapter 9 - PS\\old.txt"
new_name = "chapter 9 - PS\\new.txt"

# Rename the file
os.rename(current_name, new_name)

print(f"File renamed from {current_name} to {new_name}.")
