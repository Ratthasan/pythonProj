'''Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary

Hint
Create a counter variable and start it at 0. Loop through all of the elements of my_dictionary.values() and add each value to your counter variable.'''

def sum_values(my_dictionaty):
    total_sum_values=0
    for i in my_dictionaty.values():
        total_sum_values+=1
    return total_sum_values

print(sum_values({"milk":5, "eggs":2, "flour": 3}))