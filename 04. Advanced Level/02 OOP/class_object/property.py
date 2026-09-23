# Property is a built-in decorator in Python that allows you to define methods in a class that can be accessed like attributes. 
# and it is used to define a method in a class that can be accessed like an attribute.

"""
# 1. Without using property 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.percentage = self.marks / 500 * 100


if __name__ == "__main__":
    s = Student("Faruk", 400)
    print("Without using property:",s.percentage)   # Attribute access

"""
# 2. Using property 
class Employee:
    """ 
    প্রশ্ন: কেন দুইবার salary নাম ব্যবহার করা হয়েছে?

    উত্তর:

    Python property mechanics এর কারণে

    প্রথমে @property দিয়ে salary নামে getter function বানানো হয়েছে।

    এরপর @salary.setter দিয়ে উই একই নাম ব্যবহার করে setter attach করি।

    এটা Python-এর convention: getter এবং setter এর নাম একই হতে হবে, কারণ তারা একই property কে handle করছে।

    Getter = "আমি কীভাবে value পড়ব"

    Setter = "আমি কীভাবে value লিখব"

    দুটোই salary property এর অংশ → তাই নাম একই রাখা হয়।
    """
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # "_" thats means indicate it's "protected" variable

    # Getter
    # @property is used to define a method in a class that can be accessed like an attribute.
    # binding is a process of binding a method to an object.
    # same name binding is a process of binding a method to an object. because it's same name.Python understand it's a getter.
    # it's good practice to use property decorator.
    # salary (property) it's binding a method to an object.
    # ├─ getter -> salary(self) return _salary
    # ├─ setter -> salary(self, value) set _salary = value
    # └─ deleter -> salary(self) delete _salary
    @property
    def salary(self):
        if self._salary is None:
            return "Salary is not set!"
        else:
            return self._salary

    # Setter
    # @salary.setter is used to define a method in a class that can be accessed like an attribute.
    # binding is a process of binding a method to an object.
    # same name binding is a process of binding a method to an object. because it's same name.Python understand it's a setter.
    # it's good practice to use property decorator.
    # salary (property) it's binding a method to an object.
    # ├─ getter -> salary(self) return _salary
    # ├─ setter -> salary(self, value) set _salary = value
    # └─ deleter -> salary(self) delete _salary
    @salary.setter
    def salary(self, value):
        if value < 0 and isinstance(value, float):
            return "Salary cannot be negative!"
        else:
            self._salary = value

    # Deleter
    # @salary.deleter is used to define a method in a class that can be accessed like an attribute.
    # binding is a process of binding a method to an object.
    # same name binding is a process of binding a method to an object. because it's same name.Python understand it's a deleter.
    # it's good practice to use property decorator.
    # salary (property) it's binding a method to an object.
    # ├─ getter -> salary(self) return _salary
    # ├─ setter -> salary(self, value) set _salary = value
    # └─ deleter -> salary(self) delete _salary
    @salary.deleter
    def salary(self):
        if self._salary is not None:
            print("Deleting salary...")
            del self._salary
        else:
            return "Salary is already deleted!"

if __name__ == "__main__":
    e = Employee("Faruk", 50000)
    print("Using property:",e.salary)   # Getter called
    e.salary = 60000  # Setter called
    print("Using property:",e.salary)
    del e.salary      # Deleter called

