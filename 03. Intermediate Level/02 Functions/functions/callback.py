# ================================================================================
#                         CALLBACK FUNCTION
# ================================================================================

"""
============================= What is Callback Function ===========================

A Callback Function is a function that is passed as an argument
to another function and is called/executed by that function.

In simple words:

A callback function is a function that is passed to another function
so that the receiving function can execute it.


Example:

def simple(a, b, callback):
    return callback(a, b)


def add(a, b):
    return a + b


simple(10, 20, add)


Here:

simple()
    -> Higher-Order Function

add()
    -> Callback Function
"""


# ================================================================================
#                    HIGHER-ORDER FUNCTION
# ================================================================================

"""
============================= What is Higher-Order Function =======================

A Higher-Order Function is a function that:

1. Takes another function as an argument
   OR
2. Returns another function as a result.


In simple words:

A function that works with other functions
is called a Higher-Order Function.
"""


# ================================================================================
#              CALLBACK FUNCTION vs HIGHER-ORDER FUNCTION
# ================================================================================

"""
+----------------------+---------------------------------------------+
| Callback Function    | Higher-Order Function                       |
+----------------------+---------------------------------------------+
| The function that is | The function that takes another function   |
| passed as an argument| as an argument or returns a function       |
+----------------------+---------------------------------------------+
| It is the passed     | It is the receiving or returning function  |
| function             |                                             |
+----------------------+---------------------------------------------+
| It is usually called | It receives/calls the callback or returns   |
| inside another       | another function                            |
| function             |                                             |
+----------------------+---------------------------------------------+
| Example: add()       | Example: simple()                           |
+----------------------+---------------------------------------------+


Important:

Callback Function
    -> Describes the ROLE of a function.

Higher-Order Function
    -> Describes the BEHAVIOR of a function.
"""


# ================================================================================
# 1. Basic Callback Function Example
# ================================================================================

def simple(a, b, callback):

    return callback(a, b)


def add(a, b):

    return a + b


def sub(a, b):

    return a - b


def mul(a, b):

    return a * b


def div(a, b):

    return a / b


print(simple(10, 20, add))
# Output: 30

print(simple(10, 20, sub))
# Output: -10

print(simple(10, 20, mul))
# Output: 200

print(simple(10, 20, div))
# Output: 0.5


"""
Flow:

simple(10, 20, add)
        |
        v
callback = add
        |
        v
callback(10, 20)
        |
        v
add(10, 20)
        |
        v
30


Here:

simple()
    -> Higher-Order Function

add()
    -> Callback Function
"""


# ================================================================================
# 2. Function as an Argument
# ================================================================================

"""
A function can be passed to another function
just like other Python objects.
"""


def do_task(task, callback):

    print("Doing task:", task)

    callback()


def done():

    print("Task finished!")


def notify():

    print("Sending notification...")


do_task("Learning Python", done)

"""
Output:

Doing task: Learning Python
Task finished!
"""


do_task("Completing Homework", notify)

"""
Output:

Doing task: Completing Homework
Sending notification...
"""


"""
Here:

do_task()
    -> Higher-Order Function

done()
    -> Callback Function

notify()
    -> Callback Function
"""


# ================================================================================
# 3. Callback Function with Arguments
# ================================================================================

def do_task(task, callback):

    print("Doing task:", task)

    message = "Completed " + task + " successfully!"

    callback(message)


def done(message):

    print("Task finished!", message)


def notify(message):

    print("Notification:", message)


do_task("Learning Python", done)

"""
Output:

Doing task: Learning Python
Task finished! Completed Learning Python successfully!
"""


do_task("Completing Homework", notify)

"""
Output:

Doing task: Completing Homework
Notification: Completed Completing Homework successfully!
"""


"""
Flow:

do_task("Learning Python", done)
        |
        v
callback = done
        |
        v
message is created
        |
        v
callback(message)
        |
        v
done(message)
"""


