#Write a Python program to find whether a given number is even 
# or odd, print out an appropriate message to the user. 

#Answer:

#Program to check whether a number is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

# The program takes a number as input from the user.
# It checks if the number is divisible by 2 (num % 2 == 0).
# If yes, it prints “Even number.”
# Otherwise, it prints “Odd number.”