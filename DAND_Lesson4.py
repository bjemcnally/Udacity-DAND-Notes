# Lesson 4: Functions

# Defining Functions

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(10, 3)

'''
- def keyword indicates function (function header ends with colon)
- followed by name of function (rules for function names are the same as for variable names)
- then arguments in parentheses, separated by commas (recall that arguments are values passed as inputs to a function)
- arguments are NOT required:
'''

def print_greeting():
    print("Hello world!")

'''
- within indented body of function, we can refer to argument variables and define new variables
- local variables (like pi in first above ex) can only be used within the function
- return key is often included to give back an output value when the function is called
- if a function doesn't explicitly return anything, it will return None by default
- print gives output to the console, return just allows it to be used within Python
'''

# Default Arguments

def cylinder_volume(height, radius=5):
    pi = 3.14159
    volume = height * pi * radius **2

print(cylinder_volume(10,5)) # gives the same answer as
print(cylinder_volume(10)) # bc this defaults radius to 5 as define in the function

'''
- here the variable radius will default to 5 when used in the body of the function
- this can make code more concise
- useful when a variable has a common value, but is still potentially variable
- it's easy to use the function with a different radius by defining it when the function is called:
'''

print(cylinder_volume(10, 7))

'''
note that you can pass values to your functions in two ways:
'''

cylinder_volume(10, 7) # by position (implicitly)
cylinder_volume(height=10, radius=7) # by name (explicitly)

# Variable Scope

'''
the parts of s program that a variable can be referenced, or used, from

local scope, means defined (and only usable) within a function

this means you could use the same variable name in different functions (e.x. 'answer'), as long as those variables have different scope

global scope, variables defined outside of functions

Python doesn't allow you to change or reassign a variable that aren't in a functions' scope
'''

# Documentation

'''
documentation string or docstring, a type of comment used to explain the purpose of a function and how it should be used, ex:
'''

def population_density(population, land_area):
    """Calculate the population density of an area

    INPUT:
    population: int, the population of the area
    land_area: in or float, this function is unit-agnostic, if you pass in values in terms of sq km or sq mi the function will return a density in those units
    OUTPUT:
    population_density: population / land_area, the population density of a particular area
    """
    return population / land_area

'''
- first line is a brief explanation of the function's purpose, recommended to be a phrase ending in a period
- sometimes this is sufficient documentation (ie a single line)
- next is an explanation of the function's arguments (inputs), their purpose and what types they should be
- finally a description of the output

*** for consistency, always use triple double quotes! """ ***
*** include blank space after one line in multiline docstront
*** unless it's a one line, closing quotes should be on a line by themselves
'''

# Lambda Expressions

'''
lambda expression, used to create an anonymous function (function that doesn't have a name)

not ideal for complex functions, but can be useful for short simple functions

compare the two below
'''
# standard function
def double(x):
    """Doubles the input value."""
    return x * 2

# lambda function with same purpose
double = lambda x: x * 2

'''
both are called in the same way:
'''

double(2) # returns 4

'''
to include more than one argument in lambda function, put them before the color, separated by commas, ex:
'''

lambda x, y: x + y

# Iterators and Generators

'''
iterables are objects that can return one of their objects at a time (e.x. list with >1 elements)

iterator: an object that represents a stream of data

generator: a function that creates an iterator
'''

def my_range(x):
    # This is an example of a generator function.
    i = 0
    while i < x:
        yield i
        i += 1

'''
yield allows the function to return values one at a time and start where it left off each time it's called

yield keyword is what differentiates a generator from a typical function
'''

print(my_range(4))

'''
calling my_range(4) returns an iterator we can then iterate through

using a for loop, we can print values from this stream of data
'''

for n in my_range(4):
    print(n)

'''
generators are a lazy way to build iterables. useful when full list wouldn't fit in memory, or when cost to calculate each list element is high and you want to do it as late as possible. but, they can only be iterated over once!
'''

# Generator Expressions

'''
you can create generators in the same way you create list expressions, except with () instead of []
'''

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares