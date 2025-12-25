# 48 .  Write a Python script to sort (ascending and descending) a 
# dictionary by value.
# 
# Answer :
# 
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = sorted(d.items(), key=lambda x: x[1])
print("Sorted dictionary in ascending order by value:", dict(sorted_d))
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print("Sorted dictionary in descending order by value:", dict(sorted_d)) 

# Output:
# Sorted dictionary in ascending order by value: {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
# Sorted dictionary in descending order by value: {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

# Explanation :

# # data.items() → gets key-value pairs
# sorted() → sorts the items
# key=lambda item: item[1] → sorts using value
# reverse=True → sorts in descending order
# dict() → converts sorted data back into a dictionary