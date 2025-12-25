# 35.Write a Python program to generate and print a list of first and last 5 
#elements where the values are square of numbers between 1 and 30.

# Answer :

squares = []

for i in range(1, 31):
    squares.append(i * i)

print("First 5 elements:", squares[:5])    # First 5 elements
print("Last 5 elements:", squares[-5:])    # Last 5 elements


# Output : First 5 elements: [1, 4, 9, 16, 25]
#          Last 5 elements: [676, 729, 784, 841, 900]

# Explainnation : 1 se 30 tak ke numbers lene hain
#                 Har number ka square (i × i) nikalna hai
#                 Usse list banana hai
#                 Fir sirf first 5 aur last 5 elements print karne hain