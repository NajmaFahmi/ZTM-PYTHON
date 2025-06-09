# FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def greet():
    print("Hello!!!")
greet()


def greetings(name):    # name is parameters
    print(f"Hello {name}!!!")

greetings("Najma")   # Najma is arguments
greetings(name="Ghifari")


# using default parameters
def greets(name="Guest"):
    print(f"Hello {name}!!!")

greets()
greets("Achmad")


# keyword arguments
def intro(name, age):
    print(f"Hello {name}! You are {age} years old this year.")
intro(age=23, name="Najma")    # order is not important


# return something
def add(x, y):
    return x+y

result = add(5,2)
print(result)
print(add(6,3))


def stats(x, y):
    return x+y, x*y

added, multiplied = stats(5,2)
print(added), print(multiplied)


# function inside function
def stats(num1, num2):
    def total(x, y):
        return x+y
    def product(x, y):
        return x*y
    return total(num1, num2), product(num1, num2)

added, multiplied = stats(5, 2)
print(added)
print(multiplied)



# EXERCISE
# create function to draw the picture --> if 0 print '', if 1 print '*;
def draw_picture(pict):
    for alist in pict:
        for i in alist:
            if (i == 0):
                print(" ", end='')
            elif (i == 1):
                print("*", end='')
        print(" ")


christmas_tree = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
draw_picture(christmas_tree)

heart = [
    [0,1,0,0,0,1,0],
    [1,1,1,0,1,1,1],
    [1,1,1,1,1,1,1],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,1,0,0,0]
]
draw_picture(heart)



# Docstrings = information abt your function
def test():
    '''
    This function is a function test and will do nothing
    '''
    pass

test()
print(test.__doc__)


# Clean Code
# from this
def is_even_or_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

# to this
def is_even(num):
    return num % 2 == 0

print(is_even_or_odd(4))
print(is_even(3))


# *args --> anything as tuple
def add_all(*args):
    print(args)
    return sum(args)

x = add_all(1,2,3,4,5)
print(x)


# **kwargs --> anything as dict
def intro(**kwargs):
    print(kwargs)
    print(kwargs.values())

intro(name="Najma", city="Sukabumi")



# EXCERCISE
# create a function to know which one is the highest even number
def highest_even(a_list):
    new_list = []
    for i in a_list:
        if i % 2 == 0:
            new_list.append(i)
    highest = sorted(new_list)[-1]
    return highest

print(highest_even([10,2,3,4,8,11]))
print(highest_even([30,451,70,31,88]))

# or

def highest_even(a_list):
    new_list = [i for i in a_list if i % 2 == 0]
    highest = max(new_list)
    return highest

print(highest_even([10,2,3,4,8,11]))
print(highest_even([30,451,70,31,88]))




# WALRUS OPERATOR
# assign a value to a variable as part of an expression (:=)

# before
text = "Hellllooooooooo....."
if len(text) > 10:
    print(f"The text contains {len(text)} letters.")

# after
text = "Hellllooooooooo....."
if (n := len(text)) > 10:
    print(f"The text contains {n} letters.")

# # before
# line = input("Enter something : ")
# while line != "quit":
#     print(f"You typed: {line}")
#     line = input("Enter something : ")

# # after
# while (line := input("Enter something : ")) != "quit":
#     print(f"You typed: {line}")


# before
nums = [1,2,3,4,5]
results = []
for n in nums:
    stats = n * 2 + 2
    if stats > 0:
        results.append(stats)
print(results)

# after
nums = [1,2,3,4,5]
results = [stats for n in nums if (stats := n*2+2) > 0]
print(results)

