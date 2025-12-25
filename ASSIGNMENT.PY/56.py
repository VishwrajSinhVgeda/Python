# 56 . Write a Python program to map two lists into a dictionary 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 
#Answer :

from collections import Counter

keys = ['a', 'b', 'a', 'c', 'b', 'd']
values = [100, 200, 300, 300, 200, 400]

result = Counter()

for k, v in zip(keys, values):
    result[k] += v

print(result)

# Output:
# Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300}) 

# Explanation :

# zip(keys, values) pairs each key with its value
# Counter() automatically helps in adding values for duplicate keys
# If a key repeats, its value gets summed