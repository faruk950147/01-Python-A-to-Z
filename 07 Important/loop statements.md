# Python Internals Notes — List, Dict, Set, Tuple এবং Square Root Algorithm

# Part 1: Python Core Data Structures

## 1. List Internals

### 1.1 List কী?

Python-এর `list` হলো একটি ordered collection, যেখানে একাধিক item রাখা যায়।

**বৈশিষ্ট্য:**
- Ordered — item-এর অবস্থান বজায় থাকে।
- Mutable — item পরিবর্তন, যোগ বা মুছে ফেলা যায়।
- Duplicates allowed — একই value একাধিকবার থাকতে পারে।
- বিভিন্ন data type-এর item রাখা যায়।

### Example

```python
numbers = [10, 20, 30, 20]

print(numbers)
# [10, 20, 30, 20]
```

### 1.2 List-এর Internals

Python-এর `list` মূলত একটি **dynamic array**-এর মতো কাজ করে। CPython implementation-এ এটি `PyListObject` দিয়ে বাস্তবায়িত।

Dynamic array-এর অর্থ হলো, list-এর item বাড়লে প্রয়োজন অনুযায়ী তার storage capacity বাড়ানো যায়।

```python
numbers = [10, 20, 30]
numbers.append(40)

print(numbers)
# [10, 20, 30, 40]
```

### 1.3 Over-allocation কী?

Python list সাধারণত প্রতিটি `append()`-এর জন্য নতুন memory allocate করে না। প্রয়োজন অনুযায়ী অতিরিক্ত capacity রাখে, যাতে বারবার memory resize করতে না হয়।

ধারণাগত উদাহরণ:

```text
List items:     [10, 20, 30]
Allocated space: [10, 20, 30, _, _, _]
```

এটি শুধু বোঝার জন্য উদাহরণ; প্রকৃত capacity Python-এর implementation ও list-এর আকার অনুযায়ী পরিবর্তিত হয়।

### 1.4 List-এর Time Complexity

| Operation | Time Complexity |
|---|---|
| Index দিয়ে access | O(1) |
| Append | Amortized O(1) |
| Insert at beginning | O(n) |
| Insert in middle | O(n) |
| Remove by value | O(n) |
| Pop from end | O(1) |
| Search by value | O(n) |
| Sort | O(n log n) — সাধারণ worst-case bound |

**Amortized O(1)** অর্থ হলো, অনেকগুলো append operation একসঙ্গে বিবেচনা করলে প্রতি operation-এর গড় খরচ O(1)। তবে কোনো একটি resize-এর সময় O(n) লাগতে পারে।

### 1.5 Insert ও Delete ধীর কেন?

```python
numbers = [10, 20, 30]
numbers.insert(1, 99)

print(numbers)
# [10, 99, 20, 30]
```

Index `1`-এ `99` বসানোর জন্য পরের item-গুলোকে সরাতে হয়।

```text
Before: [10, 20, 30]
After:  [10, 99, 20, 30]
```

তাই list-এর শুরুতে বা মাঝখানে insert/delete সাধারণত O(n)।

**মনে রাখবে:** List ব্যবহার করবে যখন order বজায় রাখা, indexing এবং item পরিবর্তন করা দরকার।

---

## 2. Dictionary Internals

### 2.1 Dictionary কী?

Python-এর `dict` হলো একটি mutable collection, যা `key: value` pair আকারে data রাখে।

**বৈশিষ্ট্য:**
- Key unique হতে হবে।
- Value duplicate হতে পারে।
- Mutable।
- Python 3.7 থেকে language specification অনুযায়ী insertion order বজায় রাখে।
- Key hashable হতে হবে।

### Example

```python
student = {
    "name": "Faruk",
    "age": 20,
    "department": "Computer"
}

print(student["name"])
# Faruk
```

### 2.2 Dictionary-এর Internals

Python-এর dictionary hash table ব্যবহার করে।

ধারণাগতভাবে:

```text
Key → hash(key) → table-এ location খোঁজা → Value পাওয়া
```

Example:

```python
student = {"name": "Faruk"}

print(student["name"])
# Faruk
```

