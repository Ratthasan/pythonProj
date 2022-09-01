'''Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary

Hint
Loop through every key in the dictionary and add 10 to the value by using my_dictionary[key] += 10.'''

def add_ten(my_dictionary):
    for i in my_dictionary.keys():
        my_dictionary[i]+=10
    return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# output {1: 15, 2: 12, 3: 13}