# ============================================================
# Pass by Value vs Pass by Reference in Python
# ============================================================


# ============================================================
# 1. Basic Concepts
# ============================================================

# Pass by Value:
#
# - A function receives a copy of the value.
# - Changes made to the copy do not affect the original variable.
# - Common in some programming languages.
#
#
# Pass by Reference:
#
# - A function receives a reference to an object.
# - Changes to the object can affect the original object.
#
#
# Python's Case:
#
# Python uses "Pass by Object Reference"
# (also called "Call by Sharing").
#
# This means:
#
# - Variables are references to objects.
# - The function receives a reference to the same object.
# - Whether the original object appears to change depends on
#   whether the object is mutable or immutable.


# ============================================================
# 2. Immutable Objects
# ============================================================

# Immutable objects cannot be changed after they are created.
#
# Examples:
#
# int
# float
# str
# tuple
# bool


def modify_number(x):
    x = x + 1
    print("Inside function:", x)


num = 10

modify_number(num)

print("Outside function:", num)


# Output:
#
# Inside function: 11
# Outside function: 10


# Explanation:
#
# Initially:
#
# num ---> 10
#
# The function receives the reference to the object 10.
#
# When we write:
#
# x = x + 1
#
# Python creates a NEW integer object 11.
#
# Now:
#
# x   ---> 11
# num ---> 10
#
# Therefore, the original value of num does not change.


# ============================================================
# 3. Mutable Objects
# ============================================================

# Mutable objects can be changed after they are created.
#
# Examples:
#
# list
# dict
# set


def modify_list(lst):
    lst.append(4)

    print("Inside function:", lst)


my_list = [1, 2, 3]

modify_list(my_list)

print("Outside function:", my_list)


# Output:
#
# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]


# Explanation:
#
# Initially:
#
# my_list ---> [1, 2, 3]
#
# The function receives a reference to the same list.
#
# When we write:
#
# lst.append(4)
#
# The existing list is modified.
#
# Therefore:
#
# lst     ---> [1, 2, 3, 4]
# my_list ---> [1, 2, 3, 4]
#
# Both variables refer to the same list object.


# ============================================================
# 4. Important Difference: Reassignment vs Modification
# ============================================================

# This is VERY important when learning Python.


# ------------------------------------------------------------
# Example A: Reassignment
# ------------------------------------------------------------

def change_list(lst):
    lst = [100, 200, 300]

    print("Inside function:", lst)


my_list = [1, 2, 3]

change_list(my_list)

print("Outside function:", my_list)


# Output:
#
# Inside function: [100, 200, 300]
# Outside function: [1, 2, 3]


# Why?
#
# The statement:
#
# lst = [100, 200, 300]
#
# does NOT modify the original list.
#
# It makes lst refer to a NEW list.
#
#
# Before:
#
# lst     ----\
#              ---> [1, 2, 3]
# my_list ----/
#
#
# After reassignment:
#
# lst     ---> [100, 200, 300]
#
# my_list ---> [1, 2, 3]


# ------------------------------------------------------------
# Example B: Modification
# ------------------------------------------------------------

def change_list(lst):
    lst.append(4)

    print("Inside function:", lst)


my_list = [1, 2, 3]

change_list(my_list)

print("Outside function:", my_list)


# Output:
#
# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]


# Here append() modifies the existing list.
#
# Therefore, the change is visible outside the function.


# ============================================================
# 5. String Example
# ============================================================

def modify_string(text):
    text = text + " World"

    print("Inside function:", text)


name = "Hello"

modify_string(name)

print("Outside function:", name)


# Output:
#
# Inside function: Hello World
# Outside function: Hello


# Explanation:
#
# String is immutable.
#
# text = text + " World"
#
# creates a new string.
#
# The original string remains unchanged.


# ============================================================
# 6. Dictionary Example
# ============================================================

def modify_dict(data):
    data["age"] = 25

    print("Inside function:", data)


person = {
    "name": "Faruk"
}

modify_dict(person)

print("Outside function:", person)


# Output:
#
# Inside function: {'name': 'Faruk', 'age': 25}
# Outside function: {'name': 'Faruk', 'age': 25}


# Dictionary is mutable.
#
# Therefore, modifying the dictionary inside the function
# also changes the same dictionary outside the function.


# ============================================================
# 7. Set Example
# ============================================================

def modify_set(numbers):
    numbers.add(4)

    print("Inside function:", numbers)


my_set = {1, 2, 3}

modify_set(my_set)

print("Outside function:", my_set)


# Output:
#
# Inside function: {1, 2, 3, 4}
# Outside function: {1, 2, 3, 4}


# Set is mutable.
#
# Therefore, add() modifies the original set.


# ============================================================
# 8. Python's Actual Behavior
# ============================================================

# Python does NOT exactly use:
#
# "Pass by Value"
#
# and it does NOT exactly use:
#
# "Pass by Reference"
#
#
# Python uses:
#
# "Pass by Object Reference"
#
# or:
#
# "Call by Sharing"


# A useful mental model:
#
# Variable ---> Object
#
#
# When a function is called, the function receives
# a reference to the same object.


# ============================================================
# 9. Simple Visualization
# ============================================================


# Immutable example:
#
# num = 10
#
# num ----> 10
#
# modify_number(num)
#
# x -----> 10
# num ---> 10
#
# x = x + 1
#
# x -----> 11
# num ---> 10
#
# Original object was not changed.


# Mutable example:
#
# my_list = [1, 2, 3]
#
# my_list ----\
#              \
#               ---> [1, 2, 3]
#              /
# lst --------/
#
#
# lst.append(4)
#
# my_list ----\
#              \
#               ---> [1, 2, 3, 4]
#              /
# lst --------/
#
# The same list object was modified.


# ============================================================
# 10. Summary Table
# ============================================================

# | Object Type | Mutable? | Example              |
# |-------------|----------|----------------------|
# | int         | No       | 10                   |
# | float       | No       | 10.5                 |
# | str         | No       | "Hello"              |
# | tuple       | No       | (1, 2, 3)            |
# | bool        | No       | True                 |
# | list        | Yes      | [1, 2, 3]            |
# | dict        | Yes      | {"name": "Faruk"}    |
# | set         | Yes      | {1, 2, 3}            |


# ============================================================
# 11. Key Points to Remember
# ============================================================

# 1. Python uses Pass by Object Reference / Call by Sharing.

# 2. A function receives a reference to an object.

# 3. Immutable objects cannot be modified.

# 4. If an immutable value is changed inside a function,
#    a new object is created.

# 5. Mutable objects can be modified inside a function.

# 6. list, dict, and set are mutable.

# 7. int, float, str, tuple, and bool are immutable.

# 8. Reassigning a parameter does NOT change the caller's
#    variable.

# 9. Modifying a mutable object can affect the original object.

# 10. Do not simply say:
#
#     Immutable = Pass by Value
#     Mutable = Pass by Reference
#
#     This is a beginner-friendly shortcut, but technically
#     Python uses the same object-sharing mechanism for both.


# ============================================================
# Golden Rule
# ============================================================

# Python:
#
#     Pass by Object Reference
#
# Immutable object:
#
#     Cannot be changed
#     -> new object is created
#     -> original object remains unchanged
#
# Mutable object:
#
#     Can be changed
#     -> same object is modified
#     -> change may be visible outside the function