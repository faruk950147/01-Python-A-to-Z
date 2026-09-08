# ======================== WHAT IS GARBAGE COLLECTION ========================

# Garbage collection is the process of automatically freeing memory
# by deleting objects that are no longer in use by the program.

# ============================================================================


# ======================== HOW DOES GARBAGE COLLECTION WORK ==================

# Python uses a technique called "reference counting" to manage memory.
# Every object in Python keeps track of how many references point to it.
# When this reference count becomes zero, the object is automatically deallocated.

# However, reference counting alone cannot handle circular references.
# To fix this, Python also uses "generational garbage collection" to detect
# and remove circularly referenced objects.

# ============================================================================


# ======================== TYPES OF GARBAGE COLLECTION =======================

# 1. Reference Counting
# 2. Generational Garbage Collection

# ============================================================================


# ======================== REFERENCE COUNTING ================================

# Reference counting means each object keeps a count of how many references
# are pointing to it. When the reference count drops to zero, the memory
# occupied by the object is released.

# Example:
import sys

print("=== Reference Counting Example ===")
a = []              # Create a list object
b = a               # 'b' now refers to the same list
print("Reference count of a:", sys.getrefcount(a))  # Usually 3 (a, b, and argument)
del b               # Delete one reference
print("After deleting b:", sys.getrefcount(a))      # Count decreases
print()

# ============================================================================


# ======================== GENERATIONAL GARBAGE COLLECTION ===================

# Generational Garbage Collection divides objects into generations based
# on how long they have been in memory.
#
# Generation 0 -> Newly created objects
# Generation 1 -> Objects that survived one garbage collection
# Generation 2 -> Long-lived objects
#
# The garbage collector runs more frequently on younger generations,
# as most objects become unused quickly.

import gc

print("=== Generational Garbage Collection Example ===")
print("Garbage Collection thresholds:", gc.get_threshold())

# Manually trigger garbage collection
gc.collect()
print("Manual garbage collection performed.")
print()

# ============================================================================


# ======================== FINALIZATION ======================================

# Finalization is the process of performing cleanup operations before an
# object is destroyed. This is done using the __del__() method in Python.

print("=== Finalization Example ===")

class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print("File opened")

    def __del__(self):
        self.file.close()
        print("File closed automatically")

# Create and delete an object
f = FileHandler("test.txt")
del f  # __del__() is automatically called here

print()
print("=== End of Garbage Collection Demonstration ===")

# ============================================================================
# What’s new/improved here:

# Removed repeated “generational garbage collection” section.

# Added real examples using sys.getrefcount() and gc.collect().

# Explained circular references and object generations.

# Added finalization demo (__del__()).

# Fully formatted for readability and reusability.