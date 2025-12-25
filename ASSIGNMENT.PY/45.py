# 45 .Write a Python program to unzip a list of tuples into individual lists.
# Answer :

# List of tuples
data = [(1, 'a', 10.5), (2, 'b', 20.5), (3, 'c', 30.5)]

# Unzipping the list of tuples
list1, list2, list3 = zip(*data)

# Convert tuples to lists
list1 = list(list1)
list2 = list(list2)
list3 = list(list3)

# Output
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)

# Output: 
# List 1: [1, 2, 3]
# List 2: ['a', 'b', 'c']
# List 3: [10.5, 20.5, 30.5]

# Explanation :
# zip(*data) unzips the tuples.
# * is the unpacking operator.
# zip() groups elements from the same position.
# We convert the result into lists for easy use.
 