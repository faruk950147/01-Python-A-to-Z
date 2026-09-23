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
