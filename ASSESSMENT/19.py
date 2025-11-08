# 19. Write a Python program to count the occurrences of each word in a given sentence.
# Answer:
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
# Output:
# Enter a sentence: This is a test. This test is only a test.
# This: 2
# is: 2
# a: 1
# test.: 1
# This: 2
# test: 1
# is: 2
# only: 1
# a: 1
# test.: 1

# Explanation

# split() separates words by spaces
# A dictionary stores each word and its count
# Loop checks and counts each word 