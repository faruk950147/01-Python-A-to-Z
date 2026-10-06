# =====================================================================

# PYTHON MEMORY & DATA STRUCTURES

# =====================================================================

#

# Topics:

#

# 1. Stack

# 2. Heap

# 3. Memory

# 4. Memory Management

# 5. Call Stack

# 6. Recursion

# 7. Garbage Collection

# 8. Reference Counting

# 9. Circular Reference

# 10. Generational Garbage Collection

# 11. Memory Leak

# 12. Finalization

#

# =====================================================================

# =====================================================================

# 1. STACK

# =====================================================================

# ============================= WHAT IS STACK ==========================

# A Stack is a linear data structure that follows the LIFO principle.

#

# LIFO = Last In, First Out

#

# This means:

#

# The element that is inserted into the stack last

# will be removed first.

#

#

# Example:

#

# Push 10

# Push 20

# Push 30

#

# Stack:

#

# [10]

# [20]

# [30]  <- Top

#

# If we perform pop:

#

# 30 will be removed.

#

# Because 30 was inserted last.

#

# =====================================================================

# ============================= STACK OPERATIONS =======================

# Main stack operations:

#

# Push

# -> Adds a new element to the top of the stack.

#

# Pop

# -> Removes the element from the top of the stack.

#

# Peek / Top

# -> Returns the top element without removing it.

#

# isEmpty

# -> Checks whether the stack is empty.

#

# =====================================================================

# ============================= STACK IN PYTHON ========================

# In Python, a list can easily be used to implement a stack.

#

# append() -> Push

# pop()    -> Pop

#

# =====================================================================

# Example:

stack = []

# Push

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop

last_item = stack.pop()

print("Popped item:", last_item)
print("Stack after pop:", stack)

# Output:

#

# Stack: [10, 20, 30]

# Popped item: 30

# Stack after pop: [10, 20]

#

# =====================================================================

# ============================= STACK TOP ==============================

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

# To view the top element:

#

# stack[-1]

print("Top:", stack[-1])

# Output:

#

# Top: 30

#

# The element is not removed.

#

# =====================================================================

# ============================= STACK EXAMPLE ==========================

stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

# Output:

#

# ['A', 'B', 'C']

# C

# B

# A

#

# This demonstrates LIFO behavior.

#

# =====================================================================

# ============================= STACK USES =============================

# Stack is commonly used for:

#

# 1. Function calls

# 2. Recursion

# 3. Undo/Redo operations

# 4. Browser history

# 5. Expression evaluation

# 6. Parentheses matching

# 7. Depth First Search (DFS)

# 8. Backtracking

#

# =====================================================================

# =====================================================================

# 2. HEAP

# =====================================================================

# ============================= WHAT IS HEAP ===========================

# A Heap is a tree-based data structure.

#

# It is commonly used to implement a Priority Queue.

#

# There are two main types of heaps:

#

# 1. Min Heap

# 2. Max Heap

#

# =====================================================================

# ============================= MIN HEAP ===============================

# In a Min Heap, the smallest element is at the root/top.

#

# Example:

#

# 10

# /    \

# 20     30

#

# Here, 10 is the minimum element.

#

# =====================================================================

# ============================= MAX HEAP ===============================

# In a Max Heap, the largest element is at the root/top.

#

# Example:

#

# 30

# /    \

# 20     10

#

# Here, 30 is the maximum element.

#

# =====================================================================

# ============================= HEAP IN PYTHON =========================

# Python's heapq module is commonly used to implement a min-heap.

import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print("Heap:", heap)

smallest = heapq.heappop(heap)

print("Smallest item:", smallest)
print("Heap after pop:", heap)

# The internal order of a heap does not have to look like a sorted list.

#

# Important:

#

# The main property of a min-heap is that the smallest element

# is always at heap[0].

#

# =====================================================================

# ============================= HEAP OPERATIONS ========================

# heappush()

# -> Adds an element to the heap.

#

#

# heappop()

# -> Removes and returns the smallest element.

#

#

# heap[0]

# -> Accesses the smallest element of a min-heap.

