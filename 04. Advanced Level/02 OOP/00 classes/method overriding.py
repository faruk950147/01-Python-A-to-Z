# ====================== What is Method Overriding ======================

"""
Method Overriding is a feature of Object-Oriented Programming (OOP)
that allows a subclass (child class) to provide its own implementation
of a method that is already defined in its parent class.

The child class keeps the same method name but changes the behavior
of that method.

Method Overriding is commonly used to achieve Runtime Polymorphism.
"""


# ====================== Parent Class ======================

class Parent:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Parent class show method:", self.name)


# ====================== Child Class ======================

class Child(Parent):

    def __init__(self, name):
        super().__init__(name)

    def show(self):
        # Method Overriding
        print("Child class show method:", self.name)

        # Optional:
        # Call the parent class version of show()
        super().show()


# ====================== Main Program ======================

if __name__ == "__main__":

    child = Child("FR")

    child.show()


# ====================== Output ======================

"""
Child class show method: FR
Parent class show method: FR
"""


# ====================== How Method Overriding Works ======================

"""
Parent
   |
   | show()
   |
   v
Child
   |
   | show()  ← Overridden method
   |
   v
Child's own implementation
"""


# ====================== Calling the Child Method ======================

"""
When we write:

child.show()

Python finds show() in the Child class first.

Therefore:

def show(self):
    print("Child class show method:", self.name)

is executed instead of the parent's:

def show(self):
    print("Parent class show method:", self.name)
"""


# ====================== Using super() ======================

"""
Inside the overridden method:

super().show()

calls the parent class's version of the method.
"""


class Parent:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Parent class show method:", self.name)


class Child(Parent):

    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print("Child class show method:", self.name)
        super().show()


# Output:
#
# Child class show method: FR
# Parent class show method: FR


# ====================== Without super().show() ======================

class ChildWithoutSuper(Parent):

    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print("Child class show method:", self.name)


"""
If we remove:

super().show()

only the child's overridden method runs.

Output:

Child class show method: FR
"""


# ====================== Different Ways to Initialize Parent ======================

# 1. Using super() — Recommended

class Child1(Parent):

    def __init__(self, name):
        super().__init__(name)


# 2. Using Parent Class Name

class Child2(Parent):

    def __init__(self, name):
        Parent.__init__(self, name)


# 3. Assigning the Attribute Yourself

class Child3(Parent):

    def __init__(self, name):
        self.name = name


"""
These examples are about calling the parent constructor,
not different forms of method overriding.
"""


# ====================== Using super() ======================

class Parent:

    def __init__(self, name):
        self.name = name


class Child(Parent):

    def __init__(self, name):
        super().__init__(name)


"""
super().__init__(name)

calls the parent class constructor.
"""


# ====================== Using Parent Class Name ======================

class Child(Parent):

    def __init__(self, name):
        Parent.__init__(self, name)


"""
This directly calls the parent constructor.
"""


# ====================== Assigning the Attribute Yourself ======================

class Child(Parent):

    def __init__(self, name):
        self.name = name


"""
This does NOT call the parent constructor.

It works in a simple example because the parent constructor
only does:

self.name = name

But if the parent constructor contains additional initialization,
those attributes will not be initialized.
"""


# ====================== Example ======================

class Parent:

    def __init__(self, name):
        self.name = name
        self.age = 20
        self.address = "Dhaka"


class Child(Parent):

    def __init__(self, name):
        self.name = name


"""
Here:

self.age
self.address

will not be initialized because the parent constructor
was not called.

Therefore, when the child should use the parent's initialization,
calling:

super().__init__(name)

is generally preferable.
"""


# ====================== Method Overriding vs Method Overloading ======================

"""
Method Overriding
-----------------

Parent and child classes have methods with the same name.

Example:
"""


class Parent:

    def show(self):
        print("Parent")


class Child(Parent):

    def show(self):
        print("Child")


"""
Here:

Parent → show()
Child  → show()  ← Overridden
"""


# ====================== Method Overloading ======================

"""
Method Overloading traditionally means having multiple methods
with the same name but different parameter lists.

Python does not support traditional method overloading
in the same way as languages such as Java or C++.
"""


# ====================== Simple Definition ======================

"""
Method Overriding
        =
Child class redefines a method
of its parent class
"""


# ====================== Easy Way to Remember ======================

"""
Parent:
    show()
       ↓
Child:
    show()
       ↓
Override
"""


# ====================== Key Point ======================

"""
super() is NOT what makes overriding happen.

The overriding happens because the child defines a method
with the same name as the inherited parent method.

super() is simply a way to explicitly use the parent implementation.
""" 