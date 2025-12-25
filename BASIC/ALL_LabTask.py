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


  
# # Method no 2 ------------------------------------------->


# month = input("Enter month name")

# if month in ('January' ,  'March','may' , 'July' , "Descember"): 
#       print("31 days")
# elif month== "Fabruary":
#      print ("28 or 29 days")
# elif month in ("April" ,"June" , 'August' , 'Septamber'):
#      print("30 days")
# else :
#     print("Invelid Number")


        
# #Method number 3 ---------------------------------------------->
#  month = input ("enter month")
 
      
# match month:
#       case 'January' | 'March' | 'May' |'July' | 'Octomber' | 'December':
#         print("31 days")
#       case 'April' | 'June' | 'August' | 'September' | 'Navembe':
#         print("30 days")  
#       case 'February':
#         print("28 or 29 days")
#       case_ :
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
        
# 18 sep

# Find Method 

# c_name = "Tops tachnogies"
# i = c_name.find("s t")
# print(i)   
# i = c_name.find("s ,4 , 16")
# print("After 4th position ",i)

#find function is return the possition of sub string

# print(len(c_name))
# count = c_name.count("Tops tachnogies")
# print("count of Tops  tachnogies is :" , count)

# print(len(c_name))
# santence = "cat is animal and dog is animal"
# count = santence.count("animal")
# print("count of animal is :" , count)

#Replace Method

# str1 = "Tops"
# str2 = "12345"   
# str3 ="Tops@1234" 
# srt4 = "Tops tach"

# print(str1.isdigit() , str1.isalpha() , str1.isalnum())
# print(str2.isdigit() , str2.isalpha() , str2.isalnum()) 
# print(str3.isdigit(), str3.isalpha() , str3.isalnum())
# print(srt4.isdigit() , srt4.isalpha() , srt4.isalnum())

# lab task 18sep ------------------------------>

#print(srt1.isalpaha()) # True (only letters)
#print(srt2.isdigit()) # True (only numbers)
#print(srt3.isalnum()) # False ( @ symbol not allowed)
#print(srt4.isalnum()) # False (space not allowed)          

# User input
# string_input = input("Enter a string:")
# print(string_input.isdigit(), string_input.isalpha(), string_input.isalnum())

# sentence = input("Enter sentense ")
# print(f"{sentence} original ")
# word = input("Enter word to replace ")
# new_word = input("Enter new word to replace")
# new_sentense=sentence.replace(word,new_word)
# print(f"{new_sentense} after replacement ")
# sentence=sentence.replace(word,new_word)
#  print(f"{sentence} original ")


# 20sep------------------------------------->

# msg = "have a good day"
# print(msg.endswith("!!!"))
# email = "test@gmail.com"
# email = input("Enter your email : ")
# if email.endswith(".com"):
#     print("valid email")
# else:
#     print("invalid email")


#string with positive index


# str = "This is python"
# print(str(4))  #s
# print(str(0))  #T
# print(str(7))  #p
# print(str(13)) #n 
# print(len(str))


# string with negative index [leb task]
# str = "This is python"
# print(str[-1])  #n
# print(str[-2])  #o
# print(str[-3])  #h
# print(str[-4])  #y
# print(str[-5])  #t
# print(str[-6])  #p
# print(str[-7])  #
# print(str[-8])  #s
# print(str[-9])  #i
# print(str[-10]) #
# print(str[-11]) #s
# print(str[-12]) #i
# print(str[-13]) #h
# print(str[-14]) #T

# name = input("Enter your name : ")
# length = len(name)
# print("Length of your name is :", length) 

# for i in range(1,length+1):
#     print(f"Character at index {-i} is: {name[-i]}")

# #accessing thru index with index
# name = input("Enter your name : ")
# for i in name:    
#     print(i)

#chek vavol in string

# str1 = input("Enter string : ")
 
# vavol= 0
# for i in range (len(str1)):
#         if str1[i].lower() in 'aeiou':
#             vavol +=1
# print("vavol is :" , vavol)


# slicing --- part/ portion 

# str = "Tops Tachnologies"
# print(str[1:5])  #ops
# print(str[1:7])  #ops Tac     
# print(str[0:4])  #Top
# print(str[5:10]) #is T
# print(str[5:])   #is Tachnologies
# print(str[:10])  #Tops Tachn


# upto 10 letters

# print(f"{str[:10]} upto 10 letters")
# print(f"{str[10:]} after 10 letters")
# print(f"{str[::2]} after 2 letters")      
# print(f"{str[::3]} alternate letters")



# 23 sep --------------------------------->

#slicing half string and reverseing 

# Name = input("Enter your name : ")
# total_length = len(Name)
# half = total_length // 2
# first_half = Name[:half]
# last_half = Name[half:] 
# print(f"First half: {first_half} last {last_half}")")
# print(f"Reversed name: {Name[::-1]}")
# print(f"Reversed first half: {first_half[::-1]}")

# nam = input("Enter your name : ")
# str =  input("Enter your name : ")  
# length = len(str)
# half = length // 2  
# first_half = str[:half]
# last_half = str[half:]  
# print(f"{first_half} first half")
# print(f"{last_half} last half")
# print(f"{str[::-1]} reverse string")    

#split method ----------------------------->

# name = "Tops Tachnologies pvt ltd"
# lst  = name.split()
# print(lst)
# lan1 = name.split("t")
# print(f"split by t : {lan1}")


# join method ----------------------------->


# name = ['Tops', 'Tachnologies', 'pvt', 'ltd']
# str = ' '.join(name)
# print(str)

