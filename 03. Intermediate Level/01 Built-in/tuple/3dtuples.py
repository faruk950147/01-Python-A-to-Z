

# NOTE:
# If tuple contains mutable object (like list), that inner object can be changed

t = (1, 2, 3, [4, 5, 6])  # tuple is immutable but inner list is mutable


# ============================= 2. Basic 3D Tuple =============================

tuple3d = (
    (
        (1, 2, 3),
        (4, 5, 6)
    ),
    (
        (7, 8, 9),
        (10, 11, 12)
    )
)

print("\n3D Tuple:", tuple3d)


# ============================= 3. Tuple Access =============================

print("\nAccessing elements in 3D Tuple:")

print(tuple3d[0])
print(tuple3d[1])

print(tuple3d[0][0])
print(tuple3d[0][1])

print(tuple3d[0][0][0])
print(tuple3d[1][1][2])


# ============================= 4. Tuple Slicing =============================

print("\nSlicing 3D Tuple:")

print(tuple3d[0:2])
print(tuple3d[0:2][1])
print(tuple3d[0:2][1][0])


# ============================= 5. Tuple Add (New Tuple Creation) =============================

# Tuple is immutable → create new tuple instead of modifying
tuple3d_added = tuple3d + (((13, 14, 15), (16, 17, 18)),)

print("\nTuple after adding new block:", tuple3d_added)


# ============================= 6. Tuple Modify (Derived Data) =============================
# Cannot modify original tuple → only create new transformed versions

tuple3d_flat_sorted = tuple(
    sorted(
        item
        for level1 in tuple3d
        for level2 in level1
        for item in level2
    )
)

print("\nFlattened sorted values:", tuple3d_flat_sorted)


# ============================= 7. Tuple Delete =============================

# Individual elements cannot be deleted
temp = tuple3d
del temp
# print(temp)  # NameError (deleted)


# ============================= 8. Tuple Looping =============================

print("\nLooping through 3D Tuple:")

for level1 in tuple3d:
    for level2 in level1:
        for item in level2:
            print(item, end=" ")
        print()
    print("---")


# ============================= 9. Tuple Comprehension =============================

squares = tuple(x**2 for x in range(10))
even = tuple(x for x in range(10) if x % 2 == 0)
chars = tuple(c.upper() for c in "python")

print("\nSquares:", squares)
print("Even:", even)
print("Chars:", chars)