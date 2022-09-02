'''Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.

The function should compute the age in dog years and return the following string:

"{name}, you are {age} years old in dog years"
Test this function with your name and your age!

Hint
Since the age in dog years age * 7 is a number, we need to convert it to a string when concatenating using str(). For example: 'The age is: '+ str(age * 7).'''

def dog_years(name,age):
    age= age*7
    return "{name}, you are {age} years old in dog years".format(name=name,age=age)

print(dog_years('Billy',2))