# 47. How will you create a dictionary using tuples in python? 
# Answer :

data = [("name", "Vishwraj"), ("age", 22), ("city", "Ahmedabad")]
my_dict = dict(data)
print(my_dict)

# Output : {'name': 'Vishwraj', 'age': 22, 'city': 'Ahmedabad'}

# Explanation : 
# Each tuple in the list contains a key-value pair.
# The dict() function converts the list of tuples into a dictionary.

