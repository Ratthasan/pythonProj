'''Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.

For example, substring_between_letters("apple", "p", "e") should return "pl".

Hint
Begin by finding the indices of the start and end characters by using word.find(start) and word.find(end).
If either of those indices are -1, then the original string didn’t contain one of those characters, and you should return word.

If neither are -1, then slice word using those indices. Remember, slicing is [inclusive:exclusive]!'''

def substring_between_letters(word,start,end):
    start_word= word.find(start)
    end_word = word.find(end)
    if start_word >-1 and end_word > -1:
        print(start_word)
        print(end_word)
        return (word[start_word+1:end_word])
        
    else:
        return word


print(substring_between_letters("ratthasan", "a", "s"))
