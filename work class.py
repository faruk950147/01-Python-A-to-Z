# ========================= Python Class Working Flow with Heap Memory =========================

"""
Python Class Working Flow — Step by Step
=========================================

Important Note:
---------------
Python-এর memory model-কে সরাসরি C/C++ এর মতো
"Stack Memory এবং Heap Memory" হিসেবে ধরে নেওয়া ঠিক নয়।

CPython-এ:
- Python objects সাধারণত heap-এ allocated হয়।
- Local variables সাধারণত object-এর reference ধারণ করে।
- Function call-এর সময় execution frame তৈরি হয়।
- Implementation অনুযায়ী memory management ভিন্ন হতে পারে।

তাই নিচের explanation-এ Stack/Heap শব্দগুলো
বোঝানোর সুবিধার জন্য ব্যবহার করা হয়েছে।
"""


# ============================================================
# Step 1: Create a Class
# ============================================================

class Work:
    pass


"""
class Work:
    - Work হলো একটি class।
    - Class হলো object তৈরির blueprint বা template।
    - Python-এ class নিজেও একটি object।
    - Work class-এর type হলো 'type'।

Example:
"""

print(type(Work))

# Output:
# <class 'type'>


"""
অর্থাৎ:

Work
  ↓
একটি class object

Work-এর type
  ↓
type


Class definition-এর সময় Work class তৈরি হয়।
কিন্তু Work class-এর কোনো instance তখনও তৈরি হয়নি।
"""


# ============================================================
# Step 2: Create a Constructor (__init__)
# ============================================================

class Work:

    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
__init__():

- __init__ হলো একটি special method।
- Object তৈরি করার সময় Python সাধারণত __init__ method call করে।
- এর কাজ হলো newly created object-এর initial state তৈরি/initialize করা।

self:

- self হলো current object-এর reference।
- self.name এবং self.age হলো instance attributes।

Example:

work = Work("John", 30)

এখানে:

self
 ↓
work object

self.name
 ↓
"John"

self.age
 ↓
30
"""


# ============================================================
# Step 3: Create a Method
# ============================================================

class Work:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")


"""
showInfo():

- showInfo হলো class-এর একটি method।
- Method technically একটি function যা class-এর namespace-এর মধ্যে
  defined থাকে।
- self-এর মাধ্যমে current object-এর attributes access করা হয়।

Example:

work.showInfo()

Python conceptually এটিকে এমনভাবে ভাবা যায়:

Work.showInfo(work)

অর্থাৎ:

work
 ↓
self

তাই:

self.name
 ↓
work.name

self.age
 ↓
work.age
"""


# ============================================================
# Step 4: Create an Object
# ============================================================

work = Work("John", 30)


"""
এই statement চালানোর সময়:

work = Work("John", 30)

ধারণাগতভাবে কয়েকটি কাজ হয়:

1. Work class-এর একটি নতুন instance তৈরি হয়।
2. নতুন object-এর reference পাওয়া যায়।
3. __init__() method call হয়।
4. __init__() এর মধ্যে:
       self.name = "John"
       self.age = 30
   সেট করা হয়।
5. work variable সেই object-কে reference করে।

Conceptual Diagram:

    Variable / Reference
    -------------------

        work
          |
          |
          v
    +----------------------+
    |   Work Object        |
    |----------------------|
    | name = "John"        |
    | age  = 30            |
    +----------------------+

Python object সাধারণত heap-এ allocated হয়।

কিন্তু "work অবশ্যই stack-এ আছে"
এভাবে বলা technically guaranteed নয়।
"""


# ============================================================
# Step 5: Call the Method
# ============================================================

work.showInfo()


"""
Output:

Name: John, Age: 30


work.showInfo()

এখানে work object-এর showInfo() method call করা হচ্ছে।

Conceptually:

work.showInfo()

কে ভাবা যায়:

Work.showInfo(work)

অর্থাৎ:

work object
     ↓
    self

তারপর:

self.name
     ↓
work.name
     ↓
"John"

self.age
     ↓
work.age
     ↓
30
"""


# ============================================================
# Step 6: Create Multiple Objects
# ============================================================

work1 = Work("John", 30)
work2 = Work("Alice", 25)


"""
এখানে দুটি আলাদা Work object তৈরি হয়েছে।

Conceptual Diagram:

       work1
         |
         v
   +----------------+
   | Work Object    |
   | name = John    |
   | age = 30       |
   +----------------+


       work2
         |
         v
   +----------------+
   | Work Object    |
   | name = Alice   |
   | age = 25       |
   +----------------+


work1 এবং work2 দুটি আলাদা object।

তাই:

work1.name != work2.name
work1.age  != work2.age
"""


# ============================================================
# Step 7: Object Identity using id()
# ============================================================

print("work1 id:", id(work1))
print("work2 id:", id(work2))


"""
id():

id() একটি object-এর identity value return করে।

