# 68 .  How can you get a random number in python? 
# Answer :

import random

num = random.randint(1, 10)  # includes 1 and 10
print(num)

# Explanation :
# random.randint(a, b) returns a random integer N such that a <= N <= b 
# It includes both endpoints a and b
