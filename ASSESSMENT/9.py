# Write python program that swap two number with temp variable
# and without temp variable. 

#Answer:

# Swapping with temp variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, ", b =", b)

# Using temp variable
temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)

# Swapping without temp variable (using + and -)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, ", b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)
