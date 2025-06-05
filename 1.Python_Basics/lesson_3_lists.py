# LIST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LIST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

list_1 = ['apple', 'banana', 'orange', 'grape', 'blueberries']
list_2 = [1, 'baleno', 0.45, False]
print(list_1)
print(list_2)

print(range(5))
print(list(range(5)))

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

a, b, c, *other = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(b)
print(c)
print(other)

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(b)
print(c)
print(other)
print(d)



# LIST INDEXING ~~~~~~~~~~~~~~~~~~~~
# ----------------------------------
print(list_1[0])
print(list_1[-1])
print(list_1[1:4])
print(list_1[:-2])
print(list_1[::2])
list_1[0] = 'hello'   #changeable
print(list_1)



# MATRIX~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------
matrix_1 = [
    ['apple', 'oranges', 'strawberries', 'mango'],
    [2001, 2002, 1998, 1989],
    [True, 0.95, 'cinegar', False]
]

# Rows and Elements
for row in matrix_1:
    print(row)

for row in matrix_1:
    for items in row:
        print(items)

rows = len(matrix_1)
col_row1 = len(matrix_1[0])
print(rows)
print(col_row1)

# Matrix Indexing
print(matrix_1[0])
print(matrix_1[:-1])

print(matrix_1[0][-1])
print(matrix_1[-1][0])

last_items = [row[-1] for row in matrix_1]
print(last_items)

matrix_1[1][0] = 'hehe'   #changeable
print(matrix_1)



# LIST / ARRAY METHODS ~~~~~~~~~~~~~
# ----------------------------------
fruits = ['apple', 'banana', 'cherry']
fruits2 = fruits.copy()
print(fruits2)

print('banana' in fruits)
print('tomato' in fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.append('mango')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.extend(['tomato', 'blueberry'])
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'strawberry')  # add to index 1
print(fruits)

noms = [1, 2, 3, 6, 2]
noms.remove(2)   # remove the first occurrence
print(noms)

noms = [1, 2, 3, 6, 2]
new_noms = noms.pop(3)  # remove items at index 3
print(new_noms)
print(noms)

noms = [1, 2, 3, 6, 2]
noms.clear()
print(noms)

fruits = ['apple', 'banana', 'cherry']
print(fruits.index('cherry'))

noms = [1, 2, 3, 6, 2]
print(noms.count(2))

noms = [1, 2, 3, 6, 2]
noms.sort()  # di sorted
print(noms)

noms = [1, 2, 3, 6, 2]
noms.sort(reverse=True)  # di sorted and reverse
print(noms)

noms = [1, 2, 3, 6, 2]
new_noms = sorted(noms)
print(new_noms)
print(noms)

fruits = ['apple', 'strawberry', 'mango', 'cherry']
fruits.reverse()  # dibalik
print(fruits)






# TUPLE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TUPLE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TUPLE CAN'T BE CHANGED

tuple1 = (1, 2, 3, 4, 5)
print(tuple1[1])
print(tuple1[1:4])
print(3 in tuple1)

x, y, *others = (1, 2, 3, 4, 5)
print(others)


# OPERATIONS ~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------
tuple1 = (1, 2, 3)
tuple2 = (7,8,9)
print(tuple1 + tuple2)
print(tuple2 * 2)

# METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------
tuple1 = ((1,4), 2, False, 2, "house", 9)
print(tuple1.count(2))
print(tuple1.index("house"))






# SETS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SETS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# mutable, unordered, no indexing or slicing, no duplicates

sets1 = {1, 2, 2, 3, 2}
print(s)

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
