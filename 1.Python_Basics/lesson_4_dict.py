# DICTIONARIES
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