# 85 . When will the else part of try-except-else be executed? 
# Answer :

try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("Division by zero!")
else:
    # Code that runs only if no exception occurred in try
    print("No errors occurred, result is:", result)

# Examplaintion :
#1. Python first runs the code inside try.

#2.If an exception occurs:
        # Python skips the else block.
        # It looks for a matching except block to handle the exception.

#3.If no exception occurs:
        # The except blocks are skipped.
        # The else block is executed.