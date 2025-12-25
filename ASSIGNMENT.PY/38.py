# 38 . Write a Python program to select an item randomly from a list. 

#Answer :

import random

items = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
random_item = random.choice(items)
print("Randomly selected item:", random_item)

# Output : Randomly selected item: Mango (output may vary)

# Explainnation : 

# random → Python ka built-in module hai jo random number generation aur selection ke liye functions provide karta hai
# items → ek list hai jisme fruits ke names hain
#random.choice(list) → list me se ek item randomly select karta hai