#

#

# heapify()

# -> Converts an existing list into a heap.

#

# =====================================================================

# Example:

numbers = [30, 10, 20, 5, 40]

heapq.heapify(numbers)

print(numbers)

print("Minimum:", numbers[0])

print("Pop:", heapq.heappop(numbers))

# =====================================================================

# ============================= HEAP ACCESS =============================

# Saying "you cannot directly access a heap" is technically incorrect.

#

# Python's heap is implemented on top of a list.

#

# Therefore:

#

# heap[0]

#

# can be used to access the root/minimum element.

#

# However, accessing an arbitrary index does not give elements

# in sorted order.

#

# The main heap operations are:

#

# - heappush()

# - heappop()

# - heap[0]

#

# =====================================================================

# =====================================================================

# 3. MEMORY

# =====================================================================

# ============================= WHAT IS MEMORY =========================

# Memory is a storage area of a computer where data and instructions

# are stored while a program is executing.

#

#

# Major types of memory/storage include:

#

# 1. RAM

# 2. Cache

# 3. Secondary Storage

#

#

# RAM:

# -> Primary working memory actively used during program execution.

#

#

# SSD / HDD:

# -> Secondary storage.

#

# =====================================================================

# ============================= PYTHON MEMORY ==========================

# During program execution, Python allocates memory for objects.

#

# Example:

#

# x = 10

#

# Here, Python creates an integer object and x refers to that object.

#

# =====================================================================

x = 10

print(x)

# =====================================================================

# =====================================================================

# 4. MEMORY MANAGEMENT

# =====================================================================

# ============================= WHAT IS MEMORY MANAGEMENT ==============

# Memory Management is the process of allocating, using,

# and reclaiming memory for a program.

#

# Python uses automatic memory management.

#

# Programmers generally do not need to manually perform operations

# such as:

#

# malloc()

# free()

#

# as they commonly do in C/C++.

#

# =====================================================================

# ============================= PYTHON MEMORY MANAGEMENT ===============

# Python memory management includes:

#

# 1. Object allocation

# 2. Reference counting (CPython)

# 3. Cyclic garbage collection

# 4. Python memory allocator

#

# =====================================================================

# =====================================================================

# 5. CALL STACK

# =====================================================================

# ============================= WHAT IS CALL STACK =====================

# The Call Stack is a runtime stack structure used to track

# active function calls during program execution.

#

# It helps Python keep track of:

#

# 1. Which function is currently executing.

# 2. Which function called it.

# 3. Where execution should return after the function finishes.

#

# =====================================================================

# ============================= CALL STACK PRINCIPLE ===================

# The Call Stack follows:

#

# LIFO = Last In, First Out

#

# This means the most recently called function returns first.

#

# =====================================================================

# ============================= STACK FRAME ============================

# Each function call creates an execution frame.

#

# A frame contains information required for the function's execution,

# such as:

#

# - Local variables

# - Function arguments

# - Execution state

# - Return information

#

# =====================================================================

# ============================= CALL STACK EXAMPLE =====================

def func_a():

```
print("Inside func_a")

func_b()

print("Exiting func_a")
```

def func_b():

```
print("Inside func_b")

func_c()

print("Exiting func_b")
```

def func_c():

```
print("Inside func_c")
```

print("Program started")

func_a()

print("Program ended")

# Output:

#

# Program started

# Inside func_a

# Inside func_b

# Inside func_c

# Exiting func_b

# Exiting func_a

# Program ended

#

# =====================================================================

# ============================= CALL STACK FLOW ========================

# Program starts:

#

# [ main ]

#

#

# main -> func_a()

#

# [ main ]

# [ func_a ]       <- Top

#

#

# func_a -> func_b()

#

# [ main ]

# [ func_a ]

# [ func_b ]       <- Top

#

#

# func_b -> func_c()

#

# [ main ]

# [ func_a ]

# [ func_b ]

# [ func_c ]       <- Top

#

#

# func_c() finishes:

#

# [ main ]

# [ func_a ]

# [ func_b ]       <- Top

