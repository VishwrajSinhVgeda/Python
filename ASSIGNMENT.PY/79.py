# 79 .  Write a Python program to count the number of lines in a text file.
# Answer :

filename = "sample.txt"

line_count = 0
with open(filename, "r") as file:
    for line in file:
        line_count += 1

print("Number of lines:", line_count)

# Explanation :

# Reads the file line by line
# Efficient for large files
# Counts each line using a counter    