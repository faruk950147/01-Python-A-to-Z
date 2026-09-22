# Closure in Python (Detailed Notes)

# How becomes a Closure?
# Condition	Description
# 1.	There must be a nested function (an inner function defined inside an outer function).
# 2.	The inner function must use a variable from the outer function.
# 3.	The outer function must return the inner function, and the inner function must remember the outer variable even after the outer function has finished.


# 1. What is a Closure?

# A closure is a function object that remembers values in the enclosing scopes even if those scopes are no longer in memory.

# In simple terms:
# A closure allows an inner function to access variables from the outer (enclosing) function after the outer function has finished execution.

# 2. Structure of a Closure

# A closure typically has three components:

# An outer function that defines a variable.

# An inner function that uses that variable.

# The outer function returns the inner function.

# The returned function “closes over” the variables of the outer function.

# Example 1: Basic Closure
def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

my_func = outer_function("Hello, Closure!")
my_func()
print(f"dir(my_func): {dir(my_func)}")
print(my_func.__closure__)
print(my_func.__closure__[0].cell_contents)

# Step-by-Step Execution

# outer_function() is called → message = "Hello, Closure!"

# inner_function() is defined inside it and uses message.

# outer_function() returns inner_function → my_func now holds that inner function.

# When my_func() is called → it still remembers message, even though outer_function has already completed.

# inner_function is a closure.

# How Closures Work (Under the Hood)

# When a nested function references variables from its enclosing scope, Python creates a cell object to keep those variable values alive.

# You can inspect this using:

print(my_func.__closure__)
print(my_func.__closure__[0].cell_contents)


# The __closure__ attribute stores the variables retained by the closure.

# 4. The Role of nonlocal

# If you want to modify an outer variable (not just read it), use the nonlocal keyword.

# Example 2: Counter Using Closure
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


# nonlocal count lets the inner function modify the variable count from the outer function’s scope.

# 5. When to Use Closures

# Closures are powerful when you want:

# Data encapsulation – to hide internal variables.

# Function factories – dynamically create functions with preset parameters.

# Decorators are one of the most common real-life uses of closures.

# Example 3: Function Factory
def power_factory(n):
    def power(x):
        return x ** n
    return power

square = power_factory(2)
cube = power_factory(3)

print(square(5))  # 25
print(cube(2))    # 8


# Each returned function “remembers” its own value of n.

# 6. Closure in Decorators

# Closures are the foundation of decorators in Python.

# Example 4: Simple Decorator
def decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


# Here, wrapper() is a closure, as it remembers the func variable from the decorator() function.

# 7. Advantages of Using Closures
# Advantage	Description
# Data Hiding	You can protect variables from being accessed directly.
# State Preservation	Keeps track of state between function calls without using global variables.
# Functional Programming	Useful in decorators, callbacks, and factory patterns.
# Memory Efficiency	Stores only required variables, not the entire scope.
# 8. Limitations of Closures
# Limitation	Explanation
# Debugging Complexity	Harder to track variable states.
# Memory Leaks (rare)	If not managed properly, can keep unnecessary data alive.
# Readability	Beginners might find nested functions confusing.
# 9. Difference Between Closure and Class
# Closure	Class
# Uses function nesting	Uses OOP structure
# Lightweight	Heavy structure
# Keeps state using variables	Keeps state using attributes
# Best for simple stateful behavior	Best for complex data structures
# 10. Key Points to Remember

# A closure is formed when:

# There is a nested function.

# The inner function references variables from the outer function.

# The outer function returns the inner function.

# The outer function’s variables stay alive as long as the inner function exists.

# 11. Real-world Use Case Example
# Example: Creating a Login Counter
def login_tracker():
    count = 0
    def login(username):
        nonlocal count
        count += 1
        print(f"{username} logged in {count} times")
    return login

tracker = login_tracker()
tracker("Faruk")   # Faruk logged in 1 times
tracker("Faruk")   # Faruk logged in 2 times


# login() is a closure that remembers count between calls.

# 12. Closure Summary Table
# Concept	Description
# Definition	Function that remembers variables from its enclosing scope.
# Formed When	Nested function refers to variables from outer function.
# Memory Behavior	Keeps outer variables alive in a cell.
# Use Cases	Decorators, Function factories, Data hiding.
# Keyword	nonlocal (to modify outer variables).