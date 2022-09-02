'''Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.

First, print the sum of a and b.

Second, print c minus d.

Third, print the first number printed, multiplied by the second number printed.

Finally, return the third number printed modulo a.

Hint
To make this problem easier, you can store the result of each mathematical operation into a variable and use them as the results in step 4. For example: first_result = a + b. Also, remember that you can take the modulo of a number with %.'''


def lots_of_math(a,b,c,d):
    first = a+b
    second = c-d
    third = first*second
    fourth = third%first
    print(first)
    print(second)
    print(third)
    print(fourth)
    return fourth

lots_of_math(1,2,3,4)