# 29 . Write a Python function to get the largest number, smallest num 
#and sum of all from a list. 

# Answer :

def list_details(numbers):
    largest = max(numbers)      # biggest number
    smallest = min(numbers)     # smallest number
    total_sum = sum(numbers)    # sum of numbers
    
    return largest, smallest, total_sum


# Example list
my_list = [10, 50, 3, 99, 45]

# Call the function
big, small, total = list_details(my_list)

print("Largest number:", big)
print("Smallest number:", small)
print("Sum of all numbers:", total)


# Output : Largest number: 99
#          Smallest number: 3     
#          Sum of all numbers: 207

# # Explainntion :
#                 List = [10, 50, 3, 99, 45]
#                 Largest = 99
#                 Smallest = 3 
#                 Sum = 10 + 50 + 3 + 99 + 45 = 207