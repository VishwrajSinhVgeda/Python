# 34 . Write a Python function that takes two lists and returns true if they 
#      have at least one common member. 
# Answer :

def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

a = [1, 2, 3, 4]
b = [5, 6, 3, 8]

print(has_common_member(a, b))

# Output : True Because 3 is present in both lists.

# Exapinnation :
#               Check each item of the first list
#               If the item exists in the second list → return True
#               If nothing matches → return False