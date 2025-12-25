# Example of Exception 1 :-

no =int(input("Enter a number: "))
print(no)
ans = no/2
print(f"After division {ans}")
dict1 = {"name": "Vishwraj" , "age": 24}
print(f"Dictnary value is {dict1['name']}")
with open("abc", "r") as file:
    data = file.read()

#------------------------------------------------------
# Example of Exception 2 :-    
try:
    no = input("Enter a number: ")
    no1 =int(no)
    print(f"value is {no1}")
    ans = no1/2
    print(f"(Ans){ans}")
except:
    print("There is an exception")

#------------------------------------------------------
# Example of Exception 3 :-
 
try: 
    no = input("Enter a number: ")
    no1 =int(no)
    print(f"value is {no1}")

    ans = no1/2
    print(ans)
except ZeroDivisionError:
    print("There is a zero division error")
except ValueError:
    print(" There is value error")
finally:
    print("Have Great Day Ahead!")

#------------------------------------------------------
# Example of Exception 4 :-

import traceback
try:
    no = input("Enter a number: ")
    no1 =int(no)
    print(f"value is {no1}")

    ans = no1/0
    print(f"Ans {ans}")
except ZeroDivisionError:
    print("There is a zero division error")
    traceback.print_exc()
except ValueError:
    print(" There is value error")
    traceback.print_exc()
finally:
    print("Have glorious Day Ahead!")

#------------------------------------------------------
# Example of Exception 5 :-

from ast import In
import traceback
try:
    no = input("Enter anumber")
    print(f"Here is no {no}")
except:
    traceback.print_exc()
else:
    print("In Else")
finally:
    print("In finally")

#------------------------------------------------------------
#Example of Exception 6 :-

import traceback
class lenthException(Exception):
    pass
try:
    name = input("Enter your name: ")
    if len(name)>20:
        raise lenthException("Name is must be less than 20 characters long")
    address = input("Enter your address: ")

    if len(address)<5:
        raise lenthException("Address is to short")
    age = int(input("Enter your age: "))
    if age<0:
        raise ValueError("Age must be > 18")
except lenthException as e:
    print(f"{e}")
    traceback.print_exc()
except ValueError as e:
     print(f"{e}")