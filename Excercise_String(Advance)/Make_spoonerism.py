'''Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. Return the two new words as a single string separated by a space.

Hint
word2[0] will access the first letter of word2. word1[1:] will access everything but the first letter of word1. Combining those with a + will give you your first new word.'''

def make_spoonerism(word1, word2):
    return word2[0]+word1[1:]+" " +word1[0]+word2[1:]


make_spoonerism("Hello", "world!")
    