Python `"name"` key-এর hash ব্যবহার করে সংশ্লিষ্ট entry খুঁজে বের করে। Hash value সরাসরি array index হিসেবে ব্যবহৃত হবে—এমন নিশ্চয়তা নেই; table-এর size ও internal rules অনুযায়ী location নির্ধারিত হয়।

### 2.3 Hashable Key কী?

যে object-এর hash তার lifetime-এ স্থিতিশীল থাকে এবং যা equality comparison-এর নিয়ম মেনে চলে, সেটি hashable হতে পারে।

সাধারণ উদাহরণ:

```python
data = {
    "name": "Faruk",
    10: "Number",
    (1, 2): "Tuple key"
}
```

কিন্তু `list`, `dict` এবং `set` সাধারণত hashable নয়, তাই সরাসরি dictionary key হিসেবে ব্যবহার করা যায় না।

```python
# TypeError হবে
data = {[1, 2]: "value"}
```

Tuple-এর সব element hashable হলে tuple-টি hashable হতে পারে।

### 2.4 Collision কী?

দুটি ভিন্ন key-এর hash table-এ একই location-এ যাওয়ার পরিস্থিতিকে collision বলা হয়।

Python-এর CPython dictionary collision সামলাতে open-addressing-ভিত্তিক probing ব্যবহার করে। এটি শুধু সাধারণ linear বা quadratic probing-এর সরল উদাহরণ দিয়ে পুরোপুরি বোঝানো যায় না; এর নিজস্ব probing strategy রয়েছে।

### 2.5 Dictionary-এর Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Get / Lookup | O(1) | O(n) |
| Set / Insert | O(1) amortized | O(n) |
| Delete | O(1) | O(n) |
| Search by value | O(n) | O(n) |

সাধারণ অবস্থায় dictionary lookup খুব দ্রুত। তবে collision বেশি হলে বা resizing-এর সময় operation-এর খরচ বেড়ে যেতে পারে।

**মনে রাখবে:** Key দিয়ে দ্রুত value খুঁজতে dictionary ব্যবহার করবে।

---

## 3. Set Internals

### 3.1 Set কী?

Python-এর `set` হলো unique item-এর একটি mutable collection।

**বৈশিষ্ট্য:**
- Duplicate item রাখা যায় না।
- নির্দিষ্ট insertion order বজায় রাখার নিশ্চয়তা নেই।
- Item যোগ ও মুছে ফেলা যায়।
- Item hashable হতে হবে।

### Example

```python
numbers = {10, 20, 30, 20}

print(numbers)
# {10, 20, 30}
```

একই value একাধিকবার দিলে set-এ সেটি একবারই থাকে।

### 3.2 Set-এর Internals

CPython-এ `set` hash table ব্যবহার করে। এটি dictionary-এর মতো hashing ও probing-এর মাধ্যমে item খুঁজে পায়।

ধারণাগতভাবে:

```text
Dictionary = Key → Value
Set        = Unique item
```

Set-কে “শুধু dictionary key” হিসেবে কল্পনা করা শেখার জন্য সুবিধাজনক, কিন্তু এটি আক্ষরিকভাবে সাধারণ dictionary নয়। CPython-এর set-এর নিজস্ব implementation রয়েছে।

### 3.3 Membership Check

```python
numbers = {10, 20, 30, 40}

print(20 in numbers)
# True

print(50 in numbers)
# False
```

Hash table-এর কারণে membership check সাধারণত O(1) average time-এ হয়।

### 3.4 Set-এর Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Add | O(1) amortized | O(n) |
| Remove | O(1) | O(n) |
| Membership (`in`) | O(1) | O(n) |
| Iterate | O(n) | O(n) |

### 3.5 Set কখন ব্যবহার করবে?

```python
# Duplicate বাদ দেওয়া
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)

print(unique_numbers)
# {1, 2, 3, 4}
```

**মনে রাখবে:** Duplicate বাদ দিতে, set operation করতে এবং দ্রুত membership check-এর জন্য set ব্যবহার করবে।

---

## 4. Tuple Internals

### 4.1 Tuple কী?

Python-এর `tuple` হলো ordered এবং immutable collection।

**বৈশিষ্ট্য:**
- Ordered।
- তৈরি হওয়ার পর tuple-এর item reference পরিবর্তন করা যায় না।
- Duplicate allowed।
- Indexing করা যায়।
- সব element hashable হলে tuple hashable হতে পারে।

