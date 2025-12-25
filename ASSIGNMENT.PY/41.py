# 41 . Write a Python program to check whether a list contains a sub list.

# Answer :

def contains_sublist(main_list, sub_list):
    n = len(sub_list)
    for i in range(len(main_list) - n + 1):
        if main_list[i:i+n] == sub_list:
            return True
    return False


main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, 5]

if contains_sublist(main_list, sub_list):
    print("Sublist exists in the main list")
else:
    print("Sublist does NOT exist in the main list")


