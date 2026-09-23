# ================================================================================
#                    HIGHER-ORDER FUNCTION & CALLBACK FUNCTION
# ================================================================================


"""
===============================================================================
1. What is a Higher-Order Function?
===============================================================================

A Higher-Order Function (HOF) is a function that:

1. Takes one or more functions as arguments
   OR
2. Returns another function as a result

In simple words:

    A function that works with other functions
    is called a Higher-Order Function.


Example:

def calculate(func, a, b):
    return func(a, b)

Here:

calculate()
    ↓
takes another function
    ↓
therefore calculate() is a Higher-Order Function.
"""


# ================================================================================
# 2. What is a Callback Function?
# ================================================================================

"""
A Callback Function is a function that is passed as an argument
to another function and is called/executed inside that function.

In simple words:

একটি function-কে অন্য একটি function-এর argument হিসেবে পাঠানো হয়,
এবং receiving function-এর ভিতরে সেই function-কে call করা হয়।

Example:

def calculate(func, a, b):
    return func(a, b)

def add(a, b):
    return a + b

calculate(add, 10, 20)

Here:

calculate()
    ↓
Higher-Order Function

add()
    ↓
Callback Function


Important:

The same function can be:

- A callback when passed to another function
- A normal function when called directly

So "callback" describes the ROLE of a function in a particular context.
"""


# ================================================================================
# 3. Callback Function vs Higher-Order Function
# ================================================================================

"""
+----------------------+-----------------------------------------------+
| Callback Function   | Higher-Order Function                       |
+----------------------+-----------------------------------------------+
| Function passed     | Function that accepts or returns a function |
| as an argument      |                                               |
+----------------------+-----------------------------------------------+
| It is used/called   | It receives or returns another function      |
| by another function  |                                               |
+----------------------+-----------------------------------------------+
| Example: add()      | Example: calculate()                         |
+----------------------+-----------------------------------------------+


Example:

def calculate(func, a, b):
    return func(a, b)

def add(a, b):
    return a + b

calculate(add, 10, 20)


calculate()
    ↓
Higher-Order Function

add()
    ↓
Callback Function
"""


# ================================================================================
# 4. Function as an Argument
# ================================================================================

def higher_order1(func, a, b):
    return func(a, b)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


print(higher_order1(add, 10, 20))
# Output: 30

print(higher_order1(mul, 5, 6))
# Output: 30


"""
Here:

higher_order1()
    ↓
takes a function as an argument
    ↓
Therefore it is a Higher-Order Function.


add()
    ↓
passed into higher_order1()
    ↓
Therefore add() acts as a Callback Function.


mul()
    ↓
passed into higher_order1()
    ↓
Therefore mul() acts as a Callback Function.
"""


# ================================================================================
# 5. Function Returning Another Function
# ================================================================================

"""
A function can return another function.

A function that returns another function is also a
Higher-Order Function.
"""


def higher_order2(op):

    def add(x, y):
        return x + y

    def mul(x, y):
        return x * y

    if op == "add":
        return add

    return mul


f1 = higher_order2("add")
f2 = higher_order2("mul")


print(f1(10, 20))
# Output: 30

print(f2(5, 6))
# Output: 30


"""
Important:

return add
    → returns the function itself


return add()
    → calls the function and returns its result


Flow:

higher_order2("add")
        ↓
returns add function
        ↓
f1 = add
        ↓
f1(10, 20)
        ↓
30
"""


# ================================================================================
# 6. Function as an Argument with No Return Value
# ================================================================================

def higher_order3(func):

    print("Inside Higher-Order Function")

    func()


def say_hello():
    print("Hello!")


higher_order3(say_hello)


"""
Output:

Inside Higher-Order Function
Hello!


Here:

higher_order3()
    → Higher-Order Function

say_hello()
    → Callback Function
"""


# ================================================================================
# 7. Practical Calculation Example
# ================================================================================

def calculate(a, b, func):
    return func(a, b)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print(calculate(10, 20, add))
# Output: 30

print(calculate(20, 10, sub))
# Output: 10

print(calculate(10, 5, mul))
# Output: 50

print(calculate(20, 5, div))
# Output: 4.0


