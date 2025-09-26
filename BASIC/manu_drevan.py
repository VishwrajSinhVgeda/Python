#manu drevan program with function like upper , lower , count , findlanthuage, replace and with using mace case
while True:
    print("Menu:")
    print("1. Upper Case")
    print("2. Lower Case")
    print("3. Find Langth")
    print("4. Replace")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    match choice:
        case '1':
            str = input("Enter a string: ")
            print("Upper Case:", str.upper())
        case '2':
            str = input("Enter a string: ")
            print("Lower Case:", str.lower())
        case '3':
            str = input("Enter a string: ")
            print("Length:", len(str))
        case '4':
            str = input("Enter a string: ")
            old = input("Enter substring to replace: ")
            new = input("Enter new substring: ")
            print("Replaced Text:", str.replace(old, new))
        case '5':
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")


#manu drevan program with function like convert to reverse printing , find number od digits , count total even/odd dights of a number,
# check if number is paindrom and exit using match case

while True:
    print("Menu:")
    print("1. Reverse Number")
    print("2. Count Digits")
    print("3. Count Even/Odd Digits")
    print("4. Check Palindrome")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    match choice:
        case '1':
            num = input("Enter a number: ")
            reversed_num = 0
            while temp := int(num) > 0:
                digit = int(num) % 10
                reversed_num = reversed_num * 10 + digit
                num = str(int(num) // 10)
            print("Reversed Number:", reversed_num) 
        
        case '2':
            num = input("Enter a number: ") 
            count = 0
            while temp := int(num) > 0:
                count += 1
                num = str(int(num) // 10)   
            print("Number of Digits:", count)

        case '3':
            num = input("Enter a number: ")
            even_count = 0
            odd_count = 0
            while temp := int(num) > 0:
                digit = int(num) % 10
                if digit % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
                num = str(int(num) // 10)
            print("Even Count:", even_count)
            print("Odd Count:", odd_count)

        case '4':
            num =int(input("Enter a number: "))
            reversed_num = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                reversed_num = reversed_num * 10 + digit
                temp //= 10
            if reversed_num == num:
                print(f"{num} is a Palindrome")
            else:
                print(f"{num} is not a Palindrome")
        case '5':
            print("Exiting the program.")