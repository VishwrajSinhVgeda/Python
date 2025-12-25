# 75 . Write a Python program to read last n lines of a file. 
# Answer :

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines[-n:]

# Example usage
filename = "sample.txt"
n = 5

last_lines = read_last_n_lines(filename, n)
print("Last", n, "lines of the file:")
for line in last_lines:
    print(line.strip())

# Explanation :
# The open() function is used to open a file.
# The "r" mode opens the file for reading.
# The readlines() method reads all lines of the file into a list.
# Slicing is used to get the last n lines from the list.
# The with statement ensures proper acquisition and release of resources.
