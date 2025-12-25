# 46 . Write a Python program to convert a list of tuples into a dictionary.
#Answer :
 

data = [("name", "Vishwraj"), ("age", 22), ("city", "Ahmedabad")]

result = dict(data)

print(result)

# Output: {'name': 'Vishwraj', 'age': 22, 'city': 'Ahmedabad'}

# Explanation :
# Each tuple contains (key, value)
# dict() function converts the list of tuples into a dictionary