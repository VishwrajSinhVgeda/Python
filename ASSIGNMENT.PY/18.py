# 18. Write a Python program to count occurrences of a substring in a string. 
# Answer:
string = input("Enter a string: ")
substring = input("Enter the substring to count: ")
count = string.count(substring)
print(f"The substring '{substring}' occurs {count} times.")
# Output:
# Enter a string: Vishwraj Vishwajit Vishal
# Enter the substring to count: Vish
# The substring 'Vish' occurs 3 times.