# ============================= 1. What is Set =============================
# → Set is a collection of unique items
# → Unordered (no fixed index)
# → Mutable (can add/remove items)
# → Items must be immutable (hashable)
# → No duplicates allowed
# → Iterable (can use loop)
# → Reference type, dynamic type
# → Internally hash-table based (fast lookup)

# NOTE:
# Set is NOT indexed → no set[0]


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

set1.add(4)                 # single element add
set2.update([5, 6])         # multiple elements add
set3.update("def")          # add characters from string
set4.update(range(5, 8))    # add range values
set5.add(1)

print("\nAfter Add:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)


# ============================= 4. Set Modify Functions =============================

set1.remove(4)     # error if not found
set2.discard(5)    # no error if not found
set3.pop()         # removes random element
set4.clear()       # remove all elements
set5.discard(1)

print("\nAfter Modify:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set4:", set4)
print("set5:", set5)


# ============================= 5. Set Delete Functions =============================

# pop() only works if set is not empty safely
if set1:
    set1.pop()

if set2:
    set2.pop()

if set3:
    set3.pop()

if set4:
    set4.pop()   # already empty

if set5:
    set5.pop()   # empty check

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
set7 = {x for x in range(1, 10) if x % 2 == 0}

print("\nset6:", set6)
print("set7 (even):", set7)


# ============================= 8. Set Operations =============================

A = {1, 2, 3}
B = {3, 4, 5}

print("\nSet Operations:")
print("A:", A)
print("B:", B)

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)


# ============================= 9. Membership Test =============================

print("\nMembership Test:")
print("2 in A:", 2 in A)
print("5 not in A:", 5 not in A)