### Example

```python
coordinates = (23.7, 90.4)

print(coordinates[0])
# 23.7
```

### 4.2 Tuple-এর Internals

CPython-এ tuple `PyTupleObject` দিয়ে বাস্তবায়িত। এটি একটি fixed-size collection, যার element reference-গুলো contiguous storage-এ রাখা হয়।

Tuple তৈরি হওয়ার পর তার আকার পরিবর্তন করা যায় না। তাই list-এর মতো append করে tuple বড় করা যায় না।

```python
numbers = (10, 20, 30)

# AttributeError হবে
# numbers.append(40)
```

### 4.3 Tuple কি সব সময় List-এর চেয়ে দ্রুত?

না। Tuple কিছু ক্ষেত্রে কম memory ব্যবহার করতে পারে এবং ছোট fixed collection-এর জন্য উপযুক্ত হতে পারে। কিন্তু tuple সব operation-এ list-এর চেয়ে দ্রুত—এমন কোনো নিয়ম নেই।

Performance নির্ভর করে operation, data এবং Python implementation-এর ওপর।

### 4.4 Tuple-এর Hashability

```python
data = {
    (1, 2): "Coordinates"
}

print(data[(1, 2)])
# Coordinates
```

এখানে tuple-এর সব element hashable, তাই tuple-টি dictionary key হিসেবে ব্যবহার করা যায়।

কিন্তু:

```python
value = ([1, 2], 3)

# TypeError হবে, কারণ tuple-এর ভেতরে list আছে
# data = {value: "Example"}
```

**গুরুত্বপূর্ণ:** Tuple immutable হলেও এর ভেতরে mutable object থাকতে পারে। Tuple-এর ভেতরের list পরিবর্তন করা সম্ভব; কিন্তু tuple-এর item-কে অন্য object দিয়ে replace করা যায় না।

### 4.5 Tuple-এর Time Complexity

| Operation | Time Complexity |
|---|---|
| Index দিয়ে access | O(1) |
| Search by value | O(n) |
| Iterate | O(n) |
| Tuple তৈরি | সাধারণত O(n) |

**মনে রাখবে:** Fixed collection, coordinates এবং অপরিবর্তিত sequence-এর জন্য tuple ব্যবহার করবে।

---

## 5. List, Dict, Set ও Tuple Comparison

| Feature | List | Tuple | Set | Dict |
|---|---|---|---|---|
| Ordered | Yes | Yes | No guaranteed order | Yes, insertion order |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Allowed | Allowed | Not allowed | Key unique |
| Indexing | Yes | Yes | No | Key দিয়ে lookup |
| Average lookup | Value search O(n) | Value search O(n) | Membership O(1) | Key lookup O(1) |
| Internals (CPython) | Dynamic array | Fixed-size collection | Hash table | Hash table |

### Real-Life Examples

**List — Shopping list**

```python
shopping = ["apple", "banana", "milk"]
shopping.append("bread")
```

**Tuple — Coordinates**

```python
coordinates = (23.7, 90.4)
```

**Set — Unique IDs**

```python
ids = {101, 102, 103, 101}
```

**Dict — Student information**

```python
student = {
    "name": "Faruk",
    "age": 20
}
```

### Shortcut

```text
List  = Ordered + Mutable
Tuple = Ordered + Immutable
Set   = Unique items + Fast membership
Dict  = Key-value mapping + Fast lookup
```

---

# Part 2: Square Root Algorithm — `n**0.5`

## 6. `n**0.5` কী?

Python-এ:

```python
n ** 0.5
```

সাধারণত `n`-এর square root বা বর্গমূল হিসাব করে।

Example:

```python
n = 25

print(n ** 0.5)
# 5.0
```

Prime number check করার সময় পুরো `n` পর্যন্ত divisor পরীক্ষা না করে শুধু √n পর্যন্ত পরীক্ষা করলেই যথেষ্ট।

## 7. কেন শুধু √n পর্যন্ত পরীক্ষা করব?

যদি কোনো সংখ্যা composite হয়, তাহলে সেটিকে দুইটি integer-এর গুণফল হিসেবে লেখা যায়:

```text
36 = 2 × 18
36 = 3 × 12
36 = 4 × 9
36 = 6 × 6
```

