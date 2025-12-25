# 60 .Sample string:
#  'w3resource' Expected output: 
# • {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

# Answer :

sample_string = 'w3resource'
char_count = {}

for char in sample_string:
    if char in char_count:
        char_count[char] += 1  # Increment count if character exists
    else:
        char_count[char] = 1   # Initialize count if character is new
print(char_count)

# Output : {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# Exlanation : 

# We initialize an empty dictionary char_count.
# For each character in the string:
# If the character is already a key, increment its value.
# If it’s not, add it with a value of 1.
# Finally, print the dictionary which gives the count of each character.