#join Method No 2 ----------------------------->

# name =['Apple',"banana","Cherry"]
# fruits = " ".join(name)
# print(fruits)
# fruits = "*".join(name)
# print(fruits)

#strip Method ----------------------------->

# name = "   Tops Tachnologies pvt ltd   "
# print(len(name))
# name = name.strip()
# print(len(name))

# sort method ----------------------------->

# names = ['Vishwraj', 'Aniket', 'Sanket', 'Amol', 'Rohit']
# str = sorted(names, key=len)
# print(str)


# print the last half string and other half

# str = input("Enter your name : ")
# length = len(str)
# half = length // 2
# print(f"string : {str[half:]}{str[:half]}")

#List --------------------------------->

# num_lst1 = [1, 2 ,67, 89, 56]
# sum = 0
# for i in num_lst1:
#     sum += i
# print("Sum of elements in num_lst1:", sum)  


# 4 oct ---------------------------------------------->

# want to convert all string into upper case

# lst=[2,4,6,8,10,]
# lst= [i**2 for i in lst]
# print(lst)

#list comprehension

# lst1=[2,4,6,8,10,]
# lst2=[i for i in lst1]
# print(lst2) #output: [2, 4, 6, 8, 10] 
# lst3=[i*2 for i in lst1]
# print(lst3) #output: [4, 8, 12, 16, 20]



# 7 oct -------------------------------------------------->

#dictionary
# dict1 = { 1: "ahmedabad", 2: "surat", 3: "baroda", 4: "rajkot"}
# print(dict1)
# print = dict1.keys()
# for k,v in dict1.items():
#     print(f"key is {k} and value is {v}")
# print(dict1.values())
# print(dict1.items())

# for k in dict1.keys():
#     print(f"key is {k}")
# for v in dict1.values():
#     print(f"value is {v}")

# dict1 = { 101 : [ Vishwraj ,  python , dholka , 30000] ,
#           102 : [ Romil ,  java , ahmedabad , 35000] ,
#           103 : [ Abhijit ,  php , surat , 15000] ,
# }
# for key , value in dict1.items():
#     print(key)
#     if value[3] > 20000:
#      for i in value:
#         print(f"\t{i}")



# 11th oct ------------------------------>


#dictionary velue in upper case

# city_name = {'Ahmedabad' : "AHEMDABAD" , 'Baroda' : "BARODA" , 'Surat' : "SURAT" }
# for key in city_name.keys():
#     city_name[key] = city_name[key].upper()
# print(city_name)

# city_name = {'Ahmedabad' : "" , 'Baroda' : "" , 'Surat' : "" }
# for key in city_name.keys():
#     city_name[key] = key.upper()
# print(city_name)

#dictionary velue in length

# city_name = {'Ahmedabad' : "" , 'Baroda' : "" , 'Surat' : "" }
# for key in city_name.keys():
#     city_name[key] = key.len()
# print(city_name)

#

# sales_data = {
#     "Pen": {"Product_discription" :"Pentonic pen" ,"price" : 10, "units_sold": 150},
#     "Notebook":{"Product_discription" :"DOMS Notebook", "Price": 50, "units_sold": 90},
#     "Pencil" : {"Product_discription": "DOMS pencil", "price": 5 ,"units_sold": 300}
#     }
# for k,v in sales_data.items():
#     if v["units_sold"] > 100:
#         print(f"{k} is the {v["Product_discription"]} has unit sold over 100" )


# 14th oct--------------------------------->

# dict1 = {1:0 ,2:0 , 3:0 ,4:0 }

# # for k,v in dict1.items():
# #     dict1[k]=k**2

# dict2 = {k:k**2 for k ,v in dict1.items()}
# print(dict2)


# state_capital ={'Gujarat ' , 'Rajasthan'  , 'Maharastra'  , 'Orissa '}
# state_capital_len = {k:len (k) for k in state_capital}
# # print(state_capital_len)

# state_capital ={"Gujarat" : "Gandhinagar", "Rajasthan" : "Jaipur " , "Maharastra": "Mumbai" , "Orissa ":"Bhuvneshvaer"}
# state_capital_1= {k:v.upper() for k,v in state_capital.items() if len (k)> 7}



# state_capital ={"Gujarat": "Gandhinagar", "Rajasthan": "Jaipur " , "Maharastra": "Mumbai" }
# state_capital_1 = {k:v.upper() if len (v)>7 else v.lower() for k,v in state_capital.items()}
# print(state_capital_1)

# ---------------------------------------------->
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

#-------------------------------------------->


month = input("enter  a month")
# if month=="january" or month== "march" or month=="may" or month== "july" or month=="october" or month== "Descember":
#       print("31")     
# elif month =="fabruary":
#       print("28 or 29 days") 
# elif month== "april" or month=="june" or month=="august" or month== "septamber":
#       print("30")
# else : 
#       print("invalid number")


#--------------------------------------------------------->
# match month:
#       case 'January' | 'March' | 'May' |'July' | 'Octomber' | 'December':
#         print("31 days")
#       case 'April' | 'June' | 'August' | 'September' | 'Navember':
#         print("30 days")  
#       case 'February':
#         print("28 or 29 days")
#       case _ :
#             print("Invelid Number")

#--------------------------------------------------------->


# if month in ('January' ,  'March','may' , 'July' , "Descember"): 
#       print("31 days")
# elif month== "Fabruary":
#      print ("28 or 29 days")
# elif month in ("April" ,"June" , 'August' , 'Septamber'):
#      print("30 days")
# else :
#     print("Invelid Number")

