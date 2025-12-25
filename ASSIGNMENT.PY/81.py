# 81 . Write a Python program to write a list to a file. 
# Answer :
my_list = ["Apple", "Banana", "Mango", "Orange"]

# Open file in write mode
with open("output.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")

print("List has been written to the file.")
# Explanation :
# The open() function is used to open a file.
# The "w" mode opens the file for writing (creates a new file or truncates
# an existing file).    
# A for loop is used to iterate through each item in the list.
# The write() method writes each item to the file followed by a newline character.
# The with statement ensures proper acquisition and release of resources.
