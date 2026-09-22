# ==========================================
# PART 1: List of Dictionaries (Anonymous Data)
# ==========================================

data = [
    {"C": 80, "Python": 99, "C#": 70},
    {"Python": 80, "Java": 90, "JS": 70},
    {"HTML": 80, "CSS": 90, "Bootstrap": 70}
]

# Method 1: Manual accumulation loop
print("--- Method 1: Manual Loop ---")
lst = []
for student in data:
    sum1 = 0
    for item in student:
        sum1 += student[item]
    lst.append(sum1)
print("Totals:", lst)


# Method 2: List comprehension with sum()
print("\n--- Method 2: List Comprehension & sum() ---")
lst = [sum(student.values()) for student in data]
print("Totals:", lst)


# Method 3: Using enumerate() with index labels
print("\n--- Method 3: Using enumerate() ---")
for i, student in enumerate(data, start=1):
    total = sum(student.values())
    print(f"Student {i} Total = {total}")


# ==========================================
# PART 2: Nested Dictionaries (Named Data)
# ==========================================

students = {
    "Faruk": {"C": 80, "C++": 90, "C#": 70, "Python": 85},
    "Tamim": {"Python": 80, "Java": 90, "JS": 70},
    "Tonmoy": {"HTML": 80, "CSS": 90, "Bootstrap": 70}
}

# Method 4: Iterating over nested dictionary with .items()
print("\n--- Method 4: Nested Dictionary Loop with Names ---")
for name, marks in students.items():
    total = sum(marks.values())
    print(f"{name}'s Total = {total}")


# Method 5: Dictionary comprehension (One-liner mapping name to total)
print("\n--- Method 5: Dictionary Comprehension ---")
totals_dict = {name: sum(marks.values()) for name, marks in students.items()}
print("Totals Dictionary:", totals_dict)
