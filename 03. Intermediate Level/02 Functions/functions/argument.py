# ============================= What is Argument =============================

"""
Argument
--------

An argument is a value passed to a function when the function is called.

Example:

    def greet(name):
        return f"Hello, {name}!"

Here:
    - name -> Parameter
    - "Faruk" -> Argument

"""

def greet(name):
    return f"Hello, {name}!"


print(greet("Faruk"))
# Output: Hello, Faruk!


# ============================= Parameter vs Argument =============================

"""
Parameter:
    A variable defined in the function definition.

Argument:
    A value passed to the function when it is called.

Example:

    def greet(name):
            ↑
        parameter

    greet("Faruk")
          ↑
       argument
"""


# ============================= Types of Arguments =============================

"""
1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Mutable Default Arguments
5. Variable-Length Arguments (*args)
6. Keyword Variable-Length Arguments (**kwargs)
7. Combination of Arguments
"""


# ===============================================================
# 1. Positional Arguments
# ===============================================================

"""
Positional arguments are matched with parameters based on their
position/order.

The order is important.
"""

def display(name, age):
    return f"Name: {name}, Age: {age}"


print(display("John", 25))
# Output: Name: John, Age: 25


# IMPORTANT:
# This is also valid Python.
print(display(25, "John"))
# Output: Name: 25, Age: John

"""
Why?

Because Python matches positional arguments by position:

    display(25, "John")
            ↓      ↓
          name    age

So:
    name = 25
    age  = "John"

Python does NOT automatically know that 25 should be age.

Therefore, "wrong order" is not necessarily a syntax error.
It may simply produce logically incorrect data.
"""


# ===============================================================
# 2. Keyword Arguments
# ===============================================================

"""
Keyword arguments are passed using parameter names.

Syntax:

    function(parameter=value)

The order does not matter.
"""

def display(name, age):
    return f"Name: {name}, Age: {age}"


print(display(name="John", age=25))
# Output: Name: John, Age: 25


print(display(age=25, name="John"))
# Output: Name: John, Age: 25


"""
Because the parameter names are explicitly specified:

    name="John"
    age=25

Python knows exactly where each value belongs.
"""


# ===============================================================
# 3. Default Arguments
# ===============================================================

"""
A default argument has a predefined value.

If the caller does not provide a value,
Python uses the default value.
"""

def display(name, age=18):
    return f"Name: {name}, Age: {age}"


print(display("John"))
# Output: Name: John, Age: 18


print(display("Alice", 25))
# Output: Name: Alice, Age: 25


"""
Here:

    age=18

is a default parameter value.

If age is not provided:
    age = 18

If age is provided:
    the provided value replaces 18.
"""


# ===============================================================
# 4. Mutable Default Arguments
# ===============================================================

"""
Mutable objects:
    - list
    - dictionary
    - set

Using a mutable object as a default parameter can cause
unexpected behavior because the SAME default object is reused
between function calls.
"""


# ---------------------- BAD EXAMPLE ----------------------

def add_info_bad(name, employee_data=[]):
    employee_data.append(name)
    return employee_data


print(add_info_bad("John"))
print(add_info_bad("Alice"))

"""
Output:

['John']
['John', 'Alice']

Why?

Because the default list [] is created once and reused
for multiple calls.
"""


# ---------------------- CORRECT WAY ----------------------

"""
Use None as the default value and create a new list
inside the function when necessary.
"""

def add_info(name, employee_data=None):

    if employee_data is None:
        employee_data = []

    employee_data.append(name)

    return employee_data


print(add_info("John"))
# Output: ['John']

print(add_info("Alice"))
# Output: ['Alice']


"""
Each call gets a new list when employee_data is not provided.
"""


# ===============================================================
# Immutable vs Mutable Default Values
# ===============================================================

"""
Common immutable objects:
    int
    float
    str
    tuple
    bool
    None

Common mutable objects:
    list
    dict
    set

Example:

    def function(x=10):
        ...

    def function(name="John"):
        ...

These are generally safe because integers and strings are immutable.

For mutable objects, prefer:

    def function(data=None):
        if data is None:
            data = []
"""


# ===============================================================
# 5. Variable-Length Arguments: *args
# ===============================================================

