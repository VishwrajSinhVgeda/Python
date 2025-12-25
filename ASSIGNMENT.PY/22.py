#22. Write a Python function to reverses a string if its length is a multiple 
#of 4. 

# Answer:
def reverse_if_multiple_of_4(text):
    if len(text) % 4 == 0:
        return text[::-1]   # reverse the string
    else:
        return text         # return same string

print(reverse_if_multiple_of_4("abcd"))
print(reverse_if_multiple_of_4("python"))
print(reverse_if_multiple_of_4("data"))

# Output:
# dcba
# python
# atad

# Explanation :

#If length of string is divisible by 4 →  Reverse it
#Otherwise →  Keep it same