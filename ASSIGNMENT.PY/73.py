# 73 . Write a Python program to append text to a file and display the text. 
# Answer : 

# File name
filename = "sample.txt"

# Append text to the file
with open(filename, "a") as file:
    file.write("\nThis text is appended to the file.")

# Read and display the file content
with open(filename, "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# Explanation :
# The open() function is used to open a file.
# The "a" mode opens the file for appending text.
# The write() method appends the specified text to the file.
# The "r" mode opens the file for reading.
# The read() method reads the entire content of the file.
# The with statement ensures proper acquisition and release of resources.
