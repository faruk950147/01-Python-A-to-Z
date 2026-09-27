# ===================== What is Inheritance =====================

# Inheritance is a mechanism in which a new class is (derived) 
# child class from an existing class.
# The new class is called (Derived) child class and the existing class is called 
# (Base) parent class.
# Base = Parent
# Derived = Child

# Types of Inheritance
# 1. Single Inheritance
    # A child class inherits from only one parent class.
    # one parent inherit from one child
    # Parent -> Child
    # Parent
    #   |
    # Child
    
# ===================== Single Inheritance Example =====================
class Parent:
    def greet_parent(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")


c = Child()
c.greet_parent()
c.greet_child()



# 2. Multiple Inheritance
    # A child class inherits from more than one parent class.
#   Parent1 -> Parent2 -> Child  all parent inherit from one child
#   Parent1   Parent2
#      \     /
#       Child

# ===================== Multiple Inheritance Example =====================
class Parent1:
    def greet_parent1(self):
        print("Hello from Parent1")

class Parent2:
    def greet_parent2(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet_parent1()
c.greet_parent2()
c.greet_child()

# 3. Multilevel Inheritance
    # A child class inherits from a parent class, which itself inherits from another class.
    # Parent -> Child -> GrandChild
    # Parent
    #   |
    #   Child
    #   |
    #   GrandChild
    
    
# ===================== Multilevel Inheritance Example =====================
class Grandparent:
    def greet_grandparent(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greet_parent(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet_grandparent()
c.greet_parent()
c.greet_child()

    
    
# 4. Hierarchical Inheritance
    # Multiple child classes inherit from a single parent class.
#       Parent
#       /    \
#   Child1  Child2

# ===================== Hierarchical Inheritance Example =====================
class Parent:
    def greet_parent(self):
        print("Hello from Parent")

class Child1(Parent):
    def greet_child1(self):
        print("Hello from Child1")

class Child2(Parent):
    def greet_child2(self):
        print("Hello from Child2")

c1 = Child1()
c2 = Child2()
c1.greet_parent()
c2.greet_parent()



# 5. Hybrid Inheritance
    # Hybrid inheritance is a combination of multiple and multilevel inheritance.
    # Structure:
    # Multiple parents + multilevel chain
    
    
# ===================== Hybrid Inheritance Example =====================
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



