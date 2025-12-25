# 64 . Write a Python function that checks whether a passed string is 
# palindrome or not 

# Answer :

def is_palindrome(s):
    # Convert string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Check if string is same as its reverse
    return s == s[::-1]

# Example usage
print(is_palindrome("madam"))        # True
print(is_palindrome("nurses run"))   # True
print(is_palindrome("hello"))        # False

# Explanation :

# Convert the string to lowercase (to ignore case differences)
# Remove spaces
# Compare the string with its reverse (s[::-1])
# If both are same → Palindrome
# If you want, I can also give:
# without using reverse slicing
# character-by-character logic
