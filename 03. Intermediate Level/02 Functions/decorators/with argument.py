# ================================================================
#              FULL DECORATOR CODE (WITH ARGUMENTS)
# ================================================================

from functools import wraps


# Step 1: Decorator Factory
# This function receives arguments for the decorator.

def decorator_with_args(arg1, arg2, arg3):

    # Step 2: Actual Decorator
    # This function receives the original function.

    def decorator(func):

        # Step 3: Wrapper Function
        # This function controls the actual execution.

        @wraps(func)
        def wrapper(*args, **kwargs):

            # Decorator arguments
            print(f"Decorator args: {arg1}, {arg2}, {arg3}")

            # Call the original function
            result = func(*args, **kwargs)

            # Return the original function's result
            return result

        return wrapper

    return decorator


# ================================================================
# Step 4: Using the Decorator
# ================================================================

@decorator_with_args("Hello", "World", "!")
def greet(name):
    print(f"Hello, {name}")


# ================================================================
# Step 5: Calling the Function
# ================================================================

greet("Alice")


# Output:
#
# Decorator args: Hello, World, !
# Hello, Alice


'''
================================================================
                    COMPLETE FLOW
================================================================

When Python sees:

@decorator_with_args("Hello", "World", "!")
def greet(name):
    print(f"Hello, {name}")


Python internally processes this approximately as:

greet = decorator_with_args(
    "Hello",
    "World",
    "!"
)(greet)


----------------------------------------------------------------
Step 1: Decorator Factory
----------------------------------------------------------------

decorator_with_args("Hello", "World", "!")

This calls the decorator factory.

So:

arg1 = "Hello"
arg2 = "World"
arg3 = "!"

It returns:

decorator


----------------------------------------------------------------
Step 2: Actual Decorator
----------------------------------------------------------------

The returned decorator receives the original function:

func = greet

Conceptually:

decorator(greet)


----------------------------------------------------------------
Step 3: Wrapper
----------------------------------------------------------------

Inside decorator(), the wrapper function is created.

def wrapper(*args, **kwargs):

The wrapper is then returned:

return wrapper


So the original function is effectively replaced by
the wrapper:

greet = wrapper


----------------------------------------------------------------
Step 4: Function Call
----------------------------------------------------------------

When we write:

greet("Alice")

Python actually executes:

wrapper("Alice")


Therefore:

args = ("Alice",)


----------------------------------------------------------------
Step 5: Wrapper Execution
----------------------------------------------------------------

The wrapper first executes:

print(f"Decorator args: {arg1}, {arg2}, {arg3}")

Output:

Decorator args: Hello, World, !


Then:

result = func(*args, **kwargs)


This calls the original function:

greet("Alice")


The original function prints:

Hello, Alice


----------------------------------------------------------------
FINAL OUTPUT
----------------------------------------------------------------

Decorator args: Hello, World, !
Hello, Alice


================================================================
                     THREE MAIN FUNCTIONS
================================================================

decorator_with_args()
        ↓
Creates the decorator and receives decorator arguments.


decorator(func)
        ↓
Receives and wraps the original function.


wrapper(*args, **kwargs)
        ↓
Controls execution and calls the original function.


================================================================
                     EASY MEMORY TRICK
================================================================

Factory → Decorator → Wrapper → Original Function


================================================================
                     CORE FORMULA
================================================================

@decorator_with_args(A, B, C)
def function():
    pass


is approximately:


function = decorator_with_args(A, B, C)(function)


================================================================
                     FINAL CONCEPT
================================================================

Factory
   ↓
decorator_with_args()
   ↓
Actual Decorator
   ↓
decorator(func)
   ↓
Wrapper
   ↓
wrapper(*args, **kwargs)
   ↓
Original Function
   ↓
function()
'''