# create function which accept a number and return "Prime" or "Not Prime"
# def checkPrime(n):
#     if n <= 1:
#         return "Not Prime"
#     for i in range(2, n):
#         if n % i == 0:
#            return "Not Prime"
#     return "Prime"
    
# num = int(input("Enter a number: "))
# print(checkPrime(num))


# create function to check string is palidrome or not 

# def isPalindrome(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s
#     return s == reversed_s

# str = input("Enter a string: ")
# print(isPalindrome(str))


# fix parameter name and other details may ne differ

# def displayInfo(name, age, city):
#     print("Name:", name)
#     print("Age:", age)
#     print("City:", city)

# displayInfo(age=25, city="New jersey", name="Vishwraj")


# def square(num):
#     print(f"{num} - {num * num}")

# lst = [1,2,3]
# for i in lst:
#     square(i)



def square(num):
    return  num * num
lst = [1,2,3]
anslst = []
anslst = map(square, lst)
print(list(anslst))