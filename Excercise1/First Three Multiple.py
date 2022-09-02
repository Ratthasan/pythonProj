'''Write a function named first_three_multiples() that has one parameter named num.

This function should print the first three multiples of num. Then, it should return the third multiple.

For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

Hint
For this function, we need to print() out the results of each multiplication * then return a single value. For example, printing the result of 3 times 5 would look like print(3 * 5) and returning it would look like return 3 * 5.'''


def first_three_multiple(num):
    print(num)
    print(num*2)
    print(num*3)
    return num*3

print(first_three_multiple(5))
