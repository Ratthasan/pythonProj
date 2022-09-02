'''Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

Hint
Use a for loop to loop through all of the characters of word. If the letter is equal to the value of x, increase a counter variable by one.'''

def  count_char_x(word,x):
    count=0
    for i in word:
        if i == x:
            count+=1
    return count

print(count_char_x('earthhhhh','h'))