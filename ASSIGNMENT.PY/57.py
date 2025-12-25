# 57 . Write a Python program to find the highest 3 values in a dictionary 

#Answer :

my_dict = {
    'a': 100,
    'b': 300,
    'c': 200,
    'd': 400,
    'e': 250
}

highest_three = sorted(my_dict.values(), reverse=True)[:3]

print("Highest 3 values are:", highest_three)

# Output :
# Highest 3 values are: [400, 300, 250]

# Explainnation :

# my_dict.values() → gets all values from the dictionary
# sorted(..., reverse=True) → sorts values in descending order
# [:3] → selects the top 3 values