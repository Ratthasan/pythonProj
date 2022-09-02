'''Create a function called tip() that has two parameters named total and percentage.

This function should return the amount you should tip given a total and the percentage you want to tip.

Hint
Calculating the tip value will look something like this: (total * percentage) / 100'''

def tip(total,percentage):
    total = (total*percentage)/100
    return total

print(tip(100,1))