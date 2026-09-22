# Copying in Python: Full Guide

# Python has three main ways to handle copying of objects:
#
# 1. Assignment (No Copy)
# 2. Shallow Copy
# 3. Deep Copy


# ============================================================
# 1. Assignment (No Copy)
# ============================================================

# When you assign one variable to another using =,
# both variables point to the same object.

dict1 = {1: 'one', 2: 'two'}
dict2 = dict1  # Assignment, no copy

print(dict1)  # {1: 'one', 2: 'two'}
print(dict2)  # {1: 'one', 2: 'two'}

print(id(dict1))
print(id(dict2))  # Same ID

print(dict1 is dict2)  # True


# Changing dict2 also changes dict1
dict2[1] = 'ONE'

print(dict1)  # {1: 'ONE', 2: 'two'}
print(dict2)  # {1: 'ONE', 2: 'two'}


# Both dict1 and dict2 refer to the same object.
# Changes in one will reflect in the other.


# ============================================================
# 2. Shallow Copy
# ============================================================

# A shallow copy creates a new outer object,
# but nested objects are still shared.

a = {
    1: 'one',
    2: [10, 20]
}

b = a.copy()  # Shallow copy

print(a)  # {1: 'one', 2: [10, 20]}
print(b)  # {1: 'one', 2: [10, 20]}

print(id(a))
print(id(b))  # Different IDs

print(a is b)  # False


# The nested list is shared
print(id(a[2]))
print(id(b[2]))  # Same ID

print(a[2] is b[2])  # True


# Changing the nested list affects both
b[2].append(30)

print(a)  # {1: 'one', 2: [10, 20, 30]}
print(b)  # {1: 'one', 2: [10, 20, 30]}


# But changing a top-level value does NOT affect the original.

a = {
    1: 'one',
    2: [10, 20]
}

b = a.copy()

b[1] = 'ONE'

print(a)  # {1: 'one', 2: [10, 20]}
print(b)  # {1: 'ONE', 2: [10, 20]}


# ============================================================
# 3. Deep Copy
# ============================================================

# A deep copy creates a new object and recursively
# copies all nested objects.

import copy

dict1 = {
    1: 'one',
    2: [10, 20]
}

dict2 = copy.deepcopy(dict1)

print(dict1)  # {1: 'one', 2: [10, 20]}
print(dict2)  # {1: 'one', 2: [10, 20]}


# Now the nested lists are also different objects.

print(id(dict1[2]))
print(id(dict2[2]))  # Different IDs

print(dict1[2] is dict2[2])  # False


# Changing the nested list affects only dict2

dict2[2].append(30)

print(dict1)  # {1: 'one', 2: [10, 20]}
print(dict2)  # {1: 'one', 2: [10, 20, 30]}


# ============================================================
# Assignment vs Shallow Copy vs Deep Copy
# ============================================================

# Assignment
# ------------
# Same outer object
# Same nested objects

a = [1, 2, [3, 4]]
b = a

print(a is b)  # True


# Shallow Copy
# ------------
# Different outer object
# Same nested objects

a = [1, 2, [3, 4]]
b = a.copy()

print(a is b)  # False
print(a[2] is b[2])  # True


# Deep Copy
# ----------
# Different outer object
# Different nested objects

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

print(a is b)  # False
print(a[2] is b[2])  # False


# ============================================================
# Quick Summary
# ============================================================

# Assignment:
# a = b
# Both variables refer to the same object.

# Shallow Copy:
# b = a.copy()
# New outer object, but nested objects are shared.

# Deep Copy:
# b = copy.deepcopy(a)
# New outer object and new nested objects.


# Easy way to remember:
#
# Assignment  -> Same Object
# Shallow Copy -> New Outer Object
# Deep Copy    -> Completely Independent Nested Structure