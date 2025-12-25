# 84 .  How many except statements can a try-except block have? Name 
#       Some built-in exception classes: 

# Answer :

try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception:
    print("Some other error occurred.")

# Explainnation :
# A try-except block can have multiple except statements to handle different types of exceptions.
# Some built-in exception classes in Python include:
# 1. ValueError - Raised when a function receives an argument of the right type but inappropriate value.
# 2. TypeError - Raised when an operation or function is applied to an object of inappropriate type.
# 3. IndexError - Raised when a sequence subscript is out of range.
# 4. KeyError - Raised when a dictionary key is not found.
# 5. ZeroDivisionError - Raised when division or modulo by zero takes place.
# 6. FileNotFoundError - Raised when trying to access a file that does not exist.
# 7. ImportError - Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.
# 8. Exception - The base class for all built-in exceptions except for system-exit exceptions.
# 9. OSError - Raised when a system operation causes a system-related error.
# 10. RuntimeError - Raised when an error is detected that doesn't fall in any of the other categories.
# These are just a few examples; Python has many built-in exception classes to handle various error conditions.
