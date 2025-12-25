# 32 . Write a Python program to remove duplicates from a list. 
# Answer :

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print(unique_list)

# Output : [1, 2, 3, 4, 5]

# Exlpinnation :Create an empty list unique_list
                # Go through each element in numbers
                # Add it only if it is not already present
                # This keeps only unique values 