'''Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.
The following code will print all letters of a string by index:

my_string = "Hello World"
for i in range(len(my_string)):
print my_string[i]

In this code, i starts at 0 and increase until it is once less than the length of my_string. How could you make i increase by more than one each time?

Additionally, instead of printing each individual letter, you should add each letter to a new string using +.'''

def every_other_letter(word):
    every_other_list=[]
    every_other_str=''
    
    for i in range(0,len(word),2):
        every_other_list.append(word[i])
        every_other_str+=word[i]
    return every_other_list, every_other_str


print(every_other_letter("Hello world!"))
#output(['H', 'l', 'o', 'w', 'r', 'd'], 'Hlowrd')