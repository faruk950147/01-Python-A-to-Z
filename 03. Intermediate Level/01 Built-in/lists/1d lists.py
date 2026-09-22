# ============================= 1. What is List =============================

# ============================= 2. Basic List 1D =============================

list1d = [1, 2, 3, 4, 5]
list1d = list(range(1, 6))
list1d = list("12345")


# ============================= 3. List Access & Slicing =============================

list1 = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

print(list1[0])     # first element
print(list1[-1])    # last element

# slicing
'''
# syntax: list[start:stop:step]
list[:3] that means case missing start, so it will start from index 
list[3:] that means case missing stop, so it will go to end
list[:] that means case missing both start and stop, so it will go from start to end (full list)
list[:len(list)] that means case missing start, so it will go to end (full list)
list[1:4:2] that means case missing step, so it will go with step 1


negative indexing
list[-1] that means last element
list[-2:] that means last 2 elements
list[:-2] that means all except last 2 elements (missing last 2)


'''

print(list1[1:3])    # ['e', 'l']
print(list1[:3])     # ['H','e','l']
print(list1[0:])     # full list
print(list1[:])      # copy of list
print(list1[::2])    # step slicing
print(list1[::-1])   # reverse list

# negative indexing
print(list1[-1])     # last element
print(list1[-2:])    # last 2 elements
print(list1[:-2])    # all except last 2


# ============================= 4. List Add Functions =============================

list1 = [1, 2, 3]

list1.append(6)          # add at end
list1.extend([7, 8, 9])  # add multiple elements
list1.insert(0, 0)       # add at index

print(list1)


# ============================= 5. List Modify Functions =============================

list1 = [3, 1, 4, 2]

list1.sort()      # ascending
list1.reverse()   # reverse order

copy_list = list1.copy()  # shallow copy

print(list1)
print(copy_list)


# ============================= 6. List Delete Functions =============================

list1 = [1, 2, 3, 4, 5]

list1.remove(3)   # remove by value
list1.pop()       # remove last element
list1.pop(1)      # remove index
# list1.clear()    # remove all elements


# ============================= 7. Looping List =============================

list1 = [1, 2, 3, 4, 5]

# by index
for i in range(len(list1)):
    print(list1[i])

# direct iteration
for item in list1:
    print(item)


# ============================= 8. List Comprehension =============================

squares = [x**2 for x in range(10)]
even = [x for x in range(10) if x % 2 == 0]
chars = [c.upper() for c in "python"]

print(squares)
print(even)
print(chars)


# ============================= 9. List Condition Functions =============================

list1 = [1, 2, 3, 4, 5]

print(any(x > 3 for x in list1))   # True (at least one element is greater than 3)
print(all(x > 0 for x in list1))   # True (all elements are greater than 0)
print(max(list1))                  # 5 (maximum value in the list)
print(min(list1))                  # 1 (minimum value in the list)
print(sum(list1))                  # 15 (sum of all elements)

"""
| Method | Syntax | Description |
| :--- | :--- | :--- |
| **`append()`** | `list.append(item)` | Adds an item to the end of the list. |
| **`clear()`** | `list.clear()` | Removes all items from the list. |
| **`copy()`** | `list.copy()` | Returns a shallow copy of the list. |
| **`count()`** | `list.count(item)` | Returns the number of times an item appears in the list. |
| **`extend()`** | `list.extend(iterable)` | Adds all items from an iterable to the end of the list. |
| **`index()`** | `list.index(item, start, end)` | Returns the index of the first occurrence of an item. |
| **`insert()`** | `list.insert(index, item)` | Inserts an item at the specified index. |
| **`pop()`** | `list.pop(index)` | Removes and returns the item at the specified index. If no index is given, it removes and returns the last item. |
| **`remove()`** | `list.remove(item)` | Removes the first occurrence of the specified item. |
| **`reverse()`** | `list.reverse()` | Reverses the order of the items in the list. |
| **`sort()`** | `list.sort(key=None, reverse=False)` | Sorts the items in the list in ascending order by default. |
"""