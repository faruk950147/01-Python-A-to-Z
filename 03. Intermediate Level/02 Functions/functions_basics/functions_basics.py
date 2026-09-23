# ================================================================================
#                           PYTHON FUNCTIONS
# ================================================================================


# ================================================================================
# 1. What is a Function?
# ================================================================================

"""
A function is a block of reusable code that performs a specific task.

Instead of writing the same code multiple times, we can define it once
inside a function and call it whenever we need it.

Example:

def greet():
    print("Hello")

greet()
"""


# ================================================================================
# 2. Identifiers in Python
# ================================================================================

"""
Identifiers used in and around functions can be categorized as:

1. Local Identifier
2. Nonlocal Identifier
3. Global Identifier
4. Built-in Identifier
"""


# ================================================================================
# 3. Basic Function Syntax
# ================================================================================

"""
Syntax:

def function_name(parameters):
    # function body
    return value


Explanation:

1. def
   - 'def' is a Python keyword.
   - It is used to define a function.

2. function_name
   - The name of the function.

3. parameters
   - Variables that receive values when the function is called.

4. function body
   - The block of code that executes when the function is called.

5. return
   - Sends a value back from the function.
"""


# Example:

def add(a, b):
    return a + b


result = add(10, 20)

print(result)
# Output: 30


"""
Important:

Parameter:
    Variable written in the function definition.

Argument:
    Actual value passed when calling the function.

Example:

def add(a, b):
        ↑  ↑
    parameters


add(10, 20)
    ↑   ↑
  arguments
"""


# ================================================================================
# 4. Basic Concepts / Types Related to Functions
# ================================================================================

"""
Important function concepts:

1. First-Class Function
2. Pure Function
3. Impure Function
4. Higher-Order Function
5. Lambda Function
6. Generator Function
7. Decorator Function
"""


# ================================================================================
# 5. First-Class Function
# ================================================================================

"""
Python functions are First-Class Objects.

This means functions can be treated like other objects/data.

A function can:

1. Be stored in a variable
2. Be passed as an argument
3. Be returned from another function
4. Be stored inside data structures


Main idea:

First-Class Function
        ↓
Functions can be treated like data/objects
"""


# ============================= First-Class Function Uses =========================

"""
First-Class Functions are useful for:

- Callbacks
- Decorators
- Event handling
- Functional programming
- Higher-order functions
"""


# ---------------- 5.1 Function stored in a variable -----------------------------

def square(x):
    return x * x


f = square

print(f(5))
# Output: 25


"""
Here:

square
    ↓
Function object

f = square
    ↓
f becomes another reference to the same function

f(5)
    ↓
square(5)
    ↓
25
"""


# ---------------- 5.2 Function passed as an argument ----------------------------

def greet(name):
    return f"Hello, {name}!"


def call_func(func, value):
    return func(value)


print(call_func(greet, "Ahmed"))
# Output: Hello, Ahmed!


"""
Flow:

greet
    ↓
passed as an argument
    ↓
call_func(greet, "Ahmed")
    ↓
func(value)
    ↓
greet("Ahmed")
    ↓
Hello, Ahmed!
"""


# ---------------- 5.3 Function returned from another function -------------------

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
    → returns the function itself


return inner_func()
    → calls the function and returns its result
"""


# ---------------- 5.4 Function stored in a data structure -----------------------

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
Here:

operations["add"]
    → returns the add function

operations["add"](10, 5)
    → calls the add function
"""


# ================================================================================
# 6. Pure Function
# ================================================================================

"""
A Pure Function is a function that:

1. Always produces the same output for the same input.
2. Does not cause side effects.

In simple words:

Same Input
    ↓
Same Output

And:

No External Side Effect
"""


# ============================= Example 1: Pure Function ==========================

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

Therefore, add() is a pure function.
"""


# ============================= Example 2: Pure Function ==========================

def square(x):
    return x * x


print(square(4))
# Output: 16

print(square(4))
# Output: 16


"""
Same input:
    4

Same output:
    16

Therefore, square() is a pure function.
"""


# ================================================================================
# 7. Side Effects
# ================================================================================

"""
A Side Effect occurs when a function changes or interacts with something
outside its local computation.

Examples:

- Modifying a global variable
- Modifying external mutable data
- Writing to a file
- Updating a database
- Printing to the console
- Performing network operations
"""


# ============================= Impure Function Example ===========================

result = 0


def add_with_side_effect(a, b):
    global result

    result = a + b      # modifies global variable
    print(result)       # performs I/O

    return result


add_with_side_effect(2, 3)
# Output: 5

print(result)
# Output: 5


"""
The function changes the external/global variable 'result'.

Therefore, it has side effects and is not a pure function.
"""


# ================================================================================
# 8. Impure Function
# ================================================================================

"""
An Impure Function may:

- Change global variables
- Modify external state
- Perform I/O operations
- Depend on external state
- Produce different results for the same input
"""


# ============================= Example: Global State ============================

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
The result depends on the external variable 'total'.

Therefore, add_to_total() is an impure function.
"""


# ============================= Example: Random ================================

import random


def get_random_number():
    return random.randint(1, 10)


print(get_random_number())
print(get_random_number())


"""
The function can produce different results even without changing
the input because it depends on external/random state.

Therefore, it is considered impure.
"""


# ================================================================================
# 9. Pure Function vs Impure Function
# ================================================================================

