# 17.What are negative indexes and why are they used? 
#Answer:

#  Normally, indexes start from 0 for the first element.
#  Negative indexing starts from -1 for the last element.

#  Element        | a  | b  | c  | d  | e  |
#                 |    |    |    |    |    |
#  Positive Index | 0  | 1  | 2  | 3  | 4  |
#  Negative Index | -5 | -4 | -3 | -2 | -1 |


string = "ABCDE"
print(string[-1])  # Output: E
print(string[-2])  # Output: D
print(string[-3])  # Output: C
print(string[-4])  # Output: B
print(string[-5])  # Output: A

# Negative indexes are used for:
#To easily access elements from the end of a sequence
#Useful when you don’t know the exact length
#Makes reverse traversal eas

# Use Case Example

J = "Python"
print(J[-3:])   # Output: hon

# In this example, negative indexing allows easy access to elements from the end of the string "ABCDE" and "Python".y
# Slicing with negative indexes helps extract substrings from the end without calculating length
