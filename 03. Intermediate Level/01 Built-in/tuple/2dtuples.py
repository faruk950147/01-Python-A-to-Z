
# NOTE:
# If tuple contains mutable items (like list), those items can change.

t = (1, 2, 3, [4, 5, 6])  # tuple is immutable, but inner list is mutable


# ============================= 2. Basic 2D Tuple =============================

tuple2d = ((1, 2, 3), (4, 5, 6))

print("\n2D Tuple:", tuple2d)


# ============================= 3. Tuple Access Functions =============================

print("\nAccessing elements in 2D Tuple:")

print(tuple2d[0])
print(tuple2d[1])

print(tuple2d[0][0])
print(tuple2d[0][1])
print(tuple2d[0][2])
print(tuple2d[1][0])
print(tuple2d[1][1])
print(tuple2d[1][2])


# ============================= 4. Tuple Slicing =============================

print("\nSlicing 2D Tuple:")

print(tuple2d[0:2])
print(tuple2d[0:2][0])
print(tuple2d[0:2][1])


# ============================= 5. Tuple Add (New Tuple Creation) =============================

# Tuple is immutable → cannot use append/extend/insert
tuple2d_added = tuple2d + ((7, 8, 9), (10, 11, 12))
tuple2d_added = ((0, 0, 0),) + tuple2d_added

print("\nTuple after adding elements:", tuple2d_added)


# ============================= 6. Tuple Modify Functions =============================

tuple2d_mod = ((3, 2, 1), (6, 5, 4))

sorted_tuple = (
    tuple(sorted(tuple2d_mod[0])),
    tuple(sorted(tuple2d_mod[1]))
)

reversed_tuple = (
    tuple(reversed(tuple2d_mod[0])),
    tuple(reversed(tuple2d_mod[1]))
)

copy_tuple = tuple(tuple2d_mod)

print("\nOriginal tuple:", tuple2d_mod)
print("Sorted tuple:", sorted_tuple)
print("Reversed tuple:", reversed_tuple)
print("Copied tuple:", copy_tuple)


# ============================= 7. Tuple Loop Functions =============================

print("\nLooping through 2D tuple:")

for row in tuple2d:
    for col in row:
        print(col, end=" ")
    print()


# ============================= 8. Tuple Comprehension =============================

squares = tuple(x**2 for x in range(10))
even = tuple(x for x in range(10) if x % 2 == 0)
chars = tuple(c.upper() for c in "python")

print("\nSquares:", squares)
print("Even numbers:", even)
print("Chars:", chars)