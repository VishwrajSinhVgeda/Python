# 50 .  Write a Python script to check if a given key already exists in a 
# dictionary. 
# Answer :

my_dict = {
    "name": "Vishwraj",
    "age": 22,
    "city": "Ahmedabad"
}

key = "age"

if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")

# Output: Key exists in the dictionary

# Explanation :
# in checks directly if the key is present.
# get() returns None if the key is not found.