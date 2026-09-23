# ========================================================================
#                         PYTHON DECORATOR
# ========================================================================

"""
A Python Decorator is a feature that allows you to modify or extend
the behavior of a function or method without changing its original code.

Simply:

    Add extra functionality to an existing function.

Example idea:

    Original Function
           ↓
       Decorator
           ↓
     Wrapper Function
           ↓
    Extra Behavior
           +
    Original Function
"""


# ========================================================================
# 1. FIRST-CLASS FUNCTIONS
# ========================================================================

"""
Decorators are based on Python's first-class function concept.

In Python, functions are objects.

Therefore, a function can be:

1. Assigned to a variable.
2. Passed as an argument.
3. Returned from another function.
4. Stored in a data structure.
"""


# Function

def say_hello():
    print("Hello")


# 1. Assign function to a variable

my_function = say_hello

my_function()


# 2. Pass function as an argument

def execute(func):
    func()


execute(say_hello)


# 3. Return a function from another function

def create_function():

    def message():
        print("Hello from returned function")

    return message


new_function = create_function()

new_function()


# ========================================================================
# 2. WHAT IS A DECORATOR?
# ========================================================================

"""
A decorator is a callable that takes another callable and returns
a callable with modified or extended behavior.

In most common cases:

    Function
       ↓
    Decorator
       ↓
    Wrapper
       ↓
    Modified Function
"""


# ========================================================================
# 3. BASIC DECORATOR
# ========================================================================

def my_decorator(func):

    def wrapper():

        print("Before function")

        func()

        print("After function")

    return wrapper


@my_decorator
def say_hello():

    print("Hello!")


say_hello()


# Output:
#
# Before function
# Hello!
# After function


"""
Important:

@my_decorator

is shorthand for:

say_hello = my_decorator(say_hello)


So:

1. say_hello is passed to my_decorator.
2. my_decorator creates wrapper.
3. wrapper is returned.
4. say_hello now refers to wrapper.
5. Calling say_hello() executes wrapper().
"""


# ========================================================================
# 4. DECORATOR FLOW
# ========================================================================

"""
Original Function
       ↓
my_decorator(func)
       ↓
wrapper created
       ↓
wrapper returned
       ↓
original function name replaced
       ↓
function call
       ↓
wrapper executes
       ↓
original function executes
"""


# ========================================================================
# 5. DECORATOR WITH FUNCTION ARGUMENTS
# ========================================================================

"""
If the decorated function accepts arguments,
the wrapper must also be able to receive those arguments.
"""


def my_decorator(func):

    def wrapper(word):

        print("Before function call")

        func(word)

        print("After function call")

    return wrapper


@my_decorator
def say_hello(word):

    print("Hello", word)


say_hello("World")


# Output:
#
# Before function call
# Hello World
# After function call


# ========================================================================
# 6. DECORATOR WITH MULTIPLE FUNCTION ARGUMENTS
# ========================================================================

def my_decorator(func):

    def wrapper(a, b):

        print("Before")

        result = func(a, b)

        print("After")

        return result

    return wrapper


@my_decorator
def add(a, b):

    return a + b


print(add(5, 3))


# Output:
#
# Before
# After
# 8


# ========================================================================
# 7. *args AND **kwargs
# ========================================================================

"""
Using fixed parameters such as:

def wrapper(a, b):

only works for specific function signatures.

To make the wrapper flexible, use:

*args
**kwargs


*args:
    Collects positional arguments.

**kwargs:
    Collects keyword arguments.
"""


def my_decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper


@my_decorator
def add(a, b, c):

    return a + b + c


print(add(1, 2, 3))


# Output:
#
# Before
# After
# 6


# ========================================================================
# 8. WHY *args AND **kwargs?
# ========================================================================

"""
They allow the decorator to work with different function signatures.
"""


@my_decorator
def greet(name):

    print(f"Hello, {name}")


greet("Alice")


@my_decorator
def introduce(name, age):

    print(f"Name: {name}")
    print(f"Age: {age}")


introduce("Alice", age=25)


# ========================================================================
# 9. RETURN VALUE FROM DECORATED FUNCTION
# ========================================================================

