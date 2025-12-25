# 82 .  Write a Python program to copy the contents of a file to another file.
# Answer :

# Copy contents from one file to another

source_file = "source.txt"
destination_file = "destination.txt"

with open(source_file, 'r') as src:
    content = src.read()

with open(destination_file, 'w') as dest:
    dest.write(content)

print("File copied successfully!")

# Explainnation :

# open(source_file, 'r') opens the source file in read mode.
# read() reads the entire content of the source file.
# open(destination_file, 'w') opens/creates the destination file in write mode.
# write() writes the content into the destination file.