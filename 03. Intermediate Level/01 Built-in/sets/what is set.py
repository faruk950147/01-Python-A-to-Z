# =================== What is Set ===================

# Set is a collection of items. 
# Set is unordered, unindexed, and unchangeable but items are immutable.
# Set is written with round brackets.
# when the run output show unordered, 
# unindexed, and unchangeable, it means that the set is unordered,
# unindexed, and unchangeable.

# Creating a set
set1 = {'h', 'e', 'l', 'l', 'o'}
set2 = set((1, 2, 3, 4, 5))

print(set1) 
print(set2)

# ============================= Topic: Sets - Subset and Superset =============================
'''
# A is a main set
A = {1, 2, 3, 4, 5, 6}

# B is a subset of A
B = {1, 2}

print(f"B is a subset of A: {B < A}")
print(f"A is a superset of B: {A > B}")
# methods
print(f"B is a subset of A: {B.issubset(A)}")
print(f"A is a superset of B: {A.issuperset(B)}")

# ============================= Topic: Sets - Proper Subset and Proper Superset =============================

# A is a main set formula 2^n (n is the number of elements in the set)
A = {1, 2, 3, 4, 5, 6}

# A has 6 elements, so it has 2^6 = 64 subsets
# A proper subset is a subset that is not equal to the original set

# B is a proper subset of A
B = {1, 2}

print(f"B is a proper subset of A: {B < A}")
print(f"A is a proper superset of B: {A > B}")
# methods
print(f"B is a proper subset of A: {B.issubset(A)}")
print(f"A is a proper superset of B: {A.issuperset(B)}")

# ============================= Topic: Sets - Universal Sets =============================

universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


# ============================= Topic: Sets - Complement Sets =============================

complement_set = universal_set - {1, 2, 3}
print(f"Complement of {1, 2, 3} in universal set: {complement_set}")


'''

# ============================= Topic: Sets - Operations =============================
A = {1, 2, 3}
B = {3, 4, 5}   

# Union is the combination of two sets
print(f"Union of {A} and {B}: {A | B}")
# output: {1, 2, 3, 4, 5}

# Intersection is the common elements between two sets
print(f"Intersection of {A} and {B}: {A & B}")
# output: {3}

# Difference is the elements that are in the first set but not in the second set
print(f"Difference of {A} and {B}: {A - B}")
# output: {1, 2}

# Symmetric Difference is the elements that are in either set but not in both
print(f"Symmetric difference of {A} and {B}: {A ^ B}")
# output: {1, 2, 4, 5}

# Disjoint means that the sets have no common elements
print(f"Are {A} and {B} disjoint? {A.isdisjoint(B)}")
# output: False




