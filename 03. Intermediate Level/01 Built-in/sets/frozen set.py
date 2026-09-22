# ============================= What is Frozen Set =============================

# A frozenset is an immutable set.
# It is created using the frozenset() constructor.
# A frozenset cannot be changed after it is created.
# We cannot add or remove elements from a frozenset.
# Frozenset is hashable, so it can be used as a dictionary key
# or as an element of another set.

a = frozenset([1, 2, 3])

print(a)
# Output: frozenset({1, 2, 3})


# ============================= Operations on Frozen Set =============================

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])


# Union → returns all unique elements from both sets
print(a | b)

# Intersection → returns common elements from both sets
print(a & b)

# Difference → returns elements in a but not in b
print(a - b)

# Symmetric Difference → returns elements in either a or b,
# but not in both
print(a ^ b)

# Disjoint → returns True if the sets have no common elements
print(a.isdisjoint(b))


# ============================= Frozen Set Methods =============================

# Membership test
print(2 in a)

# Length
print(len(a))

# Subset
print(a.issubset(b))

# Superset
print(a.issuperset(b))