'''Write a function named remainder() that has two parameters named num1 and num2.

The function should return the remainder of twice num1 divided by half of num2.

Hint
In order to calculate the remainder of two numbers, we can use the modulus operator %. For example, the remainder of 5 divided by 2 is equal to 1 and we can get this result using 5 % 2.'''

def remainer(num1,num2):
    return (num1*2)%(num2*0.5)


print(remainer(5,5))