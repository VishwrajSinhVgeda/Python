# OOP Important Notes (Short & Easy Notes in Hindi)
# OOPS का मतलब Object-Oriented Programming System है।
# यह एक programming paradigm है जो software design के लिए "objects" का उपयोग करता है।
# OOPS concepts में शामिल हैं:

#  1. Class
# क्लास एक ब्लूप्रिंट है जिसमें data (attributes) और functions (methods) होते हैं।

#  2. Object
# क्लास से बना हुआ real-world entity।

#  3. Encapsulation
# Data को छुपाकर सुरक्षित रखना (private variables का उपयोग)।

#  4. Inheritance
# एक क्लास का data और methods दूसरी क्लास inherit करती है।

#  5. Polymorphism            
# एक ही नाम के function अलग-अलग class में अलग तरह से काम करते हैं।

#  6. Abstraction
# फालतू details छुपाना और सिर्फ main features दिखाना


# what is OOPS Pyhon ?
# OOPS stands for Object-Oriented Programming System.
# It is a programming paradigm that uses "objects" to design software.
   
# OOPS concepts include:

# 1. What is Encapsulation ?
#Encapsulation in OOPs means wrapping data (variables) and methods (functions)
#together into a single unit (class) and restricting direct access to some of the object’s components.
#Encapsulation = Data Hiding + Controlled Access

# 2. What is Inheritance ?
#Inheritance is a mechanism in OOPs that allows a new class (derived class or child class) to 
# inherit properties and behaviors (attributes and methods) from an existing class (base class or parent class).


# 3. What is Polymorphism ?
#Polymorphism in OOPs refers to the ability of different classes to be treated as instances of the same class through a common interface.
#It allows methods to do different things based on the object it is acting upon, even though
#they share the same name.

# 4. What is Abstraction ?
#Abstraction in OOPs is the concept of hiding the complex implementation details and showing only the essential features of the object.
#It helps in reducing complexity and increases efficiency.


#-------------------------------------------->
#Example 1 :-

# from unicodedata import name


# class Employee:
# #initialize name
#     def __init__(self):
#         self.name="Vishwraj"


# #function
#     def greet(self):
#         print("in greet")
# Vishwraj= Employee()
# romil =Employee()
# Vishwraj.greet()
# romil.greet()


# #-------------------------------------------->
# #Example 2 :-

# class Book: 


#     def __init__(self,title,author,isbn,qty,price):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#         self.qty=qty
#         self.price=price

#     def displayBook(self):
#         print(f"{self.title} by {self.author}, ISBN: {self.isbn}")
#     def CalculatePrice(self):
#         return self.qty * self.price

# book1=Book("who wil cry when you die","Robin Sharma",5,300,13)
# book2=Book("Focus","Stefan",3,250,14)
    
# book1.displayBook()
# book2.displayBook()
# print(f"{book1.title} Total Price is {book1.CalculatePrice()}")


# #-------------------------------------------->
# #Example 3 :-

# class person:
#     def __init__(self,name,c_no):
#         self.name=name
#         self.c_no=c_no

#     def display(self):
#         print(f"{self.name} - {self.c_no}")   

# class Employee(person):
#     def __init__(self,name,c_no,salary):
#         super().__init__(name,c_no)
#         self.salary=salary
#     def displayEmp(self):
#         print(f"{self.name}-{self.c_no}-{self.salary}")

# p1=person("Vishwraj","1234567890")
# p1.display()
# emp1=Employee("Abhijit","0987654321",100000)
# emp1.displayEmp(23)

#--------------------------------------------------->
#Example 4 :-

# class distance:
#     def __init__(self):
#         pass
#     def __init__(self, feet, inch):
#         self.feet = feet
#         self.inch = inch
#     def __mul__ (self,obj2):
#         inch1 =self.inch*obj2.inch
#         feet1 =self.feet*obj2.feet

#         obj = distance(feet1,inch1)
#         return obj
#     def display(self):
#         print(f"{self.feet} -{self.inch }")
#     def __lt__(self,other):
#         if self.feet<other.feet & self.inch<other.inch:
#             return True
#         else:
#             return False

# d1=distance(2,2)
# d2=distance(5,10)
# d1.display()
# d2.display()
# d3=distance(0,0)
# d3=d1*d2
# d3.display()

# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

#     def __lt__(self,other):
#         return self.age < other.age
        
#--------------------------------------------->
# Example 5 :-

# from turtle import distance
# from unicodedata import name



# class distance:
#     def __init__(self,feet,inch):
#         self.feet=feet
#         self.inch=inch


#     def __add__(self,other):
#           inch1=self.inch + other.inch
#           feet1=self.feet + other.feet

#           obj=distance(feet1,inch1)
#           return obj      
#     def display(self):
#           print(f"{self.feet} - {self.inch}")
          
# d1=distance(5,5)
# d2=distance(2,2)  
# d1.display()
# d2.display()
# d3= distance(0,0)
# d3=d1 + d2
# d3.display()

    
#------------------------------------------>  
# Example 6 :-      

# class distance:
#     def __init__(self,feet,inch):
#         self.feet=feet
#         self.inch=inch


#     def __sub__(self,other):
#           inch1=self.inch - other.inch
#           feet1=self.feet - other.feet

#           obj=distance(feet1,inch1)
#           return obj      
#     def display(self):
#           print(f"{self.feet} - {self.inch}")
          
# d1=distance(10,5)
# d2=distance(9,2)  
# d1.display()
# d2.display()
# d3= distance(0,0)
# d3=d1 - d2
# d3.display()

#------------------------------------------>  
# Example 7 :-

