#59 . Write a Python program to create a dictionary from a string. 
#  Note: Track the count of the letters from the string. 

# Answer :


input_string = "hello world"
letter_count = {}

for char in input_string:
   
    if char.isalpha():
        char = char.lower()
        
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

print("Letter count dictionary:", letter_count)

# Output : Letter count dictionary: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# Explanation : 

# We loop through each character in the string.
# char.isalpha() ensures only letters are counted.
# char.lower() treats uppercase and lowercase letters as the same.
# The dictionary letter_count keeps track of the frequency of each letter.