"""
Here:

calculate()
    ↓
Higher-Order Function


add()
sub()
mul()
div()
    ↓
Callback Functions


calculate(10, 20, add)
    ↓
add(10, 20)
    ↓
30
"""


# ================================================================================
# 8. Callback with a Task
# ================================================================================

def do_task(task, callback):

    print("Doing task:", task)

    callback()


def done():
    print("Task finished!")


do_task("Learning Python", done)


"""
Output:

Doing task: Learning Python
Task finished!


Here:

do_task()
    → Higher-Order Function

done()
    → Callback Function
"""


# ================================================================================
# 9. Callback Function with *args
# ================================================================================

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

callback = print_sum
args = (2, 3)

callback(*args)
    ↓
print_sum(2, 3)
    ↓
5
"""


# ================================================================================
# 10. Built-in Higher-Order Functions
# ================================================================================

"""
Python provides several functions that can work with other functions
or callable objects.

Common examples:

1. map()
2. filter()
3. sorted()
4. any()
5. all()
6. functools.reduce()
"""


# ----------------------------- map() --------------------------------------------

def square(x):
    return x * x


result = map(square, range(1, 6))

print(list(result))
# Output: [1, 4, 9, 16, 25]


"""
map():

map(function, iterable)

The function is applied to every item in the iterable.
"""


# ----------------------------- filter() -----------------------------------------

numbers = range(1, 6)

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(list(even_numbers))
# Output: [2, 4]


"""
filter():

filter(function, iterable)

Keeps only the elements for which the function returns True.
"""


# ----------------------------- reduce() -----------------------------------------

from functools import reduce


result = reduce(
    lambda x, y: x + y,
    range(1, 6)
)

print(result)
# Output: 15


"""
reduce():

reduce(function, iterable)

It repeatedly combines values into a single result.


1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
"""


# ----------------------------- sorted() -----------------------------------------

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print(sorted(numbers))
# Output:
# [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


"""
sorted() can also receive a key function.

Example:

words = ["Python", "C", "Java"]

sorted(words, key=len)

Here len is used as the key function.
"""


# ----------------------------- any() --------------------------------------------

print(any([False, False, True]))
# Output: True


"""
any() returns True if at least one item is truthy.
"""


# ----------------------------- all() --------------------------------------------

print(all([True, True, True]))
# Output: True


"""
all() returns True only if every item is truthy.
"""


# ================================================================================
# 11. Custom Higher-Order Function
# ================================================================================

def higher_order_function(func):
    return func()


def say_hello():
    print("Hello!")


result = higher_order_function(say_hello)

print(result)
# Output:
# Hello!
# None


"""
Why None?

say_hello() only prints "Hello!"
It does not return a value.

Therefore:

func()
    ↓
say_hello()
    ↓
prints "Hello!"
    ↓
returns None


So:

result = None
"""


# ================================================================================
# 12. Higher-Order Function + Lambda
# ================================================================================

result = higher_order_function(
    lambda: print("Hello!")
)

print(result)
# Output:
# Hello!
# None


"""
The lambda function is passed as an argument.

Therefore:

higher_order_function()
    → Higher-Order Function

lambda: print("Hello!")
    → Callback Function
"""


# ================================================================================
# 13. Higher-Order Function + Decorator
# ================================================================================

"""
Decorators are built using the idea of Higher-Order Functions.

A decorator:

1. Takes a function as an argument
2. Defines or creates another function
3. Returns the new function
"""


def decorator(func):

    def wrapper():

        print("Before function")

        func()

        print("After function")

    return wrapper


@decorator
def say_hello():
    print("Hello!")


say_hello()


"""
Output:

Before function
Hello!
After function


Flow:

say_hello
    ↓
decorator(say_hello)
    ↓
wrapper
    ↓
say_hello = wrapper
    ↓
say_hello()
"""


# ================================================================================
# 14. Decorator with *args and **kwargs
# ================================================================================

def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before function")

        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)

        result = func(*args, **kwargs)

        print("After function")

        return result

    return wrapper


@decorator
def say_hello(name, age):

    print("Hello", name, "you are", age, "years old.")


say_hello("Faruk", 25)


"""
Important:

The decorator receives the original function:

decorator(func)

The wrapper receives the actual arguments:

wrapper(*args, **kwargs)

Then:

func(*args, **kwargs)

