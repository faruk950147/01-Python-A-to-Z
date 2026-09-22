# method 1 - list of dictionaries
faruk = {"C": 80, "C++": 90, "C#": 70}
tamim = {"Python": 80, "Java": 90, "JS": 70}
tonmoy = {"HTML": 80, "CSS": 90, "Bootstrap": 70}
students = [faruk, tamim, tonmoy]
lst = []
for student in students:
    sum1 = 0
    for item in student:
        sum1 += student[item]
    # print(sum1)
    lst.append(sum1)
print(lst)

# method 2 - using sum() function
students = [faruk, tamim, tonmoy]
lst = []
for student in students:
    total = sum(student.values())
    lst.append(total)
print(lst)

# method 3 - using enumerate()
students = [faruk, tamim, tonmoy]
for i, student in enumerate(students, start=1):
    total = sum(student.values())
    print(f"Student {i} Total = {total}")

# method 4 - using list comprehension
totals = [sum(student.values()) for student in students]
print("Total marks:", totals)

# method 5 with dictionary
students = {
    "Faruk": faruk,
    "Tamim": tamim,
    "Tonmoy": tonmoy
}

for name, marks in students.items():
    total = sum(marks.values())
    print(f"{name} Total = {total}")
    

# method 6 with nested dictionary
students = {
    "Faruk": {"C": 80, "C++": 90, "C#": 70, "Python": 85},
    "Tamim": {"Python": 80, "Java": 90, "JS": 70},
    "Tonmoy": {"HTML": 80, "CSS": 90, "Bootstrap": 70}
}

for name, marks in students.items():
    total = sum(marks.values())
    print(f"{name} Total = {total}")
    
students = {
    "Faruk": {"C": 80, "C++": 90, "C#": 70, "Python": 85},
    "Tamim": {"Python": 80, "Java": 90, "JS": 70},
    "Tonmoy": {"HTML": 80, "CSS": 90, "Bootstrap": 70}
}

# Create a dictionary of {name: total_marks} in one line
totals_dict = {name: sum(marks.values()) for name, marks in students.items()}

print(totals_dict)
# Output: {'Faruk': 325, 'Tamim': 240, 'Tonmoy': 240}