# class distance:
#     def __init__(self,feet,inch):
#         self.feet=feet
#         self.inch=inch


#     def __div__(self,other):
#           inch1=self.inch / other.inch
#           feet1=self.feet / other.feet

#           obj=distance(feet1,inch1)
#           return obj      
#     def display(self):
#           print(f"{self.feet} - {self.inch}")
          
# d1=distance(20,5)
# d2=distance(2,6)  
# d1.display()
# d2.display()
# d3= distance(0,0)
# d3=d1.__div__(d2)
# d3.display()


#------------------------------------------>
#Abtraction Example 1 -:

# from abc import ABC, abstractmethod
# class bank(ABC):
#     @abstractmethod
#     def rateOfInterest(self):
#         pass  
# class SBI(bank):
#     def rateOfInterest(self):
#         return 7.5
# class AXIS(bank):
#     def rateOfInterest(self):
#         return 8.5
# sbi=SBI()
# print(f"SBI Rate of Interest: {sbi.rateOfInterest()}%") 
# axis=AXIS()
# print(f"AXIS Rate of Interest: {axis.rateOfInterest()}%")

#------------------------------------------->
#Abtraction Example 2 -:

# from abc import ABC, abstractmethod
# class class1 (ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     def greet(self):
#         print ("Good Moring")
# class class2 (class1):
#     pass 
#     def greet(self):
#         print (" HAve Glorious Day")

# obj=class1()
# obj1=class2()
# obj.greet()
# obj1.greet()

#------------------------------------------->
#Abtraction Example 3 -:

# from abc import ABC , abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def CalculateArea(self):
#         return 0.0
# class rectangle(shape):
#     def __inti__(self,lenth,breasth):
#         slef,langth=langth
#         self.breasth=breasth
        
#     def calculateAria(self):
#         return self.langth * self.breasth
    
#     def square(shape):
#         def __init__(self,side):
#             self.side =side
#         def calculateArea(self):
#             return self.side * self.side
        

            
# obj = rectangle() 
# print(f"Area of Rectangale: {obj.calculateAria()}")

#------------------------------------------->
#Access Modifiers Example 1 :-

# class class1:
#     def __init__(self,no1,no2,no3): #procted 
#         self._no1=no1
#         # private data
#         self.__no2=no2
#         self.no3=no3
#     def display(self):
#         print(f"{self._no1} - {self.__no2} - {self.no3}")
# class class2(class1):
#     def display1(self):
#         print(self._no1)
#         #print(self.__no2)
# class class3:
#     def greet(self):
#         obj=class1(2,3,4)
#         print(obj._no1)
# obj=class1(12,100,300)
# obj.display()
# obj1=class2(12,120,456)
# obj1.display1()
# obj2=class3()
# obj2.greet()

#------------------------------------------->
#Access Modifiers Example 2 :-
# class class1 :
#     def __init__(self):
#         self.var1="I am Public Variable"          #public
#         self._var2="I am Protected Variable"       #protected
#         self.__var3="I am Private Variable"        #private
# c1=class1()
# print(c1.var1)            #public   
# print(c1._var2)          #protected
# # print(c1.__var3)       #private (will raise an AttributeError)
# print(c1._class1__var3)   #accessing private variable using name mangling  

#------------------------------------------->
# #Access Modifiers Example 3 :-

# class person:
#     def __init__(self,name,age):
#         self.name=name          #public
#         self._age=age          #protected
#         self.__salary=100000   #private

#     def display(self):
#         print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

# p1=person("Vishwraj",23)
# p1.display()
# print(p1.name)          #public
# print(p1._age)         #protected   
# # print(p1.__salary)    #private (will raise an AttributeError)
# print(p1._person__salary)  #accessing private variable using name mangling

#____________________________________________________________________________________>
#what is ittretor in python ?
# An iterator in Python is an object that allows you to traverse through a collection (like a list, tuple, or dictionary) one element at a time, 
# without exposing the underlying structure of the collection.
#An iterator must implement two methods: __iter__() and __next__().

# Example of iterator in python :- 1

# lst = [11,12,13,14,15]
# i    = iter (lst)
# print(next(i))  # Output: 11
# print(next(i))  # Output: 12
# print(next(i))  # Output: 13
# print(next(i))  # Output: 14
# print(next(i))  # Output: 15

# for i1 in lst:
#     print(i1)


#__________________________________________________________________>
    

#what is generator in python ?
# A generator in Python is a special type of iterator that is
# defined using a function that contains one or more yield statements.
# When the generator function is called, it does not execute the function body immediately.
# Instead,    it returns a generator object that can be iterated over.
# Each time the next() method is called on the generator object,
# the function executes until it reaches a yield statement,
# at which point it yields the value and pauses its state. 
# Generators are memory-efficient because they generate values on-the-fly and do not store the entire collection in memory at once.

# Example of generator in python :- 1
# def get_values():
#     for i in range(5):
#         yield i


# val=get_values()
# print(val)

# for num in val:
#     print(num)  # Output: 0, 1, 2, 3, 4

# print(next(val))
# print(next(val))

#-------------------------------------------->
# Example of generator in python :- 2

# square_number = (i*i for i in range(1,7))
# print(next(square_number))
# print(next(square_number))

# print ("with loop")
# for i in square_number:
#     print(i)

# #-------------------------------------------->
# Example of generator in python :- 3 

# Generator to produce a sequence of numbers up to a specified limit
# using yield keyword
# Function to generate numbers from 1 to n


# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
# counter = count_up_to(5)    
# for num in counter:
#     print(num) # Output: 1, 2, 3, 4, 5


