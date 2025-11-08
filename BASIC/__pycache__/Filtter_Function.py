#Example of filter function 1

def checkEven(num):
    if num % 2 == 0:
        return num
lst_num = [1,2,3,4,5,6,7,8,9,10]
evenlst = filter(checkEven, lst_num)
print(list(evenlst))


#Example of filter function 2

def city_length(city):
    if len(city) > 5:
        return city
lst_city = ['Ahemdabad', 'Surat', 'Rajkot', 'Vadodara', 'Patan']
ans = filter(city_length, lst_city)
print(list(ans))


#Example of filter function 3

# square of even number from list

lst_num = [1,2,3,4,5,6,7,8,9,10]
def checkEven(num):
    if num % 2 == 0:
        return num

def squre(num):
    return num * num

evenlst = filter(checkEven, lst_num)
squrelst = map(squre, evenlst)
print(list(squrelst))


# lab task

# 1.convert those city into uper case whose lanthe is more then 5

lst_city = ['Ahemdabad', 'Surat', 'Rajkot', 'Vadodara', 'Patan']
def city_length(city):
    if len(city) > 5:
        return city
ans = list(filter(city_length, lst_city))
list1 = list(map(str.upper, ans))
print(list1)



# 2.convert Celsius to Fahrenheit.

def c_to_f(celsius):
    return (celsius * 9/5) + 32

lst_celsius = [0, 20, 37, 100]
lst_fahrenheit = list(map(c_to_f, lst_celsius))
print(lst_fahrenheit)
