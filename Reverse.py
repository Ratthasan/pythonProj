'''Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

Hint
Just like the last challenge, you want to access each letter of word by it's index.
my_string = "Hello World"
for i in range(len(my_string)):
print my_string[i]

However, you don’t want i to start at 0. Instead you want it to start at the last index of your string (len(my_string)-1) and end at 0.

Edit the call to the range function to do this. Remember, the range function can take three parameters: the starting number (inclusive), the ending number (exclusive), and the step. To count down, make the step -1.'''

def reverse_string(word):
    str_reverse=''
    for i in range(len(word)-1,-1,-1):
        str_reverse+=word[i]
    return str_reverse

print(reverse_string("Hello world!"))