"""
*args allows a function to accept any number of positional arguments.

Inside the function, args is stored as a tuple.

Example:

    def add(*numbers):

Here:
    numbers -> tuple
"""


def add(*numbers):

    total = 0

    for n in numbers:
        total += n

    return f"Sum: {total}"


print(add(10, 20))
# Output: Sum: 30


print(add(10, 20, 30, 40))
# Output: Sum: 100


print(add())
# Output: Sum: 0


"""
Example:

    add(10, 20, 30)

Inside the function:

    numbers = (10, 20, 30)

Therefore:

    *args -> tuple
"""


# ===============================================================
# 6. Keyword Variable-Length Arguments: **kwargs
# ===============================================================

"""
**kwargs allows a function to accept any number of
keyword arguments.

Inside the function, kwargs is stored as a dictionary.
"""


def info(**data):

    for key, value in data.items():
        print(f"{key}: {value}")


info(
    name="John",
    age=25,
    country="USA"
)

"""
Output:

name: John
age: 25
country: USA
"""


# ---------------------- Return kwargs ----------------------

def info_dict(**data):
    return data


print(
    info_dict(
        name="John",
        age=25,
        country="USA"
    )
)

# Output:
# {'name': 'John', 'age': 25, 'country': 'USA'}


"""
Inside the function:

    data = {
        "name": "John",
        "age": 25,
        "country": "USA"
    }

Therefore:

    **kwargs -> dictionary
"""


# ===============================================================
# 7. Combination of *args and **kwargs
# ===============================================================

"""
A function can accept both:

    *args
    **kwargs

Example:
"""

def function_name(*args, **kwargs):

    print("args:", args)
    print("kwargs:", kwargs)


function_name(
    10,
    20,
    30,
    name="John",
    age=25
)

"""
Output:

args: (10, 20, 30)

kwargs: {
    'name': 'John',
    'age': 25
}
"""


# ===============================================================
# 8. Combination of Normal Parameters, Default, *args, **kwargs
# ===============================================================

def full_info(id, name, age=18, *skills, **details):

    print(f"ID: {id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Skills: {skills}")
    print(f"Other Details: {details}")


full_info(
    101,
    "Faruk",
    22,
    "Python",
    "Django",
    "Kotlin",
    country="Bangladesh",
    profession="Programmer"
)

"""
Output:

ID: 101
Name: Faruk
Age: 22
Skills: ('Python', 'Django', 'Kotlin')
Other Details: {
    'country': 'Bangladesh',
    'profession': 'Programmer'
}
"""


# ===============================================================
# How full_info() Works
# ===============================================================

"""
Function:

    def full_info(id, name, age=18, *skills, **details):


Call:

    full_info(
        101,
        "Faruk",
        22,
        "Python",
        "Django",
        "Kotlin",
        country="Bangladesh",
        profession="Programmer"
    )


Mapping:

    id
    ↓
    101

    name
    ↓
    "Faruk"

    age
    ↓
    22

    *skills
    ↓
    ("Python", "Django", "Kotlin")

    **details
    ↓
    {
        "country": "Bangladesh",
        "profession": "Programmer"
    }
"""


# ===============================================================
# What are args and kwargs?
# ===============================================================

"""
IMPORTANT:

args and kwargs are NOT special Python keywords.

They are just conventional variable names.

The special syntax is:

    *args
    **kwargs

You could technically write:

    *numbers
    **data

instead.
"""


# ===============================================================
# *args
# ===============================================================

def function_name(*args):

    print(args)


function_name(10, 20, 30)

# Output:
# (10, 20, 30)


"""
Here:

    *args

means:

    Collect all extra positional arguments
    into a tuple.
"""


# ===============================================================
# **kwargs
# ===============================================================

def function_name(**kwargs):

    print(kwargs)


function_name(
    name="John",
    age=25,
    country="USA"
)

# Output:
# {'name': 'John', 'age': 25, 'country': 'USA'}


"""
Here:

    **kwargs

means:

    Collect all extra keyword arguments
    into a dictionary.
"""


# ===============================================================
# *args + **kwargs
# ===============================================================

def function_name(*args, **kwargs):

    print("args:", args)
    print("kwargs:", kwargs)


function_name(
    10,
    20,
    30,
    name="John",
    age=25
)

