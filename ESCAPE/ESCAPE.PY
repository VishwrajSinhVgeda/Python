# Example 1: Simple string print
name1 = "Tops Technologies"
print(name1)
# Output: Tops Technologies


# Example 2: Backslash issue (wrong escape)
# name2 = "\Tops Technologies\""
# Yeh error dega kyunki \" aur \T valid escape sequence nahi hai.

# Correct way (double quotes ko escape karna hoga):
name2 = "\"Tops Technologies\""
print(name2)
# Output: "Tops Technologies"


# Example 3: Escaping single quotes inside string
name3 = 'Tops \'Technologies\''
print(name3)
# Output: Tops 'Technologies'


# Example 4: New line escape sequence
name4 = "Tops\nTechnologies"
print(name4)
# Output:
# Tops
# Technologies


# Example 5: Tab escape sequence
name5 = "Tops\tTechnologies"
print(name5)
# Output: Tops    Technologies


# Example 6: Backspace escape sequence
name6 = "Tops\bTechnologies"
print(name6)
# Output: Topstechnologies   (p chhup gaya, kyunki \b backspace deta hai)


# Example 7: Normal print (no escape)
name7 = "Tops Technologies"
print(name7)
# Output: Tops Technologies


# ---------------------------
# Extra: Use of 'end' and 'sep'
# ---------------------------

# Example with end
print("Tops", end=" ")
print("Technologies")
# Output: Tops Technologies   (same line, space ke sath)


# Example with sep
print("Tops", "Technologies", sep="\t")
# Output: Tops    Technologies   (tab ke sath space)
