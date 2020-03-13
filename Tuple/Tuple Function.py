""" Tuple Functions """

my_tuple = (1, 2, 3, [6, 5])

# The len() function returns its length.
print(len(my_tuple))

# It returns the item from the tuple with the highest value.
a=(3,1,2,5,4,6)
print(max(a))

# the min() returns the item with the lowest values
print(min(a))

# This function returns the arithmetic sum of all the items in the tuple.
print(sum(a))

# If even one item in the tuple has a Boolean value of True, then this function returns True. Otherwise, it returns False.
print(any(('','0','')))

# The string ‘0’ does have a Boolean value of True. If it was rather the integer 0, it would’ve returned False.
print(any(('',0,'')))

# all() returns True only if all items have a Boolean value of True. Otherwise, it returns False.
print(all(('1',1,True,'')))

# The sorting is in ascending order, and it doesn’t modify the original tuple in Python.
print(sorted(a))

# This function converts another construct into a Python tuple. Let’s look at some of those:

list1 =[1,2,3]
t1 = tuple(list1)
print(t1)

str1 = "HEllo"
print(tuple(str1))

set1 = {4,3,1}
print(tuple(set1))