# ==========================================
# PYTHON DICTIONARY MASTER SCRIPT
# ==========================================

print("--- 1. CREATION & BASIC ACCESS ---")
# Different ways to create a dictionary
dict1 = {"name": "John", "age": 30}
dict2 = dict(name="John", age=30)
dict3 = dict([("name", "John"), ("age", 30)])

print("dict1:", dict1)
print("Access using key:", dict1["name"])


print("\n--- 2. BASIC OPERATIONS & MODIFICATIONS ---")
# Modify an existing value
dict1["age"] = 31
# Add a new key-value pair
dict1["city"] = "New York"
print("Modified dict1:", dict1)


print("\n--- 3. SAFE ACCESS METHODS (.get()) ---")
# .get() prevents KeyError if the key doesn't exist
print("Get existing key ('name'):", dict1.get("name"))
print("Get missing key (returns None):", dict1.get("country"))
print("Get missing key with default value:", dict1.get("country", "N/A"))


print("\n--- 4. VIEWS: KEYS, VALUES, ITEMS ---")
print("Keys:", list(dict1.keys()))
print("Values:", list(dict1.values()))
print("Items:", list(dict1.items()))


print("\n--- 5. ADD & MODIFY METHODS ---")
dict4 = {"a": 1, "b": 2}
# Add multiple items using update()
dict4.update({"c": 3, "d": 4})
# setdefault() adds the key only if it doesn't already exist
dict4.setdefault("e", 5)
dict4.setdefault("a", 999)  # Won't change 'a' because it already exists
print("dict4 after additions:", dict4)


print("\n--- 6. DELETE METHODS ---")
dict6 = {"name": "John", "age": 30, "city": "New York"}
del dict6["name"]  # Delete using del
print("After del 'name':", dict6)

popped_age = dict6.pop("age")  # Removes key and returns its value
print("Popped age value:", popped_age)
print("After pop('age'):", dict6)

last_item = dict6.popitem()  # Removes and returns the last inserted (key, value) tuple
print("Popped last item:", last_item)

dict6.clear()  # Empties the dictionary
print("After clear():", dict6)


print("\n--- 7. LOOPING THROUGH A DICTIONARY ---")
dict7 = {"x": 10, "y": 20, "z": 30}

print("Looping through keys:")
for key in dict7:
    print(f"  Key: {key}")

print("Looping through values:")
for value in dict7.values():
    print(f"  Value: {value}")

print("Looping through keys and values:")
for key, value in dict7.items():
    print(f"  Key: {key}, Value: {value}")


print("\n--- 8. DICTIONARY COMPREHENSION ---")
# Create a dictionary of squares
squares = {x: x * x for x in range(1, 6)}
print("Squares dictionary:", squares)

# Create a dictionary of even numbers with a condition
evens = {x: x for x in range(10) if x % 2 == 0}
print("Evens dictionary:", evens)


print("\n--- 9. SEARCHING & MEMBERSHIP ---")
dict8 = {"name": "John", "age": 31, "city": "New York"}
key_to_check = "city"

if key_to_check in dict8:
    print(f"Found key '{key_to_check}' with value:", dict8[key_to_check])
else:
    print("Key not found")


print("\n--- 10. NESTED STRUCTURES (Dict, List, Tuple, Set) ---")
# Nested Dictionary
student_mark = {
    "name": "Faruk",
    "department": "CSE",
    "subject": {
        "Math": 80,
        "Programming": 90
    },
    "hobbies": ["Coding", "Gaming"],       # List as value
    "coordinates": (12.34, 56.78),        # Tuple as value
    "skills": {"Python", "Git"}           # Set as value
}

print("Nested Math score:", student_mark["subject"]["Math"])
print("First hobby (List):", student_mark["hobbies"][0])

# Modifying a list inside a dictionary
student_mark["hobbies"].append("Reading")
print("Updated hobbies list:", student_mark["hobbies"])

# Modifying a set inside a dictionary
student_mark["skills"].add("SQL")
print("Updated skills set:", student_mark["skills"])

"""
| Method | Syntax | Description |
| :--- | :--- | :--- |
| **`clear()`** | `dict.clear()` | Removes all key-value pairs from the dictionary. |
| **`copy()`** | `dict.copy()` | Returns a shallow copy of the dictionary. |
| **`fromkeys()`** | `dict.fromkeys(keys, value)` | Creates a new dictionary with keys from the given sequence and assigns the specified value to all keys. The default value is `None`. |
| **`get()`** | `dict.get(key, default)` | Returns the value of the specified key. If the key does not exist, it returns `None` or the specified `default` value instead of raising a `KeyError`. |
| **`items()`** | `dict.items()` | Returns a view object containing all key-value pairs as `(key, value)` tuples. |
| **`keys()`** | `dict.keys()` | Returns a view object containing all keys in the dictionary. |
| **`pop()`** | `dict.pop(key, default)` | Removes the specified key and returns its value. If the key does not exist, it returns the `default` value or raises a `KeyError` if no default is provided. |
| **`popitem()`** | `dict.popitem()` | Removes and returns the last inserted key-value pair as a `(key, value)` tuple. |
| **`setdefault()`** | `dict.setdefault(key, default)` | Returns the value of the specified key if it exists. If the key does not exist, it inserts the key with the specified default value and returns that value. |
| **`update()`** | `dict.update(other)` | Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs. Existing keys are overwritten. |
| **`values()`** | `dict.values()` | Returns a view object containing all values in the dictionary. |
"""