Example:

id(work1)
id(work2)

দুটি object আলাদা হলে সাধারণত তাদের id আলাদা হবে।

Important:
---------
id() কে সরাসরি "memory address" বলা ঠিক নয়।

CPython implementation-এ id() সাধারণত object-এর memory address-এর
সাথে সম্পর্কিত হতে পারে, কিন্তু Python language specification অনুযায়ী
id() হলো object-এর unique identity value।

তাই:

id(work1)

কে বলা ভালো:

"work1 object-এর identity value"
"""


# ============================================================
# Step 8: Delete a Reference
# ============================================================

del work1


"""
del work1

এখানে work1 variable/reference-টি namespace থেকে remove করা হয়।

কিন্তু এর অর্থ সবসময় object সাথে সাথে delete হয়ে গেছে নয়।

যদি object-এর অন্য কোনো reference থাকে,
তাহলে object এখনও থাকতে পারে।

Example:

work1 = Work("John", 30)

another = work1

del work1

এখন:

another
   |
   v
Work Object


work1 delete হলেও object এখনও exists করে,
কারণ another এখনও object-টিকে reference করছে।
"""


# ============================================================
# Step 9: Reference Counting and Garbage Collection
# ============================================================

work1 = Work("John", 30)

work1 = None


"""
work1 = None

এখন work1 আর Work object-টিকে reference করছে না।

যদি object-এর আর কোনো reference না থাকে,
CPython-এ reference count zero হয়ে গেলে object সাধারণত
immediately deallocate হতে পারে।

Python-এর garbage collector বিশেষ করে cyclic references
handle করতে সাহায্য করে।

তাই:

"Reference নেই → Garbage Collector অবশ্যই সাথে সাথে delete করবে"

এভাবে বলা ঠিক নয়।

বরং বলা ভালো:

"Object-এর আর কোনো reachable reference না থাকলে
Python implementation সেটিকে eventually reclaim করতে পারে।
CPython-এ reference counting-এর কারণে অনেক object দ্রুত
deallocate হয়।"
"""


# ============================================================
# Complete Example
# ============================================================

import gc


class Work:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Create objects
work1 = Work("John", 30)
work2 = Work("Alice", 25)


# Call methods
work1.showInfo()
work2.showInfo()


# Object identity
print("work1 id:", id(work1))
print("work2 id:", id(work2))


# Delete reference
del work1

# Request garbage collection
gc.collect()


# work2 still exists
print("work2 still exists:", id(work2))


# ============================================================
# Complete Working Flow
# ============================================================

"""
Python Class Working Flow:

        Class Definition
               |
               v
        class Work
               |
               v
        Class Object
               |
               |
        Object Creation
               |
               v
      Work("John", 30)
               |
               v
        New Work Object
               |
               v
          __init__()
               |
               v
      self.name = "John"
      self.age  = 30
               |
               v
       work reference
               |
               v
        Work Object
        +-------------+
        | name = John |
        | age  = 30   |
        +-------------+
               |
               v
       work.showInfo()
               |
               v
      Work.showInfo(work)
               |
               v
             Output
               |
               v
      Name: John, Age: 30
               |
               v
      Reference removed
               |
               v
       Object may become
       eligible for memory
       reclamation
"""


# ============================================================
# Summary Table
# ============================================================

"""
| Step                  | What Happens                                  |
|-----------------------|-----------------------------------------------|
| Class Creation        | Class object is created                       |
| __init__ Definition   | Initialization logic is defined               |
| Method Definition     | Behavior/functionality is defined             |
| Object Creation       | A new instance is created                     |
| __init__ Execution    | Instance attributes are initialized           |
| Reference Creation    | Variable refers to the object                 |
| Method Call           | Current object is passed as self              |
| id()                  | Object identity value is returned              |
| del Reference         | A reference is removed                        |
| Garbage Collection    | Unreachable objects may be reclaimed          |


Key Concepts:

1. Class
   ↓
   Blueprint / template

2. Object
   ↓
   Instance of a class

3. self
   ↓
   Reference to the current instance

4. __init__()
   ↓
   Initializes the instance

5. Instance Attribute
   ↓
   self.name
   self.age

6. Method
   ↓
   Function defined inside a class

7. id()
   ↓
   Object identity value

8. Garbage Collection
   ↓
   Reclaims objects that are no longer reachable


Important Memory Concept:

Python-এর ক্ষেত্রে সবচেয়ে safe explanation হলো:

    Variable
       |
       v
    Reference
       |
       v
    Python Object
       |
       v
    Heap-managed memory


এবং method/function call-এর সময় Python execution frames ব্যবহার করে।

তাই Python-এর memory management ব্যাখ্যা করার সময়
"C/C++ এর মতো variable = stack এবং object = heap"
কে absolute rule হিসেবে ব্যবহার করা উচিত নয়।
"""

# ========================= End of Python Class Working Flow =========================