#

#

# func_b() finishes:

#

# [ main ]

# [ func_a ]       <- Top

#

#

# func_a() finishes:

#

# [ main ]         <- Top

#

#

# Program ends:

#

# [ empty ]

#

# =====================================================================

# ============================= PUSH / POP =============================

# Function call:

# -> A stack frame is added/pushed.

#

#

# Function return:

# -> The stack frame is removed/popped.

#

# =====================================================================

# =====================================================================

# 6. RECURSION

# =====================================================================

# ============================= WHAT IS RECURSION ======================

# Recursion is a technique in which a function calls itself.

#

# =====================================================================

def countdown(n):

```
if n == 0:
    return

print(n)

countdown(n - 1)
```

countdown(3)

# Call flow:

#

# countdown(3)

# |

# v

# countdown(2)

# |

# v

# countdown(1)

# |

# v

# countdown(0)

#

#

# Then the functions start returning.

#

# =====================================================================

# ============================= RECURSION + CALL STACK ================

# countdown(3)

#

# Stack:

#

# [ countdown(3) ]

#

#

# countdown(2)

#

# [ countdown(3) ]

# [ countdown(2) ]

#

#

# countdown(1)

#

# [ countdown(3) ]

# [ countdown(2) ]

# [ countdown(1) ]

#

#

# countdown(0)

#

# [ countdown(3) ]

# [ countdown(2) ]

# [ countdown(1) ]

# [ countdown(0) ]

#

#

# Then the functions return in reverse order.

#

# =====================================================================

# =====================================================================

# 7. STACK OVERFLOW / RECURSION ERROR

# =====================================================================

# Infinite recursion:

def infinite_recursion():

```
infinite_recursion()
```

# infinite_recursion()

#

# If this is executed, Python will eventually raise:

#

# RecursionError

#

# because the recursion depth limit is exceeded.

#

# =====================================================================

# =====================================================================

# 8. GARBAGE COLLECTION

# =====================================================================

# ============================= WHAT IS GARBAGE COLLECTION =============

# Garbage Collection is a process of automatic memory management

# that helps reclaim memory from unreachable objects.

#

# In simple terms:

#

# Objects that are no longer reachable by the program can have

# their memory reclaimed for reuse.

#

# =====================================================================

# ============================= PYTHON GC ==============================

# CPython's memory management mainly involves:

#

# 1. Reference Counting

# 2. Cyclic Garbage Collection

#

# Both play important roles in memory management.

#

# =====================================================================

# ============================= REFERENCE COUNTING =====================

# Reference Counting is a mechanism that tracks how many references

# point to an object.

#

# When an object's reference count reaches zero, CPython can generally

# reclaim the object's memory.

#

# =====================================================================

# ============================= REFERENCE COUNT EXAMPLE ================

import sys

a = []

b = a

print("Reference count:", sys.getrefcount(a))

del b

print("After deleting b:", sys.getrefcount(a))

# IMPORTANT:

#

# sys.getrefcount() itself creates a temporary reference.

#

# Therefore, the returned value is usually one greater than the

# number of visible references.

#

# The exact value can vary depending on the implementation and context.

#

# =====================================================================

# ============================= DEL KEYWORD ============================

# The del statement removes a variable reference.

#

# It does NOT directly mean "run the garbage collector".

#

# Example:

a = []

b = a

del a

# The object is still referenced by b.

#

# Therefore, the object is still reachable.

#

#

# After:

#

# del b

#

# both variable references are removed.

#

# =====================================================================

# =====================================================================

# 9. CIRCULAR REFERENCE

# =====================================================================

# ============================= WHAT IS CIRCULAR REFERENCE =============

# A circular reference occurs when two or more objects reference

# each other.

#

#

# Example:

#

# A -> B

# B -> A

#

# =====================================================================

class Node:

```
def __init__(self):

    self.ref = None
```

a = Node()
b = Node()

a.ref = b
b.ref = a

# Now:

#

# a -> b

# b -> a

#

# This is a reference cycle.

#

# Reference counting alone cannot collect these objects if the cycle

