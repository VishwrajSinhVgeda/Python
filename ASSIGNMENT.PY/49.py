# 49.Write a Python script to concatenate following dictionaries to create 
# a new one. 

#Answer :

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}
d4 = {**d1, **d2, **d3}
print(d4)

# Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Explanation :
# ** operator unpacks the dictionaries. 
# When used inside a new dictionary, it merges all key-value pairs into one.
# The result is a new dictionary containing all items from the original dictionaries.
