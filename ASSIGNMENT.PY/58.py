# 58 .  Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
# 300}, o {'item': 'item1', 'amount': 750}] 
# Expected Output: 
# • Counter ({'item1': 1150, 'item2': 300}) 

# Answer : 

from collections import Counter

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]
combined = Counter()

for entry in data:
    combined[entry['item']] += entry['amount']

print(combined)

# Output:
# Counter({'item1': 1150, 'item2': 300})

# Explanation :

# Counter() is like a dictionary but specifically for counting or summing values.
# We loop through each dictionary in the list.
# For each item, we add its amount to the Counter.
# The Counter automatically sums amounts for duplicate items.