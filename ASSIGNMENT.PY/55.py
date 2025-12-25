# 55 . Write a Python script to merge two Python dictionaries 
# Answer :

dict1 = {1: "Apple", 2: "Banana"}
dict2 = {3: "Mango", 4: "Orange"}

dict1.update(dict2)

print(dict1)

# Output:
# {1: 'Apple', 2: 'Banana', 3: 'Mango', 4: 'Orange'}

# # Explanation :

# update() copies all key-value pairs from dict2
# and adds them into dict1
# dict1 becomes the merged dictionary