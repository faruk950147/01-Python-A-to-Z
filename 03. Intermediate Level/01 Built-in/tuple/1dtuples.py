
# ============================= 2. Basic Tuple =============================

tuple1 = (1, 2, 3)
tuple2 = tuple([1, 2, 3])
tuple3 = tuple("abc")
tuple4 = tuple(range(1, 5))
tuple5 = tuple()
tuple_single = (1,)   # single element tuple

print("\n================ Basic Tuples ================")
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)
print(tuple_single)


# ============================= 3. Tuple Access & Slicing =============================

t = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

print("\n================ Tuple Slicing ================")

print(t[1:3])
print(t[:3])
print(t[0:])
print(t[:])
print(t[::2])
print(t[::3])


# ============================= Negative Indexing =============================

print("\n================ Negative Indexing ================")

print(t[-1])
print(t[-2:])
print(t[:-2])
print(t[-2:-1])
print(t[-2:-3])


# ============================= Tuple Reverse =============================

print("\n================ Tuple Reverse ================")

print(t[::-1])
print(t[::-2])
print(t[::-3])
print(t[::-4])


# ============================= 4. Tuple "Add" Functions =============================

print("\n================ Tuple Add Functions ================")

t_num = (1, 2, 3)

t_num = t_num + (4, 5)
t_num = (0,) + t_num
t_num = t_num + (6,)
t_num = t_num + tuple([7, 8, 9])

print(t_num)


# ============================= 5. Tuple Modify Functions =============================

print("\n================ Tuple Modify Functions ================")

t_mod = (3, 1, 2)

t_sorted = tuple(sorted(t_mod))
t_reversed = tuple(reversed(t_mod))
t_copy = tuple(t_mod)

print(t_mod)
print(t_sorted)
print(t_reversed)
print(t_copy)


# ============================= 6. Tuple Delete Functions =============================

print("\n================ Tuple Delete Functions ================")

t_del = (1, 2, 3, 4, 5)
del t_del
# tuple is completely deleted (no methods like remove/pop/clear exist)


# ============================= 7. Looping Tuple =============================

print("\n================ Looping Tuple ================")

t_loop = (1, 2, 3, 4, 5)

for i in range(len(t_loop)):
    print(t_loop[i])

for v in t_loop:
    print(v)


# ============================= 8. Tuple Comprehension =============================

print("\n================ Tuple Comprehension ================")

squares = tuple(x**2 for x in range(10))
even = tuple(x for x in range(10) if x % 2 == 0)
chars = tuple(c.upper() for c in "python")

print(squares)
print(even)
print(chars)

"""
| Method | Syntax | Description |
| :--- | :--- | :--- |
| **`count()`** | `tuple.count(item)` | Returns the number of times an item appears in the tuple. |
| **`index()`** | `tuple.index(item, start, end)` | Returns the index of the first occurrence 
of the specified item. Raises `ValueError` if the item is not found. |
"""