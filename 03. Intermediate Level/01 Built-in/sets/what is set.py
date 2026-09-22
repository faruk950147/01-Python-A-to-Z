# ============================= 1. What is Set =============================

# Set is a collection of unique items.
# Set is unordered → no fixed order.
# Set is unindexed → no index like set[0].
# Set is mutable → we can add or remove elements.
# Set does not allow duplicate elements.
# Set is iterable → we can use a loop.
# Set is dynamically sized → it can grow or shrink.
# Set is internally hash-table based → fast membership lookup.
#
# NOTE:
# Set itself is mutable, but its elements must be immutable (hashable).
# Example of valid elements: int, float, str, tuple
# Example of invalid element: list, set, dictionary
#
# Set is NOT indexed:
# set1[0]  # TypeError


# ============================= 2. Basic Set =============================

set1 = {1, 2, 3}
set2 = set([1, 2, 3])
set3 = set("abc")
set4 = set(range(1, 5))
set5 = set()

print("============================ 2. Basic Set =============================")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)


# ============================= 3. Set Add Functions =============================

set1.add(4)                 # Add a single element
set2.update([5, 6])         # Add multiple elements
set3.update("def")          # Add characters from a string
set4.update(range(5, 8))    # Add multiple elements from range
set5.add(1)                 # Add a single element

