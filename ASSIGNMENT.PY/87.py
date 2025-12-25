# 87 .  When is the finally block executed?
# Answer :

# 1.If no exception occurs:
        # The try block executes normally.
        # The finally block executes afterward.

# 2.If an exception occurs and is caught by an except block:
        # The except block executes.
        # Then the finally block executes.

# 3.If an exception occurs and is not caught:
        # The finally block still executes.
        # After that, the exception is propagated (raised) to the outer scope.

try:
    x = 1 / 0  # This will raise ZeroDivisionError
except ValueError:
    print("Caught ValueError")
finally:
    print("This always runs")

# Output : 

# This always runs
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero

# Exaplainnation :
# The finally block is executed regardless of whether an exception occurred or not.
# It is typically used for cleanup actions that must be executed
# under all circumstances, such as closing files or releasing resources.
