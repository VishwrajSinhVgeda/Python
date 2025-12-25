# what is decoretor in python ?
# A decorator in Python is a special type of function that modifies the behavior of another function or method.

# Decorators allow you to wrap a function with another function,
# enabling you to add functionality before and after the execution of the original function

#----------------------------------->
# decoreter Example 1

# def decorete(fuction):
#     def wrapper():
#         print("function calling")
#         fuction()
#         print("function ending")
#     return wrapper
# # @decorete
# # def greet ():
# #     print ("good morning")

# # @decorete
# def add ():
#     print (12+23)
# # greet()
# add()       

#----------------------------------->
# decoreter Example 2

# import time
# def time_chake(func):
#     def wrapper():
#         print(f"Start At {time.time()} ")
#         func()
#         print(f"End At {time.time()}")
#     return wrapper
# @time_chake
# def count():
#     C =0 
#     for i in range(10000):
#         C+=1
# count()

#----------------------------------->
# Decoreter Example 3

# def decoreter_peramiter(func):
#     def wrapper (*args , **kwargs):
#         print(args)
#         print(kwargs)
#         func(*args, **kwargs)
#         result = func(*args,**kwargs)
#         return result
#     return wrapper
# @decoreter_peramiter
# def greet(name , age,address):
#      print (f"Hello {name}! You are {age} years old and live in {address}.")

# greet ("Vishwraj", 25, "C G Road")    



#--------------------------------->
# Decoreter Example 4

# from unittest import result
# from Function import wraps
# import logging
# logging.basicConfig(level=logging.INFO)

# def log_decoretoer(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         logging.info(f"Calling:{func.__name_}")
#         logging.info(f"Arguments:args={args}, Kwargs={kwargs}")
#         result=func(*args, **kwargs)
#         logging.info(f"Retuned:{result}")
#         return result
#     return wrapper
# @log_decoretoer
# def count(num):
#     c = 0
#     for i in range(num):
#         c+=1
#         return c
#     @log_decoretoer
#     def greet(name,msg):
#         return f"Hello {name}, {msg}!"
#     greet(name = "Vishwraj", msg = "welcome.")
# count(1000)

#--------------------------------->
# RE Example 1 :-

# import re
# msg = "This is betatiful 1234 morning"
# match = re.search(r"is",msg)
# print(match)


# match1 = re.match(r"\d",msg)
# print(match1)