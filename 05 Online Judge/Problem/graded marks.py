
'''
# Grade Point Average
marks = {
    "Programming": 3.37,
    "Data Structure": 3.37,
    "Database": 3.37,
    "Web Development": 3.37,
    "Software Engineering": 3.61,
    "Computer Network": 3.50,
}

total = sum(marks.values())
print("Total GPA:", round(total/len(marks), 2))

'''

class GradeCalculator:
    def __init__(self):
        pass
    
    def calculate_cgpa(self, marks):
        total = sum(marks.values())
        return total / len(marks)
    
    def get_grade(self, cgpa):
        if cgpa >= 3.75:
            return "Excellent"
        elif cgpa >= 3.5:
            return "Good"
        elif cgpa >= 3.0:
            return "Average"
        else:
            return "Below Average"
    
    def grade_display(self, cgpa):
        print(self.get_grade(cgpa))
    
    def cgpa_display(self, marks):
        cgpa = self.calculate_cgpa(marks)
        print(cgpa)
        self.grade_display(cgpa)
    
    def result_display(self, marks):
        self.cgpa_display(marks)
        self.grade_display(self.calculate_cgpa(marks))

if __name__ == "__main__":
    grade_calculator = GradeCalculator()
    grade_calculator.result_display({
        "1st Semester": 3.37,
        "2nd Semester": 3.37,
        "3rd Semester": 3.37,
        "4th Semester": 3.37,
        "5th Semester": 3.61,
        "6th Semester": 3.50,
        "7th Semester": 3.45,
        "8th Semester": 4.00,
    })