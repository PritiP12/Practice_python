""" Methods on set """

# 1. union():it returns all the items that are in any of those sets.
set1,set2,set3={1,2,3},{3,4,5},{5,6,7}
print(set1.union(set2,set3))

# 2. intersection():This method takes as argument sets, and returns the common items in all the sets.
print(set2.intersection(set3))

# 3. difference():The difference() method returns the difference of two or more sets. It returns as a set.
print(set1.difference(set2))
print(set1.difference(set2,set3))

# 4. symmetric_difference():
# This method returns all the items that are unique to each set.
print(set1.symmetric_difference(set2))

# 5.intersection_update(): this method update the python set with common in set1 and set2.
set1.intersection_update(set2)
print(set1)

# 6. difference_update(): this method updates the Python set with the difference.
set1={1,2,3}
set2={3,4,5}
set1.difference_update(set2)
print(set1)

# 7. symmetric_difference_update():it updates the set on which it is called with the symmetric difference.
set1={1,2,3}
set2={3,4,5}
set1.symmetric_difference_update(set2)
print(set1)

# 8. copy(): The copy() method creates a shallow copy of the Python set.
set4 = set1.copy()
print(set1,set4)

# 9. isdisjoint() : This method returns True if two sets have a null intersection.
s1 = {1,2,3}
s2 = {4,5,6}
print(s1.isdisjoint(s2))

# 10. issubset(): This method returns true if the set in the argument contains this set.
s3={1,2}
s4={1,2,3}
print(s3.issubset(s4))

# 11. issuperset() : this one returns True if the set contains the set in the argument.
s5 = {1,2,3}
s6 = {1,2}
print(s5.issuperset(s6))
