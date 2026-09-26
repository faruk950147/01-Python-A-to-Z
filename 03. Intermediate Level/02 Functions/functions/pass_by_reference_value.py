# ============================================================

# Pass by Value vs Pass by Reference in Python

# ============================================================

# ============================================================

# 1. Basic Concepts

# ============================================================

# Parameter Passing

# -----------------

#

# When a value or object is passed to a function, the process

# is called parameter passing.

#

# Two common parameter-passing concepts are:

#

# 1. Pass by Value

# 2. Pass by Reference

#

# Python uses a different and more precise model:

#

# 3. Pass by Object Reference

# (also called Call by Sharing)

# ============================================================

# 2. Pass by Value

# ============================================================

# Pass by Value means:

#

# - A copy of the value is passed to the function.

# - The function works with that copy.

# - Changing the copy does not change the original variable.

#

#

# Simple idea:

#

# Original value

# |

# | copy

# v

# Function parameter

#

#

# Example:

#

# a = 10

#

# function(a)

#

# Conceptually:

#

# a = 10

# x = 10       <- copy

#

# If x is changed:

#

# x = 20

#

# The original a remains:

#

# a = 10

#

#

# Pass by Value is used by some programming languages.

# ============================================================

# 3. Pass by Reference

# ============================================================

# Pass by Reference means:

#

# - A reference to the original object is passed to the function.

# - The function can access the same object.

# - If the object is modified through that reference,

# the change can be visible outside the function.

#

#

# Simple idea:

#

# Original variable

# |

# v

# Object

# ^

# |

# Function parameter

#

# Both can refer to the same object.

#

#

# IMPORTANT:

#

# Pass by Reference and Pass by Object Reference are not exactly

# the same concept.

#

# Python uses Pass by Object Reference / Call by Sharing.

# ============================================================

# 4. Python's Argument Passing Model

# ============================================================

# Python uses:

#

# Pass by Object Reference

#

# Also called:

#

# Call by Sharing

#

#

# The important idea is:

#

# - Variables are names/references associated with objects.

# - When a function is called, the parameter is bound to

# the same object that the argument refers to.

# - The parameter itself is a local name.

#

#

# Simple visualization:

#

# argument name

# |

# v

# Object

# ^

# |

# parameter name

#

#

# Therefore:

#

# The argument and parameter can refer to the same object.

#

# What happens next depends on what the function does:

#

# 1. Reassignment

# 2. Object modification

# ============================================================

# 5. Immutable Objects

# ============================================================

# Immutable objects cannot be modified after they are created.

#

# Common immutable objects:

#

# int

# float

# str

# tuple

# bool

#

#

# Important:

#

# Immutable does NOT mean that the variable cannot be changed.

#

# It means the existing object itself cannot be modified.

#

# A variable can be reassigned to another object.

# ============================================================

# 6. Immutable Example: Integer

# ============================================================

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

# num ----> 10

#

#

# When modify_number(num) is called:

#

# num ----> 10

# ^

# |

# x

#

# Both num and x refer to the same integer object initially.

#

#

# Then:

#

# x = x + 1

#

# Python cannot modify the existing integer object 10.

#

# Instead, a new integer object 11 is created.

#

# Now:

#

# x -----> 11

#

# num ----> 10

#

#

# Therefore:

#

# Outside function: 10

#

#

# IMPORTANT:

#

# Do NOT say:

#

# "Python passed the integer by value."

#

# More precise:

#

# "Python passed the object reference, but because integers

# are immutable, x = x + 1 creates/rebinds to a new object."

# ============================================================

# 7. Mutable Objects

# ============================================================

# Mutable objects can be modified after they are created.

#

# Common mutable objects:

#

# list

# dict

# set

#

#

# Example:

#

# list  -> mutable

# dict  -> mutable

# set   -> mutable

# ============================================================

# 8. Mutable Example: List

# ============================================================

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

# my_list ----\

# \

# ---> [1, 2, 3]

# /

# lst ---------/

#

#

# Both names refer to the same list object.

#

#

# Then:

#

# lst.append(4)

#

# append() modifies the existing list.

#

#

# After modification:

#

# my_list ----\

# \

# ---> [1, 2, 3, 4]

# /

# lst ---------/

