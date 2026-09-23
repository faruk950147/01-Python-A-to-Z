"""
====================================================================
PYTHON CLOSURE — ULTIMATE DETAILED NOTES & GUIDE
====================================================================

1. What is a Closure?
--------------------------------------------------------------------
In Python, a Closure is a function object that remembers and can access 
variables from its enclosing lexical scope, even after the outer function 
has finished execution. 

Closure = Function + Captured Enclosing Environment (Remembered Variables)

A closure typically forms when:
- Condition 1: There is a nested function (an inner function defined inside an outer function).
- Condition 2: The inner function uses a variable from the outer function's scope.
- Condition 3: The outer function returns the inner function, retaining access to the outer variable.


2. Structure & Basic Example
--------------------------------------------------------------------
"""


def outer_function(message):

    def inner_function():
        print(message)

    return inner_function


my_func = outer_function("Hello, Closure!")
my_func()  # Output: Hello, Closure!


"""
--------------------------------------------------------------------
3. Under the Hood: __closure__ and cell_contents
--------------------------------------------------------------------
When a nested function references variables from its enclosing scope, 
Python creates a 'cell' object to keep those variable values alive.
You can inspect this using the __closure__ attribute.
"""

add_10 = outer_function("Testing Closure")
print(f"Closure Info: {add_10.__closure__}")
print(f"Captured Value: {add_10.__closure__[0].cell_contents}")


"""
--------------------------------------------------------------------
4. The Role of 'nonlocal'
--------------------------------------------------------------------
If you want to modify an outer variable (not just read it), 
use the 'nonlocal' keyword.
"""


# Example: Counter Using Closure
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


add = counter()
print(add())  # 1
print(add())  # 2
print(add())  # 3


"""
--------------------------------------------------------------------
5. Practical Use Cases of Closures
--------------------------------------------------------------------
- Function Factories: Dynamically create functions with preset parameters.
- Memoization / Caching: Caching results to optimize performance.
- Data Encapsulation / Hiding: Protecting variables from direct external access.
"""


# Use Case 1: Function Factory
def power_factory(n):

    def power(x):
        return x**n

    return power


square = power_factory(2)
cube = power_factory(3)
print(square(5))  # Output: 25
print(cube(2))  # Output: 8


# Use Case 2: Custom Memoization / Cache Closure (LRU Cache concept)
def memoize(func):
    cache = {}

    def wrapper(x):
        if x not in cache:
            print(f"Calculating result for {x}...")
            cache[x] = func(x)
        else:
            print(f"Fetching from cache for {x}...")
        return cache[x]

    return wrapper


@memoize
def slow_square(x):
    return x * x


print(slow_square(5))  # Calculates and caches
print(slow_square(5))  # Fetches from cache


# Use Case 3: Login Tracker
def login_tracker():
    count = 0

    def login(username):
        nonlocal count
        count += 1
        print(f"{username} logged in {count} times")

    return login


tracker = login_tracker()
tracker("Faruk")  # Faruk logged in 1 times
tracker("Faruk")  # Faruk logged in 2 times


"""
--------------------------------------------------------------------
6. Advantages and Limitations of Closures
--------------------------------------------------------------------
Advantages:
- Data Hiding: Protects variables from being accessed directly.
- State Preservation: Keeps track of state without using global variables.
- Functional Programming: Ideal for decorators and factories.

Limitations:
- Debugging Complexity: Harder to track internal variable states.
- Readability: Nested scopes can sometimes confuse beginners.


--------------------------------------------------------------------
7. Closure vs. Class vs. Bound Method
--------------------------------------------------------------------
"""


# Class-Based Equivalent (OOP Approach - Not a Closure)
class Calculator:

    def __init__(self, n):
        self.n = n

    def add(self, x):
        return x + self.n


calc_obj = Calculator(5)
print(calc_obj.add(10))  # Output: 15 (Uses object attribute self.n)

# Bound Method Check
calc_method = Calculator(5).add
print(calc_method(10))  # Output: 15
print(
    calc_method.__closure__
)  # Output: None (Bound methods are NOT closures)


"""
====================================================================
SUMMARY TABLE
====================================================================
Concept           | Description
------------------|----------------------------------------------------------
Definition        | Function that remembers variables from its enclosing scope.
Formed When       | Nested function refers to variables from outer function.
Memory Behavior   | Keeps outer variables alive in a cell object (__closure__).
Use Cases         | Decorators, Function factories, Data hiding, Memoization.
Keyword           | nonlocal (to modify outer variables).
====================================================================
"""