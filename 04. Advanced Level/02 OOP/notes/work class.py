# ========================= Python Class Working Flow with Heap Memory =========================

"""
Python Class Working Flow — Step by Step
=========================================

Step 1: Create a Class
--------------------------------
class Work:
    - Class হলো blueprint বা template যা বলে দেয় object কেমন হবে।
    - Python internally Class-কে object হিসেবেও রাখে।
    - Example:
      >>> print(type(Work))
      <class 'type'>
    - Heap memory allocation হয়নি এখনও, শুধুমাত্র Class definition আছে memory তে।

---

Step 2: Create a Constructor (__init__)
--------------------------------
def __init__(self, name, age):
    self.name = name
    self.age = age

- Constructor স্বয়ংক্রিয়ভাবে চালু হয় যখন object তৈরি করা হয়।
- self parameter হলো সেই object যেটা তৈরি হচ্ছে।
- Attribute (self.name, self.age) **heap memory**-এ সংরক্ষণ হয়।

---

Step 3: Create a Method
--------------------------------
def showInfo(self):
    print(f"Name: {self.name}, Age: {self.age}")

- Method হলো class-এর ভেতরের function।
- self বলে দেয় কোন object-এর method কল করা হচ্ছে।
- যখন work.showInfo() কল হয়, Python internally কাজ করে:
  Work.showInfo(work)

---

Step 4: Create an Object
--------------------------------
work = Work("John", 30)

- Stack memory: `work` নামে একটি reference তৈরি হয়।
- Heap memory: Python Work class-এর object তৈরি করে এবং attribute সংরক্ষণ করে।

Diagram:
          Stack Memory                Heap Memory
       ───────────────────        ──────────────────────────
       work ───────────────►  [Object of Work class]
                                 ├── name = "John"
                                 └── age  = 30

---

Step 5: Call the Method
--------------------------------
work.showInfo()

- Python দেখে showInfo method আছে কিনা object-এর মধ্যে।
- self হিসেবে work পাস করে method চালায়।
- Output: Name: John, Age: 30

---

Garbage Collection
--------------------------------
- যদি কোনো object-এর reference আর না থাকে, Garbage Collector সেটাকে heap থেকে মুছে দেয়।

Example:
work = Work("John", 30)
work = None  # Garbage collector এখন object delete করবে

---

Summary Table
| ধাপ                  | কাজ                            | Memory Location          |
|----------------------|--------------------------------|-------------------------|
| Class Creation       | Blueprint তৈরি                 | Code area               |
| Constructor (__init__) | Object initialize করা         | Heap (attributes)       |
| Method               | Object-এর কাজ নির্ধারণ       | Code area               |
| Object Creation      | Instance তৈরি                  | Heap (data), Stack (reference) |
| Method Call          | Object ব্যবহার                  | Stack → Heap            |
| Garbage Collection   | অপ্রয়োজনীয় object delete করা  | Heap                     |

---

Example Code (Working Flow + Heap Memory)

import gc

class Work:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create objects
work1 = Work("John", 30)    # Object allocated in heap
work2 = Work("Alice", 25)   # Another object in heap

# Call method
work1.showInfo()
work2.showInfo()

# Print object ids (memory addresses)
print("work1 id:", id(work1))
print("work2 id:", id(work2))

# Delete one object
del work1
gc.collect()  # Force garbage collection

print("work2 still exists:", id(work2))
"""

# ========================= End of Working Flow with Heap Memory =========================
