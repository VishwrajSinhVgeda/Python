def chekeEvan(num):
    if num % 2 == 0:
        return True
    else:
         return False
    

def positive (num):
    if num >=0 :
        return True
    else:
        return False
    
    
def isprime(num):
    for i in range(2,num):
        return True
    else: 
         return False


num=100
num1=10
def printnum():
    global num
    num=200
    num1=200
    print(f"{num}-{num1}")

num=300
num1=300
print(f"Outside function {num} - {num1}")
printnum()
print(f"After calling function Outside function {num} - {num1}")


