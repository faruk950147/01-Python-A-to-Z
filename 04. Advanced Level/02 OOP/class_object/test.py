class Student:
    school = "TMSS"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def show(self):
        print(self.name)

    # Class Method
    @classmethod
    def change_school(cls, name):
        cls.school = name
        print(cls)

    
class Math:

    # Static Method
    @staticmethod
    def add(a, b):
        return a + b


if __name__ == '__main__':
    # Instance method
    s1 = Student("Faruk")
    s1.show()

    # Class method
    Student.change_school("ABC School")
    print(Student.school)

    # Static method
    result = Math.add(5, 3)
    print(result)
