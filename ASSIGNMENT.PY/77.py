# 77. Write a Python program to read a file line by line store it into a variable. 
# Answer :

# Open the file in read mode
with open("sample.txt", "r") as file:
    lines = []          # variable to store lines
    for line in file:
        lines.append(line.strip())

# Display the stored lines
print("Lines stored in variable:")
for l in lines:
    print(l)
    
# Explanation :

# open("sample.txt", "r") → opens the file in read mode
# for line in file: → reads the file line by line
# lines → list variable that stores each line
# strip() → removes newline (\n) characters