'''
class Student:
    def __init__(self, name, record):
        self.name = name
        self.roll = record["details"]["roll"]
        self.dept = record["details"]["dept"]
        self.marks = record["details"]["marks"]

    def percentage(self):
        return sum(self.marks.values()) / len(self.marks)

students_dict = {
    "faruk": {"details": {"roll": 101, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}, 
    "tom": {"details": {"roll": 102, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}, 
    "jerry": {"details": {"roll": 103, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}
}

students = [Student(name, data) for name, data in students_dict.items()]

for student in students:
    print(f"{student.name} (Roll: {student.roll}, Dept: {student.dept}) : {student.percentage():.2f} %")

'''


def calculate_percentages(students):
    for student in students:
        marks = students[student]["details"]["marks"]
        length = len(marks)
        percentage = sum(marks.values()) / length
        print(f"{student} : {percentage:.2f} %")

students = {
    "faruk": {"details": {"roll": 101, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}, 
    "tom": {"details": {"roll": 102, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}, 
    "jerry": {"details": {"roll": 103, "dept": "CSE", "marks": {"C": 85, "C++": 80, "Python": 85, "DS": 90, "DBMS": 88, "OS": 92, "CN": 95}}}
}

calculate_percentages(students)


