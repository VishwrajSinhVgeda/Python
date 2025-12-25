#Write a Python program to sum of three given integers. However, if
#two values are equal sum will be zero.

# Answer:

# Program to find the sum of three given integers
# If any two values are equal, the sum will be zero

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b or b == c or a == c:
    sum = 0
else:
    sum = a + b + c
print("The sum is:", sum)

# The program takes three integers as input from the user.
# It checks if any two of the integers are equal using the condition (a == b or b == c or a == c).
# If the condition is true, it sets the sum to zero.