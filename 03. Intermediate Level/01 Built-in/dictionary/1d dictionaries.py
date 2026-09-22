# Python Dictionary Notes

# ============================= 1. What is Dictionary? =============================

# A dictionary is a collection of key-value pairs.

# Dictionary is ordered, changeable (mutable), and does not allow duplicate keys.

# =================== Part 1 ============================
dict1 = {"name": "John", "age": 30}

# Dictionary using dict() constructor

dict2 = dict(name="John", age=30)

# Dictionary from a list of tuples

dict3 = dict([("name", "John"), ("age", 30)])

print(dict1["name"])  # John
print(dict2["age"])   # 30

# ============================= 2. Basic Dictionary =============================

# Access a value using its key

print(dict1["name"])  # John

# Modify an existing value

dict1["age"] = 31
dict2["age"] = 31

# Add a new key-value pair

dict1["city"] = "New York"
dict2["city"] = "New York"

print(dict1)
print(dict2)

print("=========================== 2. Basic Dictionary =============================")

# ============================= 3. Dictionary Access Functions =============================

dict3 = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

print(dict3)

# Access value using key

print(dict3["name"])  # Alice

# get() safely accesses a value.

# If the key does not exist, it returns None.

print(dict3.get("country"))  # None

# get() with a default value

print(dict3.get("country", "N/A"))  # N/A

# Get all keys

print(dict3.keys())

# Get all values

print(dict3.values())

# Get all key-value pairs

print(dict3.items())

print("=========================== 3. Dictionary Access Functions =============================")

# ============================= 4. Dictionary Add Functions =============================

dict4 = {"a": 1, "b": 2}

# Add one item

dict4["c"] = 3

# Add multiple items

dict4.update({
    "d": 4,
    "e": 5
})

print(dict4)

# Add only if the key does not already exist

dict4.setdefault("f", 6)

print(dict4)

print("=========================== 4. Dictionary Add Functions =============================")

# ============================= 5. Dictionary Modify Functions =============================

dict5 = {
    "a": 1,
    "b": 2,
    "c": 3
}

# Modify one value

dict5["a"] = 100

# Modify multiple values

dict5.update({
    "b": 200,
    "c": 300
})

# Add only if the key does not exist

dict5.setdefault("d", 400)

print(dict5)

print("=========================== 5. Dictionary Modify Functions =============================")

# ============================= 6. Dictionary Delete Functions =============================

dict6 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Delete a specific key-value pair

del dict6["name"]

# Remove a specific key and return its value

age_value = dict6.pop("age")

print("Popped age:", age_value)

# Remove and return the last inserted key-value pair

last_item = dict6.popitem()

print("Last item:", last_item)

# Remove all items

dict6.clear()

print(dict6)  # {}

# Delete the entire dictionary

del dict6

print("=========================== 6. Dictionary Delete Functions =============================")

# ============================= 7. Looping Dictionary =============================

dict7 = {
    "x": 10,
    "y": 20,
    "z": 30
}

# Loop through keys

for k in dict7.keys():
    print("Key:", k)

# Loop through values

for v in dict7.values():
    print("Value:", v)

# Loop through keys and values

for k, v in dict7.items():
    print("Key:", k, "Value:", v)

print("=========================== 7. Looping Dictionary =============================")

# ============================= 8. Dictionary Comprehension =============================

# Create a dictionary of squares

squares = {x: x * x for x in range(1, 6)}

print(squares)

# Create a dictionary of even numbers

evens = {x: x for x in range(10) if x % 2 == 0}

print(evens)

print("=========================== 8. Dictionary Comprehension =============================")

# ============================= 9. Dictionary Condition / Search =============================

dict8 = {
    "name": "John",
    "age": 31,
    "city": "New York"
}

# Search for values

values = [25, 31]

result = {
    k: v
    for k, v in dict8.items()
    if v in values
}

print(result)

# Check whether a key exists

key = "city"

if key in dict8:
    print(dict8[key])
else:
    print("Key not found")

print("=========================== 9. Dictionary Condition / Search =============================")

# ==================== 10. Nested Dictionary =======================

# A dictionary can contain another dictionary as a value.

studentMark = {
    "name": "Faruk",
    "department": "CSE",
    "subject": {
        "Math": 80,
        "English": 85,
        "Programming": 90
    }
}

# Access the Dictionary

print(studentMark)

# Access a Value

print(studentMark["name"])

# Access the Nested Dictionary

print(studentMark["subject"])

# Access a Value from the Nested Dictionary

print(studentMark["subject"]["Math"])

# Update

studentMark["subject"]["Programming"] = 95

print(studentMark)

# Add

studentMark["subject"]["Physics"] = 90

print(studentMark)

# Delete the Nested Dictionary

studentMark.pop("subject")

print(studentMark)

# Delete the Last Inserted Item

studentMark.popitem()

print(studentMark)

print("==================== 10. Nested Dictionary =======================")

# ============================= 11. Dictionary Method Summary =============================

# dict[key]       -> Access / modify a value

# get()            -> Safely access a value

# keys()           -> Get all keys

# values()         -> Get all values

# items()          -> Get all key-value pairs

# update()         -> Add / modify multiple items

# setdefault()     -> Add a key only if it does not exist

# pop()            -> Remove a specific key and return its value

# popitem()        -> Remove and return the last inserted item

# clear()          -> Remove all items

# del              -> Delete an item or the entire dictionary

# ============================= 12. Important Patterns =============================

# Access

# dict["key"]

# Safe access

# dict.get("key")

# Add

# dict["key"] = value

# Modify

# dict["key"] = new_value

# Add / modify multiple items

# dict.update({

# "a": 10,

# "b": 20

# })

# Delete

# del dict["key"]

# Delete and return value

# dict.pop("key")

# Check whether a key exists

# if "key" in dict:

# print("Exists")

# Loop through keys

# for key in dict:

# print(key)

# Loop through values

# for value in dict.values():

# print(value)

# Loop through keys and values

# for key, value in dict.items():

# print(key, value)

# Dictionary comprehension

# result = {

# key: value

# for key, value in iterable

# }
