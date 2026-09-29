"""
# ===================== What is Inheritance? =====================

## 1. What is Inheritance?

**Inheritance** is an Object-Oriented Programming (OOP) mechanism in which a new class derives properties and behaviors from an existing class.

* The existing class is called the **Base / Parent class**.
* The new class is called the **Derived / Child class**.

```text
Base = Parent
Derived = Child
```

### Simple Definition

> **Inheritance allows a child class to reuse and extend the attributes and methods of a parent class.**

---

# 2. Basic Syntax

```python
class Parent:
    pass


class Child(Parent):
    pass
```

Here:

```text
Parent
   |
   ↓
Child
```

`Child` inherits from `Parent`.

---

# 3. Basic Example

```python
class Parent:
    def greet_parent(self):
        print("Hello from Parent")


class Child(Parent):
    def greet_child(self):
        print("Hello from Child")


child = Child()

child.greet_parent()
child.greet_child()
```

### Output

```text
Hello from Parent
Hello from Child
```

The `Child` object can access:

* Its own method: `greet_child()`
* Inherited parent method: `greet_parent()`

---

# 4. Types of Inheritance in Python

There are commonly five types:

```text
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
```

---

# ==================================================

# 1. Single Inheritance

# ==================================================

## What is Single Inheritance?

**Single Inheritance** occurs when one child class inherits from exactly one parent class.

### Structure

```text
Parent
   |
   ↓
Child
```

### Example

```python
class Parent:
    def greet_parent(self):
        print("Hello from Parent")


class Child(Parent):
    def greet_child(self):
        print("Hello from Child")


child = Child()

child.greet_parent()
child.greet_child()
```

### Output

```text
Hello from Parent
Hello from Child
```

### Constructor Example

```python
class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


child = Child("John", 20)

print(child.name)
print(child.age)
```

### Output

```text
John
20
```

Here:

```python
super().__init__(name)
```

calls the constructor of the parent class.

### Important

```text
Single Inheritance
       ↓
One Parent
       ↓
One Child
```

---

# ==================================================

# 2. Multiple Inheritance

# ==================================================

## What is Multiple Inheritance?

**Multiple Inheritance** occurs when one child class inherits from **more than one parent class**.

### Structure

```text
Parent1     Parent2
    \         /
     \       /
       Child
```

### Example

```python
class Parent1:
    def greet_parent1(self):
        print("Hello from Parent1")


class Parent2:
    def greet_parent2(self):
        print("Hello from Parent2")


class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from Child")


child = Child()

child.greet_parent1()
child.greet_parent2()
child.greet_child()
```

### Output

```text
Hello from Parent1
Hello from Parent2
Hello from Child
```

Here:

```text
Child inherits from Parent1 and Parent2
```

---

# Multiple Inheritance with Constructors

```python
class Parent1:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")


class Parent2:
    def __init__(self, age):
        self.age = age

    def display_age(self):
        print(f"Age: {self.age}")


class Child(Parent1, Parent2):
    def __init__(self, name, age, address):
        Parent1.__init__(self, name)
        Parent2.__init__(self, age)

        self.address = address

    def display(self):
        self.display_name()
        self.display_age()
        print(f"Address: {self.address}")


child = Child("Faruk", 20, "Bogura")

child.display()
```

### Output

```text
Name: Faruk
Age: 20
Address: Bogura
```

### Important Point

In multiple inheritance, Python has a specific order for searching methods.

This is called:

```text
MRO
↓
Method Resolution Order
```

You can check it using:

```python
print(Child.mro())
```

or:

```python
print(Child.__mro__)
```

---

# ==================================================

# 3. Multilevel Inheritance

# ==================================================

## What is Multilevel Inheritance?

**Multilevel Inheritance** occurs when a class inherits from another class, which itself inherits from another class.

### Structure

```text
Grandparent
     |
     ↓
   Parent
     |
     ↓
   Child
```

### Example

```python
class Grandparent:
    def greet_grandparent(self):
        print("Hello from Grandparent")


class Parent(Grandparent):
    def greet_parent(self):
        print("Hello from Parent")


class Child(Parent):
    def greet_child(self):
        print("Hello from Child")


child = Child()

child.greet_grandparent()
child.greet_parent()
child.greet_child()
```

### Output

```text
Hello from Grandparent
Hello from Parent
Hello from Child
```

---

# Multilevel Inheritance with Constructors

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display_age(self):
        print(f"Age: {self.age}")


class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def display_address(self):
        print(f"Address: {self.address}")


grandchild = GrandChild(
    "John",
    20,
    "Bogura"
)

grandchild.display_name()
grandchild.display_age()
grandchild.display_address()
```

### Output

```text
Name: John
Age: 20
Address: Bogura
```

Notice:

```text
GrandChild
    ↓
Child
    ↓
Parent
```

The `GrandChild` object can access methods inherited through the entire chain.

---

# ==================================================

# 4. Hierarchical Inheritance

# ==================================================

## What is Hierarchical Inheritance?

**Hierarchical Inheritance** occurs when multiple child classes inherit from the same parent class.

### Structure

```text
          Parent
          /    \
         /      \
    Child1     Child2
```

### Example

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")


class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display_age(self):
        print(f"Age: {self.age}")


class Child2(Parent):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def display_address(self):
        print(f"Address: {self.address}")


child1 = Child1("John", 20)
child2 = Child2("David", "Bogura")

child1.display_name()
child1.display_age()

child2.display_name()
child2.display_address()
```

### Output

```text
Name: John
Age: 20

Name: David
Address: Bogura
```

Here:

```text
          Parent
          /    \
         ↓      ↓
      Child1  Child2
```

Both `Child1` and `Child2` inherit from `Parent`.

---

# ==================================================

# 5. Hybrid Inheritance

# ==================================================

## What is Hybrid Inheritance?

**Hybrid Inheritance** is a combination of two or more types of inheritance.

For example, it can combine:

* Multiple inheritance
* Multilevel inheritance
* Hierarchical inheritance

### Example Structure

```text
             A
            / \
           B   C
            \ /
             D
```

This structure combines:

* Hierarchical inheritance: `A → B` and `A → C`
* Multiple inheritance: `D → B, C`

Therefore, this is **Hybrid Inheritance**.

---

# Hybrid Inheritance Example

```python
class A:
    def greet_a(self):
        print("Hello from A")


class B(A):
    def greet_b(self):
        print("Hello from B")


class C(A):
    def greet_c(self):
        print("Hello from C")


class D(B, C):
    def greet_d(self):
        print("Hello from D")


d = D()

d.greet_a()
d.greet_b()
d.greet_c()
d.greet_d()
```

### Output

```text
Hello from A
Hello from B
Hello from C
Hello from D
```

The structure is:

```text
             A
            / \
           B   C
            \ /
             D
```

This is a classic example of **Hybrid Inheritance**.

---

# 6. Method Resolution Order (MRO)

MRO is especially important in:

* Multiple inheritance
* Hybrid inheritance

Consider:

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
```

Python needs to determine:

> When `D` calls a method, which parent should Python search first?

Python uses **MRO (Method Resolution Order)**.

Check it:

```python
print(D.mro())
```

Conceptually, the order is:

```text
D → B → C → A → object
```

Python uses the **C3 linearization algorithm** to determine MRO.

---

# 7. The Diamond Problem

Hybrid/multiple inheritance can create the famous **Diamond Problem**.

### Structure

```text
        A
       / \
      B   C
       \ /
        D
```

`D` gets `A` through both `B` and `C`.

The question is:

```text
Which path should Python follow?
```

Python solves this using:

```text
MRO
+
super()
```

---

# 8. `super()` in Multiple Inheritance

A better approach in cooperative multiple inheritance is to use `super()` consistently.

Example:

```python
class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")


class C(A):
    def __init__(self):
        super().__init__()
        print("C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")


d = D()
```

### Output

```text
A
C
B
D
```

The exact order comes from the MRO.

Check:

```python
print(D.mro())
```

Conceptually:

```text
D → B → C → A → object
```

So `super()` means:

> **Call the next class in the MRO, not necessarily the direct parent class.**

This is an important Python interview point.

---

# 9. Important Correction About `super()`

Do not think:

```python
super()
```

always means:

```text
Call my immediate parent.
```

More accurately:

```text
super()
    ↓
Continue lookup according to the MRO
```

For example:

```python
class D(B, C):
```

the MRO may be:

```text
D → B → C → A → object
```

Therefore, `super()` from `B` can continue to `C`.

---

# 10. All Five Types at a Glance

## 1. Single

```text
Parent
   |
 Child
```

One parent → one child.

---

## 2. Multiple

```text
Parent1     Parent2
    \         /
     \       /
       Child
```

Multiple parents → one child.

---

## 3. Multilevel

```text
Grandparent
     |
   Parent
     |
   Child
```

Inheritance occurs through multiple levels.

---

## 4. Hierarchical

```text
       Parent
       /    \
      /      \
 Child1     Child2
```

One parent → multiple children.

---

## 5. Hybrid

```text
        A
       / \
      B   C
       \ /
        D
```

Combination of multiple inheritance patterns.

---

# 11. Inheritance vs Composition

This is an important design/interview topic.

### Inheritance

Represents:

```text
IS-A
```

Example:

```text
Dog IS-A Animal
```

```python
class Dog(Animal):
    pass
```

### Composition

Represents:

```text
HAS-A
```

Example:

```text
Car HAS-A Engine
```

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

A common design guideline is:

> **Favor composition over inheritance when composition better represents the relationship or provides more flexibility.**

This does **not** mean inheritance is always bad.

Use inheritance when there is a genuine **IS-A** relationship and polymorphic behavior through a common base class makes sense.

---

# 12. Important Interview Points

### Point 1

```text
Base Class = Parent Class
Derived Class = Child Class
```

### Point 2

Inheritance provides:

```text
Code Reusability
+
Extension
+
Polymorphism
```

### Point 3

Single inheritance:

```text
One Parent → One Child
```

### Point 4

Multiple inheritance:

```text
Multiple Parents → One Child
```

### Point 5

Multilevel:

```text
Grandparent → Parent → Child
```

### Point 6

Hierarchical:

```text
One Parent → Multiple Children
```

### Point 7

Hybrid:

```text
Combination of inheritance types
```

### Point 8

Multiple/Hybrid inheritance can involve:

```text
MRO
Method Resolution Order
```

### Point 9

Python uses:

```text
C3 Linearization
```

to determine the MRO.

---

# 13. One-Line Interview Answers

### What is Inheritance?

> **Inheritance is an OOP mechanism that allows a child class to reuse and extend the attributes and methods of a parent class.**

### What is Single Inheritance?

> **Single inheritance occurs when a child class inherits from exactly one parent class.**

### What is Multiple Inheritance?

> **Multiple inheritance occurs when a child class inherits from more than one parent class.**

### What is Multilevel Inheritance?

> **Multilevel inheritance occurs when inheritance happens across multiple levels, such as Grandparent → Parent → Child.**

### What is Hierarchical Inheritance?

> **Hierarchical inheritance occurs when multiple child classes inherit from the same parent class.**

### What is Hybrid Inheritance?

> **Hybrid inheritance is a combination of two or more types of inheritance.**

### What is MRO?

> **MRO, or Method Resolution Order, is the order Python follows to search for methods and attributes in an inheritance hierarchy.**

### What does `super()` do?

> **`super()` provides access to the next class in the MRO and is commonly used to call inherited methods or constructors.**

---

# 14. Final Cheat Sheet

```text
                 INHERITANCE
                      |
       ┌──────────────┼──────────────┐
       |              |              |
   Single         Multiple       Multilevel
       |              |              |
    A → B          A   B          A → B → C
                    \ /
                     C

       ┌─────────────────────────────┐
       |                             |
  Hierarchical                    Hybrid
       |                             |
       A                             A
      / \                           / \
     B   C                         B   C
                                   \ /
                                    D
```

## Easy Memory Trick

```text
Single
= One Parent → One Child

Multiple
= Multiple Parents → One Child

Multilevel
= Grandparent → Parent → Child

Hierarchical
= One Parent → Multiple Children

Hybrid
= Combination of Multiple Types
```

## Most Important Relationship

```text
Inheritance
     ↓
IS-A
     ↓
Dog IS-A Animal
```

And remember:

```text
Composition
     ↓
HAS-A

Aggregation
     ↓
Weak HAS-A

Association
     ↓
USES / INTERACTS WITH
```

"""