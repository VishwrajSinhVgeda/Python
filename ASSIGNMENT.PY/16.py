# 16.Write a Python program to count the number of characters (character frequency) in a string 

# Answer:


string = input("Enter a string: ")

freq = {}

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequency:")
for key, value in freq.items():
    print(key, ":", value)

# Enter a string: Vishwraj
# Character Frequency: Output
V : 1
i : 1
s : 1
h : 1
w : 1
r : 1
a : 1
j : 1

# Explanation

# We take a string from the user
# Use a dictionary freq to store character counts
# Loop through each character and update the count
# Finally, print each character with its frequency