# ================================================================================
# 4. Function Returning Another Function
# ================================================================================

"""
A function can also return another function.

A function that returns another function
is a Higher-Order Function.
"""


def create_multiplier(x):

    def multiplier(y):

        return x * y

    return multiplier


multiply_by_2 = create_multiplier(2)

print(multiply_by_2(5))

# Output:
# 10


"""
Flow:

create_multiplier(2)
        |
        v
x = 2
        |
        v
returns multiplier function
        |
        v
multiply_by_2 = multiplier
        |
        v
multiply_by_2(5)
        |
        v
2 * 5
        |
        v
10


Important:

Here multiplier() is NOT a callback.

It is a function returned by create_multiplier().

create_multiplier()
    -> Higher-Order Function
"""


# ================================================================================
# 5. Built-in Higher-Order Functions
# ================================================================================

"""
Common Python functions that work with functions/callables:

1. map()
2. filter()
3. reduce()
4. sorted()
5. any()
6. all()
"""

# ================================================================================
# 6. Important Difference
# ================================================================================

"""
Callback Function
-----------------

A callback is the function being passed to another function.

Example:

my_filter(numbers, is_even)

is_even
    -> Callback Function


Higher-Order Function
---------------------

A Higher-Order Function is the function
that receives or returns another function.

Example:

my_filter(numbers, is_even)

my_filter
    -> Higher-Order Function


Therefore:

my_filter()
    -> Higher-Order Function

is_even()
    -> Callback Function
"""


# ================================================================================
# 7. Callback is Context-Dependent
# ================================================================================

"""
A function is not permanently a "callback function".

It becomes a callback when it is passed to another function
for a particular operation.


Example:

def add(a, b):

    return a + b


Normal function call:

add(2, 3)

Here:

add()
    -> Normal Function Call


Passing it to another function:

simple(2, 3, add)

Here:

add()
    -> Callback Function


Therefore:

"Callback" describes the role of a function
in a particular context.
"""


# ================================================================================
# 8. Final Summary
# ================================================================================

"""
FUNCTION
--------
A reusable block of code.


FIRST-CLASS FUNCTION
--------------------

Functions can be:

- Stored in variables
- Passed as arguments
- Returned from functions
- Stored in data structures


HIGHER-ORDER FUNCTION
---------------------

A function that:

- Accepts another function
  OR
- Returns another function


CALLBACK FUNCTION
-----------------

A function that is passed to another function
and called/executed by that function.


PREDICATE FUNCTION
------------------

A function that returns:

True
OR
False


map()
-----

Transforms each element.


filter()
--------

Selects elements based on a condition.


reduce()
--------

Combines multiple values into one result.


sorted()
--------

Sorts values and can use a key function.


any()
-----

Returns True if at least one element is truthy.


all()
-----

Returns True only if all elements are truthy.
"""


# ================================================================================
# 9. Complete Relationship
# ================================================================================

"""
                         FUNCTION
                            |
                            v
                   FIRST-CLASS FUNCTION
                            |
                            v
              Function can be treated
                     like an object
                            |
                            v
                 HIGHER-ORDER FUNCTION
                            |
              +-------------+-------------+
              |                           |
              v                           v
       Function as Argument       Function as Return
              |
              v
          CALLBACK
              |
              v
       PREDICATE FUNCTION
       (when it returns
        True / False)


Built-in examples:

map()
filter()
reduce()
sorted()
any()
all()

These functions work with functions/callables
in different ways.
"""


# ================================================================================
# 10. One-Line Memory Trick
# ================================================================================

"""
First-Class Function
    ->
Function can be treated like data/object.


Higher-Order Function
    ->
Function takes or returns another function.


Callback Function
    ->
Function passed to another function.


Predicate Function
    ->
Function that returns True or False.


map()
    ->
Transform


filter()
    ->
Select


reduce()
    ->
Combine
"""