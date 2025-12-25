# 63 . Write a Python function to check whether a number is perfect or not.
# Answer :

def is_perfect(num):
    if num <= 1:
        return False

    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num
print(is_perfect(6))    # True  (1 + 2 + 3 = 6)
print(is_perfect(28))   # True
print(is_perfect(12))   # False

# Explaination :
# A perfect number is equal to the sum of its proper divisors
# Loop from 1 to num-1
# Add numbers that divide num exactly
# If the sum equals num, it is a perfect number