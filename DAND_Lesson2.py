# print function
''' 
include parentheses! 
'''

print('waddup')

# Arithmetic Operators
'''
+, -, *, /

exponentiation **

modulo %, returns remainder (and only the remainder) after you divide first number by the second
    9 / 2 would give 1 

integer division // rounds answer DOWN to an integer
    9 // 2 would give 4
    rounds down even if answer is negative 
    -7 // 2 would give -4
'''
# Variables and Assignment Operators

'''
= is the assignment operator, assigns a name to a value

remember that variable names should be descriptive, contain only letters, numbers and underscores, keep them lowercase 

connecting names with underscores is called snake case
'''

x = 2
y = 3
z = 4

''' is equivalent to'''

x, y, z = 2, 3, 5

'''useful for length, width, height or coordinates (for example)

+= or -= can be used to change the value of a variable

these work with all arithmetic operators

'''

# Integers and Floats

'''
floats are/allow numbers with fractional values (not integers)

type() function will tell you  the type of an object

float()
int()

converting an float to a int does not round, it just cuts off anything after the decimal

converting an int to a float just adds a 0 after the decimal

limit lines of python to 79-99 characters!

Exception is a problem that occurs when the code is running

Syntax error is a problem detected when Python checks the code before it's run
'''

# Booleans, Comparicon Operators, and Logical Operators

'''
bool, a boolean is a data type that can have a value of TRUE or FALSE

Comparison operators:
<, >, <=, >=, ==, !=


Logical operators:
and, evaluates if both sides are TRUE
or, evaluates if at least one side is TRUE
not, flips the bool value
'''

# Strings

'''
strings are another data type (text)

use backslash to escape quotes:
'''

print("'You'\re great'")

'''
+ will combine strings (concatenate)
'''

first_word = "Hello"
second_word = "There"
print(first_word + " " + second_word)

'''
* can be used to repeat strings
'''

word = "hello"
print(word * 5)

'''
len() can tell us the length of a string (number of characters)
'''

udacity_length = len("Udacity")

# Types and Type Conversion

'''
you can check the type of any object using type()

you can also use functions inside functions:
'''

print(type(600))

'''
you can change between data types as needed:
'''

float(600)
string(600)
int(600.4)

# String Methods

'''
methods are associated with different types of objects; there are different methods depending on what object you are working with

methods are functions that 'belong' to an object
'''

print("merry christmas".title())

'''
here the title() method capitalizes the first letter in each word in a string

inputs within parentheses of a function are called arguments

the object preceding the method is always its first argument

sometimes methods do take arguments within the parentheses:
'''

print("one fish", "two fish", "red fish", "bluefish".count("fish"))

# Lists Memberships Operators

'''
containers of data contain other data types and even other containers

list, a data type for mutable ordered sequences of elements, ex:
'''

months = ['January', 'February', 'March', 'April']

'''
you can look up individual elements in a list by their index, 
REMEMBER TO USE ZERO-BASED INDEXING, ex:
'''

months[0] # is 'January'

'''
use negative indexes to index from the end of the list, ex:
'''

months[-1] # this is 'April

'''
we can use Python slicing notation to access a sub-sequence of a list, ex:

list_name[start_index:end_index_plus1]

NOTE: lower bound is INCLUSIVE, upper bound is EXCLUSIVE
'''

months[1:3] # this is a list = ['February', 'March']

'''
to include ends of index:
'''

months[:3] # this starts at 0 and ends at 2

months[1:] # this starts at 1 and ends at the end

'''
both strings and lists support the len() function, indexing, and slicing

both also support membership operators:

IN, evaluates if object on left side is included in object on right

NOT IN, evaluates if object on left side is not included in object on right side
'''

greeting = "Hello there"
print('her' in greeting) # this will return TRUE (tHERe)
print('him' in greeting) # this will return FALSE

'''
NOTE: you can index a single element to return the element list_name[1] or to return a list that contains that element list_name[:2]

Lists can be modified after their creation, but strings can't (mutable vs immutable)
'''

baby_names = ['Johnathan', 'Thomas', 'Douglas', 'James']
baby_names[1] = 'Daniel' # this will replace Thomas with Daniel

'''
REMEMBER this for each data type: is it mutable? is it ordered (and therefore indexable)? different types have different methods which will dictate what type you use for an application
'''

# List Methods

'''
Useful functions:

len() returns number of elements
max() returns the greatest element (e.x. largest number or last alphabetically)
min()
sorted() returns a copy of the list sorted, but does not actually change the list itself
    add optional argument reverse=True to reverse sort order
'''

baby_names = ['Johnathan', 'Thomas', 'Douglas', 'James']
print(sorted(baby_names, reverse=True))

'''
join method (not function!)
    only works with strings
    takes a list of strings as an argument and returns a string consisting of the list elements joined by a separator string ('\n' below puts each on its own line)
    make sure list elements are seperated by commas!
'''

new_str = "\n".join(['Johnathan', 'Thomas', 'James'])

'''
append method
    adds an element to the end of the list
'''

baby_names.append('Juliette')
print(baby_names)

# Tuples

'''
for immutable ordered sequences of elements, similar to lists except that are are IMMUTABLE (ca't add, remove, or sort)
'''

dimensions = 52, 40, 100 # parenthesis are optional when using tuples

'''
tuple unpacking: assign variables to individual elements of the tuple
'''

lenth, width, height = dimensions
print("The dimensions are {}x{}x{}".format(length, width, hight))
# this will print "The dimensions are 52x40x100"

# SETS

'''
a data type for mutable unorderd collections of UNIQUE elements (remove duplicates)
'''

# if list_of_countries is a list with duplicates
country_set = set(list_of_countries) # will remove duplicates

'''
you can add elements to sets using .add() method (.append() is for lists!)
'''

country_set.add('New Country')

'''
.pop() method will randomly remove an element (random bc sets are UNordered)
'''

# Dictionaries and Identity Operators

'''
a data type for mutable objects that store mappings of unique key values
'''

elements = {'hydrogen' : 1,
         'helium' : 2, 
         'carbon' : 6}
elements['lithium'] = 3 # this will add an element
# dictionary_name[value] = key

print(elements['carbon']) # this will print 6 (the corresponding value to key 'carbon')

'''
dictionary keys are similar to list indices, we can select elements by putting the key in square brackets
'''

print('sodium' in elements) # will return False

'''
.get() method looks up keys in dictionaries but return None or default value of your choice if the key isn't found

if you are unsure if a key exists in a dictionary, .get() is safer than square brackets for lookup because square brackets will return errors which may crash your program
'''

'''
identity operators:

is, evaluates if both the sides have the same identity

is not, evaluates if both sides have different identities
'''

n = elements.get('boron')
print(n is None) # will return True (boron isn't in dictionary)
print(n in not None) # will return False

'''
= checks for equality
is checks for identity

two lists can be equal without being identical (ie. depending out how there are defined)

a = [1, 2]
b = a
c = [1, 2]

a, b, and c are equal, but only a and b are identical because they are defined as being identical
'''

# Compound Data Structures

'''
You can store a dictionary in another dictionary ('nested' dictionaries)

You can then look up information in the same way
'''

elements = {'hydrogen': {'number': 1, 
                        'weight': 1.00794,
                        'symbol': "H"},
            'helium': {'number': 2, 
                        'weight': 4.002602,
                        'symbol': 'He'}}

print(elements['helium'])
print(elements.get('unobtanium','There\'s no such element!'))

'''
to look up specific information, you just need to set of brackets (ie. provide both keys)
'''

print(elements['helium']['weight']) # will print 4.002602