প্রতিটি factor pair-এ অন্তত একটি factor √n-এর সমান বা ছোট হবে।

কারণ, যদি দুইটি factor-ই √n-এর চেয়ে বড় হয়, তাহলে তাদের গুণফল n-এর চেয়ে বড় হবে—যা সম্ভব নয়।

তাই √n পর্যন্ত কোনো divisor না পেলে n একটি prime number হতে পারে। তবে `n` অবশ্যই 2-এর সমান বা বড় হতে হবে।

## 8. Prime Number Check — Python Code

```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


print(is_prime(2))   # True
print(is_prime(7))   # True
print(is_prime(25))  # False
print(is_prime(1))   # False
```

### Code Explanation

**Step 1:** `n < 2` হলে prime নয়।

```python
if n < 2:
    return False
```

**Step 2:** 2 থেকে √n-এর floor পর্যন্ত divisor পরীক্ষা করা হয়।

```python
for i in range(2, int(n ** 0.5) + 1):
```

`range()`-এর শেষ সীমা অন্তর্ভুক্ত হয় না, তাই `+ 1` ব্যবহার করা হয়েছে।

**Step 3:** কোনো সংখ্যা দিয়ে নিঃশেষে ভাগ গেলে n composite।

```python
if n % i == 0:
    return False
```

**Step 4:** কোনো divisor না পেলে n prime।

```python
return True
```

## 9. `n` পর্যন্ত Loop বনাম √n পর্যন্ত Loop

ধরো, `n = 100`।

### পদ্ধতি ১: পুরো n পর্যন্ত

```python
for i in range(2, 100):
    pass
```

মোট iteration: 98 বার।

### পদ্ধতি ২: √n পর্যন্ত

```python
for i in range(2, int(100 ** 0.5) + 1):
    pass
```

√100 = 10।

মোট iteration: 9 বার।

| Method | Iteration |
|---|---:|
| `range(2, n)` | 98 |
| `range(2, int(n**0.5) + 1)` | 9 |

## 10. বড় সংখ্যার ক্ষেত্রে পার্থক্য

ধরো, `n = 1,000,000`।

```text
পুরো n পর্যন্ত:
range(2, n) → 999,998 iterations

√n পর্যন্ত:
range(2, int(n**0.5) + 1) → 999 iterations
```

দ্বিতীয় পদ্ধতিতে iteration অনেক কম লাগে। তবে এটিকে সব ক্ষেত্রে ঠিক 1,000 গুণ দ্রুত বলা যায় না, কারণ বাস্তব execution time আরও কিছু বিষয়ের ওপর নির্ভর করে।

## 11. Time Complexity

| Method | Time Complexity |
|---|---|
| পুরো n পর্যন্ত divisor check | O(n) |
| √n পর্যন্ত divisor check | O(√n) |

এখানে worst-case complexity বোঝানো হয়েছে, যেমন n prime হলে প্রায় সব candidate পরীক্ষা করতে হয়।

## 12. আরও Efficient Prime Check

2 ছাড়া সব even number composite। তাই 2 পরীক্ষা করার পর শুধু odd divisor পরীক্ষা করা যায়।

```python
def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True
```

এই code-এ:
- `n < 2` হলে `False`।
- `n == 2` হলে `True`।
- অন্য even number হলে `False`।
- এরপর শুধু odd divisor পরীক্ষা করা হয়।

## 13. Final Revision

```text
List       → Dynamic array
Tuple      → Fixed-size collection
Dict       → Hash table
Set        → Hash table for unique elements

List access        → O(1)
List append        → Amortized O(1)
Dict lookup        → Average O(1)
Set membership     → Average O(1)
Tuple access       → O(1)

Prime check:
Full loop          → O(n)
Square root loop   → O(√n)
```

**Interview Tip:** শুধু complexity মুখস্থ না করে কেন সেই complexity হয়, সেটিও ব্যাখ্যা করতে শেখো। List-এর ক্ষেত্রে shifting, Dict ও Set-এর ক্ষেত্রে hashing, আর prime check-এর ক্ষেত্রে divisor pair-এর ধারণাটি বুঝতে পারলে interview-এ উত্তর দেওয়া সহজ হবে।