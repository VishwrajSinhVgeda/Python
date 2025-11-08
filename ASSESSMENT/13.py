# Write a Python program that will return true if the two given
# integer values are equal or their sum or difference is 5. 

# Answer:

# Program to check if two integers are equal,
# or their sum or difference is 5

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b or (a + b == 5) or (abs(a - b) == 5):
    print(True)
else:
    print(False)
    
#Explanation:

# The program checks three conditions:

# If both numbers are equal → a == b

# If their sum is 5 → a + b == 5

# If their difference is 5 → abs(a - b) == 5 (absolute difference so order doesn’t matter)

# If any of these are true → it prints True, else False.