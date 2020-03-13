""" Tuple Method / Operation """

# index() :This method takes one argument and returns the index of the first appearance of an item in a tuple.

a = (1,2,3,2,4,5,2)
print(a.index(2))

# count() :This method takes one argument and returns the number of times an item appears in the tuple.
print(a.count(2))

# Tuple Operations:
# Membership
print(1 in a)

print(10 in a)

# Concatenation:
print((1,2,3)+(4,5,6))

# All the logical operators (like >,>=,..) can be applied on a tuple.
print((1,2,3)>(4,5,6))

# Nested Tuples in Python:
x=((1,2,3),(4,(5,6)))
print(x[1][1][1])