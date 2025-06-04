# Escape Sequences
text1 = "hello it's me, \"Najma\", nice to meet you"
print(text1)
text2 = "hello,\n welcome to the final show!"
print(text2)



# Formatted Strings
#normal
name = 'Johnny'
age = 32
print('Hi! my name is ' + name + ', and i\'m ' + str(age) + ' years old.')

#fstring
print(f'Hi! my name is {name}, and i\'m {age} years old.')

price = 4
tax = price*0.5

total = price + tax
print(f'Total cost = ${total}')

print(f'Total cost = ${price+tax}')

#.format()
print('Hi! my name is {} and i\'m {} years old.'.format(name, age))
print('Hi! my name is {0} and i\'m {1} years old.'.format(name, age))
print('Hi! my name is {new_name} and i\'m {new_age} years old'.format(new_name='Jeno', new_age=24))



# String Indexing
text = "HELLO"
print(text[0])
print(text[1])
print(text[-1])
print(text[-2])
print(text[0:2])
print(text[:2])
print(text[1:3])
print(text[1:])
print(text[2:])
print(text[:4] + " YOU")

numbers = '01234567'
print(numbers[::2])



# FUNCTIONS & METHODS
text = "HellO gOod Morning"

print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())

print(text.find('g')) #case-sensitive, -1 if not found
print(text.index('M')) #case-sensitive, error if not found
print(text.count('o')) #case-sensitive
print(text.startswith('Hell')) #case-sensitive
print(text.endswith('ing')) #case-sensitive

find_this = 'g'
if text.find(find_this) == -1:
    print("Not Found!")
else:
    print(f"Found! index = {text.find(find_this)}")

count_this = 'o'
if text.count(count_this) != 0:
    print(f"There are {text.count(count_this)} \"{count_this}\" in the text")
else:
    print(f"{count_this} is not found!")


text = "Hello-this-is-me"
print(text)
print(text.replace('-', ' '))
print(text.split('-'))

text = "  Najma "
print(text.strip())

list_cars = ['raize', 'baleno', 'wuling', 'byd']
print(" - ".join(list_cars))


birth_year = input('What year were you born?')
print(f"You are born in {birth_year}")

