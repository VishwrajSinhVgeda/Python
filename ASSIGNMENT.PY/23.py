# 23. Write a Python program to get a string made of the first 2 and the last 
#2 chars from a given a string. If the string length is less than 2, return 
#instead of the empty string. 

# Answer :

def first_last_two(s):
    if len(s) < 2:
        return ""   
    return s[:2] + s[-2:]


print(first_last_two("Python"))
print(first_last_two("Hello"))
print(first_last_two("A"))
print(first_last_two(""))

# Output :

# Pyon
# Helo

# Explanation :

# Example 1: "Python"

# First 2 → Py

# Last 2 → on

# Output → Pyon
