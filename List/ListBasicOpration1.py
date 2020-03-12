"""List Basic Operations"""

# Multidimensional Lists in Python:
a=[[[1,2],[3,4],5],[6,7]]
print(a)

# To access the element 4 here, we type the following code into the shell.
print(a[0][1][1])

# Concatenation of Python List.
a,b=[3,1,2],[5,4,6]
print(a+b)

# Multiplication.
a*=3
print(a)

# Membership.
# You can apply the ‘in’ and ‘not in’ operators on a Python list
print(3 in a)
print(1 not in a)