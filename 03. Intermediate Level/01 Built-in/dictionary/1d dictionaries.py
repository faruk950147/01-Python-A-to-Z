# ===================== What is Dictionary =====================

# ============================= 2. Basic Dictionary =============================

dict1 = {"name": "John", "age": 30}

dict2 = dict(name="John", age=30)

dict3 = dict([("name", "John"), ("age", 30)])

print(dict1["name"])   # John
print(dict2["age"])    # 30

dict1["age"] = 31
dict2["age"] = 31

dict1["city"] = "New York"
dict2["city"] = "New York"

print("=========================== 2. Basic Dictionary =============================")


# ============================= 3. Dictionary Access Functions =============================

dict3 = {"name": "Alice", "age": 25, "city": "London"}

print(dict3)

print(dict3["name"])

print(dict3.get("country"))
print(dict3.get("country", "N/A"))

print(dict3.keys())
print(dict3.values())
print(dict3.items())

print("=========================== 3. Dictionary Access Functions =============================")


# ============================= 4. Dictionary Add Functions =============================

dict4 = {"a": 1, "b": 2}

dict4["c"] = 3

dict4.update({"d": 4, "e": 5})

print(dict4)

dict4.setdefault("f", 6)

print(dict4)

print("=========================== 4. Dictionary Add Functions =============================")


# ============================= 5. Dictionary Modify Functions =============================

dict5 = {"a": 1, "b": 2, "c": 3}

dict5["a"] = 100

dict5.update({"b": 200, "c": 300})

dict5.setdefault("d", 400)

print(dict5)

print("=========================== 5. Dictionary Modify Functions =============================")


# ============================= 6. Dictionary Delete Functions =============================

dict6 = {"name": "John", "age": 30, "city": "New York"}

del dict6["name"]

age_value = dict6.pop("age")
print("Popped age:", age_value)

last_item = dict6.popitem()
print("Last item:", last_item)

dict6.clear()
print(dict6)

del dict6

print("=========================== 6. Dictionary Delete Functions =============================")


# ============================= 7. Looping Dictionary =============================

dict7 = {"x": 10, "y": 20, "z": 30}

for k in dict7.keys():
    print("Key:", k)

for v in dict7.values():
    print("Value:", v)

for k, v in dict7.items():
    print("Key:", k, "Value:", v)

print("=========================== 7. Looping Dictionary =============================")


# ============================= 8. Dictionary Comprehension =============================

squares = {x: x*x for x in range(1, 6)}
print(squares)

evens = {x: x for x in range(10) if x % 2 == 0}
print(evens)

print("=========================== 8. Dictionary Comprehension =============================")


# ============================= 9. Dictionary Condition / Search =============================

dict8 = {"name": "John", "age": 31, "city": "New York"}

values = [25, 31]
result = {k: v for k, v in dict8.items() if v in values}
print(result)

key = "city"

if key in dict8:
    print(dict8[key])
else:
    print("Key not found")

print("=========================== 9. Dictionary Condition Functions =============================")