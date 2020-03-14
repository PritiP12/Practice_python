""" Set Basic Operations """
my_set = {1,2,3}

# Accessing set:
print(my_set)

# Deleting a Set:
numbers={3,2,1,4,6,5}
print(numbers)

# discard() :This method takes the item to delete as an argument
print(numbers.discard(3))

#  remove() deletes an item from the set
print(numbers.remove(2))

# pop() method on a set.
print(numbers.pop())
print({2,3}.pop())

# clear(): It empties the set in Python.
numbers.clear()
print(numbers)

# Updating a Set:
# add() : It takes as argument the item to be added to the set
a = {1,2,3,4}
a.add(5)
print(a)

# update() : This method can add multiple items to the set at once, which it takes as arguments.
a.update([6,7],[8,9])
print(a)