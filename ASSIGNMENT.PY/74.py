# 74 .  Write a Python program to read first n lines of a file. 

# File name
filename = "sample.txt"

# Number of lines to read
n = 5

# Read first n lines of the file
with open(filename, "r") as file:
    lines = file.readlines()
    for i in range(min(n, len(lines))):
        print(lines[i].strip())

# Explanation :
# The open() function is used to open a file.
# The "r" mode opens the file for reading.
# The readlines() method reads all lines of the file into a list.
# A loop is used to print the first n lines.
# The with statement ensures proper acquisition and release of resources.