"""
If the original function returns a value,
the wrapper should normally return that value.
"""


def my_decorator(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result

    return wrapper


@my_decorator
def multiply(a, b):

    return a * b


result = multiply(5, 4)

print(result)


# Output:
#
# 20


"""
Without:

return result

the wrapper would return None by default.

Therefore, the original result would be lost.
"""


# ========================================================================
# 10. DECORATOR WITH PARAMETERS
# ========================================================================

"""
Sometimes the decorator itself needs arguments.

Example:

@repeat(3)

Here:

repeat(3)

is not directly the decorator.

It is a Decorator Factory.

The factory creates and returns the actual decorator.
"""


def repeat(n):

    # Decorator Factory

    def decorator(func):

        # Actual Decorator

        def wrapper(*args, **kwargs):

            for i in range(n):

                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello():

    print("Hello")


hello()


# Output:
#
# Hello
# Hello
# Hello


# ========================================================================
# 11. DECORATOR FACTORY
# ========================================================================

"""
A Decorator Factory is a function that creates and returns a decorator.

Structure:

    Decorator Factory
          ↓
      Decorator
          ↓
       Wrapper
          ↓
   Original Function
"""


def decorator_factory(argument):

    def decorator(func):

        def wrapper(*args, **kwargs):

            print("Decorator argument:", argument)

            return func(*args, **kwargs)

        return wrapper

    return decorator


@decorator_factory("Hello")
def greet():

    print("Welcome")


greet()


# ========================================================================
# 12. DECORATOR WITH MULTIPLE ARGUMENTS
# ========================================================================

def decorator_with_args(arg1, arg2, arg3):

    def decorator(func):

        def wrapper(*args, **kwargs):

            print(
                f"Decorator args: {arg1}, {arg2}, {arg3}"
            )

            return func(*args, **kwargs)

        return wrapper

    return decorator


@decorator_with_args("Hello", "World", "!")
def greet(name):

    print(f"Hello, {name}")


greet("Alice")


# Output:
#
# Decorator args: Hello, World, !
# Hello, Alice


# ========================================================================
# 13. COMPLETE DECORATOR FACTORY FLOW
# ========================================================================

"""
When Python sees:

@decorator_with_args("Hello", "World", "!")
def greet(name):
    print(f"Hello, {name}")


It is approximately equivalent to:

greet = decorator_with_args(
    "Hello",
    "World",
    "!"
)(greet)


Step 1:
-------

decorator_with_args("Hello", "World", "!")

This calls the Decorator Factory.


Step 2:
-------

The factory returns:

decorator


Step 3:
-------

The decorator receives:

func = greet


Step 4:
-------

The decorator creates:

wrapper


Step 5:
-------

The wrapper is returned.

So:

greet = wrapper


Step 6:
-------

When we call:

greet("Alice")

Python executes:

wrapper("Alice")


Step 7:
-------

Inside wrapper:

args = ("Alice",)


Step 8:
-------

The wrapper prints:

Decorator args: Hello, World, !


Step 9:
-------

Then:

func(*args, **kwargs)

calls the original greet function.


Final Output:

Decorator args: Hello, World, !
Hello, Alice
"""


# ========================================================================
# 14. CLOSURE
# ========================================================================

"""
Decorators commonly use closures.

A closure occurs when an inner function remembers and uses variables
from its enclosing function even after the enclosing function
has finished executing.
"""


def outer():

    message = "Hello"

    def inner():

        print(message)

    return inner


func = outer()

func()


# Output:
#
# Hello


"""
Here:

inner()

remembers:

message = "Hello"

This is possible because inner() forms a closure over message.

Decorators use the same concept to remember:

    func
    arg1
    arg2
    arg3
    other decorator-related values
"""


# ========================================================================
# 15. MULTIPLE DECORATORS
# ========================================================================

def decor1(func):

    def wrapper():

        print("Decor1 Before")

        func()

        print("Decor1 After")

    return wrapper


def decor2(func):

    def wrapper():

        print("Decor2 Before")

        func()

        print("Decor2 After")

    return wrapper


@decor1
@decor2
def test():

    print("Function Body")


test()


# Output:
#
# Decor1 Before
# Decor2 Before
# Function Body
# Decor2 After
# Decor1 After


# ========================================================================
# 16. MULTIPLE DECORATOR ORDER
# ========================================================================

"""
This:

@decor1
@decor2
def test():
    pass


is equivalent to:

test = decor1(decor2(test))


Therefore:

Application order:

    decor2
       ↓
    decor1


Execution order:

    decor1 wrapper
         ↓
    decor2 wrapper
         ↓
    original function


So:

    Decor1 Before
    Decor2 Before
    Function Body
    Decor2 After
    Decor1 After
"""


# ========================================================================
# 17. functools.wraps
# ========================================================================

"""
When a function is decorated, the wrapper can replace the original
function's metadata.

For example:

    __name__
    __doc__

To preserve this metadata, use:

from functools import wraps
"""


from functools import wraps


def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():

    """This is the greet function."""

    print("Hello")


greet()

print(greet.__name__)
print(greet.__doc__)


# Output:
#
# Hello
# greet
# This is the greet function.


# ========================================================================
# 18. REAL-LIFE USE CASE: LOGIN REQUIRED
# ========================================================================

def login_required(func):

    @wraps(func)
    def wrapper(user):

        if not user:

            print("Login first")

        else:

            return func(user)

    return wrapper


@login_required
def dashboard(user):

    print(f"Welcome to dashboard, {user}")


dashboard("Alice")


# Output:
#
# Welcome to dashboard, Alice


# ========================================================================
# 19. REAL-LIFE USE CASE: TIMING DECORATOR
# ========================================================================

import time


def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(
            "Execution Time:",
            end - start
        )

        return result

    return wrapper


@timer
def calculate():

    time.sleep(1)

    return "Done"


print(calculate())


"""
Timer Flow:

1. Record start time.
2. Execute original function.
3. Record end time.
4. Calculate elapsed time.
5. Return original result.
"""


# ========================================================================
# 20. REAL-LIFE USE CASE: LOGGING
# ========================================================================

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(
            f"Calling function: {func.__name__}"
        )

        result = func(*args, **kwargs)

        print(
            f"Function {func.__name__} finished"
        )

        return result

    return wrapper


@logger
def add(a, b):

    return a + b


print(add(10, 20))


# Output:
#
# Calling function: add
# Function add finished
# 30


# ========================================================================
# 21. REAL-LIFE USE CASE: VALIDATION
# ========================================================================

def validate_positive(func):

    @wraps(func)
    def wrapper(number):

        if number < 0:

            print("Number must be positive")

            return

        return func(number)

    return wrapper


@validate_positive
def square(number):

    print(number ** 2)


square(5)


# Output:
#
# 25


# ========================================================================
# 22. DECORATOR WITH A METHOD
# ========================================================================

"""
Decorators can also be used with class methods.

When decorating methods, *args and **kwargs are useful because
the first argument is usually self.
"""


def log_method(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(
            f"Calling method: {func.__name__}"
        )

        return func(*args, **kwargs)

    return wrapper


class Calculator:

    @log_method
    def add(self, a, b):

        return a + b


calculator = Calculator()

print(calculator.add(10, 20))


# ========================================================================
# 23. DECORATOR CAN BE USED ON METHODS
# ========================================================================

"""
Decorators are commonly used with:

    Functions
    Methods
    Class methods
    Static methods
    Properties
    Django views
    API endpoints
"""


# ========================================================================
# 24. IMPORTANT DECORATOR RULES
# ========================================================================

"""
Rule 1:
-------

A decorator receives a function or callable and normally
returns another callable.


Rule 2:
-------

@decorator

is shorthand for:

function = decorator(function)


Rule 3:
-------

A wrapper function is commonly used to add extra behavior.


Rule 4:
-------

Use:

*args
**kwargs

when the wrapper should support flexible arguments.


Rule 5:
-------

If the decorator itself accepts arguments,
an additional nested function is required.


Rule 6:
-------

Multiple decorators are applied from bottom to top.


Rule 7:
-------

The outermost decorator executes first when the decorated
function is called.


Rule 8:
-------

If the original function returns a value,
return that value from the wrapper when appropriate.


Rule 9:
-------

Use:

@wraps(func)

to preserve the original function's metadata.


Rule 10:
-------

Decorators can use closures to remember the original function
and decorator-related variables.


Rule 11:
-------

A decorator does not have to return specifically a function;
more generally, it returns a callable that can replace the
original callable.


Rule 12:
-------

A decorator can be applied to both functions and methods.
"""


# ========================================================================
# 25. HOW MANY ARGUMENTS CAN A DECORATOR HAVE?
# ========================================================================

"""
There is no fixed universal number of arguments.

A decorator factory can accept as many arguments as its
definition requires.

Example:
"""


def custom(arg1, arg2, arg3, arg4):

    def decorator(func):

        def wrapper(*args, **kwargs):

            print(arg1)
            print(arg2)
            print(arg3)
            print(arg4)

            return func(*args, **kwargs)

        return wrapper

    return decorator


@custom("A", "B", "C", "D")
def hello():

    print("Hello")


hello()


"""
The number of arguments is determined by the decorator's definition.

For example:

def custom(arg1, arg2):

    ...

requires two decorator arguments.

While:

def custom(arg1, arg2, arg3):

    ...

requires three decorator arguments.
"""


# ========================================================================
# 26. IMPORTANT DIFFERENCE
# ========================================================================

"""
There are THREE different types of arguments to understand.

1. Decorator Arguments
----------------------

Arguments passed to the decorator factory.

Example:

@repeat(3)

Here:

3

is a decorator argument.


2. Function Argument
--------------------

Arguments passed to the decorated function.

Example:

greet("Alice")

Here:

"Alice"

is a function argument.


3. *args and **kwargs
---------------------

Used by the wrapper to collect and forward
the decorated function's arguments.

Example:

def wrapper(*args, **kwargs):

    return func(*args, **kwargs)
"""


# ========================================================================
# 27. THREE-LAYER DECORATOR STRUCTURE
# ========================================================================

"""
When the decorator itself has arguments:

        decorator_with_args()
                  ↓
        Decorator Factory
                  ↓
           decorator(func)
                  ↓
             Actual Decorator
                  ↓
      wrapper(*args, **kwargs)
                  ↓
          Original Function


Easy Memory Trick:

    Factory → Decorator → Wrapper → Function
"""


# ========================================================================
# 28. SIMPLE DECORATOR VS DECORATOR FACTORY
# ========================================================================

"""
Simple Decorator:

@decorator
def function():
    pass


Structure:

decorator(func)
       ↓
   wrapper()


---------------------------------------------------------------

Decorator Factory:

@decorator_factory(argument)
def function():
    pass


Structure:

decorator_factory(argument)
           ↓
       decorator(func)
           ↓
         wrapper()
"""


# ========================================================================
# 29. COMMON REAL-WORLD USE CASES
# ========================================================================

"""
Decorators are commonly used for:

1. Authentication
2. Authorization
3. Logging
4. Timing
5. Caching
6. Validation
7. Rate Limiting
8. Permission Checking
9. Error Handling
10. Debugging
11. Performance Monitoring
12. Django Views
13. Flask Routes
14. API Endpoints
15. Retry Logic
"""


# ========================================================================
# 30. FINAL DECORATOR CONCEPT
# ========================================================================

"""
The complete decorator concept:

                Function
                   ↓
              Decorator
                   ↓
                Wrapper
                   ↓
          Extra Functionality
                   +
             Original Function
                   ↓
               Result


The decorator does NOT need to modify the original function's
source code.

Instead, it wraps the function and controls how the function
is called.
"""


# ========================================================================
# 31. FINAL SHORTCUT
# ========================================================================

"""
Remember these four concepts:

1. Function
   ↓
   The original function.

2. Decorator
   ↓
   Receives the original function.

3. Wrapper
   ↓
   Adds extra behavior and calls the original function.

4. @decorator
   ↓
   Short syntax for:

       function = decorator(function)


For decorators with arguments:

Factory → Decorator → Wrapper → Function


One-Line Definition:

Decorator = A callable that extends or modifies the behavior
of another callable without changing its original source code.
"""