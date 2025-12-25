#21. Write a Python program to add 'in' at the end of a given string (length 
#should be at least 3). If the given string already ends with 'ing' then 
#add 'ly' instead if the string length of the given string is less than 3, 
#leave it unchanged. 

#Answer:

def add_string(text):
    if len(text) < 3:
        return text
    
    if text.endswith("ing"):
        return text + "ly"
    else:
        return text + "in"

print(add_string("go"))
print(add_string("play"))
print(add_string("running"))

# Output: 
# go
#playin
#runningly

#Explanation :

#| Input String | Length | Ends with "ing"? | What Happens | Output      |
#| ------------ | ------ | ---------------- | ------------ | ----------- |
#|  "go"        | 2      | No               | No change    |  go         |
#|  "play"`     | 4      | No               | Add  "in"    |  playin     |
#|  "running"   | 7      | Yes              | Add  "ly"    |  runningly  |


