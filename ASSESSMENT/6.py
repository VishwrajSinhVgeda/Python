# Q 6.  Write a Python program to get the Fibonacci series of given range. 
# Ans :
num = int(input("Enter the range for Fibonacci series: "))
a, b = 0, 1
while a <= num:
    print(a, end=" ")
    a, b = b, a + b