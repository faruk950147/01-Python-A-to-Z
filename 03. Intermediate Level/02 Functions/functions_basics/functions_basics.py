# ============================= What is a Function? ==============================

"""
A function is a block of reusable code that performs a specific task.

Instead of writing the same code multiple times, we can define it once
inside a function and call it whenever we need it.

Example:

def greet():
    print("Hello")

greet()
"""


# ============================= Identifiers in Python =============================

"""
In Python, identifiers used inside functions can be categorized into:

1. Local Identifier
2. Nonlocal Identifier
3. Global Identifier
4. Built-in Identifier
"""


# ============================= Basic Types of Functions ==========================

"""
Some important concepts/types related to functions:

1. First-Class Function
2. Pure Function
3. Higher-Order Function
4. Lambda Function
5. Generator Function
6. Decorator Function
"""


# ============================= Syntax of a Function ==============================

"""
def function_name(parameters):
    # function body
    return value


Explanation:

1. def
   - 'def' is a keyword in Python.
   - It is used to define a function.

2. function_name
   - The name of the function.

3. parameters
   - Variables that receive values when the function is called.

4. function body
   - The block of code that executes when the function is called.

5. return
   - Used to send a value back from the function.
"""


# Example:

def add(a, b):
    return a + b


result = add(10, 20)

print(result)
# Output: 30


# ================================================================================
# 1. First-Class Function
# ================================================================================

"""
Python functions are First-Class Objects.

This means functions can be treated like other objects/data.

A function can:

1. Be stored in a variable
2. Be passed as an argument
3. Be returned from another function
4. Be stored inside data structures
"""


# ---------------- 1. Function can be stored in a variable -----------------------

def square(x):
    return x * x


f = square

print(f(5))
# Output: 25


# Here:
#
# square -> function object
# f      -> another reference to the same function
#
# f(5) is equivalent to square(5)


# ---------------- 2. Function can be passed as an argument ---------------------

def greet(name):
    return f"Hello, {name}!"


def call_func(func, value):
    return func(value)


print(call_func(greet, "Ahmed"))
# Output: Hello, Ahmed!


"""
Here:

greet
    ↓
passed as an argument
    ↓
call_func(greet, "Ahmed")
    ↓
func(value)
    ↓
greet("Ahmed")
"""


# ---------------- 3. Function can be returned from another function -------------

def outer_func():

    def inner_func():
        return "I'm inside the outer function!"

    return inner_func


result = outer_func()

print(result())
# Output: I'm inside the outer function!


"""
Important:

return inner_func
    -> returns the function itself

return inner_func()
    -> calls the function and returns its result
"""


# ---------------- 4. Function can be stored in data structures ------------------

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


operations = {
    "add": add,
    "sub": sub,
    "mul": mul
}


print(operations["add"](10, 5))
# Output: 15

print(operations["sub"](10, 5))
# Output: 5

print(operations["mul"](10, 5))
# Output: 50


"""
Here, functions are stored as values inside a dictionary.

operations["add"]
    -> returns the add function

operations["add"](10, 5)
    -> calls the add function
"""


# ================================================================================
# 2. Pure Function
# ================================================================================

"""
A Pure Function has two important properties:

1. Same input always produces the same output.
2. It does not cause side effects.

Example:

add(2, 3) -> always returns 5
"""


def add(a, b):
    return a + b


print(add(2, 3))
# Output: 5

print(add(2, 3))
# Output: 5


"""
Same input:
    2, 3

Same output:
    5

Therefore, this is a pure function.
"""


# ================================================================================
# Impure Function
# ================================================================================

"""
An Impure Function may:

- Change global variables
- Modify external state
- Perform I/O operations
- Produce different results for the same input
"""

total = 0


def add_to_total(x):
    global total
    total += x
    return total


print(add_to_total(10))
# Output: 10

print(add_to_total(20))
# Output: 30


"""
The function changes the external/global variable 'total'.

Therefore, it is an impure function.
"""


# ================================================================================
# 3. Higher-Order Function
# ================================================================================

"""
A Higher-Order Function is a function that:

1. Takes another function as an argument
       OR
2. Returns another function as a result

A function can do either one or both.
"""


# ---------------- 1. Function as an Argument ------------------------------------

def apply(func, value):
    return func(value)


print(apply(lambda x: x * 2, 5))
# Output: 10


"""
Here:

lambda x: x * 2
    ↓
is passed to apply()
    ↓
func(value)
    ↓
5 * 2
    ↓
10
"""


# Another example:

def apply(callback, value1, value2):
    return callback(value1, value2)


def add(x, y):
    return x + y


print(apply(add, 2, 3))
# Output: 5


"""
Here:

add
    ↓
passed as an argument
    ↓
apply(add, 2, 3)
    ↓
callback(2, 3)
    ↓
add(2, 3)
    ↓
5
"""


# ---------------- Using *args with callback -------------------------------------

def display(callback, *args):
    callback(*args)


def print_sum(x, y):
    print(x + y)


def print_product(x, y):
    print(x * y)


display(print_sum, 2, 3)
# Output: 5

display(print_product, 2, 3)
# Output: 6


"""
Here:

display(print_sum, 2, 3)
    -> callback = print_sum
    -> args = (2, 3)

callback(*args)
    -> print_sum(2, 3)
    -> 5
"""


# ---------------- 2. Function as a Return Value -------------------------------

def make_multiplier(n):

    def multiplier(x):
        return x * n

    return multiplier


times3 = make_multiplier(3)

print(times3(10))
# Output: 30


"""
Step-by-step:

make_multiplier(3)
        ↓
n = 3
        ↓
returns multiplier function
        ↓
times3 = multiplier
        ↓
times3(10)
        ↓
10 * 3
        ↓
30
"""


# ================================================================================
# Summary
# ================================================================================

"""
1. First-Class Function
-----------------------
Functions can be treated like data.

You can:
- Store functions in variables
- Pass functions as arguments
- Return functions from functions
- Store functions in data structures


2. Pure Function
----------------
Same input → Same output

And:

No side effects


3. Impure Function
------------------
May change external/global state.

Example:
A function that modifies a global variable.


4. Higher-Order Function
------------------------
A function that:

- Accepts another function as an argument
  OR
- Returns another function


Relationship:

First-Class Function
        ↓
Functions can be treated like data

Higher-Order Function
        ↓
Uses functions as arguments or return values

Pure Function
        ↓
Same input → Same output
No side effects
"""


# ============================= Quick Comparison ================================

"""
+----------------------+---------------------------------------------+
| Concept              | Main Idea                                   |
+----------------------+---------------------------------------------+
| First-Class Function | Function can be treated like data          |
| Pure Function        | Same input → same output, no side effects  |
| Impure Function      | Can change external/global state           |
| Higher-Order Function| Accepts or returns another function        |
+----------------------+---------------------------------------------+
"""


# ============================= Important Note ===================================

"""
First-Class Function and Higher-Order Function are NOT the same thing.

First-Class Function:
    Describes what functions CAN DO.

    Example:
        f = square

Higher-Order Function:
    Describes a function that USES other functions.

    Example:
        apply(square, 5)

So:

First-Class Function
        ↓
Functions are treated as objects/data

Higher-Order Function
        ↓
Functions are passed around or returned
"""