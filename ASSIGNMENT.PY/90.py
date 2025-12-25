# 90 .  Write python program that user to enter only odd numbers, else 
#       will raise an exception. 
# Answer :
 
 # Custom exception for even numbers
class NotOddNumberError(Exception):
    def __init__(self, message="The number is not odd!"):
        self.message = message
        super().__init__(self.message)

# Main program
try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
        # Raise exception if the number is even
        raise NotOddNumberError
    print(f"You entered a valid odd number: {num}")
except ValueError:
    print("Invalid input! Please enter an integer.")
except NotOddNumberError as e:
    print(e)

# Explanation :

#  A custom exception NotOddNumberError is defined.
# The program asks the user to enter a number.
# If the number is even, it raises the custom exception.
# If the input is not an integer, it raises a ValueError.