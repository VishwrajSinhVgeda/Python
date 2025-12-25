# Example 1: Menu Driven Program with Function

#   1. Read
#   2. Write
#   3. CopyFile
#   4. Append
#   5. Exit
# def read_file():
#     file_name = input("Enter the file name to read: ")
#     with open(file_name, 'r') as file:
#         data = file.read()
#         print(data)

# def write_file():
#     file_name = input("Enter the file name to write: ")
#     with open(file_name, 'w') as file:
#         data = input("Enter data to write to file: ")
#         file.write(data)
#         print("Data written to file successfully.")

# def copy_file():
#     file_name = input("Enter the file name to copy: ")
#     copy_file_name = input("Enter the name for the copied file: ")
#     with open(file_name, 'r') as file:
#         data = file.read()
#     with open(copy_file_name, 'w') as file:
#         file.write(data)
#         print("File copied successfully.")
        
# def append_file():
#     file_name = input("Enter the file name to append: ")
#     with open(file_name, 'a') as file:
#         data = input("Enter data to append to file: ")
#         file.write(data + '\n')
#         print("Data appended to file successfully.")
        
# while True:
#     print("Menu:")
#     print("1. Read")
#     print("2. Write")
#     print("3. CopyFile")
#     print("4. Append")
#     print("5. Exit")
#     choice = input("Enter your choice (1-5): ")
    
#     if choice == '1':
#         read_file()
#     elif choice == '2':
#         write_file()
#     elif choice == '3':
#         copy_file()
#     elif choice == '4':
#         append_file()
#     elif choice == '5':
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# Example 2: Using While Loop with writelines

# file = open('user_input.txt', 'w')
# lines = []
# while True:
#     data = input("Enter data to write to file (type 'exit' to stop): ")
#     if data.lower() == 'exit':
#         break
#     lines.append(data + '\n')
# file.writelines(lines)
# file.close()

# Example 3: Copy File.

# f1 = open('user_input.txt', 'r')
# f2 = open('copy_user_input.txt', 'w')
# f2.write(f1.read())
# f1.close()
# f2.close()
# print("File copied successfully.")