print("\nAfter Add:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)


# ============================= 4. Set Modify Functions =============================

set1.remove(4)     # Remove an element; raises KeyError if not found
set2.discard(5)    # Remove an element; no error if not found
set3.pop()         # Remove and return an arbitrary element
set4.clear()       # Remove all elements
set5.discard(1)    # Remove 1; no error if not found

print("\nAfter Modify:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)


# ============================= 5. Set Delete Functions =============================

# pop() raises KeyError if the set is empty.
# So, check the set before using pop().

if set1:
    set1.pop()

if set2:
    set2.pop()

if set3:
    set3.pop()

if set4:
    set4.pop()

if set5:
    set5.pop()

print("\nAfter Delete:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)


# ============================= 6. Looping Set =============================

print("\nLooping set1:")

for item in set1:
    print(item)


# ============================= 7. Set Comprehension =============================

set6 = {x for x in range(1, 5)}

set7 = {
    x
    for x in range(1, 10)
    if x % 2 == 0
}

print("\nset6:", set6)
print("set7 (even):", set7)


# ============================= 8. Set Operations =============================

A = {1, 2, 3}
B = {3, 4, 5}

print("\nSet Operations:")
print("A:", A)
print("B:", B)

# Union → all unique elements from both sets
print("Union:", A | B)

# Intersection → common elements
print("Intersection:", A & B)

# Difference → elements in A but not in B
print("Difference:", A - B)

# Symmetric Difference → elements in either A or B, but not both
print("Symmetric Difference:", A ^ B)


# ============================= 9. Membership Test =============================

print("\nMembership Test:")

print("2 in A:", 2 in A)
print("5 not in A:", 5 not in A)


# ============================= 10. Creating a Set =============================

set1 = {'h', 'e', 'l', 'l', 'o'}
set2 = set((1, 2, 3, 4, 5))

print("\nCreating Set:")
print("set1:", set1)
print("set2:", set2)


# ============================= 11. Empty Set =============================

# {} creates an empty dictionary, NOT an empty set.

empty_set = set()

print("\nEmpty Set:")
print(empty_set)


# ============================= 12. Set Cannot Contain Mutable Elements =============================

# Valid:

valid_set = {
    1,
    "hello",
    (1, 2, 3)
}

print("\nValid Set:")
print(valid_set)


# Invalid:

# invalid_set = {[1, 2], [3, 4]}
# TypeError: unhashable type: 'list'


# ============================= 13. Subset and Superset =============================

A = {1, 2, 3, 4, 5, 6}
B = {1, 2}

# B is a subset of A.
# Every element of B exists in A.

print("\nSubset and Superset:")

print(f"B is a subset of A: {B <= A}")
print(f"A is a superset of B: {A >= B}")

# Methods:

print(f"B is a subset of A: {B.issubset(A)}")
print(f"A is a superset of B: {A.issuperset(B)}")


# ============================= 14. Proper Subset and Proper Superset =============================

A = {1, 2, 3, 4, 5, 6}
B = {1, 2}

# Proper subset:
# B is a subset of A, but B != A.

print("\nProper Subset and Proper Superset:")

print(f"B is a proper subset of A: {B < A}")
print(f"A is a proper superset of B: {A > B}")


# NOTE:
# < means proper subset
# <= means subset
#
# > means proper superset
# >= means superset


# ============================= 15. Number of Subsets =============================

# If a set has n elements:
#
# Total number of subsets = 2^n

A = {1, 2, 3, 4, 5, 6}

n = len(A)

print("\nNumber of Subsets:")
print("Number of elements:", n)
print("Total subsets:", 2 ** n)

# 6 elements:
# 2^6 = 64 subsets


# ============================= 16. Universal Set =============================

universal_set = {
    1, 2, 3, 4, 5, 6, 7, 8, 9
}

print("\nUniversal Set:")
print(universal_set)


# ============================= 17. Complement Set =============================

universal_set = {
    1, 2, 3, 4, 5, 6, 7, 8, 9
}

A = {1, 2, 3}

# Complement of A:
# Elements that are in Universal Set
# but not in A.

complement_set = universal_set - A

print("\nComplement Set:")
print(f"Complement of {A}: {complement_set}")


# ============================= 18. Union =============================

A = {1, 2, 3}
B = {3, 4, 5}

print("\nUnion:")

print(f"Union of {A} and {B}: {A | B}")

# Output:
# {1, 2, 3, 4, 5}


# ============================= 19. Intersection =============================

print("\nIntersection:")

print(f"Intersection of {A} and {B}: {A & B}")

# Output:
# {3}


# ============================= 20. Difference =============================

print("\nDifference:")

print(f"A - B: {A - B}")
print(f"B - A: {B - A}")

# A - B:
# Elements that are in A but not in B.
#
# Output:
# {1, 2}
#
# B - A:
# Elements that are in B but not in A.
#
# Output:
# {4, 5}


# ============================= 21. Symmetric Difference =============================

print("\nSymmetric Difference:")

print(f"Symmetric difference: {A ^ B}")

# Elements that are in either A or B,
# but not in both.

# Output:
# {1, 2, 4, 5}


# ============================= 22. Disjoint Sets =============================

print("\nDisjoint:")

print(f"Are {A} and {B} disjoint? {A.isdisjoint(B)}")

# Disjoint sets have no common elements.
#
# A = {1, 2, 3}
# B = {3, 4, 5}
#
# They have 3 in common.
#
# Output:
# False


# ============================= 23. Example of Disjoint Sets =============================

C = {1, 2, 3}
D = {4, 5, 6}

print(f"Are {C} and {D} disjoint? {C.isdisjoint(D)}")

# Output:
# True


"""
| Method | Syntax | Description |
| :--- | :--- | :--- |
| **`add()`** | `set.add(item)` | Adds an item to the set. If the item already exists, nothing changes. |
| **`clear()`** | `set.clear()` | Removes all items from the set. |
| **`copy()`** | `set.copy()` | Returns a shallow copy of the set. |
| **`difference()`** | `set.difference(other)` | Returns a new set containing items that exist in this set but not in the other set. |
| **`difference_update()`** | `set.difference_update(other)` | Removes items from the set that are also present in the other set. |
| **`discard()`** | `set.discard(item)` | Removes the specified item. Does nothing if the item does not exist. |
| **`intersection()`** | `set.intersection(other)` | Returns a new set containing items common to both sets. |
| **`intersection_update()`** | `set.intersection_update(other)` | Updates the set by keeping only items common to both sets. |
| **`isdisjoint()`** | `set.isdisjoint(other)` | Returns `True` if the two sets have no common items; otherwise returns `False`. |
| **`issubset()`** | `set.issubset(other)` | Returns `True` if all items of this set are present in the other set. |
| **`issuperset()`** | `set.issuperset(other)` | Returns `True` if all items of the other set are present in this set. |
| **`pop()`** | `set.pop()` | Removes and returns an arbitrary item from the set. Raises `KeyError` if the set is empty. |
| **`remove()`** | `set.remove(item)` | Removes the specified item. Raises `KeyError` if the item does not exist. |
| **`symmetric_difference()`** | `set.symmetric_difference(other)` | Returns a new set containing items that are in either set, but not in both. |
| **`symmetric_difference_update()`** | `set.symmetric_difference_update(other)` | Updates the set with items that are in either set, but not in both. |
| **`union()`** | `set.union(other)` | Returns a new set containing all unique items from both sets. |
| **`update()`** | `set.update(other)` | Adds all items from another iterable to the set. |
"""