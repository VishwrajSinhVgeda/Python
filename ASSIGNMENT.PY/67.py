# 67 . How can you pick a random item from a range? 
# Answer :

import random

num = random.choice(range(1, 11))
print(num)

# Explanation :
# random.choice(sequence) returns one random element
# range(1, 11) generates numbers from 1 to 10
# The range must not be empty
