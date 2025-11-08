# What is the purpose continuing statement in python?
#Answer:

#The continue statement in Python is used inside loops (for or while) to skip the rest of the code in the current iteration and move to the next iteration immediately.
# The main purpose of continue is to skip certain conditions inside a loop without stopping the loop entirely.

# Example : Using continue in a for loop
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output will be:
1
2
4
5
