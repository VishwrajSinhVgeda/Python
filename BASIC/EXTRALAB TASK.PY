#string to upper case using list comprehension

names = ['vishwraj', 'aniket', 'sanket', 'amol', 'rohit']
upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)  # Output: ['VISHWRAJ', 'ANIKET', 'SANKET', 'ROHIT']

#square  of even number from the list using list comprehension
lst = [23, 56, 78 , 22 , 45 , 88 , 12]
squares_lst = [i**2 for i in lst if i % 2 == 0]
print(squares_lst)  # Output: [3136, 6084, 7744, 144]

#Creatr a new tuple with evan number and their square comprehension

tup = (23, 56, 78 , 22 , 45 , 88 , 12)
new_tup = tuple((i, i**2 , i**3) for i in tup if i % 2 == 0)
print(new_tup)  # Output: ((56, 3136), (78, 6084), (22, 484), (88, 7744), (12, 144))

#creat a new tup with evan number , their square and their cube but sum of the middle value  is in new varuable

tup = (23, 56, 78 , 22 , 45 , 88 , 12)
sum = 0
for i in tup:
    if i % 2 == 0:
        square = i ** 2
        cube = i ** 3
        sum += square 
        print((i, square, cube))
print("Sum of squares of even numbers:", sum)


# Write a program to remove all items from a list that are less then 5 e.g [12,3,4,5,67,0] output [12,5,67]

lst = [12, 3, 4, 5, 67, 0]
new_lst = [i for i in lst if i >= 5]
print(new_lst)  # Output: [12, 5, 67]


#Write a program to find common among 2 lists. eg. lst_numbers = [1,2,34,33,21] lst_numbers2=[11,2,33,45] output [2,33]

lst_numbers1 = [1, 2, 34, 33, 21]
lst_numbers2 = [11, 2, 33, 45]
common = list(set(lst_numbers1) & set(lst_numbers2))
print(common)  # Output: [2, 33]

#Write a program to sort a list of strings by their length e.g ['apple', 'banana', 'kiwi', 'orange'] output : ['kiwi', 'apple', 'orange', 'banana']

fruits = ['apple', 'banana', 'kiwi', 'orange']
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)  # Output: ['kiwi', 'apple', 'orange', 'banana']


#Write a program to accepts a list of integers and returns a tuple with the sum of all positive numbers and the sum of all negative numbers

numbers = [1 , 2 , 3, -3, -2, -1]
positive_sum = sum(i for i in numbers if i > 0)
negative_sum = sum(i for i in numbers if i < 0)
result = (positive_sum, negative_sum)  
print(result)  # Output: (6, -6) # sum() is used to calculate the sum of elements in an iterable

# write a program that takes a list of number and tuple containing the sum and product of all the numbers.
numbers = [1, 2, 3, 4 , 5, 6]
total_sum = sum(numbers)
total_product = 1 
for i in numbers:
    total_product *= i
result = (total_sum, total_product)
print(result)  # Output: (21, 720)


# Write a program to create a dictionary with key and value as a list of name , subject , city , marks of 3 subjects. Calculate total marks of each student and print total marks.

dict1 = { 101 : [ 'Vishwraj' , ' Python' , 'Dholka' ,  90  ,80 ,70] ,
          102 : [ 'Romil' ,  ' Java' , 'Ahmedabad' ,  80 ,70 ,60] ,
          103 : [ 'Abhijit' ,  ' PHP' , 'Nimaj' ,  70 ,60 ,50] ,

}
for key , value in dict1.items():
    total = sum (value[3:])
    print(f"Total marks of {value[0]} is {total}")

# output = Total marks of Vishwraj is 240
# Total marks of Romil is 210
# Total marks of Abhijit is 180


# Count frequency of list items and write in into dictionary :input List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
# output : {1: 2, 2: 2, 3: 1, 4: 2, 5: 2, 6: 1, 7: 2}

