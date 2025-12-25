# 36.  Write a Python function that takes a list and returns a new list with 
# unique elements of the first list. 

# Answer :

def unique_list(lst):
    return list(set(lst))

Name = ["Vishwraj", "Romil", "Abhijit", "Dhruv", "Vipul"]
print(unique_list(Name))

# Output : ['Dhruv', 'Romil', 'Vishwraj', 'Vipul', 'Abhijit']

# Note : The order of elements in the output list may vary since sets do not 
# maintain order.

# Explanation : The function unique_list takes a list as input and converts it 
# to a set to remove duplicate elements. It then converts the set back to a list
# and returns it.