# is unreachable.

#

# Python's cyclic garbage collector can detect and collect

# such unreachable cycles.

#

# =====================================================================

# =====================================================================

# 10. GENERATIONAL GARBAGE COLLECTION

# =====================================================================

# Python's cyclic garbage collector tracks objects using generations.

#

#

# Generation 0:

# -> Newly created objects

#

# Generation 1:

# -> Objects that survive a collection

#

# Generation 2:

# -> Objects that survive for a longer period

#

#

# General idea:

#

# Young objects are more likely to become garbage quickly.

#

# Therefore, younger generations are checked more frequently.

#

# =====================================================================

# ============================= GC THRESHOLD ============================

import gc

print("GC thresholds:", gc.get_threshold())

# get_threshold() returns the garbage collector's thresholds.

#

# =====================================================================

# ============================= MANUAL GC ===============================

import gc

collected = gc.collect()

print("Objects collected:", collected)

# gc.collect()

#

# Can manually trigger garbage collection.

#

# It is particularly useful for triggering collection of cyclic garbage.

#

# =====================================================================

# ============================= GC ENABLE / DISABLE =====================

import gc

print("GC enabled:", gc.isenabled())

# Disable:

#

# gc.disable()

#

#

# Enable:

#

# gc.enable()

#

# =====================================================================

# =====================================================================

# 11. FINALIZATION

# =====================================================================

# ============================= WHAT IS FINALIZATION ====================

# Finalization refers to performing cleanup-related actions

# when an object is being finalized.

#

# A Python class can define the **del**() method.

#

# However, **del**() should not be treated as a reliable mechanism

# for deterministic resource cleanup.

#

# =====================================================================

# ============================= **del** EXAMPLE ========================

class MyClass:

```
def __init__(self, name):

    self.name = name

def __del__(self):

    print(f"{self.name} is being finalized")
```

obj = MyClass("Object1")

del obj

# In CPython, in a simple reference-counting situation,

# **del**() may be called quickly.

#

# However, code should not depend on its exact timing for

# resource cleanup.

#

# =====================================================================

# =====================================================================

# 12. RESOURCE CLEANUP

# =====================================================================

# Instead of using **del**() for file cleanup,

# use a context manager.

#

# Example:

with open("test.txt", "w") as f:

```
f.write("Hello Python")
```

# When the with block ends, the file is automatically closed.

#

# This is the recommended approach for file/resource management.

#

# =====================================================================

# =====================================================================

# 13. MEMORY LEAK

# =====================================================================

# ============================= WHAT IS MEMORY LEAK =====================

# A memory leak generally refers to a situation where a program

# retains memory that is no longer needed, causing memory usage

# to grow or remain higher than necessary.

#

# Even though Python has garbage collection, unnecessary references

# can keep objects alive in memory.

#

# =====================================================================

# ============================= MEMORY LEAK EXAMPLE ====================

leaky_list = []

def create_data():

```
for i in range(10000):

    leaky_list.append("x" * 1000)
```

create_data()

print("Objects are still referenced by leaky_list.")

# Here, the objects are stored inside leaky_list.

#

# Therefore, as long as the list remains alive, the stored objects

# remain referenced.

#

# This is a simplified example of retained memory.

#

# Real-world memory leaks can be more complex.

#

# =====================================================================

# ============================= HOW TO AVOID MEMORY LEAK ===============

# 1. Remove unnecessary references.

#

# 2. Avoid unnecessarily large global lists.

#

# 3. Control the size of caches.

#

# 4. Properly remove event listeners / callbacks.

#

# 5. Properly close open files.

#

# 6. Properly close database connections.

#

# 7. Use context managers.

#

# 8. Review references held by long-lived objects.

#

# =====================================================================

# =====================================================================

# 14. STACK vs HEAP vs CALL STACK

# =====================================================================

# STACK:

#

# General data structure.

#

# Principle:

# LIFO

#

# Python:

# Can be implemented using a list.

#

# Uses:

# Push, pop, undo, DFS, etc.

#

#

# HEAP:

#

# Tree-based data structure.

