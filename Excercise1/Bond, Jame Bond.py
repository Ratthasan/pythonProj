'''Write a function named introduction() that has two parameters named first_name and last_name.

The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

Hint
In order to concatenate strings in python, we can use the + operator. For example, if we wanted to create the string 'Hello, how are you?' from multiple strings, we could do: 'Hello' + ', ' + 'how are you?'''


def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

introduction("Ratthasan","Srisongmueang")