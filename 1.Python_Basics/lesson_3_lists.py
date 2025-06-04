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
