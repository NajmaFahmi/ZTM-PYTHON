#MATH FUNCTIONS
import math
import statistics
import random

print(abs(3.3))
print(round(3.6))
print(math.floor(3.8))
print(math.ceil(3.2))
print(round(3.41567, 2))

print(max(1,0.9,4,2,9,6,9.2))
print(min(1,0.9,4,2,9,6,9.2))
print(sum([1,4,2,9,6,9]))
print(statistics.mean([1,4,2,9,6,9]))
print(statistics.median([1,4,2,9,6,9]))
print(statistics.stdev([1,4,2,9,6,9]))

print(random.randint(2,9))
print(random.random())
print(random.choice([1,4,2,9,6,9]))



# Augmented Assignment Operations
#normal
x = 5
x = x + 2
print(x)

# AAO
x = 5
x += 2
print(x)

x = 3
x *= 4
print(x)

x = 4
x **= 2
print(x)



# Strings
print("hi")

school = 'Padjadjaran University'
print(school)

long_text = '''
this is me
Najma
in 2025
'''
print(long_text)

first_name = 'Katarina'
last_name = 'Bluee'
full_name = first_name + ' ' + last_name
print(full_name)

print('Najma' + ' Fahmi')
print('Najma' + ' 26 ' + 'years old')



# Type Conversion
a = str(100) #integer to string
print(a + ' tahun')

b = float(2) #integer to decimal
print(b)



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