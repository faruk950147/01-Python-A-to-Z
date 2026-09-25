# ======================= What is object =================================
# Object is an instance of a class.
# Class is the blueprint, and object is the real-world entity created from it.

# ======================= How to create an object =========================
# 1. Create an object using the class name.
# 2. Create an object using the class name and pass the arguments to the constructor.
# 3. Create an object using the class name and pass the arguments to the constructor and assign it to a variable.

# ======================= How to access an object =========================
# 1. Access an object using the object name.
# 2. Access an object using the object name and the attribute name.
# 3. Access an object using the object name and the attribute name and the method name.

# ======================= How to delete an object =========================
# 1. Delete an object using the del keyword.
# 2. Delete an object using the del keyword and the object name.
# 3. Delete an object using the del keyword and the object name and the attribute name.

# ======================= Example Class ============================
class Cartoon:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")


# ======================= Object Creation ============================
# 1. Using class name
cartoon1 = Cartoon("Tom", 5)

# 2. Accessing object attributes
print(cartoon1.name)
print(cartoon1.age)

# 3. Accessing object methods
cartoon1.showInfo()

# ======================= Deleting object/attribute ==================
# Delete specific attribute
del cartoon1.age

# Delete whole object
del cartoon1


# ======================= Built-in Objects ===========================
# int object
obj = 70
print(type(obj))   # <class 'int'>
print(obj)

# float object
obj = 3.14
print(type(obj))   # <class 'float'>
print(obj)

# str object
obj = "Cartoon"
print(type(obj))   # <class 'str'>
print(obj)

# list object
obj = [1, 2, 3]
print(type(obj))   # <class 'list'>
print(obj)

# tuple object
obj = (1, 2, 3)
print(type(obj))   # <class 'tuple'>
print(obj)

# dict object
obj = {"name": "Tom", "age": 5}
print(type(obj))   # <class 'dict'>
print(obj)
class Cartoon:
    pass

if __name__ == "__main__":
    cartoon = Cartoon()
    print(cartoon)
    
class Cartoon:
    # default constructor
    # def __init__(self):
    #     pass
    # instance variables and parameterized constructor
    def __init__(self, name, age):
        self.name = name    # instance variable 'name'
        self.age = age      # instance variable 'age'

    # instance method
    def display(self):
        print(self.name, self.age)
if __name__ == "__main__":
    cartoon = Cartoon("Cartoon", 10)
    cartoon.display()

class Cartoon:
    # class variables
    name = "Cartoon"    # class variable 'name'
    age = 10            # class variable 'age'

    # instance method
    def display(self):
        print(self.name, self.age)
if __name__ == "__main__":
    cartoon = Cartoon("Cartoon", 10)
    cartoon.display()
    
    
class Cartoon:
    name = "Cartoon"   # class variable
    age = 10           # class variable
    
    # default constructor
    # def __init__(self):
    #     pass
    
    # instance variables and parameterized constructor
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age      # instance variable

    # instance method
    def display(self):
        print(self.name, self.age)
        print(Cartoon.name, Cartoon.age)

if __name__ == "__main__":
    cartoon = Cartoon("Tom", 5)
    cartoon.display()
