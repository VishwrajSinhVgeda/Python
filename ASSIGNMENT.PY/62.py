# 62 . Write a Python function to check whether a number is in a given range 

# Answer :

def is_in_range(num, start, end):
    return start <= num <= end
print(is_in_range(5, 1, 10))  # Output: True

# Explanation :
# The function checks if 'num' lies between 'start' and 'end' (inclusive)
# using the comparison operators. If it does, it returns True; otherwise, it returns False.
