# ========================== what is destructor =========================
# destructor is a special method that is called when an object is destroyed.
# destructor is denoted by __del__

# ========================== example =========================
class Employee:
    def __init__(self, name):
        self.name = name
        print(f"Employee {self.name} is created")
        
    def __del__(self):
        print(f"Employee {self.name} is deleted")
        
if __name__ == "__main__":  
    # creating object
    emp = Employee("John")
    # deleting object
    del emp
