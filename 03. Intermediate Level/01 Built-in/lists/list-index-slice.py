'''
# ===================== what is slice =====================
"""
Python Slice
1. What is slice?

slice is a built-in Python function that creates a slice object.

A slice is used to extract a portion of a sequence such as:

string
list
tuple
range
Syntax
slice(start, stop, step)

You can also use:

slice(start, stop)

or

slice(stop)
Example
s = "Hello World"

x = slice(0, 5)

print(s[x])

Output:

Hello

The same operation can usually be written using slicing syntax:

print(s[0:5])
2. Slicing Syntax

The most common syntax is:

sequence[start:stop:step]

For example:

tup[2:8:2]

Meaning:

start = 2
stop  = 8
step  = 2

Python starts at index 2, moves by 2, and stops before index 8.

3. Important Rule: stop is Exclusive

This is one of the most important rules of slicing.

tup[start:stop]

means:

start included
stop excluded

For example:

tup = ("h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d")

print(tup[2:7])

Indexes:

       0    1    2    3    4    5    6    7    8    9   10
       h    e    l    l    o         w    o    r    l    d

2:7 gives:

2, 3, 4, 5, 6

Output:

('l', 'l', 'o', ' ', 'w')

Index 7 is not included.

4. Positive and Negative Index

Given:

tup = ("h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d")

The indexes are:

Positive:   0    1    2    3    4    5    6    7    8    9   10
            h    e    l    l    o         w    o    r    l    d

Negative: -11  -10   -9   -8   -7   -6   -5   -4   -3   -2   -1
            h    e    l    l    o         w    o    r    l    d
Positive index

Positive indexing starts from:

0

from the left.

tup[0]   # h
tup[1]   # e
tup[10]  # d
Negative index

Negative indexing starts from:

-1

from the right.

tup[-1]   # d
tup[-2]   # l
tup[-11]  # h
5. step

step determines how many positions Python moves at a time.

sequence[start:stop:step]

For example:

tup[0:10:2]

Indexes selected:

0 → 2 → 4 → 6 → 8

Output:

('h', 'l', 'o', 'w', 'r')
Step = 1
tup[0:5:1]
0 → 1 → 2 → 3 → 4
Step = 2
tup[0:10:2]
0 → 2 → 4 → 6 → 8
Step = 3
tup[0:10:3]
0 → 3 → 6 → 9
6. Positive Slice

A positive slice has a positive step.

step > 0

It moves:

LEFT → RIGHT

Example:

tup[2:9:1]

Indexes:

2 → 3 → 4 → 5 → 6 → 7 → 8

Result:

('l', 'l', 'o', ' ', 'w', 'o', 'r')

Another example:

tup[0:11:2]

Indexes:

0 → 2 → 4 → 6 → 8 → 10

Result:

('h', 'l', 'o', 'w', 'r', 'd')
7. Negative Slice

A negative slice has:

step < 0

Therefore, it moves:

RIGHT → LEFT

For example:

tup[10:5:-1]

Indexes:

10 → 9 → 8 → 7 → 6

Result:

('d', 'l', 'r', 'o', 'w')

Notice again:

stop = 5

Index 5 is not included.

8. Negative Slice with Negative Index

You can also use negative indexes:

tup[-1:-6:-1]

Let's follow it:

-1 → -2 → -3 → -4 → -5

Result:

('d', 'l', 'r', 'o', 'w')

The direction is:

RIGHT → LEFT
9. Very Important: Step Determines Direction

Remember this rule:

step > 0  → LEFT → RIGHT
step < 0  → RIGHT → LEFT

For example:

tup[2:8:1]

moves:

2 → 3 → 4 → 5 → 6 → 7

But:

tup[8:2:-1]

moves:

8 → 7 → 6 → 5 → 4 → 3
10. Why tup[2:8:-1] Doesn't Work

This is an important concept.

tup[2:8:-1]

does not produce a reverse slice.

Why?

Because:

start = 2
stop  = 8
step  = -1

A negative step means:

RIGHT → LEFT

But 2 → 8 requires:

LEFT → RIGHT

The direction and indexes conflict.

Therefore:

tup[2:8:-1]

returns:

()

For reverse slicing, the start should generally be greater than the stop:

tup[8:2:-1]
11. Omitting start, stop, and step

You can leave parts empty.

[:stop]

Start from the beginning.

tup[:5]

Indexes:

0 → 1 → 2 → 3 → 4
[start:]

Go from start to the end.

tup[5:]
[:]

Copy/extract the entire sequence.

tup[:]
[::step]

Use a step over the entire sequence.

tup[::2]

Result:

('h', 'l', 'o', 'w', 'r', 'd')
12. Reverse a Sequence

One of the most useful slicing techniques:

tup[::-1]

This means:

start = default
stop  = default
step  = -1

Therefore, Python traverses the entire tuple from:

RIGHT → LEFT

Result:

('d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h')

This also works with strings:

s = "hello"

print(s[::-1])

Output:

olleh
13. slice() Function vs Slice Syntax

These two are closely related:

Slice syntax
tup[2:8:2]
slice() object
x = slice(2, 8, 2)

print(tup[x])

Both produce:

('l', 'o', 'w')

You can think of:

tup[2:8:2]

as applying a slice directly, while:

slice(2, 8, 2)

creates the slice object first.

14. Quick Cheat Sheet
sequence[start:stop:step]
Syntax	Meaning
a[:]	entire sequence
a[2:]	index 2 → end
a[:5]	beginning → before 5
a[2:8]	2 → before 8
a[::2]	every 2nd element
a[::-1]	reverse
a[8:2:-1]	8 → before 2, right → left
a[-1:]	last element onward
a[:-1]	everything except last
a[-1:-6:-1]	reverse using negative indexes
Golden Rules
1. start is usually INCLUDED.
2. stop is always EXCLUDED.
3. step determines the jump.
4. step > 0 → LEFT → RIGHT.
5. step < 0 → RIGHT → LEFT.
6. Negative index starts from -1 at the right.
7. For reverse slicing, start normally needs to be to the right of stop.

Your original definition of negative index should be slightly corrected: the -1, -2, etc. 
are negative indexes, but stop is not itself “the index of the element after the last extracted element” 
in a simple universal sense. The safest rule is: stop is the boundary where slicing stops, and that index 
is excluded; with a negative step, Python moves toward smaller indexes and stops before reaching stop.
"""

=========================================================================
# Python List Indexing & Slicing

## 1. List Indexing

**Indexing** is the process of accessing a **single element** from a list using its index.

### Syntax

```python
list[index]
```

### Example

```python
lst = [10, 20, 30, 40, 50, 60]

print(lst[0])
print(lst[2])
print(lst[5])
```

### Output

```text
10
30
60
```

### Index Positions

```text
List:      [10, 20, 30, 40, 50, 60]
Index:       0   1   2   3   4   5
```

Therefore:

```python
lst[0]  # 10
lst[1]  # 20
lst[2]  # 30
lst[3]  # 40
lst[4]  # 50
lst[5]  # 60
```

---

# 2. Indexing with a Loop

We can use a `for` loop to access every element of a list.

```python
lst = [10, 20, 30, 40, 50, 60]

for i in range(len(lst)):
    print(lst[i])
```

### Output

```text
10
20
30
40
50
60
```

Here:

```python
lst[i]
```

returns **one element at a time**.

```text
i = 0 → lst[0] → 10
i = 1 → lst[1] → 20
i = 2 → lst[2] → 30
i = 3 → lst[3] → 40
i = 4 → lst[4] → 50
i = 5 → lst[5] → 60
```

This is called **List Indexing**.

---

# 3. List Slicing

**Slicing** is the process of extracting a **part of a list**.

### Syntax

```python
list[start:end]
```

* `start` → starting index
* `end` → ending boundary
* The `end` index is **not included**

### Example

```python
lst = [10, 20, 30, 40, 50, 60]

print(lst[1:4])
```

### Output

```text
[20, 30, 40]
```

Because:

```text
Index:   0   1   2   3   4   5
Value:  10  20  30  40  50  60
             ↑       ↑
           start     end
```

`lst[1:4]` includes indexes:

```text
1, 2, 3
```

but not index `4`.

---

# 4. `lst[:i]` — Prefix Slicing

```python
lst[:i]
```

means:

> Take elements from the beginning up to, but not including, index `i`.

### Example

```python
lst = [10, 20, 30, 40, 50, 60]

for i in range(len(lst)):
    print(lst[:i])
```

### Output

```text
[]
[10]
[10, 20]
[10, 20, 30]
[10, 20, 30, 40]
[10, 20, 30, 40, 50]
```

### Step-by-step

```text
i = 0 → lst[:0] → []
i = 1 → lst[:1] → [10]
i = 2 → lst[:2] → [10, 20]
i = 3 → lst[:3] → [10, 20, 30]
i = 4 → lst[:4] → [10, 20, 30, 40]
i = 5 → lst[:5] → [10, 20, 30, 40, 50]
```

This is **slicing**, not indexing.

---

# 5. `lst[i:]` — Suffix Slicing

```python
lst[i:]
```

means:

> Take elements from index `i` to the end of the list.

### Example

```python
lst = [10, 20, 30, 40, 50, 60]

for i in range(len(lst)):
    print(lst[i:])
```

### Output

```text
[10, 20, 30, 40, 50, 60]
[20, 30, 40, 50, 60]
[30, 40, 50, 60]
[40, 50, 60]
[50, 60]
[60]
```

---

# 6. Indexing vs Slicing

| Code       | Name           | Result                |
| ---------- | -------------- | --------------------- |
| `lst[i]`   | Indexing       | One element           |
| `lst[i:j]` | Slicing        | A part of the list    |
| `lst[:i]`  | Prefix Slicing | From beginning to `i` |
| `lst[i:]`  | Suffix Slicing | From `i` to the end   |

### Example

```python
lst = [10, 20, 30, 40, 50, 60]

print(lst[2])
print(lst[2:5])
```

Output:

```text
30
[30, 40, 50]
```

So:

```python
lst[2]
```

→ **Indexing**

```python
lst[2:5]
```

→ **Slicing**

---

# 7. Negative Indexing

Python also supports indexing from the end of a list.

```text
Value:       10   20   30   40   50   60
Positive:     0    1    2    3    4    5
Negative:    -6   -5   -4   -3   -2   -1
```

### Example

```python
lst = [10, 20, 30, 40, 50, 60]

print(lst[-1])
print(lst[-2])
print(lst[-6])
```

### Output

```text
60
50
10
```

---

# 8. Slicing with Step

The complete slicing syntax is:

```python
list[start:end:step]
```

### Example

```python
lst = [10, 20, 30, 40, 50, 60]

print(lst[0:6:2])
```

### Output

```text
[10, 30, 50]
```

Here:

```text
start = 0
end   = 6
step  = 2
```

So every second element is selected.

---

# 9. Reverse a List Using Slicing

```python
lst = [10, 20, 30, 40, 50, 60]

print(lst[::-1])
```

### Output

```text
[60, 50, 40, 30, 20, 10]
```

`[::-1]` reverses the list using slicing.

---

# 10. Most Important Difference

### Indexing

```python
lst[i]
```

Returns **one element**.

```python
lst[2]
# 30
```

### Slicing

```python
lst[i:j]
```

Returns a **new list containing multiple elements**.

```python
lst[2:5]
# [30, 40, 50]
```

---

# Quick Revision

```text
lst[i]
    ↓
Indexing
    ↓
One element


lst[i:j]
    ↓
Slicing
    ↓
Part of a list


lst[:i]
    ↓
From the beginning to i-1


lst[i:]
    ↓
From i to the end


lst[::-1]
    ↓
Reverse the list
```

## Shortcut

```text
[]     → Indexing
[:]    → Slicing
```

### Remember

> **Indexing = Access one element**
>
> **Slicing = Extract a part of a list**

'''
