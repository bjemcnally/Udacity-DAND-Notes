# Lesson 5: Scripting

"""
- Python Installation and Environment Setup
- Running and Editing Python Scripts
- Interacting with User Input
- Handling Exceptions
- Reading and Writing Files
- Importing Local, Standard, and Third-Party Modules
- Experimenting with an Interpreter

Python Installation

- to open command line in Windows:
    go to run... type cmd and press enter

- to check for previously installed software using command line:
    python --version

    or

    git --version

Running a Python Scripting

- start git cmd
- use CD to Change Directory until you are in the folder that contains your script, ex:

cd Desktop/DAND/

- use dir to check that the file is in that Directory
- to run the file type:
"""

python filename.py

"""
- CNTRL Z + ENTER on Windows will exit python
"""

# Programming Environment Setup

"""
- This course recommends saving .py files in code editor and then running them from command line (not from within the editor), get in the habit of doing this now!
"""

# Scripting with Raw Input

name = input('Enter a name: ')
print('Hello', name.title())

"""
- input() function has an optional argument that can be used to specify a prompt shown to the User
- input() interprets the input as a string so you'll have to wrap it int() or float() if you want to use it as a number
"""

num = float(input('Enter a number: '))
num += 20
print(num)

"""
- eval() is a built-in function that evaluates a string as a line of Python:
"""

num = 30
x = eval('num + 42')
print(x)

# See Q_scripting_raw_input

# Errors and Exceptions

"""Two types of errors:

- syntax errors, when Python can't interpret the code because of incorrect syntax (missing parentheses or ", etc.)

- exceptions, when unexpected things happen during execution of the code
    - ValueError occurs when a built-in operation of function is given an argument with the correct type, but an inappropriate value
    - NameError occurs when we try to reference a variable that we didn't define yet (or miss-typed)
"""

# Handling Errors

x = int(input('Enter a number: '))
# raises an error if you input a word, rather than crash the code, use a try statement

"""
Try Statement, code in try block is first run and if Python runs into any exceptions it will jump to the except block

the program then continues to run whether or not it runs into an exception during the try block (ex below 'Attempted Input' will print either way)
"""

try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number!')

print('\nAttempted Input\n')

"""
if you want the code to continue running until a valid number is supplied, use a while loop and break the loop if all the code in the try block successfully executes

this code, below, won't print 'Attempted Input' after taking a valid number because it's within the while loop
"""

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number!')

    print('\nAttempted Input\n')

"""
if we want to print 'Attempted Input' after every attempt, use the optional finally component of the try statement:
"""

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number!')
    finally: # this will print after every attempt
        print('\nAttempted Input\n')

"""
4 components of a try statement:

- try, the only mandatory portion
- except, if Python runs into an exception while running the try block, it will jump to the except block that handles that exception
- else, if Python runs into no exceptions in the try block, it will run this block after the try block
- finally, before Python leaves the try statement, it will run the finally block under any conditions, even if it's ending the program

rather than except ANY error, you can specify which error:
"""

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError, KeyboardInterrupt: #specifies type(s) of error
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')

"""
to stop a Python program that is running, use CNTRL + C

the finally block is run NO MATTER WHAT as the program exits the try statement

you can specify which errors to except, or, if you want to execute different blocks of code depending on the error raised, use multiple except blocks:
"""

while True:
    try x = int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s not a valid number!')
    except KeyboardInterrupt:
        print('No input taken')
        break
    finally:
        print('\nAttempted Input\n')

# see Q_handling_errors.py

# Accessing Error Messages

"""
When you handle an exception, you can still access its error message like this:
"""

try:
    # some code
except ZeroDivisionError as e:
    # some code
    print('ZeroDivisionError occurred: {}'.format(e))

"""
this means you can access and see your error messages, even if you handle them to keep your program from crashing

if you don't have a specific error you're handling, you can access errors generically like this:
"""

try:
    # some code
except Exception as e:
    # some code
    print('Exception occurred: {}'.format(e))

# Reading and Writing Files

"""
we can automate tasks involving files using Python programs!

open the file using built-in function open(), include a string with a path to the file and any optional parameters we want to specify. this returns a file object that Python uses to interact with the file itself.
"""

f = open('/my_path/my_file.txt', 'r')
# f is the variable name we have assigned
# r says 'read-only' , this is the default if left unspecified

"""
once a file has been opened, we use the .read() method to access the contents of the file, this takes the text contained in the file and puts it into a string
"""

f = open('/my_path/my_file.txt', 'r')
file_data = f.read()
# file_data is now the string return from this method

"""
when you finish with a file, you should close it:
"""

