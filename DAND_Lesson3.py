# CONTROL FLOW: INTRODUCTION

'''
conditional statements and loops
    Boolean expressions
    for and while loops
    break and continue to exit or skip loops
    helpful built in functions (e.x. zip and enumerate)
    list comprehensions
'''

# CONDITIONAL STATEMENTS

'''
if statements run or skip indented code based upon whether a statement is TRUE or FALSE 
'''

if phone_balance < 5:
        phone_balance += 10
        bank_balance -=

'''
if, elif, and else

elif evaluates if previous if is false. you can have multiple elif blocks to handle different situations

indentation, multiples of four (4) spaces
'''

# Quiz

points = 174  # use this input when submitting your answer

# write your if statement here
if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dea, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
elif prize <= 200:
    result = "Congratulations! You won a pengiun!"

print(result)

'''
Note: Lower bounds of comparison operators are not required because previous statement would apply if points was <50, etc.
'''

# Boolean Expressions for Conditions

'''
Complex Boolean Expressions can contain multiple comparisons, logical operators, and even calculations, ex:
'''
weight = 55
height = 164

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

'''
also works for non-numerical data, ex
'''

if is_raining and is_sunny:
    print("Is there a rainbow?") #will print if both are TRUE

'''
combine AND, OR, and NOT - use parentheses as needed!

entire IF statement must be Boolean, ie evaluate as TRUE or FALSE

if statements evaluate Boolean expressions as Boolean objects (ie either TRUE or FALSE)

Truth Value Testing, the following constants are defined to be False (non-Boolean objects as conditions in if statements):
- None and False
- zero of any numeric type: 0, 0.0, etc
- empty sequences and colletions: (), [], {}, etc
'''

errors = 3
if errors: #evaluates as True because errors != 0
    print("There are " + errors + " mistakes")
    #print("You have {} errors to fix!".format(errors)) will also work, {} is replaced with second arg of .format() method
else:
    print("No mistakes here!")

# FOR LOOPS

'''
loops can iterate over an iterable, ie an object that can return one of its elements at a time (strings, lists, tuples, dictionaries and files)
'''

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities: # cities is the iterable and city is the loop's iteration variable
    print(city.title())

'''
its common to name the iteration variable in this way (as the singular of the list name, etc.)

for loops can create and modify lists:
'''

capitalized_cities = [] # create empty list

for city in cities: # this loop adds cities to new list 
    capitalized_cities.append(city.title())

print capitalized_cities

'''
modifying a list is more involved and requires the use of a new function: range(start, stop, step)

range is a built-in function used to create immutable sequences of numbers
- all three arguments must be integers
- start is the first number
- stop is one above the last number (ie it is exclusive)
- step is the difference between the numbers in the sequence
- if unspecified, start defaults to 0 and step defaults to 1

calling range with one integer makes it that the stop argument
'''

print(list(range(4)))
# will return [0, 1, 2, 3]
# starts at 0, ends at 3, step is 1

'''
calling range with two integers will make them the start and stop
'''

print(list(range(2, 6)))
# will return [2, 3, 4, 5]

'''
calling range with three integers will return list from first to second minus one separated by the third
'''

print(list(range(1, 10, 2)))
# will return [1, 3, 5, 7, 9]

'''
printing the output of range() only shows you a range object, in these examples we adopt range in a list so that a list is printed

you can view the values in a range by converting to a list or iterating through it using a for loop

use range function to generate the indices of each value in the cities list
'''
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)): 
    # len(cities) = 4, since it is the only argument, it is the stop argument
    # range will be from 0 to 3
    cities[index] = cities[index].title()
        # here we loop through the range 0-3 using index variable from our range and replace original with capitalized version by redefining each element in the cities list

'''
you can iterate through a range, but to see its values you must convert it to a list or iterate using a for loop
'''

# Iterating Through Dictionaries with For Loops

'''
iterating through a dictionary like this
'''

for n in dictionary_name:

'''
will only give you access to the keys

if you want to iterate through both keys and values, use built-in method .items():
'''

