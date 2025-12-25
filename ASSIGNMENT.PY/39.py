#39 .Write a Python program to find the second smallest number in a list. 

# Answer :

numbers = [12, 5, 7, 3, 9]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_smallest = unique_numbers[1]

print("Second smallest number is:", second_smallest)

# Output : Second smallest number is: 5    

#Explainnation :
#set(numbers) → removes duplicate values
#sort() → arranges numbers in ascending order
#unique_numbers[1] → gives the second smallest element