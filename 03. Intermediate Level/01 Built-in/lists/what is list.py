"""
# Python List

## What is a List?

A **list** is an ordered, mutable collection of items in Python.

### Basic Syntax

```python
my_list = [10, 20, 30, 40]
```

---

## Main Characteristics of List

### 1. Collection of Items

A list is used to store multiple items in a single variable.

```python
numbers = [10, 20, 30, 40]
```

---

### 2. Ordered

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

### 3. Indexed

Each item has an index starting from `0`.

```python
numbers = [10, 20, 30]

print(numbers[0])   # 10
print(numbers[1])   # 20
print(numbers[-1])  # 30
```

---

### 4. Mutable / Changeable

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

### 5. Duplicate Values Allowed

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

### 6. Heterogeneous Data

A list can contain different data types.

```python
items = [10, "Python", 3.14, True]
```

---

### 7. Iterable

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

## One-Line Definition

> **A list is an ordered, indexed, mutable, and iterable collection of items that allows duplicate and heterogeneous values.**

"""
