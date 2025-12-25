# 83 .  Explain Exception handling? What is an Error in Python? 
# ANswer :

# Exception handling is a mechanism in Python used to handle runtime errors so that the normal flow of a program does not stop abruptly.

# Python uses the following keywords for exception handling:

# try – code that may cause an exception
# except – code that runs if an exception occurs
# else – code that runs if no exception occurs
# finally – code that always runs (exception or not)

# Example of Exception Handling :

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Division successful")
finally:
    print("Program ended")
    
# Explanation :
# In the above example, we try to divide two numbers.
# If the user enters zero as the second number, a ZeroDivisionError is raised, and the corresponding except block is executed.
# If the user enters a non-integer value, a ValueError is raised, and its except block is executed.
# If no exceptions occur, the else block is executed.