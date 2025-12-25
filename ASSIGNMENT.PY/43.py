# 43 . What is tuple? Difference between list and tuple. 
# Answer :

# Tuple is a collection of elements enclosed in parentheses. 
# It is immutable, meaning once created, its elements cannot be changed.

# Example of a tuple

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple) # Output : Tuple: (1, 2, 3, 4, 5)

# Explanation :
# my_tuple = (1, 2, 3, 4, 5)    
# This creates a tuple with 5 elements.
# print() → prints the tuple

# Example of a list 
# A list in Python is a collection of items that are:Ordered , Changeable (mutable)
# Can store different types of data

my_list = [1, 2, 3, 4, 5]
print("List:", my_list) # Output : List: [1, 2, 3, 4, 5]

# Explanation :
# my_list = [1, 2, 3, 4, 5]
# This creates a list with 5 elements.
# print() → prints the list

# Difference between List and Tuple :


# | Feature  | List                                | Tuple                       |
# | -------- | ----------------------------------- | --------------------------- |
# | Brackets | [ ]                                 | ( )                         |
# | Mutable  | Yes (can change)                    | No (cannot change)          |
# | Speed    | Slower                              | Faster                      |
# | Memory   | Uses more memory                    | Uses less memory            |
# | Methods  | Many methods (append, remove, etc.) | Very few methods            |
# | Use case | When data needs to change           | When data should stay fixed |

