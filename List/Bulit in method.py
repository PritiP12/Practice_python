""" Python Built In Method """
# It adds an item to the end of the list.
a = [1, 2, 3, 9, 5, 0]
a.append(4)
print(a)

# It inserts an item at a specified position.
a.insert(4, 5)
print(a)

# It removes the first instance of an item from the Python list.
x = [3, 5, 6, 8, 7, 3, 1]
x.remove(3)
print(x)

# It removes the element at the specified index, and prints it to the screen.
x.pop(1)
print(x)

# It empties the Python list.
x.clear()
print(x)

# It returns the first matching index of the item specified.
print(a.index(3))

# It returns the count of the item specified.
print(a.count(3))

# It sorts the list in an ascending order.
print(a.sort())

# It reverses the order of elements in the Python lists
print(a.reverse())
