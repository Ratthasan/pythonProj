'''Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.

Hint
Begin by creating two variables named largest_key and largest_value. Initialize largest_value to be the smallest number possible (you can use float("-inf")). Initialize largest_key to any value you want (this will be immediately overwritten once we find the first value later than negative infinity).
Loop through all keys/value pair in the dictionary. Any time you find a value larger than what is currently stored in largest_value, replace largest_value with that new value. Similarly, replace largest_key with the key associated with the new largest value.

After looping through all key/value pairs, return largest_key.'''

def max_key(my_dictionary):
    
  largest_key = float("-inf")
  largest_value = float("-inf")
  
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
      
  return largest_key

print(max_key({1:100, 2:48, 3:488, 4:10}))
#should print 1