cast = {
            "Jerry Seinfeld": "Jerry Seinfeld",
            "Julie Louis-Dreyfus": "Elaine Benes",
            "Jason Alexander": "George Costanza",
            "Michael Richards": "Cosmo Kramer"
    }

for key in cast:
    print(key) # will only print keys

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
    # this will print keys and values from dictionary cast

'''
.items() returns tuples of key, value pairs which you can use to iterate over dictionaries in for loops
'''

# While Loops

"""
for loop are 'definite iteration' meaning the loop's body is run a predefined number of times

while loops are 'indefinite iteration'

sum() function returns to sum of elements in a list

.pop() method is the opposite of the append method, it removes last element from a list an returns it

the indented body of the WHILE loop should modify at lease one variable in the test expression or will result in an infinite loop
"""

# Break, Continue

'''
break statement terminates a for or while loop immediately
'''

manifest = [('bananas', 15), ('mattresses', 34), ('dog kennels', 42), ('machine', 120), ('cheeses', 5)]

weight = 0
items = []
for cargo in manifest:
    if weight >= 100:
        break
    else:
        items.append(cargo[0]) # add cargo to items list
        weight += cargo[1] # add cargos weight to weight
# this gives the wrong result and is used to introduce continue
'''
continue statement terminates one iteration of a for or while loop
'''
fruit = ['orange', 'strawberry', 'apple']
foods = ['apple', 'apple', 'hummus', 'toast']

fruit_count = 0
for food in foods:
    if food not in fruit:
        print('Not a fruit')
        continue
    fruit count += 1
    print('Found a fruit!')

print('Total fruit: ', fruit_count)

# output will be:
# Found a fruit!
# Found a fruit!
# Not a fruit!
# Not a fruit!
# Total fruit: 2

# Zip and Enumerate

'''
zip returns an iterator that combines multiple iterables into one sequence of tuples. each tuple contains the elements in that position from all the iterables.

need to convert to list to see the elments via print or iterate through it with a for loop to print the values
'''

items = ['bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses']
weights = [15, 34, 42, 120, 5]

print(list(zip(items, weights)))
# or
for cargo in zip(items, weights): # each element in zip is now cargo (a tuple of the paired elements of items and weights)
    print(cargo[0], cargo[1]) # returns each of the elements in each of the tuples in the zip
# or
for item, weight in zip(items, weights):
    print(item,weight)

'''
you can unzip a list using an asterisk (*)
'''

items, weight = zip(*manifest)
# will result in two lists items taking the first element from each tuple in the list, weight taking the second

'''
sometimes its helpful to iterate and keep track of the index of each element:
'''

for i, item in zip(range(len(items)), items):
    print(i, item)

# will print:
# 0 bananas
# 1 mattresses ,etc

'''
or use enumerate function:
'''

for i, item in enumerate(items):
    print(i, item)

'''
can also use zip to create a dictionary:
'''
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

new_dictionary = dict(zip(list1, list2))

# Quiz

# MY ANSWER
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    point = "{}: {}, {}, {}".format(label, x, y, z)
    points.append(point)

for point in points:
    print(point)

# THEIR ANSWER

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

# this works because each element in new zip consists of label, x_coord, etc. already

# List Comprehensions

'''
use list comprehensions to crease lists quickyl and concisely
'''

cities = ['new york', 'mountain view', 'chicago', 'los angeles']

# old way:

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

# list comprehensions allow us to create a list using a for loop in one step (instead of 2), we also don't need to create an empty list beforehand and append each element as we would in a for loop

capitalized_cities = [city.title() for city in cities]

'''
another example
'''

squares = []
for x in range(9):
    squares.append(x**2)
print(squares)

# as list comprehension:

squares = [x**2 for x in range(9)]
print(squares)

'''
you can also add conditionals to list comprehensions:
'''

squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

'''
to break this one down in English (aka simpler Python):
squares = []
    for x in range(9)
        if x % 2 == 0:
            squares.append(x**2)

the [] brackets indicate a list, the first item is what is to be added to the list given some for loop and condition

if you want to add ELSE. you have to move the conditions to the beginning of the list comprehension (listcomp):
'''

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
