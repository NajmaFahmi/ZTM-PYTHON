# CONDITIONAL LOGIC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONDITIONAL LOGIC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


is_student = True
is_teacher = False
is_academia = True
is_woman = False
is_man = True

if is_student:
    print("You are a student")
else:
    print("You're not a student!! Access denied!")

x = "You are a student" if is_student else "You're not a student"
print(x)


if is_woman:
    print("You are a woman")
elif is_man:
    print("You are a man")
else:
    print("No gender revealed")


# LOGICAL OPERATORS
# and
if is_student and is_woman:
    print("You are placed in women area")
elif is_student & is_man:
    print("You are placed in men area")
else:
    print("You are not a student!")

# or
if is_student or is_teacher:
    print("You are welcomed here..")
else:
    print("Please go back!")

# not
if not is_academia:
    print("You cant access this website")
else:
    print("Welcome academia!") 


# # EXERCISE
# check if you are an expert magician --> "You are a master magician"
# check if you are a magician but not an expert --> "At least you're getting there"
# check if you are not a magician --> "You need magic powers"
is_magician = True
is_expert = False

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician:
    print("You need magic powers")







# LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# FOR LOOP
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

for letter in "hello":
    print(letter)

for i in range(5):
    print(i)

for _ in range(10, 0, -1):
    print(_)

x = 0
for i in range(1, 10, 2):
    print(i)
    x += i
print(x)

for i in {12, 13, 14}:
    for x in ('hello', 'hi', 'welcome'):
        print(i, x)


# FOR AND ELSE LOOP
for i in range(5):
    print(i)
else:
    print("Finished loop")


# WHILE LOOP
count = 0
while count <= 10:
    print(count)
    count += 1

# while True:
#     response = input("Say something: ")
#     if response == "bye":
#         break


# BREAK
count = 0
while count <= 10:
    if count == 5:
        break   # stop the loop
    print(count)
    count += 1


# CONTINUE 
for i in range(5):
    if i == 3:
        continue  # skip that current loop
    print(i)


# PASS
for i in range(5):
    pass  # i'll think abt this later


# NESTED LOOP
for fruit in fruits:
    for letter in fruit:
        print(letter)


# RANGE LEN AND ENUMERATE
my_list = [1, 3, 10, 23, 21]
print(len(my_list))
print(range(len(my_list)))

for i in range(len(my_list)):
    print(my_list[i])

for i, x in enumerate(my_list):
    print(i)
    print(x)
    print(i, x)

for i, char in enumerate("NAJMA"):
    print(i, char)


# FOR LOOPS
user = {
    'name': "Najma",
    'age': 23,
    'is_student': False
}

for i in user.items():
    print(i)

for value in user.values():
    print(value)



# EXERCISE ! CHRISTMAS TREE
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
# iterate over picture, if 0 print '', if 1 print '*;

for alist in picture:
    for i in alist:
        if (i == 0):
            print(" ", end='')
        elif (i == 1):
            print("*", end='')
    print(" ")


# EXERCISE ! Check for duplicates
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

unique_value = []
duplicates = []
for i in my_list:
    if i not in unique_value:
        unique_value.append(i)
    else:
        duplicates.append(i)
print(unique_value)
print(duplicates)

# or

duplicates = []
for i in my_list:
    if my_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)