#

# Common use:

# Priority Queue

#

# Python:

# heapq

#

#

# CALL STACK:

#

# Runtime structure used to manage function calls.

#

# Principle:

# LIFO

#

# Uses:

# Function execution

# Recursion

# Return flow

#

# =====================================================================

# =====================================================================

# 15. STACK vs HEAP MEMORY

# =====================================================================

# There is an important distinction:

#

# The terms "Stack" and "Heap" are used in different contexts.

#

#

# 1. Stack Data Structure

# 2. Heap Data Structure

#

# In programming language/runtime contexts:

#

# 3. Call Stack

# 4. Heap Memory

#

#

# These are not the same concepts.

#

# =====================================================================

# ============================= CALL STACK =============================

# Call Stack:

# -> A runtime structure used for function execution.

#

# -> Manages function calls and returns.

#

# -> Follows LIFO behavior.

#

# =====================================================================

# ============================= HEAP MEMORY ============================

# Heap Memory:

# -> A runtime memory area generally used for dynamically allocated

# objects.

#

# Python objects are generally allocated in memory managed by Python's

# object allocator, conceptually associated with heap memory.

#

# This is different from the "heap data structure".

#

# =====================================================================

# =====================================================================

# 16. HEAP DATA STRUCTURE

# =====================================================================

# Heap Data Structure:

#

# A tree-based data structure.

#

# Commonly used for:

#

# Priority Queue

#

#

# Example:

#

# import heapq

#

# heap = []

#

# heapq.heappush(heap, 30)

# heapq.heappush(heap, 10)

# heapq.heappush(heap, 20)

#

# print(heapq.heappop(heap))

#

# Output:

#

# 10

#

# =====================================================================

# =====================================================================

# 17. MEMORY FLOW

# =====================================================================

# Program starts

# |

# v

# Function call

# |

# v

# Call Stack

# |

# v

# Function creates objects

# |

# v

# Objects occupy memory

# |

# v

# References change/remove

# |

# v

# Object becomes unreachable

# |

# v

# Reference counting / cyclic GC

# |

# v

# Memory can be reclaimed

#

# =====================================================================

# =====================================================================

# 18. COMPLETE CALL STACK EXAMPLE

# =====================================================================

def a():

```
print("A start")

b()

print("A end")
```

def b():

```
print("B start")

c()

print("B end")
```

def c():

```
print("C running")
```

print("Program started")

a()

print("Program ended")

# Execution:

#

# Program started

#

# |

# v

#

# a()

#

# |

# v

#

# b()

#

# |

# v

#

# c()

#

# |

# v

#

# c() returns

#

# |

# v

#

# b() returns

#

# |

# v

#

# a() returns

#

# |

# v

#

# Program ended

#

# =====================================================================

# =====================================================================

# 19. IMPORTANT EXAM POINTS

# =====================================================================

# STACK:

#

# - Linear data structure

# - LIFO

# - Push

# - Pop

# - Top

# - Python list can implement a stack

#

#

# HEAP:

#

# - Tree-based data structure

# - Used for priority queues

# - Min Heap / Max Heap

# - Python heapq provides min-heap operations

#

#

# CALL STACK:

#

# - Tracks active function calls

# - Uses stack frames

# - LIFO

# - Function call -> frame added

# - Function return -> frame removed

# - Recursion uses the call stack

#

#

# MEMORY:

#

# - RAM is primary working memory

# - SSD/HDD are secondary storage

# - Python manages object memory automatically

#

#

# GARBAGE COLLECTION:

#

# - Automatic memory management

# - Helps reclaim unreachable objects

# - CPython uses reference counting

# - Cyclic GC handles unreachable reference cycles

#

#

# REFERENCE COUNTING:

#

# - Tracks references to objects

# - Zero references -> CPython can generally reclaim memory

#

#

# CIRCULAR REFERENCE:

#

# - Objects reference each other

# - Reference counting alone cannot resolve the cycle

# - Cyclic GC can detect unreachable cycles

#

#

# MEMORY LEAK:

#

