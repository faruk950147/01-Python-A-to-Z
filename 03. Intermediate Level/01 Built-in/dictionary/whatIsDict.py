"""
# Python Dictionary

## What is a Dictionary?

A **dictionary** is a collection of **key-value pairs** in Python.

Each key is used to access its corresponding value.

### Basic Syntax

```python
student = {
    "name": "Faruk",
    "age": 22,
    "department": "CSE"
}
```

Here:

```text
"name"       → key
"Faruk"      → value

"age"        → key
22           → value
```

---

# Main Characteristics of Dictionary

## 1. Key-Value Pair

A dictionary stores data in the form:

```text
key : value
```

Example:

```python
person = {
    "name": "Faruk",
    "age": 22
}
```

---

## 2. Ordered

Dictionaries preserve **insertion order** in modern Python.

```python
data = {
    "a": 10,
    "b": 20,
    "c": 30
}
```

The order of insertion is maintained.

> Dictionary preserves insertion order, but it is **not accessed by numerical index like a list**.

---

## 3. Mutable / Changeable

A dictionary can be changed after creation.

```python
student = {
    "name": "Faruk",
    "age": 22
}

student["age"] = 23

print(student)
```

Output:

```text
{'name': 'Faruk', 'age': 23}
```

---

## 4. Keys Must Be Unique

A dictionary cannot have duplicate keys.

```python
data = {
    "name": "Faruk",
    "name": "Ahmed"
}

print(data)
```

Output:

```text
{'name': 'Ahmed'}
```

The later value replaces the earlier value.

---

## 5. Values Can Be Duplicated

Dictionary **values** can be duplicate.

```python
data = {
    "a": 10,
    "b": 10,
    "c": 20
}
```

Here, `10` appears more than once.

---

## 6. Keys Must Be Hashable

Dictionary keys must be **hashable** objects.

Common valid keys:

```python
data = {
    "name": "Faruk",
    101: "Student",
    (10, 20): "Point"
}
```

Lists cannot be dictionary keys:

```python
# data = {
#     [10, 20]: "value"
# }
```

This produces:

```text
TypeError: unhashable type: 'list'
```

### Common hashable types

```python
str
int
float
bool
tuple
frozenset
```

Mutable types such as `list`, `dict`, and `set` cannot normally be dictionary keys.

---

## 7. Values Can Be Any Data Type

Dictionary values can contain different types.

```python
data = {
    "name": "Faruk",
    "age": 22,
    "marks": 85.5,
    "passed": True,
    "subjects": ["Python", "C"]
}
```

---

# Creating a Dictionary

## 1. Using `{}`

```python
student = {
    "name": "Faruk",
    "age": 22
}
```

---

## 2. Empty Dictionary

```python
data = {}
```

Check type:

```python
print(type(data))
```

Output:

```text
<class 'dict'>
```

---

## 3. Using `dict()`

```python
student = dict(
    name="Faruk",
    age=22,
    department="CSE"
)

print(student)
```

Output:

```text
{'name': 'Faruk', 'age': 22, 'department': 'CSE'}
```

---

# Accessing Dictionary Values

Dictionary values are accessed using their keys.

```python
student = {
    "name": "Faruk",
    "age": 22
}

print(student["name"])
print(student["age"])
```

Output:

```text
Faruk
22
```

---

# Accessing with `get()`

Instead of:

```python
print(student["email"])
```

which raises `KeyError` if the key doesn't exist, you can use:

```python
print(student.get("email"))
```

Output:

```text
None
```

You can also provide a default value:

```python
print(student.get("email", "Not Found"))
```

Output:

```text
Not Found
```

### Difference

```python
student["email"]
```

→ Raises `KeyError` if missing.

```python
student.get("email")
```

→ Returns `None` if missing.

---

# Adding a New Key-Value Pair

```python
student = {
    "name": "Faruk",
    "age": 22
}

student["department"] = "CSE"

print(student)
```

Output:

```text
{'name': 'Faruk', 'age': 22, 'department': 'CSE'}
```

---

# Updating an Existing Value

```python
student = {
    "name": "Faruk",
    "age": 22
}

student["age"] = 23
```

Now:

```python
print(student)
```

Output:

```text
{'name': 'Faruk', 'age': 23}
```

---

# Adding or Updating with `update()`

```python
student = {
    "name": "Faruk",
    "age": 22
}

student.update({
    "age": 23,
    "department": "CSE"
})
```

Output:

```python
print(student)
```

```text
{'name': 'Faruk', 'age': 23, 'department': 'CSE'}
```

`update()`:

* Existing key → updates value
* New key → adds key-value pair

---

# Removing Dictionary Items

## 1. `pop()`

Removes a specific key and returns its value.

```python
student = {
    "name": "Faruk",
    "age": 22,
    "department": "CSE"
}

age = student.pop("age")

print(age)
print(student)
```

Output:

```text
22
{'name': 'Faruk', 'department': 'CSE'}
```

---

## 2. `popitem()`

Removes and returns the **last inserted key-value pair**.

```python
student = {
    "name": "Faruk",
    "age": 22,
    "department": "CSE"
}

item = student.popitem()

print(item)
print(student)
```

Output:

```text
('department', 'CSE')
{'name': 'Faruk', 'age': 22}
```

---

## 3. `del`

Remove a specific key:

```python
del student["age"]
```

You can also delete the entire dictionary:

```python
del student
```

---

## 4. `clear()`

Removes all items but keeps the dictionary object.

```python
student = {
    "name": "Faruk",
    "age": 22
}

student.clear()

print(student)
```

Output:

```text
{}
```

---

# Checking if a Key Exists

Use the `in` operator.

```python
student = {
    "name": "Faruk",
    "age": 22
}

print("name" in student)
print("email" in student)
```

Output:

```text
True
False
```

### Important

`in` checks **keys**, not values.

```python
print("Faruk" in student)
```

Output:

```text
False
```

To check values:

```python
print("Faruk" in student.values())
```

Output:

```text
True
```

---

# Dictionary Length

Use `len()`:

```python
student = {
    "name": "Faruk",
    "age": 22
}

print(len(student))
```

Output:

```text
2
```

---

# Dictionary Methods

Important built-in dictionary methods:

```text
keys()
values()
items()
get()
update()
pop()
popitem()
clear()
copy()
setdefault()
fromkeys()
```

---

# `keys()`

Returns a view containing all keys.

```python
student = {
    "name": "Faruk",
    "age": 22
}

print(student.keys())
```

You can iterate:

```python
for key in student.keys():
    print(key)
```

Output:

```text
name
age
```

---

# `values()`

Returns a view containing all values.

```python
for value in student.values():
    print(value)
```

Output:

```text
Faruk
22
```

---

# `items()`

Returns key-value pairs.

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Faruk
age 22
```

This is one of the most commonly used dictionary operations.

---

# Dictionary Iteration

A dictionary can be iterated using loops.

```python
student = {
    "name": "Faruk",
    "age": 22
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

### Iterate over values

```python
for value in student.values():
    print(value)
```

### Iterate over key-value pairs

```python
for key, value in student.items():
    print(key, value)
```

---

# Nested Dictionary

A dictionary can contain another dictionary.

```python
students = {
    "student1": {
        "name": "Faruk",
        "age": 22
    },
    "student2": {
        "name": "Ahmed",
        "age": 23
    }
}
```

Access nested values:

```python
print(students["student1"]["name"])
```

Output:

```text
Faruk
```

---

# Dictionary with List Values

A dictionary value can be a list.

```python
student = {
    "name": "Faruk",
    "subjects": [
        "Python",
        "C",
        "Java"
    ]
}
```

Access:

```python
print(student["subjects"][0])
```

Output:

```text
Python
```

---

# Dictionary with Tuple Values

```python
data = {
    "point": (10, 20),
    "size": (100, 200)
}
```

---

# Dictionary with Set Values

```python
data = {
    "languages": {"Python", "C", "Java"}
}
```

---

# Copying a Dictionary

## Shallow Copy

```python
student = {
    "name": "Faruk",
    "age": 22
}

new_student = student.copy()
```

Now they are separate dictionary objects.

```python
new_student["age"] = 25

print(student)
print(new_student)
```

Output:

```text
{'name': 'Faruk', 'age': 22}
{'name': 'Faruk', 'age': 25}
```

---

# Important: Assignment vs Copy

This:

```python
a = {
    "name": "Faruk"
}

b = a
```

does **not** create an independent dictionary.

Both variables refer to the same dictionary.

```python
b["name"] = "Ahmed"

print(a)
```

Output:

```text
{'name': 'Ahmed'}
```

But:

```python
b = a.copy()
```

creates a separate top-level dictionary.

---

# Dictionary Merging

Python allows dictionaries to be merged using `**`.

```python
student = {
    "name": "Faruk"
}

details = {
    "age": 22
}

data = {
    **student,
    **details
}

print(data)
```

Output:

```text
{'name': 'Faruk', 'age': 22}
```

---

# What Does `**dict` Mean?

`**` is called **dictionary unpacking** when used in a dictionary literal or function call.

Example:

```python
student = {
    "name": "Faruk",
    "age": 22
}

data = {
    **student
}

print(data)
```

Output:

```text
{'name': 'Faruk', 'age': 22}
```

It means:

```text
Take all key-value pairs from student
and unpack them here.
```

---

# Dictionary Unpacking with Multiple Dictionaries

```python
a = {
    "name": "Faruk"
}

b = {
    "age": 22
}

c = {
    **a,
    **b
}

print(c)
```

Output:

```text
{'name': 'Faruk', 'age': 22}
```

### Duplicate keys

If the same key appears more than once:

```python
a = {
    "name": "Faruk"
}

b = {
    "name": "Ahmed"
}

c = {
    **a,
    **b
}

print(c)
```

Output:

```text
{'name': 'Ahmed'}
```

The later value wins.

---

# `**kwargs`

`**` is also used in function definitions.

```python
def student(**kwargs):
    print(kwargs)

student(
    name="Faruk",
    age=22,
    department="CSE"
)
```

Output:

```text
{
    'name': 'Faruk',
    'age': 22,
    'department': 'CSE'
}
```

Here, `kwargs` is a dictionary.

---

# Dictionary Comprehension

Dictionary comprehension provides a short way to create dictionaries.

### Normal way

```python
squares = {}

for x in range(1, 6):
    squares[x] = x * x
```

### Dictionary comprehension

```python
squares = {
    x: x * x
    for x in range(1, 6)
}
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Syntax

```python
{key: value for item in iterable}
```

---

# Dictionary Comprehension with Condition

```python
even_squares = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}
```

Output:

```text
{
    2: 4,
    4: 16,
    6: 36,
    8: 64,
    10: 100
}
```

---

# `setdefault()`

`setdefault()` returns the value of a key.

If the key does not exist, it inserts the key with a default value.

```python
student = {
    "name": "Faruk"
}

student.setdefault("age", 22)

print(student)
```

Output:

```text
{'name': 'Faruk', 'age': 22}
```

If the key already exists:

```python
student.setdefault("name", "Ahmed")
```

The existing value remains unchanged.

---

# `fromkeys()`

Creates a dictionary from a sequence of keys.

```python
keys = ["name", "age", "department"]

student = dict.fromkeys(keys)

print(student)
```

Output:

```text
{'name': None, 'age': None, 'department': None}
```

You can provide a default value:

```python
student = dict.fromkeys(keys, "Unknown")

print(student)
```

Output:

```text
{
    'name': 'Unknown',
    'age': 'Unknown',
    'department': 'Unknown'
}
```

---

# Dictionary Membership

### Check key

```python
"name" in student
```

### Check key doesn't exist

```python
"email" not in student
```

### Check value

```python
"Faruk" in student.values()
```

---

# Dictionary vs List

| Feature          | Dictionary          | List               |
| ---------------- | ------------------- | ------------------ |
| Data structure   | Key-value           | Ordered collection |
| Access           | Key                 | Index              |
| Mutable          | Yes                 | Yes                |
| Duplicate keys   | No                  | Not applicable     |
| Duplicate values | Yes                 | Yes                |
| Ordered          | Yes                 | Yes                |
| Example          | `{"name": "Faruk"}` | `["Faruk", 22]`    |

---

# Dictionary vs Set

| Feature          | Dictionary      | Set                |
| ---------------- | --------------- | ------------------ |
| Stores           | Key-value pairs | Unique values      |
| Syntax           | `{key: value}`  | `{value1, value2}` |
| Duplicate values | Allowed         | Not allowed        |
| Mutable          | Yes             | Yes                |
| Empty syntax     | `{}`            | `set()`            |

Important:

```python
{}
```

creates an **empty dictionary**, not an empty set.

For an empty set:

```python
set()
```

---

# Important Dictionary Concepts

### Key

Used to identify/access a value.

```python
"name"
```

### Value

The data associated with a key.

```python
"Faruk"
```

### Item

A complete key-value pair.

```python
"name": "Faruk"
```

---

# Common Errors

## `KeyError`

```python
student = {
    "name": "Faruk"
}

print(student["age"])
```

Because `"age"` doesn't exist.

Use:

```python
print(student.get("age"))
```

if you want a safe lookup.

---

## `TypeError: unhashable type`

Invalid:

```python
data = {
    [1, 2]: "value"
}
```

Because a list is not hashable.

Use a tuple instead:

```python
data = {
    (1, 2): "value"
}
```

---

# Useful Built-in Functions

## `len()`

```python
len(student)
```

Returns the number of key-value pairs.

---

## `type()`

```python
type(student)
```

Output:

```text
<class 'dict'>
```

---

## `sorted()`

Sorts dictionary keys:

```python
data = {
    "c": 30,
    "a": 10,
    "b": 20
}

print(sorted(data))
```

Output:

```text
['a', 'b', 'c']
```

---

# Practical Example

```python
student = {
    "name": "Faruk",
    "age": 22,
    "department": "CSE",
    "skills": ["Python", "Django", "SQL"],
    "is_student": True
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Department:", student["department"])

print("\nSkills:")

for skill in student["skills"]:
    print(skill)
```

Output:

```text
Name: Faruk
Age: 22
Department: CSE

Skills:
Python
Django
SQL
```

---

# Interview Important Points

### Q1. Is dictionary mutable?

Yes.

```python
student["age"] = 23
```

---

### Q2. Can dictionary have duplicate keys?

No.

If duplicate keys are provided, the later value replaces the earlier one.

---

### Q3. Can dictionary have duplicate values?

Yes.

```python
{
    "a": 10,
    "b": 10
}
```

---

### Q4. Can a list be a dictionary key?

No.

```python
# {[1, 2]: "value"}
```

because lists are unhashable.

---

### Q5. Can a tuple be a dictionary key?

Yes, provided the tuple itself contains only hashable elements.

```python
{
    (10, 20): "Point"
}
```

---

### Q6. How do you check whether a key exists?

```python
if "name" in student:
    print("Key exists")
```

---

### Q7. What is the difference between `[]` and `get()`?

```python
student["age"]
```

Raises `KeyError` if the key is missing.

```python
student.get("age")
```

Returns `None` by default if the key is missing.

---

### Q8. What does `**dict` mean?

It means **dictionary unpacking** in contexts such as:

```python
data = {
    **student
}
```

It can also be used for keyword arguments:

```python
def func(**kwargs):
    print(kwargs)
```

---

# One-Line Definition

> **A dictionary is a mutable, ordered collection of key-value pairs where keys are unique and hashable, while values can be of any data type.**

---

# Quick Cheat Sheet

```python
# Create
data = {"name": "Faruk", "age": 22}

# Access
data["name"]

# Safe access
data.get("name")

# Add
data["city"] = "Bogura"

# Update
data["age"] = 23

# Multiple update
data.update({"age": 24, "city": "Dhaka"})

# Delete
del data["age"]

# Remove and return
data.pop("city")

# Remove last item
data.popitem()

# Remove everything
data.clear()

# Keys
data.keys()

# Values
data.values()

# Key-value pairs
data.items()

# Check key
"name" in data

# Length
len(data)

# Copy
new_data = data.copy()

# Dictionary unpacking
new_data = {**data}

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
```

---

# Most Important Things to Remember

```text
Dictionary
    ↓
Key : Value
    ↓
Keys → Unique + Hashable
Values → Any Data Type
    ↓
Mutable
    ↓
Insertion Order Preserved
    ↓
Access → dictionary[key]
    ↓
Safe Access → dictionary.get(key)
    ↓
Iteration → keys(), values(), items()
    ↓
Merge → update() / **dict
    ↓
Create Efficiently → Dictionary Comprehension
```

"""