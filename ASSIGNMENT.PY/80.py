# 80 .  Write a Python program to count the frequency of words in a file. 
# Answer  :

def word_frequency(filename):
    freq = {}

    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                # Remove punctuation
                word = word.strip('.,!?";:-()[]{}')
                freq[word] = freq.get(word, 0) + 1

    return freq


# Example usage
filename = "sample.txt"
result = word_frequency(filename)

for word, count in result.items():
    print(f"{word}: {count}")

# Explanation :

# Opens the file in read mode
# Reads the file line by line
# Converts words to lowercase (to avoid case mismatch)
# Removes common punctuation
# Uses a dictionary to store word counts