"""
Output:

args: (10, 20, 30)

kwargs: {
    'name': 'John',
    'age': 25
}
"""


# ===============================================================
# Argument Unpacking
# ===============================================================

"""
* can also be used when CALLING a function.

It unpacks an iterable into positional arguments.
"""

numbers = [10, 20, 30]


def add(a, b, c):
    return a + b + c


print(add(*numbers))
# Output: 60


"""
Without unpacking:

    add(10, 20, 30)

With unpacking:

    add(*numbers)

The list:

    [10, 20, 30]

becomes:

    10, 20, 30
"""


# ===============================================================
# Keyword Argument Unpacking
# ===============================================================

"""
** can be used when CALLING a function.

It unpacks a dictionary into keyword arguments.
"""

person = {
    "name": "John",
    "age": 25
}


def display(name, age):
    return f"Name: {name}, Age: {age}"


print(display(**person))

# Output:
# Name: John, Age: 25


"""
Dictionary:

    {
        "name": "John",
        "age": 25
    }

becomes:

    display(
        name="John",
        age=25
    )
"""


# ===============================================================
# Positional-Only Arguments
# ===============================================================

"""
Python also allows parameters that MUST be passed
positionally.

Use:

    /

Example:
"""

def add(a, b, /):
    return a + b


print(add(10, 20))
# Output: 30


# This is NOT allowed:
#
# add(a=10, b=20)


"""
Everything before / is positional-only.
"""


# ===============================================================
# Keyword-Only Arguments
# ===============================================================

"""
Parameters after a bare * must be passed using keywords.
"""

def student(name, *, age, country):
    return f"{name}, {age}, {country}"


print(
    student(
        "Faruk",
        age=22,
        country="Bangladesh"
    )
)


# This is NOT allowed:
#
# student("Faruk", 22, "Bangladesh")


"""
Here:

    name
    ↓
    Can be positional.

    age
    country
    ↓
    Must be keyword arguments.
"""


# ===============================================================
# Argument Order Rules
# ===============================================================

"""
When calling a function, positional arguments generally come
before keyword arguments.

Correct:

    function(10, 20, name="John")


Incorrect:

    function(name="John", 10, 20)


Example:
"""

def example(a, b, c):
    return a, b, c


print(
    example(
        10,
        20,
        c=30
    )
)

# Output:
# (10, 20, 30)


# ===============================================================
# Important Difference: Parameter vs Argument
# ===============================================================

"""
PARAMETER
---------

Defined in the function definition.

Example:

    def greet(name):
                ↑
             parameter


ARGUMENT
--------

Passed during function call.

Example:

    greet("Faruk")
          ↑
       argument
"""


# ===============================================================
# Final Summary
# ===============================================================

"""
┌──────────────────────────┬──────────────────────────────┐
│ Type                     │ Meaning                      │
├──────────────────────────┼──────────────────────────────┤
│ Positional               │ Matched by position          │
│ Keyword                  │ Matched by parameter name   │
│ Default                  │ Uses predefined value        │
│ *args                    │ Extra positional → tuple    │
│ **kwargs                 │ Extra keyword → dictionary  │
│ /                        │ Positional-only parameters  │
│ *                        │ Keyword-only parameters     │
└──────────────────────────┴──────────────────────────────┘
"""


# ===============================================================
# Memory Trick
# ===============================================================

"""
Argument
    ↓
Value passed to function

Parameter
    ↓
Variable defined in function

*args
    ↓
Extra positional arguments
    ↓
TUPLE

**kwargs
    ↓
Extra keyword arguments
    ↓
DICTIONARY

* at CALL
    ↓
Unpack iterable

** at CALL
    ↓
Unpack dictionary

/ 
    ↓
Positional-only

*
    ↓
Keyword-only
"""


# ===============================================================
# Complete Mental Model
# ===============================================================

"""
                    FUNCTION CALL
                         |
             ┌───────────┴───────────┐
             ↓                       ↓
       Positional                Keyword
             |                       |
             ↓                       ↓
         by order              by name
             |                       |
             └───────────┬───────────┘
                         ↓
                  Parameter Matching
                         |
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Normal         *args          **kwargs
       Parameter          |              |
                          ↓              ↓
                        Tuple         Dictionary
"""