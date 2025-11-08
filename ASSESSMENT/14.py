# 14. Write a python program to sum of the first n positive integers.

# Answer:
 
# Program to find the sum of the first n positive integers
n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n + 1):
    sum += i  #sum = sum + i
print("The sum of the first", n, "positive integers is:", sum)

# The program takes a positive integer n as input from the user.
# It initializes a variable sum to 0.
# It uses a for loop to iterate through the range of numbers from 1 to n (inclusive).
# In each iteration, it adds the current number i to sum.