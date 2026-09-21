# ============================= 1. Basic Dictionary =============================

# Dictionary of Dictionaries (2D)

dict1 = {
    "person1": {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    }
}

# List of Dictionaries (2D)

dict_list = [
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    }
]

# ============================= 2. Dictionary Access Functions =============================

# Dictionary of Dictionary access

print(dict1["person1"]["name"])       # John
print(dict1["person2"]["city"])       # Los Angeles

# List of Dictionary access

print(dict_list[0]["name"])           # John
print(dict_list[1]["city"])           # Los Angeles

# get() → Safe access

print(dict1.get("person3"))                # None
print(dict1.get("person3", "Not Found"))   # Not Found

# keys(), values(), items()

print(dict1.keys())
print(dict1.values())
print(dict1.items())

# ============================= 3. Dictionary Add Functions =============================

# Add a new key-value pair

dict1["person3"] = {
    "name": "Alice",
    "age": 28,
    "city": "Chicago"
}

# update() → Add multiple key-value pairs

dict1.update({
    "person4": {
    "name": "Bob",
    "age": 22,
    "city": "Miami"
    }
})

# setdefault() → Add key if it does not exist

dict1.setdefault("person5", {
    "name": "David",
    "age": 35,
    "city": "Boston"
})

print(dict1)

# ============================= 4. Dictionary Modify Functions =============================

# Modify a specific value

dict1["person1"]["age"] = 31

# Modify multiple values

dict1["person2"].update({
    "age": 26,
    "city": "San Francisco"
})

print(dict1)

# ============================= 5. Dictionary Delete Functions =============================

# del → Delete a specific key

del dict1["person5"]

print(dict1)

# pop() → Remove and return a specific value

removed = dict1.pop("person4")

print("Removed:", removed)

# popitem() → Remove and return the last inserted item

last_item = dict1.popitem()

print("Last item:", last_item)

# clear() → Remove all items

dict1.clear()

print(dict1)     # {}

# ============================= 6. Looping Dictionary =============================

# Create dictionary again for looping

dict1 = {
    "person1": {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    }
}

# Loop through Dictionary of Dictionaries

for key, value in dict1.items():
    print(key)

    for inner_key, inner_value in value.items():
        print("   ", inner_key, "→", inner_value)


# Loop through List of Dictionaries

for item in dict_list:
    for key, value in item.items():
        print(key, "→", value)


# ============================= 7. Dictionary Comprehension =============================

# Create squares dictionary

squares = {
    x: x * x for x in range(1, 6)
}

print(squares)

# Create dictionary containing only even numbers

evens = {
    x: x for x in range(10) if x % 2 == 0
}

print(evens)

# ============================= 8. Dictionary Condition Functions =============================

dict2 = {
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
}

# Filter dictionary based on age

values = [25, 31]

result = {k: v for k, v in dict2.items() if v["age"] in values}

print(result)

# Check whether a key exists

key = "person1"

if key in dict2:
    print(dict2[key])
else:
    print("Key not found")
