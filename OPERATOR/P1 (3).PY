#Operators
#1.Arithmetic Operators
a = 10
b = 3
print("Addition :",a+b) #Addition 13
print("Subtraction :",a-b) #Subtraction 7
print("Multiplication :",a*b) #Multiplication 30
print("Division :",a/b) #Division 3.333
print("Floor Division :",a//b) #Floor Division (integer) 3 #Doubt
print("Remainder :",a%b) #Modulus (Remainder) 1
print("Exponent :",a**b) #Exponent (power) 

print("\n")

#2.Relation / Comparison Operators
x = 10
y = 20

print("Greater Then :",x > y)            #False
print("Less Then :",x < y)               #True
print("Equal To :",x == y)               #False
print("Not Equal To :",x != y)           #True
print("Greater Then Equal To :",x >= y)  #False
print("Less Then Equal To :",x <= y)     #True

print("\n")

#3.Logical Operator
p = True
q = False

print("End Operator :", p and q)  #False
print("OR Operator :", p or q)    #True
print("NOT Operator :",not p)     #False

print("\n")

#4.Identity Operators #Doubt
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) #False (Different Objects in memory)
print(a is not b) #True

print("\n")

#5.Assignment Operators

#6.Membership Operators
fruits = ["Apple", "Banana", "Mango"] 
print("Apple" in fruits) #True
print("Grapes" not in fruits) #True
print("Grapes" is fruits) #False

