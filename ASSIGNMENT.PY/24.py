#24. Write a Python function to insert a string in the middle of a string. 

#Answer:

def insert_middle(main_str, insert_str):
    middle = len(main_str) // 2    # find middle position
    result = main_str[:middle] + insert_str + main_str[middle:]
    return result

#Output: HelloPythonWorld


#Explainnation:

# Middle position = 10 // 2 = 5
# "Hello" + "Python" + "World"
# Final Result → HelloPythonWorld