#89 . How Do You Handle Exceptions with Try/Except/Finally in Python? 
#     Explain with coding snippets. 

# In Python, exceptions are handled using the try, except, and finally blocks.
# The try block contains code that might raise an exception.
# The except block catches and handles specific exceptions.
# The finally block executes regardless of whether an exception occurred or not.

try:
    x = 1 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
finally:
    print("This always runs")

# Output :
# Caught ZeroDivisionError
# This always runs
# Explanation :
# 1. The code inside the try block attempts to divide 1 by 0, which raises a ZeroDivisionError.
# 2. The except block catches the ZeroDivisionError and prints a message.
# 3. The finally block executes afterward, printing "This always runs", regardless of whether an exception occurred or not.
# The finally block is typically used for cleanup actions that must be executed
# under all circumstances, such as closing files or releasing resources.
