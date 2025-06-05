# SETS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SETS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# mutable, unordered, no indexing or slicing, no duplicates

# METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------
sets1 = {1, 2, 2, 3, 2}
print(sets1)

sets1 = {4, 5, 6, 7, 8}
sets1.add("hello")
print(sets1)

sets1 = {4, 5, 6, 7, 8}
sets1.remove(4)   # error if no elements
print(sets1)

sets1 = {4, 5, 6, 7, 8}
sets1.discard(100)  # no error if no elements
print(sets1)

sets1 = {4, 5, 6, 7, 8}
sets1.pop()
print(sets1)

sets1 = {4, 5, 6, 7, 8}
sets1.clear()
print(sets1)


# OPERATIONS ~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------
sets1 = {1,2,3,4,6}
sets2 = {1,3,7,8,9,11}

# union --> no duplicates
print(sets1 | sets2)
print(sets1.union(sets2))
# intersection --> in both
print(sets1 & sets2)
print(sets1.intersection(sets2))
# intersection update --> only pick the same elements in both
sets1.intersection_update(sets2)
print(sets1)

sets1 = {1,2,3,4,6}
sets2 = {1,3,7,8,9,11}
# difference --> not in the second
print(sets1 - sets2)
print(sets1.difference(sets2))
# difference update --> only pick unique elements in a (difference from b)
sets1.difference_update(sets2)
print(sets1)

sets1 = {1,2,3,4,6}
sets2 = {1,3,7,8,9,11}
# symmetric difference --> unique in both
print(sets1^sets2)
print(sets1.symmetric_difference(sets2))
# isdisjoint --> check if there's no element that same
print(sets1.isdisjoint(sets2))  # true if no, false if there is


# issubset --> check if all elements in a are in b
sets1 = {1, 2}
sets2 = {1, 4, 2, 5}
print(sets1.issubset(sets2))
# issuperset() --> check if a have all elements in b
print(sets2.issuperset(sets1))