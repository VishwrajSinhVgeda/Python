
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


if month in ('January' ,  'March','may' , 'July' , "Descember"): 
      print("31 days")
elif month== "Fabruary":
     print ("28 or 29 days")
elif month in ("April" ,"June" , 'August' , 'Septamber'):
     print("30 days")
else :
    print("Invelid Number")