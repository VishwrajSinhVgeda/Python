
print("\n1. addition : + ")
print("\n2. Subtraction : - ")
print("\n3. Multiplication : * ")
print("\n4. Division: / ") 

choice =int(input("Enter your choice "))
number1=int(input("Enter number "))
number2=int(input("Enter number "))

match choice:
    case 1:print(f"Addition is ",number1+number2)
    case 2:print(f"Subtraction is {number1-number2}")
    case 3:print(f"Multilication is {number1*number2}")
    case 4:print(f"Division is {number1/number2}")
    case 5:print(f"floor Division is {number1/number2}")
    case _:print("Invalid choice ")


