# 70 . How will you randomize the items of a list in place? 
# Ansswer :

import random

items = [1, 2, 3, 4, 5]
random.shuffle(items)

print(items)

# Explanation :
# random.shuffle(x) shuffles the sequence x in place    
# It modifies the original list and does not return a new list
# The order of items in the list is randomized
