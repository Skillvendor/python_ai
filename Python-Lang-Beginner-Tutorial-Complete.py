
# coding: utf-8

# In[1]:


x = 3
print(type(x)) # Prints "<class 'int'>"
print(x)       # Prints "3"
print(x + 1)   # Addition; prints "4"
print(x - 1)   # Subtraction; prints "2"
print(x * 2)   # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y)) # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"


# In[2]:


t = True
f = False
print(type(t)) # Prints "<class 'bool'>"
print(t and f) # Logical AND; prints "False"
print(t or f)  # Logical OR; prints "True"
print(not t)   # Logical NOT; prints "False"
print(t != f)  # Logical XOR; prints "True"


# In[3]:


hello = 'hello'    # String literals can use single quotes
world = "world"    # or double quotes; it does not matter.
print(hello)       # Prints "hello"
print(len(hello))  # String length; prints "5"
hw = hello + ' ' + world  # String concatenation
print(hw)  # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # 


# In[4]:


# documentation on more from string: https://docs.python.org/3.5/library/stdtypes.html#string-methods


# In[5]:


#A list is the Python equivalent of an array, but is resizeable and can contain elements of different types:

xs = [3, 1, 2]    # Create a list
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
print(xs[-1])     # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'     # Lists can contain elements of different types
print(xs)         # Prints "[3, 1, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)         # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()      # Remove and return the last element of the list
print(x, xs)      # Prints "bar [3, 1, 'foo']"


# In[19]:


# For Loops
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# Prints "cat", "dog", "monkey", each on its own line.

#If you want access to the index of each element within the body of a loop, use the built-in enumerate function:

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line


# In[25]:


# Loop over 2 arrays at the same time
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#What is your name?  It is lancelot.
#What is your quest?  It is the holy grail.
#What is your favorite color?  It is blue.


# In[10]:


# Most of the time you need to iterate over the elements of a list and apply operations to get another list. This can be done in three ways(best way is the last one):
# 1
squares = []
for x in range(10):
    squares.append(x**2)
print(squares) # Prints "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"

# 2
squares = list(map(lambda x: x**2, range(10)))
print(squares) # Prints "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"

# 3
squares = [x**2 for x in range(10)]
print(squares) # Prints "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"


# In[13]:


# By writing without a for loop we call it a List Comprehension. They have an expression(anything) which is followed
# by one or more For clauses which in turn are followed by one or more IF statements, and we put everything in brackets.
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs) # Prints "[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]"

#Exercise: What would this be equivalent to if we were to write it with For loops?
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs) # Prints "[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]"


# In[16]:


# We can also have nested list comprehensions:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Let's transpose the matrix using for statements:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed) # Prints "[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]"

# Exercise 2: transpose the matrix without employing the for loop(use the list comprehension fact that the first argument can be any expression)
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose) # Prints "[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]"


# In[17]:


#Slicing
nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"


# In[21]:


# Tuples
t = 12345, 54321, 'hello!'
print(t[0]) # Prints 12345
print(t) # Prints (12345, 54321, 'hello!')
print(len(t)) # Prints 3
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u) # Print ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
#t[0] = 88888
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])

# Odd cases when you need to make empty tuples or 1 elements tuples:
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty)) # Prints 0
print(len(singleton)) # Prints 1
print(singleton) # Prints ('hello',)


# In[22]:


# Dictionaries are your normal hashes
d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print(d['cat'])       # Get an entry from a dictionary; prints "cute"
print('cat' in d)     # Check if a dictionary has a given key; prints "True"
d['fish'] = 'wet'     # Set an entry in a dictionary
print(d['fish'])      # Prints "wet"
# print(d['monkey'])  # KeyError: 'monkey' not a key of d
print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
del d['fish']         # Remove an element from a dictionary
print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # {'guido': 4127, 'jack': 4098, 'sape': 4139}


# In[23]:


# Loop for dictionaries
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"


# In[26]:


#If you want access to keys and their corresponding values, use the items method:

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"


# In[27]:


# Dictionary comprehensions: These are similar to list comprehensions, but allow you to easily construct dictionaries. For example:

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"


# In[33]:


# Loops: Iterating over a set has the same syntax as iterating over a list; however since sets are unordered, you cannot make assumptions about the order in which you visit the elements of the set:

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: fish", "#2: dog", "#3: cat"


# In[34]:


# Set comprehensions: Like lists and dictionaries, we can easily construct sets using set comprehensions:

from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)  # Prints "{0, 1, 2, 3, 4, 5}"


# In[37]:


d = {(x, x + 1): x for x in range(6)}  # Create a dictionary with tuple keys
t = (5, 6)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"
print(d)          # Prints "{(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, (5, 6): 5}"


# In[38]:


#Functions
#Python functions are defined using the def keyword. For example:

def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))
# Prints "negative", "zero", "positive"

#We will often define functions to take optional keyword arguments, like this:

def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)

hello('Bob') # Prints "Hello, Bob"
hello('Fred', loud=True)  # Prints "HELLO, FRED!"


# In[42]:


# Lambda Expressions
# Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0)) # Prints 42
print(f(1)) # Prints 43


#The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs) # Prints [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# You can also use lambda with map(just use list comprehension)
arr = [1,2,3]
print(list(map(lambda x: x ** 2, arr))) # Prints [1, 4, 9]


# In[43]:


# Classes
# The syntax for defining classes in Python is straightforward:

class Greeter(object):

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"

