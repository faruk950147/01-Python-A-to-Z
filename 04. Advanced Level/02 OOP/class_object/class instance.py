class Human:
    # Class variable (shared by all instances)
    species = "Homo sapiens"

    def __init__(self, name, age):
        # Instance variables (unique for each object)
        self.name = name
        self.age = age

    # Instance methods (require an object)
    # They carry the object reference (self)
    def showName(self):
        print(f"Name: {self.name}")

    def showAge(self):
        print(f"Age: {self.age}")

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
    # Class method (does not require an object)
    # It carries the class reference (cls)
    # Can access and modify class variables
    @classmethod # why use class method? because it can access and modify class variables
    def showClassName(cls):
        print(f"Class Name: {cls.__name__}")
        print(f"Species: {cls.species}")

    # Static method (requires neither object nor class reference)
    # It carries no reference
    # Used for general-purpose utility work
    @staticmethod # why use static method? because it requires neither object nor class reference   
    def showClassInfo():
        print("This is the Human class, representing all human beings.")
        

if __name__ == "__main__":
    # Creating an object (instance)
    human = Human("Faruk", 22)

    # Instance method examples (object required)
    human.showName()
    human.showAge()
    human.showInfo()

    print("------------------------")

    # Class method examples (no object required)
    Human.showClassName()

    print("------------------------")

    # Static method examples (no object or class reference required)
    Human.showClassInfo()
