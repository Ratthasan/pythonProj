'''Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.

We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

Hint
Loop through the list of English letters and check to see if each letter is included in word by using in.'''


from enum import unique


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    unique= 0
    for i in letters:
        if i in word:
            unique+=1
    return unique


print(unique_english_letters("mississippi"))