lst = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
frequency = {}    
for item in lst:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)  # Output: {1: 2, 2: 2, 3: 1, 4: 2, 5: 2, 6: 1, 7: 2}


# Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.

name = input("Enter your name: ")
if len(name) > 5:
        print(name.upper())
else:
     print(name.lower()) 


# #Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.

text = input("Enter a string: ")

result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i].upper()   # even index → uppercase
    else:
        result += text[i].lower()   # odd index → lowercase

print(result)

# Write a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values ]

numbers = [10, 0, 20, 30, 0, 40]
non_zero_numbers = [i for i in numbers if i != 0]
if len(non_zero_numbers) > 0:
    average = sum(non_zero_numbers) / len(non_zero_numbers)
    print("Average (excluding zeros):", average)
else:
    print("No non-zero numbers to calculate average.")
# Output: Average (excluding zeros): 25.0

#Write a function that accepts a string and returns True if the string is a valid email address (contains "@" and "."), otherwise False.

email = input("Enter an email address: ")

if "@" in email and "." in email:
    print(True)
else:
    print(False)
# Output: True or False based on the input


#Write a function that accepts a list of integers and returns the second largest number in the list.

numbers = [10, 20, 4, 45, 99, 99]
unique_numbers = list(set(numbers))  # Remove duplicates  
unique_numbers.sort()  # Sort the list
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]  # Second largest number
    print("Second largest number is:", second_largest)


#--------------------[Function Examples]----------------------

# Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.
def divisible(num):
    new_lst = []
    for i in num:
        if i % 3 == 0:
            new_lst.append(i)
    return new_lst
num = [10, 21, 33, 46, 55, 60, 72]
print(divisible(num))  # Output: [21, 33, 60, 72]


# Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.
def square_numbers(num):
    square_numbers =[]
    for i in num:
        square_numbers.append(i ** 2)
        return square_numbers
    numbers = [1,2,3,4,5]
    print(square_numbers(numbers))  # Output: [1, 4, 9, 16, 25]
# Write a function that accepts a string and counts how many vowels are in the string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
string = "Hello World"
print(count_vowels(string))  # Output: 3

# Write a function that accepts a list of strings and returns the longest string in the list.
def longest_string(srings):
    lomgest =""
    for s in strings:
        if len (s) > len (longest_string):
            longest_string = s
            return longest_string
strings = ["apple", "banana", "kiwi", "orange"]
print(longest_string(strings))  # Output: "banana"


# Write a function that accepts a number and checks if it is an Armstrong number.
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num
number = 153
print(is_armstrong(number))  # Output: True


# Write a function that accepts a number and returns the sum of its digits.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
number = 12345
print(sum_of_digits(number))  # Output: 15

# Write a function that accepts a list of strings and returns a new list with only the strings that have an odd length.
def odd_length_strings(strings):
    return [s for s in strings if len(s) % 2 == 1]
strings = ["apple", "nut","kiwi", "pear", "fig"]
print(odd_length_strings(strings))  # Output: ["nut", "fig"]

# Write a function that accepts a string and a substring, and returns True if the substring is found in the string, otherwise False.
def contains_substring(string, substring):
    return substring in string
string = "hello world"
substring = "world"
print(contains_substring(string, substring))  # Output: True

# Write a function that accepts a list of numbers and returns a new list with all the numbers that are divisible by both 2 and 3.
def divisible_by_2_and_3(numbers):
    return [n for n in numbers if n % 2 == 0 and n % 3 == 0]
numbers = [1, 2, 3, 4, 5, 6, 12, 18]
print(divisible_by_2_and_3(numbers))  # Output: [6, 12, 18]


# Write a function that accepts two strings and returns the common characters between them
def common_characters(str1, str2):
    return set(str1) & set(str2)
str1 = "hello"
str2 = "world"
print(common_characters(str1, str2))  # Output: {'o', 'l'}

