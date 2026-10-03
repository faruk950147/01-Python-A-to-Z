"""
# Python List

## What is a List?

A **list** is an ordered, mutable collection of items in Python.

### Basic Syntax

```python
my_list = [10, 20, 30, 40]
```

---

# Main Characteristics of List

## 1. Collection of Items

A list is used to store multiple items in a single variable.

```python
numbers = [10, 20, 30, 40]
```

---

## 2. Ordered

A list is **ordered**, meaning the items maintain their insertion order.

```python
numbers = [10, 20, 30]

print(numbers)
```

Output:

```text
[10, 20, 30]
```

---

## 3. Indexed

Each item has an index starting from `0`.

```python
numbers = [10, 20, 30]

print(numbers[0])   # 10
print(numbers[1])   # 20
print(numbers[-1])  # 30
```

Output:

```text
10
20
30
```

### Positive Index

```text
Value:  10    20    30    40
Index:   0     1     2     3
```

### Negative Index

```text
Value:  10    20    30    40
Index:  -4    -3    -2    -1
```

---

## 4. Mutable / Changeable

A list is **mutable**, meaning its items can be changed after creation.

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

Items can also be added or removed.

```python
numbers.append(40)
numbers.remove(20)
```

---

## 5. Duplicate Values Allowed

A list can contain duplicate values.

```python
numbers = [10, 20, 10, 30, 20]

print(numbers)
```

Output:

```text
[10, 20, 10, 30, 20]
```

---

## 6. Heterogeneous Data

A list can contain different data types.

```python
items = [10, "Python", 3.14, True]
```

---

## 7. Iterable

A list can be traversed using loops.

```python
numbers = [10, 20, 30]

for item in numbers:
    print(item)
```

Output:

```text
10
20
30
```

---

# Creating a List

## 1. Using Square Brackets

```python
numbers = [10, 20, 30]
```

---

## 2. Empty List

```python
numbers = []
```

Check type:

```python
print(type(numbers))
```

Output:

```text
<class 'list'>
```

---

## 3. Using `list()`

```python
numbers = list((10, 20, 30))

print(numbers)
```

Output:

```text
[10, 20, 30]
```

You can also create a list from a string:

```python
letters = list("Python")

print(letters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

# Accessing List Elements

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Output:

```text
Apple
Banana
Mango
```

---

# Negative Indexing

Negative indexes start from the end.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])
print(fruits[-2])
```

Output:

```text
Mango
Banana
```

---

# List Slicing

Slicing is used to extract a portion of a list.

### Syntax

```python
list[start:stop:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

The `stop` index is excluded.

---

## Start Omitted

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
```

Output:

```text
[10, 20, 30]
```

---

## Stop Omitted

```python
print(numbers[2:])
```

Output:

```text
[30, 40, 50]
```

---

## Copy Using Slicing

```python
new_numbers = numbers[:]
```

---

## Step

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[::2])
```

Output:

```text
[10, 30, 50]
```

---

## Reverse Using Slicing

```python
print(numbers[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

# Adding Items

## 1. `append()`

Adds one item to the end.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

---

## 2. `insert()`

Adds an item at a specific index.

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
```

Output:

```text
[10, 15, 20, 30]
```

### Syntax

```python
list.insert(index, value)
```

---

## 3. `extend()`

Adds multiple items from another iterable.

```python
numbers = [10, 20]

numbers.extend([30, 40, 50])

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

### `append()` vs `extend()`

```python
a = [1, 2]

a.append([3, 4])

print(a)
```

Output:

```text
[1, 2, [3, 4]]
```

But:

```python
a = [1, 2]

a.extend([3, 4])

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

### Remember

```text
append() → adds one object
extend() → adds elements from an iterable
```

---

# Removing Items

## 1. `remove()`

Removes the first matching value.

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 30, 20]
```

---

## 2. `pop()`

Removes and returns an item by index.

```python
numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)
print(numbers)
```

Output:

```text
20
[10, 30]
```

Without an index, `pop()` removes the last item:

```python
numbers.pop()
```

---

## 3. `del`

Remove an item by index.

```python
numbers = [10, 20, 30]

del numbers[1]

print(numbers)
```

Output:

```text
[10, 30]
```

Remove a range:

```python
del numbers[0:2]
```

---

## 4. `clear()`

Removes all elements.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

---

# Searching in a List

## `in`

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```text
True
```

---

## `not in`

```python
print(50 not in numbers)
```

Output:

```text
True
```

---

# Finding the Position with `index()`

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))
```

Output:

```text
1
```

If the value does not exist, Python raises:

```text
ValueError
```

---

# Counting Items with `count()`

```python
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```

Output:

```text
3
```

---

# Sorting a List

## `sort()`

Sorts the original list.

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### Descending Order

```python
numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

---

# `sorted()` vs `sort()`

### `sort()`

Changes the original list.

```python
numbers = [30, 10, 20]

numbers.sort()

print(numbers)
```

### `sorted()`

Returns a new sorted list.

```python
numbers = [30, 10, 20]

new_numbers = sorted(numbers)

print(numbers)
print(new_numbers)
```

Output:

```text
[30, 10, 20]
[10, 20, 30]
```

### Important

```text
sort()   → modifies original list
sorted() → returns a new sorted list
```

---

# Reversing a List

## `reverse()`

```python
numbers = [10, 20, 30]

numbers.reverse()

print(numbers)
```

Output:

```text
[30, 20, 10]
```

`reverse()` modifies the original list.

---

# Copying a List

## Assignment

```python
a = [10, 20, 30]

b = a
```

Here, `a` and `b` refer to the same list.

```python
b[0] = 100

print(a)
```

Output:

```text
[100, 20, 30]
```

---

## `copy()`

```python
a = [10, 20, 30]

b = a.copy()

b[0] = 100

print(a)
print(b)
```

Output:

```text
[10, 20, 30]
[100, 20, 30]
```

---

## Copy Using Slicing

```python
b = a[:]
```

---

## Copy Using `list()`

```python
b = list(a)
```

These create a new top-level list.

---

# List Concatenation

Two lists can be combined using `+`.

```python
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

---

# List Repetition

Use `*`.

```python
numbers = [1, 2, 3]

print(numbers * 2)
```

Output:

```text
[1, 2, 3, 1, 2, 3]
```

---

# List Packing

Packing means collecting multiple values into one variable/container.

```python
numbers = [10, 20, 30, 40]
```

The values are stored together inside a list.

More importantly, `*args` can pack multiple function arguments:

```python
def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)
```

Output:

```text
(10, 20, 30, 40)
```

Here, `args` contains all positional arguments as a tuple.

---

# List Unpacking

Unpacking means taking elements from a collection and assigning them to separate variables.

```python
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

The number of variables must normally match the number of elements.

---

# Extended Unpacking with `*`

```python
numbers = [10, 20, 30, 40, 50]

a, *b, c = numbers

print(a)
print(b)
print(c)
```

Output:

```text
10
[20, 30, 40]
50
```

Here:

```text
a → 10
b → [20, 30, 40]
c → 50
```

---

# `*` List Unpacking

```python
numbers = [10, 20, 30]

print(*numbers)
```

Output:

```text
10 20 30
```

It can also be used to combine lists:

```python
a = [1, 2]
b = [3, 4]

c = [*a, *b]

print(c)
```

Output:

```text
[1, 2, 3, 4]
```

### Remember

```text
*args → packing
*a    → unpacking
```

---

# Nested List

A list can contain another list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Access an element:

```python
print(matrix[0][1])
```

Output:

```text
2
```

---

# List of Dictionaries

A list can contain dictionaries.

```python
students = [
    {"name": "Faruk", "age": 22},
    {"name": "Ahmed", "age": 23}
]
```

Access:

```python
print(students[0]["name"])
```

Output:

```text
Faruk
```

This structure is very common when working with APIs and JSON data.

---

# Dictionary of Lists

A dictionary can also contain lists.

```python
student = {
    "name": "Faruk",
    "skills": ["Python", "Django", "SQL"]
}
```

Access:

```python
print(student["skills"][0])
```

Output:

```text
Python
```

---

# List Comprehension

List comprehension provides a concise way to create lists.

### Normal Approach

```python
squares = []

for x in range(1, 6):
    squares.append(x * x)

print(squares)
```

### List Comprehension

```python
squares = [x * x for x in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### Syntax

```python
[expression for item in iterable]
```

---

# List Comprehension with Condition

```python
even_numbers = [
    x
    for x in range(1, 11)
    if x % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10]
```

### Syntax

```python
[expression for item in iterable if condition]
```

---

# List Comprehension with `if-else`

```python
result = [
    "Even" if x % 2 == 0 else "Odd"
    for x in range(1, 6)
]

print(result)
```

Output:

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# Useful Built-in Functions

## `len()`

Returns the number of elements.

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output:

```text
3
```

---

## `min()`

```python
numbers = [10, 20, 5, 30]

print(min(numbers))
```

Output:

```text
5
```

---

## `max()`

```python
print(max(numbers))
```

Output:

```text
30
```

---

## `sum()`

```python
print(sum(numbers))
```

Output:

```text
65
```

---

## `any()`

Returns `True` if at least one element is truthy.

```python
data = [False, False, True]

print(any(data))
```

Output:

```text
True
```

---

## `all()`

Returns `True` if all elements are truthy.

```python
data = [True, True, True]

print(all(data))
```

Output:

```text
True
```

---

# Iterating with `enumerate()`

`enumerate()` gives both index and value.

```python
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```text
0 Apple
1 Banana
2 Mango
```

This is often better than manually using indexes.

---

# Iterating with `zip()`

`zip()` combines elements from multiple iterables.

```python
names = ["Faruk", "Ahmed", "Karim"]
ages = [22, 23, 24]

for name, age in zip(names, ages):
    print(name, age)
```

Output:

```text
Faruk 22
Ahmed 23
Karim 24
```

---

# List Methods Cheat Sheet

```python
append()    # Add one item at the end
extend()    # Add multiple items
insert()    # Add item at a specific position

remove()    # Remove by value
pop()       # Remove by index
clear()     # Remove all items

index()     # Find index of a value
count()     # Count occurrences

sort()      # Sort original list
reverse()   # Reverse original list

copy()      # Create a shallow copy
```

---

# List vs Tuple

| Feature       | List            | Tuple      |
| ------------- | --------------- | ---------- |
| Syntax        | `[]`            | `()`       |
| Mutable       | Yes             | No         |
| Ordered       | Yes             | Yes        |
| Indexed       | Yes             | Yes        |
| Duplicates    | Allowed         | Allowed    |
| Heterogeneous | Yes             | Yes        |
| Methods       | More            | Fewer      |
| Typical use   | Changeable data | Fixed data |

Example:

```python
my_list = [10, 20, 30]

my_tuple = (10, 20, 30)
```

---

# List vs Set

| Feature    | List    | Set                                                                    |
| ---------- | ------- | ---------------------------------------------------------------------- |
| Ordered    | Yes     | No guaranteed insertion-order semantics for use as an indexed sequence |
| Indexed    | Yes     | No                                                                     |
| Duplicates | Allowed | Not allowed                                                            |
| Mutable    | Yes     | Yes                                                                    |
| Syntax     | `[]`    | `{}`                                                                   |

Example:

```python
my_list = [10, 20, 10]
my_set = {10, 20, 10}

print(my_list)
print(my_set)
```

Output:

```text
[10, 20, 10]
{10, 20}
```

---

# Time Complexity of Common List Operations

For a Python list:

| Operation             | Average Complexity |
| --------------------- | -----------------: |
| Access by index       |             `O(1)` |
| Update by index       |             `O(1)` |
| Append                |   `O(1)` amortized |
| Pop last item         |             `O(1)` |
| Search                |             `O(n)` |
| `in`                  |             `O(n)` |
| Insert at beginning   |             `O(n)` |
| Delete from beginning |             `O(n)` |
| Delete by value       |             `O(n)` |
| Sort                  |       `O(n log n)` |

### Important DSA Point

```python
numbers[0]
```

is `O(1)` because Python lists support direct index access.

But:

```python
10 in numbers
```

is `O(n)` because Python may need to check many elements.

---

# Common Errors

## IndexError

```python
numbers = [10, 20, 30]

print(numbers[5])
```

There is no index `5`, so Python raises:

```text
IndexError
```

---

## ValueError

```python
numbers = [10, 20, 30]

numbers.remove(100)
```

Because `100` does not exist, Python raises:

```text
ValueError
```

---

# Important Interview Questions

## Q1. Is a Python list mutable?

Yes.

```python
numbers[0] = 100
```

---

## Q2. Can a list contain duplicate values?

Yes.

```python
[10, 10, 20]
```

---

## Q3. Can a list contain different data types?

Yes.

```python
[10, "Python", 3.14, True]
```

---

## Q4. What is the difference between `append()` and `extend()`?

```text
append() → adds one object
extend() → adds elements from an iterable
```

Example:

```python
a = [1, 2]

a.append([3, 4])
# [1, 2, [3, 4]]
```

```python
a = [1, 2]

a.extend([3, 4])
# [1, 2, 3, 4]
```

---

## Q5. Difference between `remove()` and `pop()`?

```text
remove(value) → removes by value
pop(index)    → removes by index and returns the item
```

---

## Q6. Difference between `sort()` and `sorted()`?

```text
sort()   → modifies original list
sorted() → returns a new sorted list
```

---

## Q7. What is list slicing?

Extracting a portion of a list:

```python
numbers[1:4]
```

---

## Q8. What is list comprehension?

A concise way to create a list:

```python
squares = [x * x for x in range(1, 6)]
```

---

## Q9. What does `*` do in list unpacking?

```python
a = [1, 2]
b = [3, 4]

c = [*a, *b]
```

Output:

```text
[1, 2, 3, 4]
```

It unpacks the elements of the lists.

---

## Q10. What is the difference between `a = b` and `a = b.copy()`?

```python
a = b
```

Both refer to the same list.

```python
a = b.copy()
```

Creates a separate top-level list.

---

# One-Line Definition

> **A list is an ordered, indexed, mutable, and iterable collection of items that allows duplicate and heterogeneous values.**

---

# Quick Cheat Sheet

```python
# Create
numbers = [10, 20, 30]

# Access
numbers[0]

# Negative index
numbers[-1]

# Slice
numbers[1:3]

# Add
numbers.append(40)

# Add multiple
numbers.extend([50, 60])

# Insert
numbers.insert(1, 15)

# Remove by value
numbers.remove(20)

# Remove by index
numbers.pop(0)

# Delete
del numbers[0]

# Clear
numbers.clear()

# Search
20 in numbers

# Count
numbers.count(20)

# Find index
numbers.index(20)

# Sort
numbers.sort()

# Reverse
numbers.reverse()

# Copy
new_list = numbers.copy()

# Concatenate
a + b

# Repeat
a * 2

# Unpack
x, y, z = [10, 20, 30]

# Extended unpacking
x, *y, z = [10, 20, 30, 40]

# Unpack using *
c = [*a, *b]

# List comprehension
squares = [x * x for x in range(1, 6)]
```

---

# Final Summary

```text
Python List
    ↓
Ordered
    ↓
Indexed
    ↓
Mutable
    ↓
Iterable
    ↓
Duplicates Allowed
    ↓
Different Data Types Allowed
    ↓
Indexing → O(1)
    ↓
Search → O(n)
    ↓
Add → append(), extend(), insert()
    ↓
Remove → remove(), pop(), del(), clear()
    ↓
Search → in, index(), count()
    ↓
Ordering → sort(), sorted(), reverse()
    ↓
Unpacking → *, a, b = list
    ↓
Comprehension → [expression for item in iterable]
```

"""
