# 40 . Write a Python program to get unique values from a list 

# Answer :

numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_numbers = list(set(numbers))
print("Unique values in the list are:", unique_numbers)

# Output : Unique values in the list are: [1, 2, 3, 4, 5, 6] (order may vary)

# Explainnation :
# set(numbers) → removes duplicate values from the list
# list() → converts the set back to a list


