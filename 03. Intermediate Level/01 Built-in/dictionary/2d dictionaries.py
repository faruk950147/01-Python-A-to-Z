
# ============================= 2. Basic Dictionary =============================

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

# ============================= 3. Dictionary Access Functions =============================

# Dictionary of Dictionary access
print(dict1["person1"]["name"])   # John
print(dict_list[1]["city"])       # Los Angeles

# List of Dictionary access
print(dict_list[0]["name"])       # John
print(dict_list[1]["city"])       # Los Angeles

# get() safe access
print(dict1.get("person3"))                 # None
print(dict1.get("person3", "Not Found"))    # Not Found

# keys, values, items
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# ============================= 4. Dictionary Add Functions =============================

dict1["person1"]["age"] = 31
dict1.update({
    "person3": {"name": "Alice", "age": 28, "city": "Chicago"}
})
dict1.setdefault("person4", {"name": "Bob", "age": 22, "city": "Miami"})

print(dict1)

# ============================= 5. Dictionary Modify Functions =============================

dict1["person1"]["age"] = 31
dict1.update({
    "person3": {"name": "Alice", "age": 28, "city": "Chicago"}
})
dict1.setdefault("person4", {"name": "Bob", "age": 22, "city": "Miami"})

print(dict1)

# ============================= 6. Dictionary Delete Functions =============================

# delete specific key
del dict1["person2"]

# pop() → remove and return value
removed = dict1.pop("person3")
print("Removed:", removed)

# popitem() → remove last inserted item
last_item = dict1.popitem()
print("Last item:", last_item)

# clear() → remove all items
dict1.clear()
print(dict1)

# ============================= 7. Looping Dictionary =============================

# loop through dictionary of dictionaries
for key, value in dict1.items():
    print(key)
    for inner_key, inner_value in value.items():
        print("   ", inner_key, "→", inner_value)

# loop through list of dictionaries
for item in dict_list:
    for key, value in item.items():
        print(key, "→", value)

# ============================= 8. Dictionary Comprehension =============================

squares = {x: x*x for x in range(1, 6)}
print(squares)

evens = {x: x for x in range(10) if x % 2 == 0}
print(evens)

# ============================= 9. Dictionary Condition Functions =============================

dict2 = {
    "person1": {"name": "John", "age": 31, "city": "New York"},
    "person2": {"name": "Jane", "age": 25, "city": "Los Angeles"}
}

values = [25, 31]
result = {k: v for k, v in dict2.items() if v["age"] in values}
print(result)

key = "person1"
if key in dict2:
    print(dict2[key])
else:
    print("Key not found")