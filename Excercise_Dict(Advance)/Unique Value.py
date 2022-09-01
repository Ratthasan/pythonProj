'''Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.

Hint
Begin by creating a new empty list named seen_values. Loop through all of the values of my_dictionary. For every value, check to see if that value is in seen_values. If it is, continue to the next value. If it is not, add it to seen_values. After looping through all values, return the length of seen_values.'''

def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)       


print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2