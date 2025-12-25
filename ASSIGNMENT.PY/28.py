# 28. Differentiate between append () and extend () methods? 
# Answer :

# .append

list1 = [1, 2, 3]
list1.append(10)
print(list1)

# Output : [1, 2, 3, 10]

# .extend

list1 = [1, 2, 3]
list1.extend([4, 5])
print(list1)

#Output : [1, 2, 3, 4, 5]
 

# Exaplintion : 

# append()	Adds one item to the end	[1,2,3, [4,5]]
# extend()	Adds many items individually	[1,2,3,4,5]