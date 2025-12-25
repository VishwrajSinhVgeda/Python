# 76 . Write a Python program to read a file line by line and store it into a list
# Answer :
def read_file_to_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]
# Example usage
filename = "sample.txt"
lines_list = read_file_to_list(filename)
print("Lines in the file stored in a list:")
for line in lines_list:
    print(line)
# Explanation :
# The open() function is used to open a file.
# The "r" mode opens the file for reading.
# The readlines() method reads all lines of the file into a list.
# A list comprehension is used to strip newline characters from each line.
# The with statement ensures proper acquisition and release of resources.

    