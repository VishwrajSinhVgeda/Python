# 72 . Write a Python program to read an entire text file. 
# Answer :

# Open the file in read mode
with open("sample.txt", "r") as file:
    content = file.read()

# Print the entire file content
print(content)

# Explanation :
# The open() function is used to open a file.
# The "r" mode opens the file for reading.
# The read() method reads the entire content of the file.
# The with statement ensures proper acquisition and release of resources.

