# 53 .  Write a Python script to print a dictionary where the keys are 
# numbers between 1 and 15.
# 
# Answer :
my_dict = {}

for i in range(1, 16):
    my_dict[i] = i * i

print(my_dict)


# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, ..., 15: 225}

# Explanation : 

# range(1, 16) generates numbers from 1 to 15
# Each number is added as a key
# The value is the square of the key
# Finally, the dictionary is printed