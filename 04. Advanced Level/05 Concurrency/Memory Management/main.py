"""
# =====================================================================
#                 PYTHON MEMORY & DATA STRUCTURES
# =====================================================================
#
# Topics:
#
# 1. Stack
# 2. Heap
# 3. Memory
# 4. Memory Management
# 5. Call Stack
# 6. Garbage Collection
# 7. Reference Counting
# 8. Generational Garbage Collection
# 9. Circular Reference
# 10. Memory Leak
# 11. Finalization
#
# =====================================================================



# =====================================================================
#                         1. STACK
# =====================================================================


# ============================= WHAT IS STACK ==========================

# Stack হলো একটি linear data structure যা LIFO principle অনুসরণ করে।
#
# LIFO = Last In, First Out
#
# অর্থাৎ:
#
# সর্বশেষ যে element stack-এ ঢুকবে,
# সেটিই প্রথমে বের হবে।
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
# এখন pop করলে:
#
# 30 বের হবে।
#
# কারণ 30 সর্বশেষে ঢুকেছে।
#
# =====================================================================


# ============================= STACK OPERATIONS =======================

# Main stack operations:
#
# Push
# -> Stack-এর top-এ নতুন element যোগ করা।
#
# Pop
# -> Stack-এর top থেকে element remove করা।
#
# Peek / Top
# -> Top element দেখা, remove না করে।
#
# isEmpty
# -> Stack empty কিনা check করা।
#
# =====================================================================


# ============================= STACK IN PYTHON ========================

# Python-এ list ব্যবহার করে সহজেই stack implement করা যায়।
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

# Top element দেখতে:
#
# stack[-1]

print("Top:", stack[-1])


# Output:
#
# Top: 30
#
# এখানে element remove হয়নি।
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
# এটি LIFO behavior।
#
# =====================================================================


# ============================= STACK USES =============================

# Stack ব্যবহার হয়:
#
# 1. Function calls
# 2. Recursion
# 3. Undo/Redo
# 4. Browser history
# 5. Expression evaluation
# 6. Parentheses matching
# 7. Depth First Search (DFS)
# 8. Backtracking
#
# =====================================================================



# =====================================================================
#                           2. HEAP
# =====================================================================


# ============================= WHAT IS HEAP ===========================

# Heap হলো একটি tree-based data structure।
#
# এটি সাধারণত Priority Queue implement করার জন্য ব্যবহার করা হয়।
#
# প্রধান দুই ধরনের heap:
#
# 1. Min Heap
# 2. Max Heap
#
# =====================================================================


# ============================= MIN HEAP ===============================

# Min Heap-এর ক্ষেত্রে smallest element root/top-এ থাকে।
#
# Example:
#
#          10
#        /    \
#       20     30
#
# এখানে 10 হলো minimum element।
#
# =====================================================================


# ============================= MAX HEAP ===============================

# Max Heap-এর ক্ষেত্রে largest element root/top-এ থাকে।
#
# Example:
#
#          30
#        /    \
#       20     10
#
# এখানে 30 হলো maximum element।
#
# =====================================================================


# ============================= HEAP IN PYTHON =========================

# Python-এর heapq module সাধারণত min-heap implement করতে ব্যবহৃত হয়।

import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print("Heap:", heap)

smallest = heapq.heappop(heap)

print("Smallest item:", smallest)
print("Heap after pop:", heap)


# Output-এর internal order sorted list-এর মতো হওয়া জরুরি নয়।
#
# Important:
#
# heap-এর প্রধান property হলো smallest element heap[0]-এ থাকে।
#
# =====================================================================


# ============================= HEAP OPERATIONS ========================

# heappush()
# -> Heap-এ element যোগ করে।
#
#
# heappop()
# -> Smallest element remove করে।
#
#
# heap[0]
# -> Min-heap-এর smallest element দেখা যায়।
#
#
# heapify()
# -> Existing list-কে heap-এ convert করে।
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

# "Heap-এ direct access করা যায় না" বলা technically correct নয়।
#
# Python-এর heap হলো list-এর উপর তৈরি structure।
#
# তাই:
#
# heap[0]
#
# দিয়ে root/minimum element access করা যায়।
#
# তবে arbitrary index access করলে heap ordering-এর অর্থ অনুযায়ী
# sorted order পাওয়া যায় না।
#
# Heap-এর main operations:
#
# - heappush()
# - heappop()
# - heap[0]
#
# =====================================================================



# =====================================================================
#                           3. MEMORY
# =====================================================================


# ============================= WHAT IS MEMORY =========================

# Memory হলো computer-এর এমন storage area যেখানে program execution-এর
# সময় data এবং instructions রাখা হয়।
#
#
# প্রধান memory/storage:
#
# 1. RAM
# 2. Cache
# 3. Secondary Storage
#
#
# RAM:
# -> Program execution-এর সময় actively ব্যবহৃত primary memory।
#
#
# SSD / HDD:
# -> Secondary storage।
#
# =====================================================================


# ============================= PYTHON MEMORY ==========================

# Python program execution-এর সময় objects-এর জন্য memory allocate করে।
#
# Example:
#
# x = 10
#
# এখানে Python একটি integer object তৈরি করে এবং x সেই object-কে
# reference করে।
#
# =====================================================================


x = 10

print(x)


# =====================================================================



# =====================================================================
#                       4. MEMORY MANAGEMENT
# =====================================================================


# ============================= WHAT IS MEMORY MANAGEMENT ==============

# Memory Management হলো program-এর জন্য memory allocate,
# use এবং reclaim করার process।
#
# Python automatic memory management ব্যবহার করে।
#
# Programmer-কে সাধারণত C/C++-এর মতো manually:
#
# malloc()
# free()
#
# করতে হয় না।
#
# =====================================================================


# ============================= PYTHON MEMORY MANAGEMENT ===============

# Python memory management-এর মধ্যে রয়েছে:
#
# 1. Object allocation
# 2. Reference counting (CPython)
# 3. Cyclic garbage collection
# 4. Python memory allocator
#
# =====================================================================



# =====================================================================
#                         5. CALL STACK
# =====================================================================


# ============================= WHAT IS CALL STACK =====================

# Call Stack হলো program execution-এর সময় active function calls
# track করার জন্য ব্যবহৃত LIFO-based stack structure।
#
# এটি Python-কে বুঝতে সাহায্য করে:
#
# 1. বর্তমানে কোন function execute হচ্ছে।
# 2. কোন function থেকে call করা হয়েছে।
# 3. Function শেষ হলে কোথায় return করতে হবে।
#
# =====================================================================


# ============================= CALL STACK PRINCIPLE ===================

# Call Stack follows:
#
# LIFO = Last In, First Out
#
# অর্থাৎ সর্বশেষ function call আগে return করবে।
#
# =====================================================================


# ============================= STACK FRAME ============================

# প্রতিটি function call-এর সাথে একটি execution frame তৈরি হয়।
#
# একটি frame-এর মধ্যে function execution-এর প্রয়োজনীয় information
# থাকতে পারে, যেমন:
#
# - Local variables
# - Function arguments
# - Execution state
# - Return information
#
# =====================================================================


# ============================= CALL STACK EXAMPLE =====================

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

# Program শুরু:
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
# func_c() শেষ:
#
# [ main ]
# [ func_a ]
# [ func_b ]       <- Top
#
#
# func_b() শেষ:
#
# [ main ]
# [ func_a ]       <- Top
#
#
# func_a() শেষ:
#
# [ main ]         <- Top
#
#
# Program শেষ:
#
# [ empty ]
#
# =====================================================================


# ============================= PUSH / POP =============================

# Function call:
# -> Stack frame push/add হয়।
#
#
# Function return:
# -> Stack frame pop/remove হয়।
#
# =====================================================================



# =====================================================================
#                         6. RECURSION
# =====================================================================


# ============================= WHAT IS RECURSION ======================

# Recursion হলো এমন technique যেখানে একটি function নিজেকেই
# call করে।
#
# =====================================================================


def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)


countdown(3)


# Call flow:
#
# countdown(3)
#      |
#      v
# countdown(2)
#      |
#      v
# countdown(1)
#      |
#      v
# countdown(0)
#
#
# তারপর functions return করতে শুরু করবে।
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
# তারপর reverse order-এ return হবে।
#
# =====================================================================



# =====================================================================
#                       7. STACK OVERFLOW / RECURSION ERROR
# =====================================================================


# Infinite recursion:

def infinite_recursion():

    infinite_recursion()


# infinite_recursion()
#
# এটি চালালে Python eventually:
#
# RecursionError
#
# দেখাবে।
#
# কারণ recursion depth limit exceed হয়।
#
# =====================================================================



# =====================================================================
#                       8. GARBAGE COLLECTION
# =====================================================================


# ============================= WHAT IS GARBAGE COLLECTION =============

# Garbage Collection হলো automatic memory management-এর একটি process
# যা unreachable objects-এর memory reclaim করতে সাহায্য করে।
#
# সহজভাবে:
#
# যে objects program-এর জন্য আর reachable নয়,
# তাদের memory পুনরায় ব্যবহারযোগ্য করা হয়।
#
# =====================================================================


# ============================= PYTHON GC ==============================

# CPython-এর memory management-এ:
#
# 1. Reference Counting
# 2. Cyclic Garbage Collector
#
# গুরুত্বপূর্ণ ভূমিকা রাখে।
#
# =====================================================================


# ============================= REFERENCE COUNTING =====================

# Reference Counting হলো এমন mechanism যেখানে object-এর দিকে
# কতগুলো reference আছে তা track করা হয়।
#
# যখন reference count zero হয়, CPython সাধারণত সেই object-এর
# memory reclaim করতে পারে।
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
# sys.getrefcount() function নিজেও temporary reference তৈরি করে।
#
# তাই returned value সাধারণত visible references-এর count থেকে
# 1 বেশি হতে পারে।
#
# Exact value implementation/context অনুযায়ী পরিবর্তিত হতে পারে।
#
# =====================================================================


# ============================= DEL KEYWORD ============================

# del variable reference remove করে।
#
# এটি সরাসরি "garbage collector চালানো" নয়।
#
# Example:

a = []

b = a

del a

# Object এখনো b দ্বারা referenced।
#
# তাই object reachable।
#
#
# এরপর:
#
# del b
#
# করলে object-এর এই দুই variable reference-ই remove হবে।
#
# =====================================================================



# =====================================================================
#                       9. CIRCULAR REFERENCE
# =====================================================================


# ============================= WHAT IS CIRCULAR REFERENCE =============

# যখন দুই বা তার বেশি object একে অপরকে reference করে,
# তখন circular reference তৈরি হতে পারে।
#
#
# Example:
#
# A -> B
# B -> A
#
# =====================================================================


class Node:

    def __init__(self):

        self.ref = None


a = Node()
b = Node()

a.ref = b
b.ref = a


# এখন:
#
# a -> b
# b -> a
#
# এটি একটি reference cycle।
#
# Reference counting alone এই cycle-এর unreachable objects
# collect করতে পারে না।
#
# Python-এর cyclic garbage collector এই ধরনের cycle
# শনাক্ত করে collect করতে পারে।
#
# =====================================================================



# =====================================================================
#                  10. GENERATIONAL GARBAGE COLLECTION
# =====================================================================


# Python-এর cyclic garbage collector objects-কে generations-এর
# মাধ্যমে track করে।
#
#
# Generation 0:
# -> নতুন objects
#
# Generation 1:
# -> Collection-এর পর surviving objects
#
# Generation 2:
# -> দীর্ঘসময় survive করা objects
#
#
# সাধারণ ধারণা:
#
# Young objects দ্রুত garbage হওয়ার সম্ভাবনা বেশি।
#
# তাই younger generation বেশি frequently পরীক্ষা করা হয়।
#
# =====================================================================


# ============================= GC THRESHOLD ============================

import gc

print("GC thresholds:", gc.get_threshold())


# get_threshold() garbage collector-এর thresholds return করে।
#
# =====================================================================


# ============================= MANUAL GC ===============================

import gc

collected = gc.collect()

print("Objects collected:", collected)


# gc.collect()
#
# manually garbage collection trigger করতে পারে।
#
# এটি বিশেষভাবে cyclic garbage collect করার জন্য useful।
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
#                         11. FINALIZATION
# =====================================================================


# ============================= WHAT IS FINALIZATION ====================

# Finalization হলো object finalization-এর সময় cleanup-related
# action করার process।
#
# Python class-এ __del__() method define করা যায়।
#
# তবে __del__() কে reliable resource cleanup mechanism হিসেবে
# ব্যবহার করা উচিত নয়।
#
# =====================================================================


# ============================= __del__ EXAMPLE ========================

class MyClass:

    def __init__(self, name):

        self.name = name

    def __del__(self):

        print(f"{self.name} is being finalized")


obj = MyClass("Object1")

del obj


# CPython-এ সাধারণ reference-counting situation-এ __del__()
# দ্রুত call হতে পারে।
#
# কিন্তু language-level code-এ এর timing-এর ওপর নির্ভর করে
# resource cleanup করা উচিত নয়।
#
# =====================================================================



# =====================================================================
#                       12. RESOURCE CLEANUP
# =====================================================================


# File cleanup-এর জন্য __del__() ব্যবহার না করে
# context manager ব্যবহার করা উচিত।
#
# Example:

with open("test.txt", "w") as f:

    f.write("Hello Python")


# with block শেষ হলে file automatically close হবে।
#
# এটি file/resource management-এর recommended approach।
#
# =====================================================================



# =====================================================================
#                         13. MEMORY LEAK
# =====================================================================


# ============================= WHAT IS MEMORY LEAK =====================

# Memory Leak বলতে সাধারণভাবে এমন situation বোঝায় যেখানে program
# এমন memory ধরে রাখে যা আর প্রয়োজন নেই, ফলে memory usage
# অপ্রয়োজনীয়ভাবে বাড়তে থাকে।
#
# Python-এ garbage collector থাকা সত্ত্বেও unnecessary references
# থাকলে objects memory-তে থেকে যেতে পারে।
#
# =====================================================================


# ============================= MEMORY LEAK EXAMPLE ====================

leaky_list = []


def create_data():

    for i in range(10000):

        leaky_list.append("x" * 1000)


create_data()

print("Objects are still referenced by leaky_list.")


# এখানে objects leaky_list-এর মধ্যে রাখা হয়েছে।
#
# তাই list যতক্ষণ থাকবে, stored objects-গুলোর references থাকবে।
#
# এটি একটি simplified example of retained memory।
#
# Real-world memory leaks আরও complex হতে পারে।
#
# =====================================================================


# ============================= HOW TO AVOID MEMORY LEAK ===============

# 1. Unnecessary references remove করা।
#
# 2. Large global lists avoid করা।
#
# 3. Cache-এর size control করা।
#
# 4. Event listeners / callbacks properly remove করা।
#
# 5. Open files properly close করা।
#
# 6. Database connections properly close করা।
#
# 7. Context managers ব্যবহার করা।
#
# 8. Long-lived objects-এর references review করা।
#
# =====================================================================



# =====================================================================
#                  14. STACK vs HEAP vs CALL STACK
# =====================================================================


# STACK:
#
# General data structure.
#
# Principle:
# LIFO
#
# Python:
# list দিয়ে implement করা যায়।
#
# Uses:
# push, pop, undo, DFS, etc.
#
#
# HEAP:
#
# Tree-based data structure।
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
# Function calls manage করার runtime structure।
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
#                 15. STACK vs HEAP MEMORY
# =====================================================================


# এখানে একটি গুরুত্বপূর্ণ distinction:
#
# "Stack" এবং "Heap" শব্দ দুটি দুই context-এ ব্যবহৃত হতে পারে।
#
#
# 1. Stack Data Structure
# 2. Heap Data Structure
#
# আবার programming language/runtime context-এ:
#
# 3. Call Stack
# 4. Heap Memory
#
#
# এগুলো এক জিনিস নয়।
#
# =====================================================================


# ============================= CALL STACK =============================

# Call Stack:
# -> Function execution-এর জন্য runtime structure।
#
# -> Function call/return manage করে।
#
# -> LIFO behavior।
#
# =====================================================================


# ============================= HEAP MEMORY ============================

# Heap Memory:
# -> Runtime-এ dynamically allocated objects রাখার জন্য ব্যবহৃত
#    memory area হিসেবে সাধারণভাবে বোঝানো হয়।
#
# Python objects সাধারণত heap-allocated।
#
# এটি "heap data structure" থেকে আলাদা concept।
#
# =====================================================================



# =====================================================================
#                         16. HEAP DATA STRUCTURE
# =====================================================================


# Heap Data Structure:
#
# Tree-based data structure।
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
#                         17. MEMORY FLOW
# =====================================================================


# Program starts
#       |
#       v
# Function call
#       |
#       v
# Call Stack
#       |
#       v
# Function creates objects
#       |
#       v
# Objects occupy memory
#       |
#       v
# References change/remove
#       |
#       v
# Object becomes unreachable
#       |
#       v
# Reference counting / cyclic GC
#       |
#       v
# Memory can be reclaimed
#
# =====================================================================



# =====================================================================
#                   18. COMPLETE CALL STACK EXAMPLE
# =====================================================================


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


# Execution:
#
# Program started
#
#       |
#       v
#
# a()
#
#       |
#       v
#
# b()
#
#       |
#       v
#
# c()
#
#       |
#       v
#
# c() returns
#
#       |
#       v
#
# b() returns
#
#       |
#       v
#
# a() returns
#
#       |
#       v
#
# Program ended
#
# =====================================================================



# =====================================================================
#                    19. IMPORTANT EXAM POINTS
# =====================================================================


# STACK:
#
# - Linear data structure
# - LIFO
# - Push
# - Pop
# - Top
# - Python list can implement stack
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
# - Recursion uses call stack
#
#
# MEMORY:
#
# - RAM is primary memory
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
# - __del__() can participate in object finalization
# - Not recommended for deterministic resource cleanup
#
# =====================================================================



# =====================================================================
#                         20. INTERVIEW QUESTIONS
# =====================================================================


# Q1. What is a Stack?
#
# Answer:
# Stack is a linear data structure that follows LIFO
# (Last In, First Out).


# Q2. How can you implement a Stack in Python?
#
# Answer:
# Python list can be used as a stack using append() and pop().


# Q3. What is a Heap?
#
# Answer:
# Heap is a tree-based data structure commonly used to implement
# priority queues.


# Q4. What is a Min Heap?
#
# Answer:
# A Min Heap keeps the smallest element at the root.


# Q5. What is a Call Stack?
#
# Answer:
# Call Stack is a runtime stack structure used to track active
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


# Q15. Is __del__() recommended for file cleanup?
#
# Answer:
# No. Use context managers such as the 'with' statement for
# deterministic resource cleanup.


# =====================================================================
#                         21. FINAL SUMMARY
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
#        +
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
# LIFO-based linear data structure.
#
# Heap:
# Tree-based data structure commonly used for priority queues.
#
# Call Stack:
# Function calls এবং return flow manage করে।
#
# Memory Management:
# Program-এর memory allocation এবং reclamation manage করে।
#
# Garbage Collection:
# Unreachable objects-এর memory reclaim করতে সাহায্য করে।
#
# Memory Leak:
# Unnecessary references-এর কারণে memory প্রয়োজনের চেয়ে বেশি
# সময় ধরে retained থাকা।
#
# =====================================================================

"""