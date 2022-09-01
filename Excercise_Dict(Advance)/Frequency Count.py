'''Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words.

Hint
First, create a new empty dictionary. Then, loop through every word in words. If word is not a key in the dictionary, make word a key with a value of 1. If word is already a key, increase the value associated with word by 1.'''

def frequency_dictionary(words):
    count ={}
    for i in words:
        if i not in count:
         count[i]=0
        count[i]+=1
    return count
    
        
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}