"""List Basic Operations"""
# Creating a list is as simple as putting different comma-separated values between square brackets.
days = ['Monday', 'Tuesday', 'Wednesday', 4, 5, 6, 7.0]
print(days)

# A list may have python list.
Languages = [['Hindi', 'English'], ['Spanish', 'Chinese'], 'Marathi']
print(Languages)
print(type(Languages))

# A list may also contain tuples or so.
languages = [('Hindi', 'English'), ('Marathi', 'Hindi')]
print(languages)
print(type(languages))  # output:<class 'list'>
print(type(languages[0]))  # output:<class 'tuple'>

languages[0][0] = 'Arabian'
print(languages)  # TypeError: 'tuple' object does not support item assignment

# Slicing a Python List:
indices = ['zero', 'one', 'two', 'three', 'four', 'five']
# This returns items from index 2 to index 4-1 (i.e., 3)
print(indices[2:4])
# This returns items from the beginning of the list to index 3
print(indices[:4])
# It returns items from index 4 to the end of the list in Python.
print(indices[4:])
# This returns the whole list.
print(indices[:])

# Negative indices:
# This returns item from the list’s beginning to two items from the end.
print(indices[:-2])
# It returns items from the item at index 1 to two items from the end.
print(indices[-2:-1])
# This returns items from two from the end to one from the end.
print(indices[-1:-2])

# Reassigning a Python List (Mutable):
colors = ['caramel', 'gold', 'silver', 'occur']
print(colors)
# Reassigning a few elements.
# colors[2:3] reassigns the element at index 2, which is the third element.
colors[2:3] = ['bronze','silver']
print(colors)

# Reassigning a single element:
colors[3]='bronze'
print(colors)

# Delete a Python List:
# Deleting the entire Python list:
del colors
print(colors)

# Deleting a few elements:
del colors[2:4]
print(colors)

# Deleting a single element:
del colors[0]
print(colors)
