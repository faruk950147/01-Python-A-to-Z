class University:
    def __init__(self, name):
        self.name = name
        # class of University current object
        
    def display(self):
        print(self.name)
    # Nested class for Department
    class Department:
        def __init__(self, name):
            self.name = name

        def display(self):
            print(self.name)
if __name__ == "__main__":
    u = University("TMSS Technical University")
    u.display()
    department1 = u.Department("CSE")
    department2 = u.Department("EEE")

    department1.display()  # CSE
    department2.display()  # EEE

class University:
    def __init__(self, name):
        self.name = name
        self.department = self.Department("Department")  # default department
        
    def display(self):
        print(self.name)

    class Department:
        def __init__(self, name):
            self.name = name

        def display(self):
            print(self.name)


if __name__ == "__main__":
    u = University("TMSS Technical University")
    u.display()  # prints "TMSS Technical University"
    u.department.display()  # prints "Department"
    u.department1 = University.Department("CSE")
    u.department2 = University.Department("EEE")

    u.department1.display()  # prints "CSE"
    u.department2.display()  # prints "EEE"

