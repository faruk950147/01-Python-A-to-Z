# ============================= Pass by Value vs Pass by Reference in Python =============================

# 1. Concepts

# Pass by Value:
# - A function gets a copy of the variable.
# - Changes inside the function do not affect the original variable.
# - Common in languages like C, Java (primitive types).

# Pass by Reference:
# - A function gets a reference (memory address) of the variable.
# - Changes inside the function affect the original variable.
# - Common in languages like C++ (with pointers), Java (objects).

# Python’s Case:
# - Python does not have true pass by value.
# - Python does not have true pass by reference.
# - Python uses “pass by object reference”:
#   - Immutable objects (int, str, tuple) behave like pass by value.
#   - Mutable objects (list, dict, set) behave like pass by reference.

# | Object Type | Behaviour                |
# | ----------- | ------------------------ |
# | int, float  | Pass by value works      |
# | str, tuple  | Pass by value works      |
# | list, dict  | Pass by reference works  |
# | set         | Pass by reference works  |


# 2. Immutable Objects Example (Behaves like pass by value)
def modify_number(x):
    x = x + 1
    print("Inside function:", x)

num = 10
modify_number(num)
print("Outside function:", num)

# Output:
# Inside function: 11
# Outside function: 10

# 3. Mutable Objects Example (Behaves like pass by reference)
def modify_list(lst):
    lst.append(4)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)

# Output:
# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]

# 4. Summary Table
# Object Type   | Python Behavior                     | Example
# ------------- | ---------------------------------- | ----------------
# Immutable     | Pass by value (original unchanged) | int, str, tuple
# Mutable       | Pass by reference (original changes) | list, dict, set

# 5. Key Points:
# 1. Python always passes references to objects.
# 2. Immutable objects → function creates a new object → original unchanged.
# 3. Mutable objects → function modifies the same object → original changed.
# 4. True pass by value does not exist in Python, but immutables act like it.