#

#

# The same list object was modified.

#

# Therefore, the change is visible through my_list.

# ============================================================

# 9. VERY IMPORTANT:

# Reassignment vs Modification

# ============================================================

# This is one of the most important concepts in Python.

# ------------------------------------------------------------

# Example A: Reassignment

# ------------------------------------------------------------

def change_list(lst):
lst = [100, 200, 300]

```
print("Inside function:", lst)
```

my_list = [1, 2, 3]

change_list(my_list)

print("Outside function:", my_list)

# Output:

#

# Inside function: [100, 200, 300]

# Outside function: [1, 2, 3]

# Explanation:

#

# Initially:

#

# my_list ----\

# \

# ---> [1, 2, 3]

# /

# lst ---------/

#

#

# Then:

#

# lst = [100, 200, 300]

#

# This is REASSIGNMENT.

#

# A new list object is created.

#

# Now:

#

# lst ---------> [100, 200, 300]

#

# my_list -----> [1, 2, 3]

#

#

# The original list was NOT modified.

#

# Only the local parameter lst was rebound to another object.

# ------------------------------------------------------------

# Example B: Modification

# ------------------------------------------------------------

def change_list(lst):
lst.append(4)

```
print("Inside function:", lst)
```

my_list = [1, 2, 3]

change_list(my_list)

print("Outside function:", my_list)

# Output:

#

# Inside function: [1, 2, 3, 4]

# Outside function: [1, 2, 3, 4]

# Explanation:

#

# Here:

#

# lst.append(4)

#

# modifies the existing list.

#

# No new list is assigned to lst.

#

# Therefore:

#

# my_list ----\

# \

# ---> [1, 2, 3, 4]

# /

# lst ---------/

#

#

# The modification is visible outside the function.

# ============================================================

# 10. String Example

# ============================================================

def modify_string(text):
text = text + " World"

```
print("Inside function:", text)
```

name = "Hello"

modify_string(name)

print("Outside function:", name)

# Output:

#

# Inside function: Hello World

# Outside function: Hello

# Explanation:

#

# Strings are immutable.

#

# Therefore:

#

# text = text + " World"

#

# does not modify the existing string.

#

# A new string object is created.

#

#

# Initially:

#

# name ----> "Hello"

# ^

# |

# text

#

#

# After:

#

# text ----> "Hello World"

#

# name ----> "Hello"

#

#

# Therefore, name remains unchanged.

# ============================================================

# 11. Dictionary Example

# ============================================================

def modify_dict(data):
data["age"] = 25

```
print("Inside function:", data)
```

person = {
"name": "Faruk"
}

modify_dict(person)

print("Outside function:", person)

# Output:

#

# Inside function: {'name': 'Faruk', 'age': 25}

# Outside function: {'name': 'Faruk', 'age': 25}

# Explanation:

#

# Dictionary is mutable.

#

# The statement:

#

# data["age"] = 25

#

# modifies the existing dictionary object.

#

# Therefore, the change is visible outside the function.

# ============================================================

# 12. Set Example

# ============================================================

def modify_set(numbers):
numbers.add(4)

```
print("Inside function:", numbers)
```

my_set = {1, 2, 3}

modify_set(my_set)

print("Outside function:", my_set)

# Output:

#

# Inside function: {1, 2, 3, 4}

# Outside function: {1, 2, 3, 4}

#

# NOTE:

#

# Set elements are unordered, so the printed order may differ.

#

#

# Explanation:

#

# Set is mutable.

#

# add() modifies the existing set object.

#

# Therefore, the change is visible outside the function.

# ============================================================

# 13. Reassignment Does NOT Modify the Original Object

# ============================================================

# Consider:

#

# def change(x):

# x = new_object

#

#

# This means:

#

# "Make x refer to another object."

#

# It does NOT mean:

#

# "Replace the caller's variable."

#

#

# Example:

#

# my_list = [1, 2, 3]

#

# def change(lst):

# lst = [4, 5, 6]

#

#

# After reassignment:

#

# lst -----> [4, 5, 6]

#

# my_list --> [1, 2, 3]

#

#

# The caller's variable still refers to the original list.

# ============================================================

# 14. Modification Changes the Shared Object

# ============================================================

