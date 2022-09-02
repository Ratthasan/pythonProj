'''Write a function named square_root() that has one parameter named num.

Use exponents (**) to return the square root of num.

Hint
Remember to use def when defining the function. To take the square root of a value, you can use the power operator **. The square root of a number is the same as taking the ½ power of the number. For example, the square root of 6 would look like: 6 ** 0.5.'''


def square_root(num):
    return num**0.5


print(square_root(9))