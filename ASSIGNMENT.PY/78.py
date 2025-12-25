# 78 . Write a python program to find the longest words. 
# Answer :
 
def find_longest_words(text):
    words = text.split()          # Split the string into words
    max_length = max(len(word) for word in words)
    
    # Find all words with maximum length
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words, max_length


# Example usage
text = "Python programming is very interesting and powerful"
words, length = find_longest_words(text)

print("Longest word(s):", words)
print("Length:", length)

# Output :
# Longest word(s): ['programming', 'interesting']
# Length: 11

# Explainnation : 

# The string is split into words using split()
# max() finds the maximum length of the words
# A list comprehension collects all words with that maximum length