# Write a function count_character(string, char) that accepts a string and a character, and returns the number of times the character appears in the string.
def count_character(string, char):
    return string.count(char)
string = "hello"
char = "l"
print(count_character(string, char))  # Output: 2

# Write a function concatenate_with_separator(lst, separator) that accepts a list of strings and a separator string, then returns a new string where all elements of the list are joined using the separator.
def concatenate_with_separator(lst, separator):
    return separator.join(lst)
strings = ["apple", "banana", "cherry"]
separator = " / "
print(concatenate_with_separator(strings, separator))  # Output: "apple / banana / cherry"

# Write a function merge_dicts(dict1, dict2) that accepts two dictionaries and returns a single dictionary that contains the merged key-value pairs from both dictionaries.
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 3, 'c': 4}

# Write a function longest_word(sentence) that accepts a sentence and returns the longest word in the sentence.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
sentence = "The python programming language is awesome"
print(longest_word(sentence))  # Output: "programming"

# Write a function create_frequency_dict(lst) that accepts a list and returns a dictionary where the keys are the elements of the list, and the values are the count of how often each element appears.
def create_frequency_dict(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency
lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(create_frequency_dict(lst))  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# Write a function merge_lists_into_dict(list1, list2) that accepts two lists of equal length and merges them into a dictionary where the keys are the indices (0 to n-1) and the values are the elements from both lists.def merge_lists_into_dict(list1, list2):
def merge_lists_into_dict(list1, list2):
    merged_dict = {}
    for i in range(len(list1)):
        merged_dict[i] = (list1[i], list2[i])
    return merged_dict
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(merge_lists_into_dict(list1, list2))  # Output: {0: ('a', 1), 1: ('b', 2), 2: ('c', 3)}


#-------------------[Map Function Example]----------------------

#Write a Python program that uses `map()` to convert a list of strings to uppercase. Input: `['apple', 'banana', 'cherry']` - Output: `['APPLE', 'BANANA', 'CHERRY']`
   
def to_uppercase(s):
    return s.upper()
fruits = ['apple', 'banana', 'cherry']
print(list(map(to_uppercase, fruits)))  # Output: ['APPLE', 'BANANA', 'CHERRY']

#Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]`
celsius = [0, 25, 100]
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print(fahrenheit)  # Output: [32.0, 77.0, 212.0]


# Write a Python program that uses the `map()` function to square each number in a given list of integers. Input: `[1, 2, 3, 4]` , Output: `[1, 4, 9, 16]`
def square(num):
    return num * num
print(list(map(square, [1, 2, 3, 4])))  # Output: [1, 4, 9, 16]

# Write a Python program that uses `map()` to convert a list of strings to uppercase. Input: `['apple', 'banana', 'cherry']` - Output: `['APPLE', 'BANANA', 'CHERRY']`
def to_uppercase(s):
    return s.upper()
print(list(map(to_uppercase, ['apple', 'banana', 'cherry'])))  # Output: ['APPLE', 'BANANA', 'CHERRY']

# Write a Python program that uses `map()` to find the length of each string in a list of strings. Input: `['hello', 'world', 'python']` Output: `[5, 5, 6]`
def find_length(s):
    return len(s)
print(list(map(find_length, ['hello', 'world', 'python'])))  # Output: [5, 5, 6]

# Write a Python program that uses `map()` to add a given number to each element in a list. - Input: `[1, 2, 3, 4]`, `5` Output: `[6, 7, 8, 9]`
def add_number(num):
    return num + i
lst = [1, 2, 3, 4]
i = 5
ans = list(map(add_number, lst))
print(ans)  # Output: [6, 7, 8, 9]

# Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]`
def c_to_f(celsius):
    return (celsius * 9/5) + 32
celsius_values = [0, 25, 100]
fahrenheit_values = list(map(c_to_f, celsius_values))
print(fahrenheit_values)  # Output: [32.0, 77.0, 212.0]
