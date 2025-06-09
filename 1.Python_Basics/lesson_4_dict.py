# DICTIONARIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DICTIONARIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary)
print(dictionary['b'])


dictionary = {
    'a': 'hello',
    'b': [7, 8, 9],
    'c': False
}

print(dictionary['c'])
print(dictionary['b'][1])

# Check Keys or Values in Dictionary
print('c' in dictionary.keys())
print("hello" in dictionary.values())


person = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}

print(person.keys())
print(person.values())
print(person.items())

# get values, None if there's no specified key
print(person.get("name"))
print(person.get("country")) 
print(person.get("country", 'Indonesia'))  # if None, return Indonesia
# add items
person["city"] = 'Jakarta'
# update items
person["age"] = 32
# remove key, return value
print(person.pop("is_student"))
print(person)
# remove all items
person.clear()
print(person)


# CREATE DICTIONARY
make_dict = dict(name='Adam Ghifari', age=27, city='Bandung')
print(make_dict)

make_dict = dict([ ("apple", 25000), ("banana", 13000), ("tomato", 7500) ])
print(make_dict)



# DICTIONARIES INSIDE A LIST
my_list = [
    {
        'name': 'najma',
        'age': 22,
        'nickname': ['ma', 'tth']
    },
    {
        'highschool': 'SMAN3',
        'univ': ['unpad', 2019]
    }
]

print(my_list)
print(my_list[0])
print(my_list[0]['nickname'])
print(my_list[-1]['univ'][1])






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