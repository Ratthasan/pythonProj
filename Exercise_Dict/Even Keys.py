'''Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.

Hint
Create a counter variable and start it at 0. Loop through all of the elements of the keys of the dictionary by using my_dictionary.keys(). If the key is even (which you can check by using key % 2 == 0), add the corresponding value to the counter.'''

def sum_even_keys(my_dictionary):
    total = 0
    for i in my_dictionary.keys():
        if i %2 == 0:
            total=my_dictionary[i]
    return total


print(sum_even_keys({1:5, 2:2, 3:3}))
#print 2