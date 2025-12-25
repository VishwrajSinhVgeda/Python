#what is RE  Regular Expression in Python ?

#RE (Regular Expression) is a pattern-matching tool used to:
#atch patterns 
#Validate input (email, phone, password)
#Extract data
#Replace text
#In Python, Regular Expressions are handled using the re module.

#______________________________________________>
# RE Example 1 :-

# import re
# msg = "This is betatiful 23456 morning"
# match = re.search(r"is",msg)    
# #match=re.serch(r"\d",msg)
# print(match)

# if match:
#     print(f"{match.start()} - {match.end()} - {match.span()}")
# match1 = re.match(r"\d",msg)
# print(match1)


#______________________________________________>
# RE Example 2 :-

# import re

# msg = "This is betatiful ,Today is beatiful Morning"
# match = re.search(r"\Amorning",msg)
# print(match)

# msg1 ="Thisn is Good Morning , good Aftrenoon"
# #match1 = re.serch(r"d+,"test 122 12345")
# #print(match1)

# lst = re.findall(r"\d+","test 122 12345")
# for i in lst:
#     print(i)    
# lst = re.findall(r"\d+", "test 122 12345")    

#______________________________________________>
# RE Example 3 :-

# import re

# msg = "This is IND, This is JPA"
# match = re.search(r"JPA$",msg)
# print(match)

#______________________________________________>
# RE Example 4 :-

# import re

# lst =re.findall(r"\d{10}", "test 122 1234567890")
# for i in lst:
#     print (i)

#______________________________________________>
#Labtask 1
#Differentiate search , match ,

# from ast import pattern
# import re

# lst = ['test','23232344','sdfsdfdsf2323','33333333']
# count = 0

# for item in lst:
#     if re.fullmatch(r'\d{8}', item):
#         count += 1

# print("Total contact numbers:", count)

#______________________________________________>
# # Example 5 :-

# import re
# lst_co_nummber = ['+91779069433', '+331234567890', '9-0987654321']
# r.search(r"+\d{2}- \d{10}",i)
     


import re
lst_email_address = ['vishwrajvegda@gmail.com', '123@.com']
match 

# for item in lst_email_address:
#     if re.fullmatch
#         print(f"{item} is valid email address")
#     else:
#         print(f"{item} is invalid email address")