"""
Pure Function:

- Same input → Same output
- No side effects
- Does not modify external state
- Easier to test
- Easier to debug
- Easier to reason about


Impure Function:

- May produce different results
- May depend on external state
- May modify external state
- May perform I/O
- Can be harder to test and debug
"""


# Quick Comparison:

"""
+-------------------+-----------------------------------------------+
| Pure Function     | Impure Function                              |
+-------------------+-----------------------------------------------+
| Same input        | May produce different output                 |
| → same output     | depending on external state                  |
+-------------------+-----------------------------------------------+
| No side effects   | May have side effects                        |
+-------------------+-----------------------------------------------+
| Does not modify   | May modify global/external state              |
| external state    |                                               |
+-------------------+-----------------------------------------------+
| Easier to test    | Can be harder to test                        |
+-------------------+-----------------------------------------------+
"""


# ================================================================================
# 10. Pure Function Optimization
# ================================================================================

"""
Pure functions are predictable.

Because the same input always produces the same output,
their results can be cached.

One common technique is:

Memoization

Memoization means storing previously calculated results
and reusing them when the same input appears again.
"""


# ============================= Fibonacci with Memoization ========================

cache = {}


def fib(n):

    if n in cache:
        return cache[n]

    if n <= 1:
        cache[n] = n

    else:
        cache[n] = fib(n - 1) + fib(n - 2)

    return cache[n]


print(fib(10))
# Output: 55


"""
Flow:

fib(10)
    ↓
calculate result
    ↓
store result in cache
    ↓
next time same value is needed
    ↓
return result from cache


Important:

Memoization works especially well when the function's result depends
only on its inputs and the function does not depend on changing
external state.
"""


# ================================================================================
# 11. Higher-Order Function
# ================================================================================

"""
A Higher-Order Function is a function that:

1. Takes another function as an argument
       OR

2. Returns another function as a result

A function can do either one or both.
"""


# ================================================================================
# 12. Function as an Argument
# ================================================================================

def apply(func, value):
    return func(value)


print(apply(lambda x: x * 2, 5))
# Output: 10


"""
Flow:

lambda x: x * 2
        ↓
passed to apply()
        ↓
func(value)
        ↓
5 * 2
        ↓
10
"""


# ============================= Another Example ================================

def apply(callback, value1, value2):
    return callback(value1, value2)


def add(x, y):
    return x + y


print(apply(add, 2, 3))
# Output: 5


"""
Flow:

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


# ================================================================================
# 13. Callback Function with *args
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
# 14. Function as a Return Value
# ================================================================================

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
# 15. First-Class Function vs Higher-Order Function
# ================================================================================

"""
These two concepts are related but NOT the same.

First-Class Function:
    Describes what functions CAN DO.

    Example:

    f = square


Higher-Order Function:
    Describes a function that USES another function.

    Example:

    apply(square, 5)


Therefore:

First-Class Function
        ↓
Functions can be treated as objects/data


Higher-Order Function
        ↓
A function accepts another function
OR
returns another function
"""


# ================================================================================
# 16. Practical Uses of Pure Functions
# ================================================================================

"""
Pure functions are useful in:

1. Data Processing
   - map()
   - filter()
   - reduce()

2. Business Logic
   - Discount calculation
   - Tax calculation
   - Price calculation

3. Algorithms
   - Searching
   - Sorting
   - Recursion

4. Functional Programming

5. Memoization / Caching
"""


# ============================= Example: map() ====================================

nums = [1, 2, 3, 4, 5]


def square(x):
    return x * x


squared = list(map(square, nums))

print(squared)
# Output: [1, 4, 9, 16, 25]


"""
map() applies the square() function to every element.

nums:
    [1, 2, 3, 4, 5]

square():
    1 → 1
    2 → 4
    3 → 9
    4 → 16
    5 → 25

Result:
    [1, 4, 9, 16, 25]
"""


# ================================================================================
# 17. Final Summary
# ================================================================================

"""
1. Function
-----------
A reusable block of code that performs a specific task.


2. First-Class Function
-----------------------
Functions can be treated like data.

Functions can be:

- Stored in variables
- Passed as arguments
- Returned from functions
- Stored in data structures


3. Pure Function
----------------
Same input → Same output

And:

No side effects


4. Impure Function
------------------
May:

- Change external state
- Modify global variables
- Perform I/O
- Depend on external state


5. Higher-Order Function
------------------------
A function that:

- Accepts another function
  OR
- Returns another function


6. Callback
-----------
A function passed to another function to be called later
or during its execution.


7. Memoization
--------------
Caching previously calculated results to avoid repeated computation.
"""


# ================================================================================
# 18. Complete Concept Relationship
# ================================================================================

"""
                           PYTHON FUNCTIONS
                                  |
              +-------------------+-------------------+
              |                   |                   |
              ↓                   ↓                   ↓
       First-Class            Pure / Impure      Higher-Order
        Function               Function            Function
              |                   |                   |
              ↓                   ↓                   ↓
       Function treated     Pure → predictable   Accepts function
       like data            Impure → state       OR
                                                   returns function
              |
              |
      +-------+--------+
      |       |        |
      ↓       ↓        ↓
   Variable  Argument  Data Structure
      |
      ↓
   Function


Important relationship:

First-Class Function
        ↓
Functions can be treated as objects


Higher-Order Function
        ↓
Uses functions as arguments or return values


Pure Function
        ↓
Same input → Same output
No side effects


Impure Function
        ↓
May depend on or modify external state
"""