# Consider:

#

# my_list = [1, 2, 3]

#

# def change(lst):

# lst.append(4)

#

#

# Here:

#

# lst.append(4)

#

# modifies the existing object.

#

#

# Before:

#

# my_list ----\

# \

# ---> [1, 2, 3]

# /

# lst ---------/

#

#

# After:

#

# my_list ----\

# \

# ---> [1, 2, 3, 4]

# /

# lst ---------/

#

#

# Both names still refer to the same object.

# ============================================================

# 15. Mutable vs Immutable

# ============================================================

# Immutable:

#

# int

# float

# str

# tuple

# bool

#

#

# Mutable:

#

# list

# dict

# set

#

#

# IMPORTANT:

#

# Mutable/Immutable describes whether an OBJECT can be modified.

#

# It does NOT describe how Python passes arguments.

# ============================================================

# 16. Summary Table

# ============================================================

# | Type   | Mutable? | Example             |

# |--------|----------|---------------------|

# | int    | No       | 10                  |

# | float  | No       | 10.5                |

# | str    | No       | "Hello"             |

# | tuple  | No       | (1, 2, 3)           |

# | bool   | No       | True                |

# | list   | Yes      | [1, 2, 3]           |

# | dict   | Yes      | {"name": "Faruk"}   |

# | set    | Yes      | {1, 2, 3}           |

# ============================================================

# 17. Common Mistake

# ============================================================

# WRONG shortcut:

#

# Immutable = Pass by Value

# Mutable   = Pass by Reference

#

#

# This is NOT technically correct for Python.

#

#

# Correct understanding:

#

# Python uses the SAME argument-passing model:

#

# Pass by Object Reference / Call by Sharing

#

#

# The result looks different because:

#

# Immutable object

# ->

# Existing object cannot be modified

# ->

# Reassignment creates/binds to another object

#

#

# Mutable object

# ->

# Existing object can be modified

# ->

# Modification can be visible outside the function

# ============================================================

# 18. Important Terminology

# ============================================================

# Argument:

#

# The value/object supplied when calling a function.

#

# Example:

#

# modify_list(my_list)

#

# Here:

#

# my_list = argument

#

#

# Parameter:

#

# The local name defined in the function.

#

# Example:

#

# def modify_list(lst):

#

# Here:

#

# lst = parameter

# ============================================================

# 19. Key Points to Remember

# ============================================================

# 1. Python uses Pass by Object Reference.

#

# 2. It is also called Call by Sharing.

#

# 3. Function parameters are local names.

#

# 4. The parameter is bound to the same object that the

# argument refers to.

#

# 5. Immutable objects cannot be modified.

#

# 6. Mutable objects can be modified.

#

# 7. int, float, str, tuple, and bool are immutable.

#

# 8. list, dict, and set are mutable.

#

# 9. Reassignment changes what the local parameter refers to.

#

# 10. Reassignment does NOT change the caller's variable.

#

# 11. Modification changes the existing object.

#

# 12. Modification of a mutable object can be visible outside

# the function.

#

# 13. Do NOT say:

#

# Immutable = Pass by Value

# Mutable   = Pass by Reference

#

# This is only a beginner-friendly shortcut, not the

# technically correct explanation.

# ============================================================

# 20. Golden Rule

# ============================================================

# PYTHON

# |

# v

# Pass by Object Reference

# / Call by Sharing

# |

# ┌─────────┴─────────┐

# |                   |

# v                   v

# Immutable             Mutable

# |                   |

# v                   v

# Cannot modify          Can modify

# existing object        existing object

# |                   |

# v                   v

# Reassignment          Modification

# |                   |

# v                   v

# Local parameter       Same object changes

# refers elsewhere     and change can be visible

#

#

# MOST IMPORTANT:

#

# Reassignment != Modification

#

#

# lst = [100, 200]

# |

# -> Reassignment

#

#

# lst.append(100)

# |

# -> Modification

#

#

# FINAL STATEMENT:

#

# Python uses Pass by Object Reference (Call by Sharing).

# The parameter is bound to the same object as the argument.

# If the function reassigns the parameter, the caller's variable

# is not changed. If the function mutates a mutable object,

# the modification can be visible through the caller's variable.

# ============================================================
