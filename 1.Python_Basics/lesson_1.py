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



