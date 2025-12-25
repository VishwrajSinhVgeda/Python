# 86 . Can one block of except statements handle multiple exception? 
# Answer :

try:
    # code that may raise an exception
    x = int(input("Enter a number: "))
    y = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)

# Explainnation :

#  ValueError could occur if the input cannot be converted to an integer.
# ZeroDivisionError could occur if the input is 0.
# The single except block catches both types of exceptions, and e gives access to the exception object.