calls the original function.
"""


# ================================================================================
# 15. Generic Calculate Function
# ================================================================================

def calculate(func, *args, **kwargs):

    return func(*args, **kwargs)


def add(*args):

    return sum(args)


def sub(*args):

    return args[0] - sum(args[1:])


def mul(*args):

    result = 1

    for value in args:
        result *= value

    return result


def div(*args):

    result = args[0]

    for value in args[1:]:
        result /= value

    return result


print(calculate(add, 10, 20, 30))
# Output: 60

print(calculate(sub, 100, 20, 10))
# Output: 70

print(calculate(mul, 2, 3, 4))
# Output: 24

print(calculate(div, 100, 2, 5))
# Output: 10.0


"""
calculate()
    ↓
Higher-Order Function


add()
sub()
mul()
div()
    ↓
Callback Functions


calculate(add, 10, 20, 30)
    ↓
add(10, 20, 30)
    ↓
60
"""


# ================================================================================
# 16. Function as Return Value
# ================================================================================

def display():

    def add(x, y):
        return x + y

    return add


add_function = display()

print(add_function(2, 3))
# Output: 5


"""
Here:

display()
    ↓
returns add function
    ↓
add_function = add
    ↓
add_function(2, 3)
    ↓
5


display() is a Higher-Order Function
because it returns another function.
"""


# ================================================================================
# 17. Another Higher-Order Function Example
# ================================================================================

def display(func, nums):

    return func(nums)


def add_numbers(nums):

    return sum(nums)


result = display(add_numbers, [2, 3, 4])

print(result)
# Output: 9


"""
Here:

display()
    ↓
Higher-Order Function


add_numbers()
    ↓
Callback Function


display(add_numbers, [2, 3, 4])
    ↓
add_numbers([2, 3, 4])
    ↓
9
"""


# ================================================================================
# 18. Important Correction
# ================================================================================

"""
Avoid doing this:

add = display(add, [2, 3, 4])


Why?

Because the name 'add' originally refers to the function:

def add(nums):
    return sum(nums)


But after:

add = display(add, [2, 3, 4])

the name 'add' now refers to the RETURNED VALUE (9).

So:

add
    ↓
9

It is no longer referring to the function.

Better:

result = display(add, [2, 3, 4])

print(result)
# 9
"""


# ================================================================================
# 19. Practical Uses of Higher-Order Functions
# ================================================================================

"""
Higher-Order Functions are commonly used for:

1. Callbacks
2. Decorators
3. Functional Programming
4. Data Processing
5. Event Handling
6. Reusable Logic
7. Custom Sorting
8. map()
9. filter()
10. reduce()
"""


# ================================================================================
# 20. Complete Concept Relationship
# ================================================================================

"""
                         FUNCTIONS
                             |
                             ↓
                    First-Class Function
                             |
                             ↓
                Functions can be treated
                     like objects/data
                             |
              +--------------+--------------+
              |                             |
              ↓                             ↓
     Function as Argument          Function as Return
              |                             |
              ↓                             ↓
          Callback                  Higher-Order
              |                       Function
              +-------------+-------------+
                            |
                            ↓
                    Higher-Order Function
                            |
              +-------------+-------------+
              |             |             |
              ↓             ↓             ↓
            map()        filter()      reduce()
              |
              ↓
          Decorators
"""


# ================================================================================
# 21. Final Summary
# ================================================================================

"""
Function
--------
Reusable block of code.


First-Class Function
--------------------
Functions can be:

- Stored in variables
- Passed as arguments
- Returned from functions
- Stored in data structures


Higher-Order Function
---------------------
A function that:

- Accepts another function
  OR
- Returns another function


Callback Function
-----------------
A function passed as an argument to another function
and called by that function.


Decorator
---------
A special use of Higher-Order Functions where a function
is wrapped to add or modify behavior.


Lambda
------
A small anonymous function that can also be used as
a callback.


Built-in Higher-Order Functions
-------------------------------
- map()
- filter()
- reduce()
- sorted()
- any()
- all()


Core Relationship
-----------------

First-Class Function
        ↓
Functions can be treated as objects

Higher-Order Function
        ↓
Accepts or returns functions

Callback Function
        ↓
A function passed to another function

Decorator
        ↓
Uses Higher-Order Function concept
to wrap another function
"""