# 66. How can you pick a random item from a list or tuple? 
# Answer :

# Exampple of list :

import random

items = [10, 20, 30, 40, 50]
random_item = random.choice(items)

print(random_item)

# Example of tuple :

import random

items = (10, 20, 30, 40, 50)
random_item = random.choice(items)

print(random_item)

# Explanation :
# random.choice(sequence) returns one random element
# Works with lists, tuples, and strings
# The sequence must not be empty
