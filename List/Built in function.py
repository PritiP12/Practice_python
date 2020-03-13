""" Built-in List Functions """

list1=[1,2,6,8,9,7,4]
# length of the list.
print(len(list1))

# It returns the item from the list with the highest value.
print(max(list1))

# If all the items in your list are strings, it will compare.
a=['a','aa','aaa']
print(max(a))

# It returns the item from the Python list with the lowest value.
print(min(list1))

# It returns the sum of all the elements in the list.
print(sum(list1))

# It returns a sorted version of the list, but does not change the original one.
print(sorted(list1))

# If the Python list members are strings, it sorts them according to their ASCII values.
x=['Hi','hi','HI']
print(sorted(x))

# It converts a different data type into a list.
print(list('Hello'))

# It returns True if even one item in the Python list has a True value.
print(any(['','','1']))

# It returns False for an empty iterable.
print(any([]))

# It returns True if all items in the list have a True value
print(all(['','','1']))

# It returns True for an empty iterable.
print(all([]))