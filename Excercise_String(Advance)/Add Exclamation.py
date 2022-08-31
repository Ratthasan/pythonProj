'''Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.

Hint
Use a while loop to add exclamation points to word. The while loop should stop when the length of word is greater than or equal to 20.'''

def add_exclamation(word):
    while(len(word)<100):
        word+='!'
    return word

print(add_exclamation("Hooray"))
#Output Hooray!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!