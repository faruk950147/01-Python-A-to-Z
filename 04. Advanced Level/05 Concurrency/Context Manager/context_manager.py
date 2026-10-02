"""
# Python Context Manager

## 1. What is a Context Manager?

A **Context Manager** is a Python mechanism used to **manage resources safely and automatically**.

It ensures that a resource is properly **acquired before use** and **released after use**, even if an exception occurs.

A context manager is commonly used with the `with` statement.

### Basic Syntax

```python
with expression as variable:
    # work with the resource
```

For example:

```python
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
```

Here:

```text
open() → opens the file
with   → manages the file
read() → reads the file
exit   → file is automatically closed
```

You do not need to manually call:

```python
file.close()
```

---

# 2. Why Use Context Managers?

Without a context manager:

```python
file = open("file.txt", "r")

data = file.read()

file.close()
```

If an exception occurs before `file.close()`, the file may not be closed properly.

With a context manager:

```python
with open("file.txt", "r") as file:
    data = file.read()
```

Python automatically handles the cleanup.

### Main Benefits

```text
Context Manager
      │
      ├── Resource setup
      ├── Resource usage
      ├── Automatic cleanup
      └── Exception-safe cleanup
```

Commonly managed resources include:

```text
File
Database Connection
Network Connection
Lock
Socket
Temporary Resource
```

---

# 3. `open()` and File Modes

Python's `open()` function can be used with different file modes.

```python
open("file.txt", mode)
```

Common modes are:

| Mode | Meaning              |
| ---- | -------------------- |
| `r`  | Read                 |
| `w`  | Write                |
| `a`  | Append               |
| `x`  | Create a new file    |
| `r+` | Read and write       |
| `b`  | Binary mode modifier |
| `t`  | Text mode modifier   |

> **Important:** `b` and `t` are mode modifiers. They are normally combined with another mode, such as `rb`, `wb`, or `rt`.

---

# 4. Read Mode — `r`

`r` means **read**.

It opens an existing file for reading.

```python
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
```

If the file does not exist, Python raises:

```python
FileNotFoundError
```

---

# 5. Write Mode — `w`

`w` means **write**.

It creates a new file if the file does not exist.

If the file already exists, its existing content is **overwritten**.

```python
with open("file.txt", "w") as file:
    file.write("Hello, World!")
```

### Important

```text
Existing file
     ↓
    "w"
     ↓
Old content is removed
     ↓
New content is written
```

---

# 6. Append Mode — `a`

`a` means **append**.

It writes new content at the end of the file.

```python
with open("file.txt", "a") as file:
    file.write("Hello, World!")
```

Existing content is preserved.

For example:

```text
Before:

Hello

After:

Hello
Hello, World!
```

---

# 7. Read and Write Mode — `r+`

`r+` allows both **reading and writing**.

The file must already exist.

```python
with open("file.txt", "r+") as file:
    data = file.read()
    print(data)

    file.write("Hello, World!")
```

### Important

`r+` does **not** automatically append to the end.

If you want to write at the end after reading, use:

```python
with open("file.txt", "r+") as file:
    data = file.read()
    print(data)

    file.write("Hello, World!")
```

Because the file position is after the `read()` operation, the write occurs from the current file position.

---

# 8. Create Mode — `x`

`x` means **exclusive creation**.

It creates a new file.

```python
with open("file.txt", "x") as file:
    file.write("Hello, World!")
```

If the file already exists, Python raises:

```python
FileExistsError
```

---

# 9. Binary Mode — `b`

`b` means **binary mode**.

It is normally combined with another mode.

For example:

```python
with open("image.jpg", "rb") as file:
    data = file.read()
```

Here:

```text
r → read
b → binary

rb → read binary
```

For writing binary data:

```python
with open("image.jpg", "wb") as file:
    file.write(binary_data)
```

### Important

This is **not normally valid**:

```python
open("file.txt", "b")
```

Instead, use combinations such as:

```python
rb
wb
ab
rb+
```

---

# 10. Text Mode — `t`

`t` means **text mode**.

It is the default mode for normal text files.

For example:

```python
with open("file.txt", "rt") as file:
    data = file.read()
    print(data)
```

You can also simply write:

```python
with open("file.txt", "r") as file:
    data = file.read()
```

because text mode is the default.

Similarly:

```python
wt
at
rt
```

are valid combinations.

---

# 11. Context Manager with File Reading

```python
with open("file.txt", "r") as file:
    data = file.read()

print(data)
```

After leaving the `with` block:

```python
file.closed
```

will be:

```python
True
```

Example:

```python
with open("file.txt", "r") as file:
    print(file.read())

print(file.closed)
```

Output:

```text
True
```

---

# 12. Context Manager Automatically Closes Resources

Consider:

```python
with open("file.txt", "r") as file:
    data = file.read()
```

The general flow is:

```text
Enter Context
      ↓
Open File
      ↓
Use File
      ↓
Exit Context
      ↓
Close File
```

Even if an exception occurs inside the block, the context manager performs the required cleanup.

---

# 13. How Does a Context Manager Work?

A class can implement the **Context Manager Protocol** using two special methods:

```python
__enter__()
__exit__()
```

### Basic Structure

```python
class MyContext:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
```

Usage:

```python
with MyContext() as obj:
    print("Inside context")
```

Output:

```text
Entering context
Inside context
Exiting context
```

---

# 14. `__enter__()` Method

`__enter__()` is called when execution enters the `with` block.

```python
def __enter__(self):
    print("Entering context")
    return self
```

It is commonly used to:

```text
Allocate resource
Initialize resource
Open connection
Acquire lock
```

---

# 15. `__exit__()` Method

`__exit__()` is called when execution leaves the `with` block.

```python
def __exit__(self, exc_type, exc_value, traceback):
    print("Exiting context")
```

It is commonly used to:

```text
Close resource
Release lock
Close connection
Cleanup
```

---

# 16. Custom Context Manager Example

```python
class MyContext:

    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")


with MyContext():
    print("Working with resource")
```

Output:

```text
Resource acquired
Working with resource
Resource released
```

---

# 17. Context Manager Using `contextlib`

Python also provides the `contextlib` module for creating context managers.

```python
from contextlib import contextmanager


@contextmanager
def my_context():

    print("Resource acquired")

    try:
        yield

    finally:
        print("Resource released")


with my_context():
    print("Working with resource")
```

Output:

```text
Resource acquired
Working with resource
Resource released
```

---

# 18. Context Manager with `yield`

The `yield` statement separates the setup and cleanup parts.

```python
@contextmanager
def my_context():

    # Setup
    print("Start")

    try:
        yield

    finally:
        # Cleanup
        print("End")
```

Flow:

```text
Setup
  ↓
yield
  ↓
with block executes
  ↓
finally
  ↓
Cleanup
```

---

# 19. Context Manager and Exceptions

A major advantage of context managers is safe cleanup when an exception occurs.

```python
class MyContext:

    def __enter__(self):
        print("Resource acquired")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")


with MyContext():
    print("Working")

    raise ValueError("Something went wrong")
```

Even though an exception occurs:

```text
Resource acquired
Working
Resource released
```

The `__exit__()` method is still called.

---

# 20. Important File Modes

```text
r   → Read
w   → Write / overwrite
a   → Append
x   → Create new file
r+  → Read + Write
b   → Binary mode
t   → Text mode
```

Common combinations:

```text
rb  → Read binary
wb  → Write binary
ab  → Append binary

rt  → Read text
wt  → Write text
at  → Append text

rb+ → Read + Write binary
```

---

# 21. Easy Way to Remember

```text
Context Manager
       ↓
     with
       ↓
  Acquire Resource
       ↓
   Use Resource
       ↓
 Automatically Cleanup
```

For files:

```text
with open(...)
        ↓
     Read/Write
        ↓
   File automatically
       closes
```

---

# 22. Context Manager vs Manual Resource Management

### Without Context Manager

```python
file = open("file.txt", "r")

try:
    data = file.read()
finally:
    file.close()
```

### With Context Manager

```python
with open("file.txt", "r") as file:
    data = file.read()
```

The second approach is usually cleaner and safer for resource management.

---

# 23. Important Interview Questions

### Q1. What is a Context Manager?

A context manager is a Python mechanism used to manage resources safely and automatically using the `with` statement.

### Q2. Which keyword is used with a context manager?

```python
with
```

### Q3. Which methods implement the Context Manager Protocol?

```python
__enter__()
__exit__()
```

### Q4. Why use a context manager?

To ensure resources are properly cleaned up, even when an exception occurs.

### Q5. What is `contextlib.contextmanager`?

It is a decorator from Python's `contextlib` module that allows you to create a context manager using a generator function.

### Q6. What is the difference between `w` and `a`?

```text
w → writes and overwrites existing content
a → writes at the end and preserves existing content
```

### Q7. What is the difference between `r` and `r+`?

```text
r  → read only
r+ → read and write
```

### Q8. What does `x` do?

It creates a new file and raises `FileExistsError` if the file already exists.

---

# 24. Final Summary

The key concepts are:

```text
Context Manager
│
├── with
│
├── Resource Management
│   ├── File
│   ├── Database
│   ├── Lock
│   └── Network Connection
│
├── Context Manager Protocol
│   ├── __enter__()
│   └── __exit__()
│
└── contextlib
    └── @contextmanager
```

### Most Important Example

```python
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
```

The main idea is:

```text
Acquire
   ↓
Use
   ↓
Cleanup
```

That is the core purpose of a **Context Manager in Python**.
"""