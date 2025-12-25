#Write a Python program to test whether a passed letter is a vowel or not.

#Answer:

# Program to check whether a letter is a vowel or not
letter = input("Enter a letter: ")
if letter.lower() in 'aeiou':
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")
# The program takes a letter as input from the user.
# It converts the letter to lowercase and checks if it is in the string 'aeiou'.