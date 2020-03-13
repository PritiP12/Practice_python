""" Basic operation of Tuple """

# To declare a Python tuple, you must type a list of items separated by commas, inside parentheses. Then assign it to a variable
values = (10,30,50,40)

# we can also create a Python tuple without parentheses. This is called tuple packing.
a = 'One',2,3

# You can also create a Python tuple without parentheses. This is called tuple packing.
print(values)

# Accessing a single item
print(values[1])

# Slicing a Tuple in Python.
print(values[0:4])

# This prints out items from the beginning to the item at index 3.
print(values[:4])

# this returns an empty Python tuple.
print(values[2:2])

# Negative indexing:
# This prints out the items from the tuple’s beginning to two items from the end.
print(values[:-2])
# This prints out items from two items from the end to the end.
print(values[-2:])
# This prints out items from index 2 to two items from the end.
print(values[2:-2])

# Deleting a Python Tuple:
del values
print(values)