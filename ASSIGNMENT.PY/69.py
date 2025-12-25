# 69 .  How will you set the starting value in generating random numbers? 
# Answer :

import random

random.seed(10)   # set starting value (seed)
print(random.random())
print(random.random())

# Explanation :
# random.seed(a) initializes the random number generator with
# a specific starting value 'a'
# Using the same seed value will produce the same sequence of random numbers
# This is useful for reproducibility in experiments or tests
