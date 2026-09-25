# ============================================================
# What is a Nested Function?
# ============================================================

# A nested function is a function defined inside another function.
#
# The outer function contains the inner function.
#
#
# Basic Structure:
#
# def outer():
#
#     def inner():
#         # inner function code
#
#     inner()


# ============================================================
# Example 1: Basic Nested Function
# ============================================================

def outer():

    print("outer")

    def inner():
        print("inner")

    # Calling inner function inside outer function
    inner()


# Calling outer function
outer()


# Output:
#
# outer
# inner


# ============================================================
# Explanation
# ============================================================

# Here:
#
# outer() is the outer function.
#
# inner() is the nested / inner function.
#
# inner() is defined inside outer().
#
# Therefore, inner() is available inside the scope of outer().
#
#
# Structure:
#
# outer()
#   |
#   +-- inner()
#
#
# When we call:
#
# outer()
#
# Python executes:
#
# print("outer")
#
# and then:
#
# inner()
#
# which prints:
#
# inner


# ============================================================
# Example 2: Function Assigned to a Variable
# ============================================================

def outer():

    print("outer")


# Assigning the function object to a variable
fun = outer

# Calling outer() through fun
fun()


# Output:
#
# outer


# Explanation:
#
# In Python, functions are first-class objects.
#
# Therefore, we can assign a function to a variable.
#
#
# fun = outer
#
# means:
#
# fun and outer refer to the same function.
#
#
# So:
#
# fun()
#
# is equivalent to:
#
# outer()


# Important:
#
# fun = outer
#
# Correct
#
# fun = outer()
#
# Different!
#
# outer() executes the function immediately.
#
# outer refers to the function object.


# ============================================================
# Example 3: Nested Function with Parameters
# ============================================================

def add(a, b):

    def subtract(a, b):
        return a - b

    # Calling subtract() inside add()
    print("Subtract:", subtract(a, b))

    return a + b


print("Add:", add(9, 6))


# Output:
#
# Subtract: 3
# Add: 15


# ============================================================
# Explanation
# ============================================================

# When we call:
#
# add(9, 6)
#
# Python enters the add() function.
#
# Inside add(), Python creates the nested function:
#
# subtract()
#
# Then:
#
# subtract(9, 6)
#
# returns:
#
# 9 - 6 = 3
#
# So:
#
# print("Subtract:", subtract(a, b))
#
# prints:
#
# Subtract: 3
#
# Finally:
#
# return a + b
#
# returns:
#
# 9 + 6 = 15
#
# Therefore:
#
# Add: 15


# ============================================================
# Example 4: Assigning add() to Another Variable
# ============================================================

def add(a, b):

    def subtract(a, b):
        return a - b

    print("Subtract:", subtract(a, b))

    return a + b


# Assign the function object to d
d = add

# Calling add() through d
print("Add:", d(9, 7))


# Output:
#
# Subtract: 2
# Add: 16


# Explanation:
#
# d = add
#
# means d refers to the same function as add.
#
# Therefore:
#
# d(9, 7)
#
# is equivalent to:
#
# add(9, 7)


# ============================================================
# Example 5: Nested Function and Scope
# ============================================================

def outer():

    message = "Hello"

    def inner():
        print(message)

    inner()


outer()


# Output:
#
# Hello


# Explanation:
#
# inner() can access the variable message
# because message belongs to the outer function's scope.
#
#
# outer()
#   |
#   |-- message = "Hello"
#   |
#   +-- inner()
#         |
#         +-- can access message


# ============================================================
# Example 6: Nested Function with Outer Parameter
# ============================================================

def greet(name):

    def say_hello():
        return "Hello, " + name

    return say_hello()


print(greet("Faruk"))


# Output:
#
# Hello, Faruk


# Explanation:
#
# name belongs to greet().
#
# say_hello() is inside greet().
#
# Therefore, say_hello() can access name.


# ============================================================
# Example 7: Language-Based Greeting
# ============================================================

def greet(lang, name):

    def english(word):
        return word + ", " + name

    def bangla(word):
        return word + ", " + name

    if lang == "english":
        return english("Hello")

    elif lang == "bangla":
        return bangla("হ্যালো")


print(greet("english", "Faruk"))
print(greet("bangla", "Faruk"))


# Output:
#
# Hello, Faruk
# হ্যালো, Faruk


# ============================================================
# Important Concept: Scope
# ============================================================

# A variable/function defined inside a function
# normally belongs to that function's local scope.
#
#
# Example:
#
# def outer():
#
#     def inner():
#         print("inner")
#
#
# inner() can be called inside outer().
#
# But we cannot normally call inner() directly
# from outside outer().
#
#
# Example:
#
# def outer():
#
#     def inner():
#         print("inner")
#
#
# outer()
#
# inner()   # NameError
#
#
# Why?
#
# Because inner() is local to outer().


# ============================================================
# Example 8: Returning a Nested Function
# ============================================================

def outer():

    def inner():
        return "Hello from inner"

    return inner


# outer() returns the inner function
fun = outer()

# Now we can call inner through fun
print(fun())


# Output:
#
# Hello from inner


# Explanation:
#
# outer()
#    |
#    +---- creates inner()
#    |
#    +---- return inner
#             |
#             v
#            fun
#
#
# Then:
#
# fun()
#
# calls the returned inner function.


# ============================================================
# Nested Function vs Normal Function
# ============================================================

# Normal function:
#
# def add(a, b):
#     return a + b
#
#
# Nested function:
#
# def outer():
#
#     def inner():
#         print("Hello")
#
#     inner()


# ============================================================
# Why Use Nested Functions?
# ============================================================

# Nested functions are useful when:
#
# 1. A function is needed only inside another function.
#
# 2. We want to keep helper logic private to the outer function.
#
# 3. The inner function needs to access variables
#    from the outer function.
#
# 4. Closures are needed.
#
# 5. We want to organize complex logic into smaller functions.


# ============================================================
# Key Points to Remember
# ============================================================

# 1. A function defined inside another function
#    is called a nested function.
#
# 2. The outer function contains the inner function.
#
# 3. The inner function can normally be called
#    inside the outer function.
#
# 4. The inner function can access variables
#    from the outer function's scope.
#
# 5. The inner function is normally not directly
#    accessible from outside the outer function.
#
# 6. Python functions are first-class objects.
#
# 7. Therefore, a function can be assigned to a variable:
#
#       d = add
#
# 8. Then the function can be called using:
#
#       d(9, 7)
#
# 9. A nested function can also be returned from
#    the outer function.
#
# 10. Returning a nested function is an important concept
#     behind Python closures.


# ============================================================
# Golden Rule
# ============================================================

# Nested Function:
#
#     Function inside another function
#
#
# Example:
#
#     def outer():
#
#         def inner():
#             pass
#
#
# Scope:
#
#     inner() belongs to the local scope of outer().
#
#
# Function as Object:
#
#     d = add
#
#     d(9, 7)
#
#     is the same as:
#
#     add(9, 7)