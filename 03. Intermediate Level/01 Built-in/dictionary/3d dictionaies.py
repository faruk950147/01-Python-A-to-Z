# ============================= 1. Basic Dictionary =============================

# Dictionary of Dictionaries (3D)

dict1 = {

    "dept1": {

        "person1": {
            "name": "John",
            "age": 31,
            "city": "New York"
        },

        "person2": {
            "name": "Jane",
            "age": 25,
            "city": "Los Angeles"
        }
    },

    "dept2": {

        "person3": {
            "name": "Alice",
            "age": 28,
            "city": "London"
        },

        "person4": {
            "name": "Bob",
            "age": 35,
            "city": "Paris"
        }
    }

}

# List of Dictionaries (3D)

list1 = [

    {

        "dept1": {

            "person1": {
                "name": "John",
                "age": 31,
                "city": "New York"
            },

            "person2": {
                "name": "Jane",
                "age": 25,
                "city": "Los Angeles"
            }
        },

        "dept2": {

            "person3": {
                "name": "Alice",
                "age": 28,
                "city": "London"
            },

            "person4": {
                "name": "Bob",
                "age": 35,
                "city": "Paris"
            }
        }
    }

]

# ============================= 2. Dictionary Access Functions =============================

# Dictionary of Dictionaries access

print(dict1["dept1"]["person1"]["name"])     # John
print(dict1["dept1"]["person2"]["age"])      # 25

# List of Dictionaries access

print(list1[0]["dept1"]["person1"]["name"])  # John
print(list1[0]["dept1"]["person2"]["age"])   # 25

# ============================= 3. Dictionary Add Functions =============================

# Add a new person to dept1

dict1["dept1"]["person5"] = {
    "name": "David",
    "age": 40,
    "city": "Boston"
}

# Add a new person to dept2

dict1["dept2"]["person6"] = {
    "name": "Mike",
    "age": 29,
    "city": "Chicago"
}

# Add to List of Dictionaries

list1[0]["dept1"]["person5"] = {
    "name": "David",
    "age": 40,
    "city": "Boston"
}

list1[0]["dept2"]["person6"] = {
    "name": "Mike",
    "age": 29,
    "city": "Chicago"
}

print(dict1)
print(list1)

# ============================= 4. Dictionary Modify Functions =============================

# Modify nested value

dict1["dept1"]["person1"]["age"] = 32

dict1["dept2"]["person4"]["age"] = 36

# Modify nested value in List of Dictionaries

list1[0]["dept1"]["person1"]["age"] = 32

list1[0]["dept2"]["person4"]["age"] = 36

print(dict1)
print(list1)

# ============================= 5. Dictionary Delete Functions =============================

# pop() → Delete a specific person

dict1["dept1"].pop("person5")

# pop() → Delete an entire department

dict1.pop("dept2")

# Delete from List of Dictionaries

list1[0]["dept1"].pop("person5")

list1[0].pop("dept2")

print(dict1)
print(list1)

# ============================= 6. Looping Dictionary =============================

# Loop through Dictionary of Dictionaries

for dept, persons in dict1.items():
    print(f"Department: {dept}")

    for person, data in persons.items():
        print(f"  Person: {person}")

        for key, value in data.items():
            print(f"    {key} → {value}")


# Loop through List of Dictionaries

for dic in list1:
    for dept, persons in dic.items():

        print(f"Department: {dept}")

        for person, data in persons.items():

            print(f"  Person: {person}")

            for key, value in data.items():

                print(f"    {key} → {value}")


# ============================= 7. Dictionary Comprehension =============================

# Square of numbers

squares = {
    x: x ** 2
    for x in range(1, 6)
}

print(squares)

# Even number squares

even_squares = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)

# ============================= 8. Dictionary Condition Functions =============================

dictA = {
    "a": 1,
    "b": 2,
    "c": 3
}

dictB = {
    "a": 1,
    "b": 2,
    "c": 3
}

dictC = {
    "a": 1,
    "b": 5,
    "d": 9
}

# Compare dictionaries

print(dictA == dictB)        # True
print(dictA == dictC)        # False

# Check key existence

print("a" in dictA)          # True
print("z" in dictA)          # False

# Check value existence

print(2 in dictA.values())   # True
print(9 in dictA.values())   # False

# Common keys

print(dictA.keys() & dictC.keys())

# {'a'}

# Keys in dictA but not in dictC

print(dictA.keys() - dictC.keys())

# {'b', 'c'}

# Common key-value pairs

print(dictA.items() & dictC.items())

# {('a', 1)}
