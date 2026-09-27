# ===================== what is Hierarchical Inheritance =====================
# Hierarchical Inheritance is a type of inheritance in which a class is child (derived)
# class of another class which is child (derived) class of another class.

# Base = Parent
# Derived = Child

class Parent:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"I'm from Parent class attribute name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Parent.__init__ of parent class
        self.age = age
        
    def display(self):
        super().display()  # Parent.display(self) of parent class
        print(f"I'm from Child class attribute age: {self.age}")

class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)  # Child.__init__ of child class
        self.address = address
        
    def display(self):
        super().display()  # Child.display(self) of child class
        print(f"I'm from GrandChild class attribute address: {self.address}")

grandChild = GrandChild("John", 20, "Bogura")
grandChild.display()
