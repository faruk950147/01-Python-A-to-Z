class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.id, self.name, self.salary)

class Company:
    def __init__(self, name):
        self.name = name
        # Accessing Employee class inside Company class (this is called composition)
        self.employee = Employee(123, "John", 5000)

    def display(self):
        print(self.name)
        # Accessing Employee class inside Company class (this is called composition)
        self.employee.display() 
if __name__ == "__main__":        
    # Creating Company class object
    company = Company("ABC")
    company.display()
    
class A:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(self.name)
        
class B:
    def __init__(self, age):
        self.age = age
        # this is called composition
        self.a = A("John")
        
    def display(self):
        print(self.age)
        self.a.display()
    
# Bonus (important interview point)
# composition is a "has-a" relationship
# ✔ Composition = flexible (recommended)
# ✔ Inheritance = tight coupling
# composition is better than inheritance