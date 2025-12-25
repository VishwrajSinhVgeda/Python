# 61 . Write a Python function to calculate the factorial of a number (a 
# nonnegative integer) 

# Answer :

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))  # Output: 120

# Explanation : 

# Factorial of n is:
# n! = 1 × 2 × 3 × ... × n
# 0! is defined as 1
# The loop multiplies numbers from 1 to n