f = open('/my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)

"""
in addition to reading from a file, you can write to a file, which will change the content of the file. just open the file in writing mode:
"""

f = open('some_file.txt', 'w')
# w specifies writing mode

"""
once you open a file in writing mode, anything that it contained previously will be deleted

if you want to add to an existing file, use append mode instead

if the file does not exist, Python will create a new one for you

then you can use the .write() method to write to it
"""

f = open('new_file.txt', 'w')
f.write('Hello World!')
f.close() # don't forget to close it!

"""
Python provides a special syntax that auto closes a file

with keyword allows you to open a file, use it, and then automatically closes it after the indented code is executed
"""

with open('another_file', 'r') as f:
    file_data = f.read()

"""
however, the file (f) is only accessible within the with statement

but the file_data variable is accessible!
"""

# Importing Local Scripts

"""
in addition to reading data from files, we can import Python code from other scripts

if the script you want to import is in the same directory as the one you are working on, import like this:
"""

import other_script # leave off .py extension from name

"""
import statements are written at the top of a Python script, each one on a separate line

module, a file with Python definitions and statements

when you import a file (e.x. other_script) it creates an object called other_script with a type module

you can access variables from other script like this:
"""

print(other_script.variable_name) # this will print variable_name from other_script module

"""
you can access functions from another file in the same way:
"""

file_name.function_name(argument1, argument2)

"""
instead of typing out the other file's name each time you want to access it, add and alias
"""

import other_file as of
# now you can use 'of' in place of other_file when calling functions or variables from that file

"""
if you want Python to ignore parts of other_file (ex. code that tests its functionality), put those parts within a if __name__ block:
"""

def function1(arg1):
    # code for this function

def function2(arg2):
    # code for this function

if __name__ == '__main__':
    # code you want ignored when importing to another script

"""
if __name__ block is only executed when the file is run directly, NOT when it is imported to another script

it is generally a good idea to include executable statements in a if __name__ block or, alternatively, include them in a function called Main and call this in the if __name__ block
"""

def main():
    # code you want ignored when importing to another script

if __name__ == '__main__':
    main()

"""
import statement creates module (object type), to access objects from imported modules, you need to use dot notation
"""

import other_python_file
other_python_file.function_name(arguments)

"""
instead of referencing imported module by its full name, you can create an alias
"""

import other_python_file as opf
opf.function_name(arguments)

"""
to avoid running executable statements in an imported script, include if __name__ == "__main__" block. or, alternatively, include exectubles in a function called main and call this function in the if main block
"""

# see demo.py and useful_functions.other_python_file

# The Standard Library

"""
tons of useful modules have already been written, they just need to be imported!
"""

import math

print(math.factorial(4))

# Techniques for Importing Modules

"""
instead of importing an entire module, you can specify a function(s) or class(es):
"""

from module_name import object_name, another_object_name

"""
this way you only import what you need and you don't need to use dot notation to access it (just refer to it as object_name)

some modules have standard abbreviations, check the documentation!

you can also abbreviate an imported objects name:
"""

from module_name import object_name as on

"""
some large modules are split into sub-modules that are contained within a package (ie a module that contains submodules)

submodule names include a "." ex: os.path

two ways to use objects in submodules:
"""

import os.path # import only submodule

os.path.isdir('my_path')

# or

import os # import the whole module

os.path.isdir('my_path')

"""
sometimes objects in a module have the same name as the module:
"""

from datetime import datetime

"""
using datetime after this will refer to the datetime object NOT the entire module
"""

# Third-Party Libraries

"""
we can install libraries using pip, a package manager that is included with Python 3. A popular alternative to pip is Anaconda, which is designed specifically for data science.
"""

pip install pytz # in cmd will install pytz library

"""
once installed, you can import 3rd party packages using the same notation used to import from the standard library

it is standard practice to put import statements for third party libaries AFTER import statements from the standard library

if you are using many third party packages, list them (the project's dependencies) in a file called requirements.txt

each line of the file contains the name of the package and its version number, ex:
"""

beautifulsoup==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1

"""
its important to use the same version that the program author used when they wrote the program... which is why its a good idea to include version in requirements.txt

you can use pip to install all of a projects dependencies at once using this command in cmd:
"""

pip install -r requirements.txt

# Experimenting with an Interpreter

"""
when you open your terminal and type 'python' you start the Python interactive interpreter where you can interact with Python directly

in an interpreter, the value of the last line will be output (printed) automatically

to close the command interpreter type 'exit()' or CTRL + Z
"""

# Online Resources

"""
bookmarked in DAND folder
"""