#20. Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each string.

#Answer:


str1 = "Vishwraj"
str2 = "Vegda"

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]


result = new_str1 + " " + new_str2
print(result)        # Output: #Veshwraj Vigda


# Explanation

# Slicing is used to get the first two characters of each string
# Concatenation combines the swapped parts to form new strings
# Finally, both new strings are joined with a space in between

