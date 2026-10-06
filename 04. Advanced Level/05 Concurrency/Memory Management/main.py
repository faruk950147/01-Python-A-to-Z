"""
# Python Memory & Data Structures — Easy English Notes

## Topics

1. Stack
2. Heap
3. Memory
4. Memory Management
5. Call Stack
6. Recursion
7. Garbage Collection
8. Reference Counting
9. Circular Reference
10. Generational Garbage Collection
11. Memory Leak
12. Finalization

---

# 1. Stack

## What is a Stack?

A **Stack** is a linear data structure.

It follows the **LIFO** rule.

**LIFO = Last In, First Out**

This means:

> The last item added to the stack is the first item removed.

### Example

Suppose we add:

```text
Push 10
Push 20
Push 30
```

The stack becomes:

```text
[10]
[20]
[30] ← Top
```

If we call `pop()`:

```text
30
```

will be removed first.

Because `30` was added last.

---

# 2. Stack Operations

There are four common stack operations.

### 1. Push

Adds an item to the top.

```text
Push 10
```

### 2. Pop

Removes the top item.

```text
Pop → 30
```

### 3. Peek / Top

Shows the top item without removing it.

### 4. isEmpty

Checks whether the stack is empty.

---

# 3. Stack in Python

A Python `list` can be used as a stack.

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
```

Output:

```text
[10, 20, 30]
```

Here:

```text
append() → Push
pop()    → Pop
```

### Pop Example

```python
last_item = stack.pop()

print(last_item)
print(stack)
```

Output:

```text
30
[10, 20]
```

---

# 4. How to See the Top Element?

Use:

```python
stack[-1]
```

Example:

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack[-1])
```

Output:

```text
30
```

Important:

```python
stack[-1]
```

only shows the top element.

It does **not** remove it.

---

# 5. Stack Example

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
```

Output:

```text
['A', 'B', 'C']

C
B
A
```

This is LIFO:

```text
Last added  → C
First out   → C
```

---

# 6. Uses of Stack

Stacks are commonly used in:

1. Function calls
2. Recursion
3. Undo/Redo
4. Browser history
5. Expression evaluation
6. Parentheses matching
7. DFS
8. Backtracking

---

# 7. Heap

The word **Heap** can mean two different things in programming.

Here we first discuss the **Heap Data Structure**.

A Heap is a **tree-based data structure**.

It is commonly used for a **Priority Queue**.

There are two main types:

1. Min Heap
2. Max Heap

---

# 8. Min Heap

In a **Min Heap**, the smallest element is at the root.

Example:

```text
       10
      /  \
    20    30
```

Here:

```text
10 = smallest element
```

So:

```text
Min Heap → Smallest element at the top
```

---

# 9. Max Heap

In a **Max Heap**, the largest element is at the root.

Example:

```text
       30
      /  \
    20    10
```

Here:

```text
30 = largest element
```

So:

```text
Max Heap → Largest element at the top
```

---

# 10. Heap in Python

Python provides the `heapq` module.

It provides a **min-heap** implementation.

```python
import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)
```

The smallest element is available at:

```python
heap[0]
```

Example:

```python
print(heap[0])
```

Output:

```text
10
```

---

# 11. Heap Operations

### `heappush()`

Adds an element to the heap.

```python
heapq.heappush(heap, 5)
```

### `heappop()`

Removes and returns the smallest element.

```python
heapq.heappop(heap)
```

### `heap[0]`

Shows the smallest element without removing it.

```python
heap[0]
```

### `heapify()`

Converts a normal list into a heap.

```python
numbers = [30, 10, 20, 5, 40]

heapq.heapify(numbers)

print(numbers)
```

Important:

> A heap is **not a sorted list**.

It only follows the heap property.

---

# 12. Can We Access a Heap?

Yes.

In Python, a heap is stored using a list.

So we can use:

```python
heap[0]
```

to access the root/minimum element of a min-heap.

But arbitrary indexes are **not sorted**.

For example:

```python
heap[1]
heap[2]
```

do not necessarily contain the second and third smallest values.

---

# 13. Memory

## What is Memory?

**Memory** is the storage used by a computer to keep data and instructions while programs are running.

Common types include:

```text
RAM
Cache
SSD/HDD
```

### RAM

RAM is the main working memory used while programs are running.

### SSD/HDD

SSD and HDD are secondary storage.

They keep data even when the computer is turned off.

---

# 14. Python Memory

When Python runs a program, it creates objects in memory.

Example:

```python
x = 10
```

Python creates an integer object representing `10`.

The variable `x` refers to that object.

Conceptually:

```text
x
│
▼
10
```

So we can think:

```text
Variable
   ↓
Reference
   ↓
Object
```

This is an important Python concept.

---

# 15. Memory Management

## What is Memory Management?

**Memory Management** means:

> Allocating, using, and releasing memory during program execution.

Python uses **automatic memory management**.

In languages such as C, programmers often manage memory manually:

```text
malloc()
free()
```

Python normally manages object memory automatically.

---

# 16. Python Memory Management

Python memory management includes several mechanisms:

1. Object allocation
2. Reference counting in CPython
3. Cyclic garbage collection
4. Python's memory allocator

Therefore, Python programmers usually do not need to manually free objects.

---

# 17. Call Stack

The **Call Stack** is a runtime structure used to manage function calls.

It helps Python remember:

1. Which function is running
2. Which function called it
3. Where execution should return

The call stack follows:

```text
LIFO
```

---

# 18. Stack Frame

Every function call creates an **execution frame**.

A frame contains information needed for that function call, such as:

* Local variables
* Function arguments
* Execution state
* Information needed to continue execution

Simple idea:

```text
Function Call
      ↓
New Frame
      ↓
Call Stack
```

---

# 19. Call Stack Example

Consider:

```python
def func_a():
    print("Inside func_a")
    func_b()
    print("Exiting func_a")


def func_b():
    print("Inside func_b")
    func_c()
    print("Exiting func_b")


def func_c():
    print("Inside func_c")


print("Program started")
func_a()
print("Program ended")
```

Output:

```text
Program started
Inside func_a
Inside func_b
Inside func_c
Exiting func_b
Exiting func_a
Program ended
```

---

# 20. Call Stack Flow

At the beginning:

```text
[main]
```

When `func_a()` is called:

```text
[main]
[func_a] ← Top
```

When `func_a()` calls `func_b()`:

```text
[main]
[func_a]
[func_b] ← Top
```

When `func_b()` calls `func_c()`:

```text
[main]
[func_a]
[func_b]
[func_c] ← Top
```

When `func_c()` finishes:

```text
[main]
[func_a]
[func_b] ← Top
```

When `func_b()` finishes:

```text
[main]
[func_a] ← Top
```

When `func_a()` finishes:

```text
[main] ← Top
```

Then the program ends.

---

# 21. Push and Pop in Call Stack

When a function is called:

```text
New frame is added
```

When a function returns:

```text
Its frame is removed
```

So:

```text
Function Call
     ↓
Add Frame

Function Return
     ↓
Remove Frame
```

Easy way to remember:

```text
Call     → Push Frame
Return   → Pop Frame
```

---

# 22. Recursion

## What is Recursion?

**Recursion** means a function calls itself.

Example:

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

Call:

```python
countdown(3)
```

Flow:

```text
countdown(3)
      ↓
countdown(2)
      ↓
countdown(1)
      ↓
countdown(0)
```

After reaching the base case, the functions return one by one.

---

# 23. Recursion and Call Stack

When we call:

```python
countdown(3)
```

The call stack becomes:

```text
[countdown(3)]
```

Then:

```text
[countdown(3)]
[countdown(2)]
```

Then:

```text
[countdown(3)]
[countdown(2)]
[countdown(1)]
```

Then:

```text
[countdown(3)]
[countdown(2)]
[countdown(1)]
[countdown(0)]
```

After the base case, the functions return in reverse order.

This is why recursion uses the call stack.

---

# 24. Recursion Error

Consider:

```python
def infinite_recursion():
    infinite_recursion()
```

There is no stopping condition.

Eventually Python raises:

```text
RecursionError
```

Why?

Because Python has a limit on recursion depth.

Easy rule:

```text
Too much recursion
       ↓
RecursionError
```

---

# 25. Garbage Collection

## What is Garbage Collection?

**Garbage Collection (GC)** is an automatic memory-management system.

It helps Python reclaim memory from objects that are no longer reachable.

Simple idea:

```text
Object is no longer needed
          ↓
Object becomes unreachable
          ↓
Memory can be reclaimed
```

---

# 26. Garbage Collection in CPython

CPython mainly uses:

```text
Reference Counting
        +
Cyclic Garbage Collection
```

These two mechanisms work together.

* Reference counting handles many objects.
* Cyclic GC handles unreachable reference cycles.

---

# 27. Reference Counting

**Reference Counting** keeps track of how many references point to an object.

Example:

```python
a = []
```

Conceptually:

```text
a
│
▼
[]
```

Now:

```python
b = a
```

Conceptually:

```text
a ──┐
    ├──> []
b ──┘
```

Now two variables refer to the same object.

If we do:

```python
del b
```

only the reference from `b` is removed.

`a` still refers to the object.

---

# 28. Reference Count Example

In CPython, we can inspect reference counts using:

```python
import sys

a = []

b = a

print(sys.getrefcount(a))

del b

print(sys.getrefcount(a))
```

Important:

```python
sys.getrefcount()
```

temporarily creates another reference to the object.

So the returned number is usually one higher than the number we expect.

The exact value can change depending on the situation.

---

# 29. What Does `del` Do?

`del` removes a **name/reference**.

It does **not** mean:

> "Run garbage collection now."

Example:

```python
a = []
b = a

del a
```

The object still exists because:

```text
b → object
```

There is still a reference.

Then:

```python
del b
```

removes the second reference.

If there are no other references, CPython can generally reclaim the object through reference counting.

---

# 30. Circular Reference

A **Circular Reference** happens when objects refer to each other in a cycle.

Example:

```text
A → B
B → A
```

Python example:

```python
class Node:

    def __init__(self):
        self.ref = None


a = Node()
b = Node()

a.ref = b
b.ref = a
```

Now:

```text
a → b
b → a
```

This is called a **reference cycle**.

---

# 31. Why Are Circular References Important?

Suppose we remove:

```python
del a
del b
```

The objects can still reference each other.

Conceptually:

```text
Object A → Object B
    ↑          ↓
    └──────────┘
```

There are no external references, but the objects still reference each other.

Reference counting alone cannot remove this cycle.

The **cyclic garbage collector** can find unreachable cycles and reclaim them.

---

# 32. Generational Garbage Collection

Python's cyclic garbage collector uses different generations.

Conceptually:

```text
Generation 0
     ↓
Young objects

Generation 1
     ↓
Objects that survived collection

Generation 2
     ↓
Long-lived objects
```

Main idea:

> Young objects are more likely to become garbage quickly.

So younger generations are checked more often.

---

# 33. GC Threshold

We can see the GC thresholds using:

```python
import gc

print(gc.get_threshold())
```

The exact values depend on the Python version and runtime settings.

---

# 34. Manual Garbage Collection

We can manually request a garbage-collection pass:

```python
import gc

collected = gc.collect()

print("Objects collected:", collected)
```

`gc.collect()` performs garbage collection.

It can be useful when we specifically want to trigger a collection, especially for cyclic garbage.

---

# 35. Enable and Disable GC

Check whether GC is enabled:

```python
import gc

print(gc.isenabled())
```

Disable GC:

```python
gc.disable()
```

Enable GC:

```python
gc.enable()
```

Normally, we should not disable GC unless there is a specific reason.

---

# 36. Finalization

**Finalization** means performing cleanup-related actions when an object is being finalized.

A class can define:

```python
__del__()
```

Example:

```python
class MyClass:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being finalized")
```

Then:

```python
obj = MyClass("Object1")

del obj
```

In simple CPython cases, `__del__()` may run quickly.

However, we should **not depend on its exact timing**.

---

# 37. Why Not Use `__del__()` for Resource Cleanup?

Do not normally use:

```python
__del__()
```

for important resource cleanup such as:

* Closing files
* Closing database connections
* Releasing locks
* Closing network connections

Why?

Because the exact time of finalization is not guaranteed in general Python behavior.

---

# 38. Context Manager

For resource cleanup, use a **context manager**.

Example:

```python
with open("test.txt", "w") as f:
    f.write("Hello Python")
```

When the `with` block finishes, the file is automatically closed.

This is safer and more predictable.

Easy rule:

```text
Resource Cleanup
       ↓
Use with
```

---

# 39. Memory Leak

## What is a Memory Leak?

A **Memory Leak** happens when a program keeps memory that it no longer needs.

In Python, unnecessary references can keep objects alive.

Example:

```python
leaky_list = []


def create_data():
    for i in range(10000):
        leaky_list.append("x" * 1000)


create_data()
```

The objects remain inside:

```python
leaky_list
```

As long as the list exists, those objects are still referenced.

This is an example of **retained memory**.

Real memory leaks can be more complex.

---

# 40. How to Reduce Memory Leaks

Useful practices include:

1. Remove unnecessary references.
2. Avoid very large global lists.
3. Limit cache size.
4. Remove unused callbacks/event listeners.
5. Close files properly.
6. Close database connections.
7. Use context managers.
8. Check long-lived objects that keep references.

---

# 41. Stack vs Heap vs Call Stack

These terms are often confusing.

## Stack Data Structure

A general data structure.

It follows:

```text
LIFO
```

Python example:

```python
stack.append(10)
stack.pop()
```

A Python `list` can be used as a stack.

---

## Heap Data Structure

A tree-based data structure.

Common use:

```text
Priority Queue
```

Python module:

```python
heapq
```

---

## Call Stack

A runtime structure that manages function calls.

It is used for:

* Function execution
* Recursion
* Return flow

---

# 42. Stack Data Structure vs Call Stack

These are not exactly the same thing.

### Stack Data Structure

It is a general data structure.

```text
LIFO
Push
Pop
Peek
```

### Call Stack

It is a runtime mechanism used to manage function calls.

```text
Function Call
     ↓
Stack Frame
     ↓
Call Stack
```

Both follow LIFO behavior, but their purposes are different.

---

# 43. Stack vs Heap Memory

There are also runtime memory concepts:

```text
Call Stack
Heap Memory
```

Do not confuse them with:

```text
Stack Data Structure
Heap Data Structure
```

They are different concepts.

---

# 44. Call Stack

The call stack manages function calls.

Example:

```text
main()
  ↓
function_a()
  ↓
function_b()
  ↓
function_c()
```

The most recent function is at the top.

When a function returns, its frame is removed.

---

# 45. Heap Memory

**Heap memory** is a runtime memory area used for dynamically allocated objects.

Python manages object memory through its memory-management system.

Conceptually:

```text
Variable
   ↓
Python Object
   ↓
Heap-managed Memory
```

Important:

> Heap memory is **not** the same as the Heap data structure.

---

# 46. Heap Data Structure

A Heap data structure is:

```text
Tree-based data structure
```

Common use:

```text
Priority Queue
```

Python example:

```python
import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heapq.heappop(heap))
```

Output:

```text
10
```

---

# 47. Memory Flow

A simple memory flow is:

```text
Program starts
      ↓
Function is called
      ↓
Call stack gets a frame
      ↓
Function creates objects
      ↓
Objects use memory
      ↓
References change/remove
      ↓
Object becomes unreachable
      ↓
Reference Counting / Cyclic GC
      ↓
Memory can be reclaimed
```

---

# 48. Complete Call Stack Example

```python
def a():
    print("A start")
    b()
    print("A end")


def b():
    print("B start")
    c()
    print("B end")


def c():
    print("C running")


print("Program started")

a()

print("Program ended")
```

Execution:

```text
Program started
      ↓
     a()
      ↓
     b()
      ↓
     c()
      ↓
c() returns
      ↓
b() returns
      ↓
a() returns
      ↓
Program ended
```

Call stack:

```text
main
 ↓
a
 ↓
b
 ↓
c
```

Then functions return in reverse order:

```text
c
 ↓
b
 ↓
a
 ↓
main
```

This is LIFO behavior.

---

# 49. Important Exam Points

## Stack

* Linear data structure
* Follows LIFO
* Push adds an item
* Pop removes an item
* Peek/Top shows the top
* Python `list` can be used as a stack

---

## Heap

* Tree-based data structure
* Commonly used for priority queues
* Min Heap → smallest element at root
* Max Heap → largest element at root
* Python `heapq` provides min-heap operations

---

## Call Stack

* Manages active function calls
* Uses stack frames
* Follows LIFO
* Function call → frame added
* Function return → frame removed
* Recursion uses the call stack

---

## Memory

* RAM → primary working memory
* SSD/HDD → secondary storage
* Python automatically manages object memory

---

## Garbage Collection

* Automatic memory-management process
* Helps reclaim unreachable objects
* CPython uses reference counting
* Cyclic GC handles unreachable reference cycles

---

## Reference Counting

* Counts references to objects
* When the count reaches zero, CPython can generally reclaim the object

---

## Circular Reference

* Objects refer to each other
* Example: `A → B` and `B → A`
* Reference counting alone cannot handle unreachable cycles
* Cyclic GC can detect and collect them

---

## Memory Leak

* Unnecessary memory remains retained
* Often caused by unwanted references
* Long-lived objects can keep other objects alive

---

## Finalization

* `__del__()` can participate in object finalization
* Do not depend on it for predictable resource cleanup
* Use context managers instead

---

# 50. Interview Questions

## Q1. What is a Stack?

**Answer:**

A Stack is a linear data structure that follows the **LIFO** principle.

LIFO means **Last In, First Out**.

---

## Q2. How do you implement a Stack in Python?

**Answer:**

We can use a Python list as a stack.

```python
stack.append(10)  # Push
stack.pop()       # Pop
```

---

## Q3. What is a Heap?

**Answer:**

A Heap is a tree-based data structure commonly used to implement a priority queue.

---

## Q4. What is a Min Heap?

**Answer:**

A Min Heap is a heap where the smallest element is at the root.

---

## Q5. What is a Max Heap?

**Answer:**

A Max Heap is a heap where the largest element is at the root.

---

## Q6. What is a Call Stack?

**Answer:**

A Call Stack is a runtime structure that manages active function calls and their return flow.

---

## Q7. What happens when a function is called?

**Answer:**

A new execution frame is created and added to the call stack.

---

## Q8. What happens when a function returns?

**Answer:**

Its frame is removed from the call stack, and execution returns to the previous point.

---

## Q9. What is Recursion?

**Answer:**

Recursion is a technique where a function calls itself.

---

## Q10. What is Garbage Collection?

**Answer:**

Garbage Collection is an automatic memory-management process that helps reclaim memory from unreachable objects.

---

## Q11. What is Reference Counting?

**Answer:**

Reference Counting keeps track of how many references point to an object.

In CPython, when the reference count reaches zero, the object can generally be reclaimed.

---

## Q12. Why can't reference counting alone handle circular references?

**Answer:**

Because objects in a cycle can continue referencing each other even when the cycle is no longer reachable from the program.

---

## Q13. How does Python handle circular references?

**Answer:**

CPython has a cyclic garbage collector that can detect and collect unreachable reference cycles.

---

## Q14. What does `gc.collect()` do?

**Answer:**

It manually requests a garbage-collection pass.

---

## Q15. What is a Memory Leak?

**Answer:**

A memory leak is a situation where memory remains unnecessarily retained, so memory usage stays higher than needed.

---

## Q16. Should `__del__()` be used for file cleanup?

**Answer:**

No.

Use a context manager such as the `with` statement for predictable resource cleanup.

---

# 51. Final Summary

```text
STACK
  ↓
LIFO Data Structure

HEAP
  ↓
Tree-based Data Structure
Used for Priority Queues

CALL STACK
  ↓
Manages Function Calls

RECURSION
  ↓
Function Calls Itself
Uses Call Stack

MEMORY
  ↓
Stores Data Used by Programs

MEMORY MANAGEMENT
  ↓
Allocates and Reclaims Memory

REFERENCE COUNTING
  ↓
Counts References to Objects

GARBAGE COLLECTION
  ↓
Helps Reclaim Unreachable Objects

CIRCULAR REFERENCE
  ↓
Objects Reference Each Other

GENERATIONAL GC
  ↓
Groups Objects by Age

MEMORY LEAK
  ↓
Unnecessary Memory Remains Retained

FINALIZATION
  ↓
Cleanup-related Actions During Object Finalization
```

# One-Line Definitions

### Stack

> A Stack is a LIFO-based linear data structure.

### Heap

> A Heap is a tree-based data structure commonly used for priority queues.

### Call Stack

> A Call Stack manages active function calls and their return flow.

### Memory

> Memory is the storage used by a computer while programs are running.

### Memory Management

> Memory Management handles memory allocation, use, and reclamation.

### Recursion

> Recursion is when a function calls itself.

### Garbage Collection

> Garbage Collection helps reclaim memory from unreachable objects.

### Reference Counting

> Reference Counting tracks how many references point to an object.

### Circular Reference

> A Circular Reference happens when objects reference each other in a cycle.

### Memory Leak

> A Memory Leak happens when memory remains unnecessarily retained.

### Finalization

> Finalization is the cleanup-related process associated with an object being finalized.

---

# Most Important Concept

Remember this flow:

```text
Function Call
     ↓
Call Stack
     ↓
Stack Frame
     ↓
Function Creates Objects
     ↓
Objects Use Memory
     ↓
References Are Added/Removed
     ↓
Object Becomes Unreachable
     ↓
Reference Counting / Cyclic GC
     ↓
Memory Can Be Reclaimed
```

## Very Important Difference

Never confuse these concepts:

```text
Stack Data Structure
        ≠
Call Stack
        ≠
Stack Memory
```

and:

```text
Heap Data Structure
        ≠
Heap Memory
```

They have similar names, but they are **different concepts**.

"""