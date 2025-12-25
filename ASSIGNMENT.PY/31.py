# Write a Python program to count the number of strings where the string  
# length is 2 or more and the first and last character are same from a given list 
# of strings. 

# Answer :

def count_strings(words):
    count = 0

    for w in words:
        if len(w) >= 2 and w[0] == w[-1]:
            count += 1

    return count

# Example list
my_list = ["aba", "xyz", "1221", "aa", "ab", "123"]

print(count_strings(my_list))

#Output : 3

# # Explainntion :
# Word must have length ≥ 2
# Word’s first character == last character
# If both conditions are true → increase count by 1

# | Word   | Length ≥2? | First == Last? | Count |
# | ------ | ---------- | -------------- | ----- |
# | "aba"  | Yes        | a == a (Yes)   | +1    |
# | "xyz"  | Yes        | x != z (No)    | 0     |
# | "1221" | Yes        | 1 == 1 (Yes)   | +1    |
# | "aa"   | Yes        | a == a (Yes)   | +1    |
# | "ab"   | Yes        | a != b (No)    | 0     |
# | "123"  | Yes        | 1 != 3 (No)    | 0     |
