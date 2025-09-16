#Python me Variable Declaration
#✅ Rule 1: Directly value assign karke variable ban jata hai
x = 10
name = "Vishwraj"
pi = 3.14
is_ok = True


#✅ Rule 2: Ek hi line me multiple variables
a , b , c = 10, 20, 30
print (a, b, c) #Output 10 20 30


#✅ Rule 3: Same value multiple variables ko
x = y = z = 100
print(x, y, z)  #Output: 100 100  100

#---------------------------------------------------------------------------------
#✅ Rule 4: Variables ke liye naming rules

#Sirf letters (a-z, A-Z), digits (0-9), aur underscore _ allowed hai.

#Variable name digit se start nahi hona chahiye.
#❌ 1name (wrong), ✅ name1 (right)

#Reserved keywords use nahi kar sakte (jaise if, for, while etc.).

#Case-sensitive hote hain → Name aur name alag variables hain.
#---------------------------------------------------------------------------------

#✅ Rule 5: type() function
#Agar Check Karna Hai Ki Variable Ka Data Type Kya Hai

x = 10
y = 3.14
z = "Hello"
print(type(x))
print(type(y))
print(type(z))



