#example of reduce function 1

data = [{'name': 'Vishwraj', 'age':24},
        {'name': 'Romil', 'age': 23},
        {'name': 'Abhijit', 'age': 22}]
def add_age(x,y):
    return x + y
def get_ages(i):
    return i ['age']
from functools import reduce
ages = list(map(get_ages, data))
average_age = reduce(add_age, ages) / len(ages)
print("Average age is:", average_age) #Output: Average age is: 23.0)




