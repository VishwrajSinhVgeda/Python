# Q 5. Write a Python program to get the Factorial number of given numbers. 
# Ans :
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is", factorial)
