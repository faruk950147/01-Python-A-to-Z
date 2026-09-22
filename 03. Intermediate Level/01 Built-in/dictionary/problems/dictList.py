# 1. There is a dictionary containing student data. 
# and how fetch the last key-value pair from the dictionary.
students = {
    "name": "Faruk",
    "age": 21,
    "gender": "Male",
    "course": "BSc in CSE",
    "cgpa": 3.5,
    "courses": ["CSE", "EEE", "BBA"]
}
# names = list(students.keys())
# print(f"{names[-1]}: {students[names[-1]]}")  # access the last key and its value
# print(names[-1])  # access the last key
# print(students[names[-1]])  # access the value of the last key

# 2. write a program to count the number of items having list as value.

# count = 0
# for value in students.values():
#     if isinstance(value, list):
#         count += 1
# print(count)

# names = list(students.keys())
# if isinstance(names, list):
#     for name in names:
#         print(name)
# else:
#     print("names is not a list")

# print the list of elements in courses


# Check if courses is a list
if isinstance(students["courses"], list):
    for course in students["courses"]:
        print(course)
else:
    print("courses is not a list")
    
if isinstance(students["courses"], list):
    for course in range(len(students["courses"])):
        print(students["courses"][course])
else:
    print("courses is not a list")