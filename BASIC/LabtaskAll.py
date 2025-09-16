# number swap
#  num1 = 10
#  num2 = 20

# temp = num1
# num1 = num2 
# # num2 = temp
# temp =num2

# Swapping Number
# num1 = 10
# num2 = 20

# print(f"\nBefore Swapping {num1}")
# print(f"\nBefore Swapping : {num2}")

# temp = num1
# num1 = num2
# num1 = temp

# print(f"\nAfter Swapping {num1}")
# print(f"\nAfter Swapping : {num2}")

# Swapping Number Without using thrid Party Vriable

# num1 = 10 
# num2 = 20

# num1 , num2 = num2 , num1 

# print("num1 =" , num1, "num2 =" , num2)


#----------------------------------------------------->


# num = int(input (" Enter Number"))
# for i in range (num):
#     for j in range (i,num):
#         print("*" , end = " ")
#     print( )
# for i in range (num):
#     for j in range (i):
#         print("*" , end = " ")
#     print( )

#--------------------------------------------------------->

# month = input("enter  a month")
# if month=="january" or month== "march" or month=="may" or month== "july" or "october" or "Descember":
#       print("31")
# elif month =="fabruary":
#       print("28 or 29 days") 
# elif month== "april" or month=="june" or month=="august" or month== "septamber":
#       print("30") 
# else : 
#       print("invalid number")    


  
# # Method no 2 ------------------------------------------->


# # month = input("Enter month name")

# if month in ('January' ,  'March','may' , 'July' , "Descember"): 
#       print("31 days")
# elif month== "Fabruary":
#      print ("28 or 29 days")
# elif month in ("April" ,"June" , 'August' , 'Septamber'):
#      print("30 days")
# else :
#     print("Invelid Number")


        
# #Method number 3 ---------------------------------------------->
#  month = input ("enter  a month")
 
#  Macth month: 
#     case 'January' | 'March' | 'May' |'July' | 'Octomber' | 'December':
#         print("31 days")
#      case 'April' | 'June' | 'August' | 'September' | 'Navembe':
#         print("30 days")  
#     case 'February':
#         print("28 or 29 days")
#     case _ :
#         print("Invelid Number") 



# Count Evan and odd number ---------------------------------------->


# start = int(input("Enter Srart Number"))
# end = int(input("Enter End Number"))
# Count_Evan = 0 
# Count_Odd = 0
# for i in range(start ,end + 1):
#   if i % 2== 0 : 
#        Count_Evan+=1
#   else: 
#       Count_Odd+=1
#   total_num = count_even + count_odd

#   print(f"total number = {total_num}:::Evan = {Count_evan} and odd = {odd_num}")  


 
# 16th sep -------------------------------->


# for i in range (10):
#     print(i)
#     if i== 4:
#         break
#     print("ENd")


#While
 
# i =0
# while i<=10:
#     print(i)
#     if i==4:
#         break
#     i+=1
   

# for i in range (10):
#     if i == 4:
#         continue
#     print(i)
    

# for i in range (10):
#     if i == 4:
#        pass
#     print(i)


# string sequnce of name ------------------------->

# " vishwraj 777"
# 'vishwraj'  #String

# # string example

# c_name = "Tops Tachnologies"
# s = c_name.upper()
# print(s) 

# c_name = "Tops Tachnologies"
# s = c_name.lower()
# print(s)

# c_name = "Tops Tachnologies"
# s = c_name.title()
# print(s) 

# c_name = "Tops Tachnologies"
# s = c_name.capitalize()
# print(s) 

#lab task 16 sep

# for i in range(5):
#     user_input = input(f"Enter string {i+1}: ")
#     print(user_input.upper())
#     print(user_input.lower())
#     print(user_input.title())
#     print(user_input.capitalize())


# num = int(input (" Enter Number rows :"))
# count = 1
# for i in range (1 , num+1):
#     for j in range (1 , i+1):
#         print(count , end = " ")
#     print( )
#     count +=2


# --------------------------------------->


# month = input("Enter month :")
# if month == 'january' or month == 'march':
#       print("31 days")
# elif month == "february":
#       print("28 days")
# elif month == 'april' or month == 'june':
#       print("30 days")            
# else :
#       print("invelid number")


#-------------------------------------------------->


#comperition_opretor

# number1 = int(input("plesae enter number1"))
# number2 = int(input("plesae enter number2"))
# print(number1>number2)
# print(number1<number2)
# print(number1>=number2)
# print(number1<=number2)
# print(number1!=number2)
# print(number1==number2)

# #arethmatic_opretor

# a = 5
# b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)
# print(a // b)


# #assiment_opretor

# num = 10 
# num += 10
# print("num :", num )

# num *= 10
# print("num :", num )

# num -= 10
# print("num :", num )

# num /= 10
# print("num :", num )

# num %= 10
# print("num :", num )

# num **= 10
# print("num :", num )

# num //= 10
# print ("num :" , num )


# # example of hellow *5

# a= input ("enter value : ")
# print(f"{a} * 5 is {a * 5 }")
# []



#---------------------------------------------->


# #if and else
# num = int(input("age "))
# if num<18:
#     print("you are just mainor")
# else:
#     print("you are in adult")



#-------------------------------------------->


# marks = int (input(" Enter your marks "))
# if marks  >=90 and marks <= 100:
#     print("You got A grede. ")
# elif marks < 90 and marks >= 70:
#     print("You got B grede. ")
# elif marks < 70 and marks >= 60:
#      print("You got C grede. ")    
# elif marks < 60 and marks >= 50:
#      print("You got D grede. ")   
# else:
#      print("You got E grede. ")


# #------------------------------------------------->


# print("\n1. addition : + ")
# print("\n2. Subtraction : - ")
# print("\n3. Multiplication : * ")
# print("\n4. Division: / ") 

# choice =int(input("Enter your choice "))
# number1=int(input("Enter number "))
# number2=int(input("Enter number "))

# match choice:
#     case 1:print(f"Addition is ",number1+number2)
#     case 2:print(f"Subtraction is {number1-number2}")
#     case 3:print(f"Multilication is {number1*number2}")
#     case 4:print(f"Division is {number1/number2}")
#     case 5:print(f"floor Division is {number1/number2}")
#     case _:print("Invalid choice ") 

#------------------------------------------------------------->
        

