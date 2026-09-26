class Student:
    def __init__(self, name):
        self.name = name

    def show(self):   # instance method
        print(self.name)



class Student:
    school = "TMSS"

    @classmethod
    def change_school(cls, name): # class method
        cls.school = name
        print(cls)
        

class Math:
    
    @staticmethod
    def add(a, b):
        return a + b # static method
    
s1 = Student("Faruk")
s1.show()

Student.change_school("ABC School")
Student.school

Math.add(5, 3)