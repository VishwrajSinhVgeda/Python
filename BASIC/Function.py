# Functions and Module 


# ---> functions are set of instruction to perform perticular task 
# 	built in & user defined 
#     build in -- input(),print(),upper(),lower(),int(),list(),append()....
# 	you can create your own function - user defin
# 	usign def keyword 
#    function declaration/definition
# 	def function_name():
# 		stmt
# 		stmt
# 		stmt
#      function call
#      function_name()
#      functions have parameter and return 
#      return ? always return 



# Example -: 1

# def f1():
#     print("Good Morning Vishwarj ")
# def close():
#     print("Bye..")
#     print("This is example of function ")
# f1()

# close()
# close()


# # Paramerized function 
# def greet(name,grade,age):
#     print("Good Morning ",name,"You have ",grade," and age is ",age)
    

# greet("vishwaraj","Grade A",23)
# greet("Romil","Grade A+",23)



# #Example -: 2 loop , input 

# def greet(name,grade,age):
#     print("Good Morning ",name,"You have ",grade," and age is ",age)
    
# for i in range(3):
#     n=input("Enter name ")
#     g=input("Enter grade ")
#     a=int(input("Enter age "))
#     greet(n,g,a)


# # Example -: 3

# def chekeNumber(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# ans=chekeNumber(23)
# print(ans)



# #Example -: 4 function with return 

# def checkNumber(num):
#     if num%2==0:
#         return "EVEN"
#     else:
#         return "ODD"

# ans=checkNumber(23)
# print(ans)
# ans=checkNumber(922222)
# print(ans)
# for i in range(100):
#     print(f"{i} - {checkNumber(i)}")    


# Example 5  type of function

# default arguments
# keyword arguments
# variable length arguments

# from unicodedata import name

# def addition (*args):
#     sum=0
#     for i in args:
#         if type(i)==int:
#            sum+=i
#     return sum
# print(addition(12,23))
# print(addition(1,2,3,4,5,6,))
# print(addition(10,20,30,name,40,50))

# # Example 5 

# def greet(name,age=20):
#     print("Good Morning ",name,age)

# greet("Dharmishtha",30)
# greet("Vishwraj")
# greet("Dhruv")
# greet("Abhijit",22)

# # Example 6
     
# def greet(name,msg):
#     print(name,msg)
# greet("Good morning","Dharmishtha")
# greet(msg="Good morning",name="Dharmishtha")

# # Example 7

# def personDetails(*abhi):
    
#     for i in abhi:
#         print(i)

# print("Person1 ")
# personDetails(101,"Dharmishtha",30)
# print("Person2 ")
# personDetails(201,"Abhijit","BTech","Ahemedabad")
# print("Person 3 ")
# personDetails("Dhruv","BTech","dhruv@gmail.com",1213134)


# # Example 8

# def addition(*args):
#     sum=0
#     for i in args:
#         if type(i)==int:
#             sum+=i
#     return sum
# ans=addition(12,23)
# print(ans)
# print(addition(23,657,5656))
# print(addition(23,345,567567,13123,34.5656))
# print(addition(23,345,"ertertre",567567,13123))


# def addition (*args):
#     sum=0
#     for i in args:
#         if type(i)==int:
#            sum+=i
#     return sum
# print(addition(12,23))
# print(addition(1,2,3,4,5,6,))
# print(addition(10,20,30,name,40,50))

# # Example 9

# def personDetails(**kwargs):
#     #print(kwargs)
#     if kwargs['age']>=30:
#         print(kwargs['name'])
# def details():
#     return 1,"Dharmishtha",30,"Python"
# personDetails(name="Dharmishtha",age=30)
# personDetails(city="Ahedmbad",name="Dhruv",age=20)
# personDetails(name="Abhijit",age=22)
# personDetails(name="etets",age=30)
# print(details())




