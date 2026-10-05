"""
# Python Multiprocessing — Notes

## 1. Multiprocessing কী?

**Multiprocessing** হলো এমন একটি technique যেখানে একটি Python program একাধিক **process** ব্যবহার করে একসাথে একাধিক কাজ করতে পারে।

সহজভাবে:

> একাধিক Process ব্যবহার করে কাজকে parallelভাবে execute করাকে Multiprocessing বলে।

Python-এ multiprocessing করার জন্য built-in `multiprocessing` module ব্যবহার করা হয়।

```python
import multiprocessing
```

---

## 2. Process কী?

**Process** হলো একটি running program।

যেমন, যখন আমরা একটি Python program চালাই, তখন একটি process তৈরি হয়।

```text
Python Program
      ↓
   Process
```

একটি program-এর মধ্যে একাধিক process তৈরি করা যায়।

```text
Program
   │
   ├── Process 1
   ├── Process 2
   └── Process 3
```

---

## 3. Main Process

Python program শুরু হলে প্রথম যে process তৈরি হয় তাকে **Main Process** বলা হয়।

```python
import multiprocessing

print(multiprocessing.current_process().name)
```

Output:

```text
MainProcess
```

---

## 4. `current_process()`

বর্তমানে যে process code execute করছে সেটি জানতে:

```python
multiprocessing.current_process()
```

ব্যবহার করা হয়।

Example:

```python
import multiprocessing

process = multiprocessing.current_process()

print(process)
```

এটি current process-এর object return করে।

---

## 5. Process-এর Name

Process-এর নাম দেখতে:

```python
multiprocessing.current_process().name
```

Example:

```python
import multiprocessing

print(multiprocessing.current_process().name)
```

Output:

```text
MainProcess
```

### মনে রাখবে:

```text
.name → Process-এর নাম
```

---

## 6. Process ID / `ident`

প্রতিটি process-এর একটি identifier থাকে।

এটি দেখতে:

```python
multiprocessing.current_process().ident
```

Example:

```python
import multiprocessing

print(multiprocessing.current_process().ident)
```

Output হতে পারে:

```text
12345
```

এই value প্রতিবার একই হবে এমন নয়।

### মনে রাখবে:

```text
.ident → Process-এর unique identifier
```

---

## 7. `is_alive()`

কোনো process বর্তমানে active/running কিনা check করতে:

```python
process.is_alive()
```

ব্যবহার করা হয়।

Example:

```python
import multiprocessing

process = multiprocessing.current_process()

print(process.is_alive())
```

Output:

```text
True
```

### `True`

Process বর্তমানে active।

### `False`

Process আর running নেই।

---

# 8. তোমার Code-এর সম্পূর্ণ Explanation

```python
import multiprocessing

print(multiprocessing.current_process().name)
print(multiprocessing.current_process().ident)
print(multiprocessing.current_process().is_alive())
```

Output:

```text
MainProcess
12345
True
```

এখানে:

| Code                | কাজ                           |
| ------------------- | ----------------------------- |
| `current_process()` | বর্তমান process বের করে       |
| `.name`             | process-এর নাম                |
| `.ident`            | process-এর identifier         |
| `.is_alive()`       | process active কিনা check করে |

---

# 9. Child Process

Main Process থেকে আমরা নতুন process তৈরি করতে পারি। এই নতুন process-কে **Child Process** বলা হয়।

```text
             Main Process
                  │
          ┌───────┴───────┐
          ↓               ↓
      Child 1          Child 2
```

Example:

```python
import multiprocessing

def task():
    print("Child process is running")

process = multiprocessing.Process(target=task)

process.start()
process.join()
```

---

# 10. `multiprocessing.Process`

নতুন process তৈরি করার জন্য:

```python
multiprocessing.Process()
```

ব্যবহার করা হয়।

সাধারণ syntax:

```python
process = multiprocessing.Process(target=function)
```

Example:

```python
def task():
    print("Hello from child process")

process = multiprocessing.Process(target=task)
```

এখানে `task` function child process-এ execute হবে।

---

# 11. `target`

```python
Process(target=task)
```

এখানে:

```text
target = যে function child process-এ execute হবে
```

Example:

```python
def download():
    print("Downloading...")

process = multiprocessing.Process(target=download)
```

এখানে `download` function child process-এ চলবে।

### Important:

সঠিক:

```python
target=download
```

ভুল:

```python
target=download()
```

কারণ `download()` লিখলে function-টি process তৈরি হওয়ার আগেই execute হয়ে যাবে।

---

# 12. `start()`

Child process শুরু করার জন্য:

```python
process.start()
```

ব্যবহার করা হয়।

Example:

```python
import multiprocessing

def task():
    print("Child process running")

process = multiprocessing.Process(target=task)

process.start()
```

Flow:

```text
Process object তৈরি
       ↓
process.start()
       ↓
Child Process তৈরি
       ↓
task() execute
```

---

# 13. `join()`

Main Process যেন Child Process শেষ হওয়ার জন্য অপেক্ষা করে, তার জন্য:

```python
process.join()
```

ব্যবহার করা হয়।

Example:

```python
process.start()
process.join()

print("Main process finished")
```

Flow:

```text
Child Process শুরু
       ↓
Main Process অপেক্ষা করবে
       ↓
Child Process শেষ
       ↓
Main Process continue করবে
```

---

# 14. Complete Example

```python
import multiprocessing

def task():
    print("Child Process is running")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()

    print("Main Process finished")
```

Output:

```text
Child Process is running
Main Process finished
```

---

# 15. `if __name__ == "__main__":`

Multiprocessing-এর ক্ষেত্রে এটি খুব গুরুত্বপূর্ণ:

```python
if __name__ == "__main__":
```

বিশেষ করে **Windows**-এ multiprocessing ব্যবহার করার সময় এটি ব্যবহার করা উচিত।

Example:

```python
import multiprocessing

def task():
    print("Hello")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)
    process.start()
    process.join()
```

---

# 16. Multiprocessing কেন ব্যবহার করব?

Multiprocessing বিশেষভাবে useful যখন কাজগুলো **CPU-intensive**।

যেমন:

* Large mathematical calculations
* Image processing
* Video processing
* Data processing
* Scientific computation
* CPU-heavy algorithms

---

# 17. Normal Execution বনাম Multiprocessing

### Normal Execution

```text
Task 1
  ↓
Task 2
  ↓
Task 3
  ↓
Task 4
```

একটির পর একটি কাজ হয়।

### Multiprocessing

```text
          Main Process
          /    |     \
         ↓     ↓      ↓
      Task 1 Task 2  Task 3
```

একাধিক process আলাদা CPU core-এ parallelভাবে কাজ করতে পারে।

---

# 18. Multiprocessing-এর গুরুত্বপূর্ণ Terms

```text
Process
   ↓
Main Process
   ↓
Child Process
   ↓
PID / ident
   ↓
start()
   ↓
join()
   ↓
is_alive()
```

### Quick Revision

| Term                | Meaning                        |
| ------------------- | ------------------------------ |
| `multiprocessing`   | Multiprocessing module         |
| `current_process()` | Current process                |
| `name`              | Process name                   |
| `ident`             | Process identifier             |
| `is_alive()`        | Process active কিনা            |
| `Process()`         | New process তৈরি               |
| `target`            | কোন function execute হবে       |
| `start()`           | Process শুরু                   |
| `join()`            | Process শেষ হওয়া পর্যন্ত wait  |
| `MainProcess`       | Main process                   |
| Child Process       | Main process থেকে তৈরি process |

---

# 19. Interview Questions

### Q1. Multiprocessing কী?

**Answer:**

একাধিক process ব্যবহার করে CPU-intensive কাজগুলো parallelভাবে execute করার technique হলো multiprocessing।

### Q2. Python-এ multiprocessing-এর জন্য কোন module ব্যবহার করা হয়?

```python
import multiprocessing
```

### Q3. Current process কীভাবে পাওয়া যায়?

```python
multiprocessing.current_process()
```

### Q4. Process-এর নাম কীভাবে পাওয়া যায়?

```python
multiprocessing.current_process().name
```

### Q5. Process ID কীভাবে পাওয়া যায়?

```python
multiprocessing.current_process().ident
```

### Q6. Process alive কিনা কীভাবে check করা হয়?

```python
process.is_alive()
```

### Q7. নতুন process কীভাবে তৈরি করা হয়?

```python
process = multiprocessing.Process(target=task)
```

### Q8. Process শুরু করার method কী?

```python
process.start()
```

### Q9. Child process শেষ না হওয়া পর্যন্ত wait করার method কী?

```python
process.join()
```

---

# Shortcut

```text
current_process()
       │
       ├── name      → নাম
       ├── ident     → ID
       └── is_alive  → Alive?
```

নতুন Process-এর জন্য:

```text
Process()
   ↓
start()
   ↓
join()
```

### মনে রাখবে:

**Process তৈরি → `Process()`**

**Process শুরু → `start()`**

**Process শেষ হওয়া পর্যন্ত অপেক্ষা → `join()`**

**Current Process → `current_process()`**

**Process Name → `.name`**

**Process ID → `.ident`**

**Process Alive → `.is_alive()`**


"""