# - Unnecessary memory remains retained

# - Often caused by unwanted references

#

#

# FINALIZATION:

#

# - **del**() can participate in object finalization

# - Not recommended for deterministic resource cleanup

#

# =====================================================================

# =====================================================================

# 20. INTERVIEW QUESTIONS

# =====================================================================

# Q1. What is a Stack?

#

# Answer:

# A Stack is a linear data structure that follows LIFO

# (Last In, First Out).

# Q2. How can you implement a Stack in Python?

#

# Answer:

# A Python list can be used as a stack using append() and pop().

# Q3. What is a Heap?

#

# Answer:

# A Heap is a tree-based data structure commonly used to implement

# priority queues.

# Q4. What is a Min Heap?

#

# Answer:

# A Min Heap keeps the smallest element at the root.

# Q5. What is a Call Stack?

#

# Answer:

# A Call Stack is a runtime stack structure used to track active

# function calls and their execution/return flow.

# Q6. What happens when a function is called?

#

# Answer:

# A new execution frame is created for that function call and

# added to the call stack.

# Q7. What happens when a function returns?

#

# Answer:

# Its frame is removed from the call stack and control returns

# to the previous execution point.

# Q8. What is Recursion?

#

# Answer:

# Recursion is a technique where a function calls itself.

# Q9. What is Garbage Collection?

#

# Answer:

# Garbage Collection is an automatic memory-management process

# that helps reclaim memory from unreachable objects.

# Q10. What is Reference Counting?

#

# Answer:

# Reference counting tracks the number of references to an object.

# In CPython, when that count reaches zero, the object's memory

# can generally be reclaimed.

# Q11. Why can't Reference Counting alone handle circular references?

#

# Answer:

# Because objects in a cycle can keep references to each other even

# when the cycle is unreachable from the program.

# Q12. How does Python handle circular references?

#

# Answer:

# CPython has a cyclic garbage collector that can detect and

# collect unreachable reference cycles.

# Q13. What does gc.collect() do?

#

# Answer:

# It manually triggers garbage collection.

# Q14. What is a Memory Leak?

#

# Answer:

# A memory leak is a situation where memory remains unnecessarily

# retained, causing memory usage to grow or remain higher than needed.

# Q15. Is **del**() recommended for file cleanup?

#

# Answer:

# No. Use context managers such as the 'with' statement for

# deterministic resource cleanup.

#

# =====================================================================

# =====================================================================

# 21. FINAL SUMMARY

# =====================================================================

# STACK:

#

# LIFO data structure.

#

# Python:

# list.append() -> Push

# list.pop()    -> Pop

#

#

# HEAP:

#

# Tree-based data structure.

#

# Used for:

# Priority Queue

#

# Python:

# heapq

#

#

# CALL STACK:

#

# Runtime structure for function calls.

#

# Function call -> Stack frame added

# Function return -> Stack frame removed

#

#

# MEMORY:

#

# RAM -> Primary working memory

# SSD/HDD -> Secondary storage

#

#

# MEMORY MANAGEMENT:

#

# Python automatically manages object memory.

#

#

# GARBAGE COLLECTION:

#

# Helps reclaim memory from unreachable objects.

#

#

# CPYTHON:

#

# Reference Counting

# +

# Cyclic Garbage Collection

#

#

# MEMORY LEAK:

#

# Unnecessary references can keep objects alive.

#

#

# RECURSION:

#

# Uses the call stack.

#

#

# RECURSION ERROR:

#

# Excessive recursion can exceed Python's recursion depth limit.

#

# =====================================================================

# ========================== ONE-LINE SUMMARY ==========================

# Stack:

# A LIFO-based linear data structure.

#

# Heap:

# A tree-based data structure commonly used for priority queues.

#

# Call Stack:

# Manages function calls and return flow.

#

# Memory Management:

# Manages memory allocation and reclamation for a program.

#

# Garbage Collection:

# Helps reclaim memory from unreachable objects.

#

# Memory Leak:

# Memory being retained longer than necessary because of

# unnecessary references or other retention issues.

#

# =====================================================================
