# 54 .  Write a Python program to check multiple keys exists in a dictionary 
# Answer :


student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "city": "Delhi"
}
keys_to_check = ["name", "age", "course"]

if all(key in student for key in keys_to_check):
    print("All keys exist in the dictionary")
else:
    print("Some keys are missing")

# Output:
# All keys exist in the dictionary

# # Explanation :

# key in student → checks one key at a time
# for key in keys_to_check → loops through all keys
# all() → returns True only if ALL keys are present
# If even one key is missing, result becomes False
