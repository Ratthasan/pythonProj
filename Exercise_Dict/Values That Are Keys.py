'''Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.

Hint
Loop through all values in the dictionary by using for value in my_dictionary.values(). Check to see if value is in my_dictionary.keys() and if so, append it to a list.'''

def values_that_are_keys(my_dictionary):
    list=[]
    for i in my_dictionary.values():
        if i in my_dictionary.keys():
         list.append(i)
    return list

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]