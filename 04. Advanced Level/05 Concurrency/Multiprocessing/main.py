"""
# Python Multiprocessing — Full Notes

## 1. What is Multiprocessing?

**Multiprocessing** হলো Python-এর এমন একটি technique যেখানে একটি program-এর কাজ একাধিক **process**-এর মাধ্যমে একসাথে চালানো যায়।

প্রতিটি process-এর আলাদা memory space থাকে এবং CPU-এর একাধিক core ব্যবহার করতে পারে।

Multiprocessing বিশেষভাবে **CPU-intensive / CPU-bound** কাজের জন্য useful।

### Example

```python
import multiprocessing

def task():
    print("Child process is running")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()

    print("Main process finished")
```

---

# 2. What is a Process?

**Process** হলো একটি running program।

যখন আমরা একটি Python program চালাই, operating system সেটিকে একটি process হিসেবে চালায়।

একটি program-এর মধ্যে একাধিক process থাকতে পারে।

### Example

```text
Python Program
      |
      v
Main Process
      |
      +------ Child Process 1
      |
      +------ Child Process 2
      |
      +------ Child Process 3
```

---

# 3. Main Process

যে process থেকে Python program শুরু হয় তাকে সাধারণত **Main Process** বলা হয়।

Example:

```python
import multiprocessing

current = multiprocessing.current_process()

print(current)
```

Output-এর মতো হতে পারে:

```text
<_MainProcess name='MainProcess' parent=None started>
```

---

# 4. multiprocessing.current_process()

বর্তমান process-এর information পাওয়ার জন্য:

```python
multiprocessing.current_process()
```

ব্যবহার করা হয়।

### Example

```python
import multiprocessing

process = multiprocessing.current_process()

print(process)
```

---

# 5. Process Name

Process-এর name দেখতে:

```python
process.name
```

### Example

```python
import multiprocessing

process = multiprocessing.current_process()

print(process.name)
```

Output:

```text
MainProcess
```

---

# 6. Process ID / PID

প্রতিটি process-এর একটি unique **Process ID (PID)** থাকে।

Python-এ PID পাওয়ার জন্য:

```python
import os

print(os.getpid())
```

### Example

```python
import multiprocessing
import os

process = multiprocessing.current_process()

print("Process Name:", process.name)
print("PID:", os.getpid())
```

---

# 7. Process ident

`multiprocessing` process object-এর `ident` property process-এর identifier দেয়।

```python
import multiprocessing

process = multiprocessing.current_process()

print(process.ident)
```

---

# 8. is_alive()

কোনো process বর্তমানে running কিনা জানতে:

```python
process.is_alive()
```

ব্যবহার করা হয়।

### Example

```python
import multiprocessing
import time

def task():
    time.sleep(3)

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()

    print(process.is_alive())

    process.join()

    print(process.is_alive())
```

সম্ভাব্য output:

```text
True
False
```

---

# 9. Child Process

Main process থেকে তৈরি হওয়া process-কে **Child Process** বলা হয়।

```text
Main Process
     |
     v
Child Process
```

### Example

```python
import multiprocessing

def task():
    print("Child process is running")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()
```

এখানে:

```python
process
```

হলো child process।

---

# 10. multiprocessing.Process()

নতুন process তৈরি করার জন্য:

```python
multiprocessing.Process()
```

ব্যবহার করা হয়।

Basic syntax:

```python
process = multiprocessing.Process(target=task)
```

---

# 11. target কী?

`target` হলো যে function-টি নতুন process-এ execute হবে।

Example:

```python
def task():
    print("Hello from child process")

process = multiprocessing.Process(target=task)
```

এখানে:

```python
target=task
```

মানে child process-এর ভিতরে `task()` function execute হবে।

---

# 12. target=task vs target=task()

এটি খুব important।

Correct:

```python
process = multiprocessing.Process(target=task)
```

Incorrect:

```python
process = multiprocessing.Process(target=task())
```

### কেন?

`target=task`:

```text
Function object → Process-এর কাছে পাঠানো হচ্ছে
```

`target=task()`:

```text
Function এখনই execute হয়ে যাচ্ছে
```

তাই সাধারণভাবে:

```python
target=task
```

ব্যবহার করতে হবে।

---

# 13. start()

Process শুরু করার জন্য:

```python
process.start()
```

ব্যবহার করা হয়।

### Example

```python
import multiprocessing

def task():
    print("Child process is running")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
```

`start()` call করার পর child process execution শুরু করে।

---

# 14. join()

Child process শেষ হওয়া পর্যন্ত main process-কে অপেক্ষা করানোর জন্য:

```python
process.join()
```

ব্যবহার করা হয়।

### Example

```python
import multiprocessing
import time

def task():
    time.sleep(3)
    print("Child finished")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()

    print("Main finished")
```

এখানে main process আগে:

```python
process.join()
```

এ গিয়ে child process-এর জন্য wait করবে।

---

# 15. start() vs join()

### start()

```python
process.start()
```

কাজ:

```text
Process শুরু করে
```

### join()

```python
process.join()
```

কাজ:

```text
Process শেষ হওয়া পর্যন্ত অপেক্ষা করে
```

সহজভাবে:

```text
start() = Start the process

join() = Wait for the process
```

---

# 16. Windows-এ if **name** == "**main**":

Windows-এ multiprocessing ব্যবহার করার সময় এটি অত্যন্ত গুরুত্বপূর্ণ:

```python
if __name__ == "__main__":
```

### Recommended structure

```python
import multiprocessing

def task():
    print("Child process is running")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()
```

---

# 17. Windows-এ Main Guard কেন দরকার?

Windows-এ multiprocessing সাধারণত নতুন Python interpreter শুরু করে।

যদি process creation code main guard-এর বাইরে থাকে, তাহলে child process আবার সেই code execute করার চেষ্টা করতে পারে।

ফলে:

```text
Recursive process creation
```

হতে পারে।

তাই Windows-এ:

```python
if __name__ == "__main__":
```

ব্যবহার করা উচিত।

---

# 18. Complete Basic Multiprocessing Program

```python
import multiprocessing

def task():
    print("Child process is running")

if __name__ == "__main__":

    process = multiprocessing.Process(
        target=task
    )

    process.start()
    process.join()

    print("Main process finished")
```

---

# 19. Parent and Child Process

একটি process অন্য process তৈরি করলে:

```text
Parent Process
      |
      v
Child Process
```

Example:

```python
import multiprocessing
import os

def task():
    print("Child PID:", os.getpid())
    print("Parent PID:", os.getppid())

if __name__ == "__main__":
    print("Main PID:", os.getpid())

    process = multiprocessing.Process(target=task)

    process.start()
    process.join()
```

---

# 20. Child Process-এর Name

Defaultভাবে child process-এর name সাধারণত এরকম হতে পারে:

```text
Process-1
```

### Example

```python
import multiprocessing

def task():
    process = multiprocessing.current_process()
    print("Child Name:", process.name)

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()
```

---

# 21. Custom Process Name

নিজের মতো process name দেওয়া যায়।

```python
process = multiprocessing.Process(
    target=task,
    name="MyProcess"
)
```

### Example

```python
import multiprocessing

def task():
    process = multiprocessing.current_process()
    print("Process Name:", process.name)

if __name__ == "__main__":
    process = multiprocessing.Process(
        target=task,
        name="Worker-1"
    )

    process.start()
    process.join()
```

---

# 22. Multiple Child Processes

একাধিক process তৈরি করা যায়।

```python
import multiprocessing

def task(number):
    print("Task:", number)

if __name__ == "__main__":

    p1 = multiprocessing.Process(
        target=task,
        args=(1,)
    )

    p2 = multiprocessing.Process(
        target=task,
        args=(2,)
    )

    p3 = multiprocessing.Process(
        target=task,
        args=(3,)
    )

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
```

Output order fixed নাও হতে পারে:

```text
Task: 2
Task: 1
Task: 3
```

অথবা:

```text
Task: 1
Task: 3
Task: 2
```

কারণ process scheduling operating system control করে।

---

# 23. args

Child process-এর function-এ argument পাঠাতে:

```python
args=
```

ব্যবহার করা হয়।

Example:

```python
import multiprocessing

def task(name):
    print("Hello", name)

if __name__ == "__main__":
    process = multiprocessing.Process(
        target=task,
        args=("Faruk",)
    )

    process.start()
    process.join()
```

Output:

```text
Hello Faruk
```

### Important

একটি argument হলেও tuple-এর মধ্যে comma দিতে হবে:

```python
args=("Faruk",)
```

---

# 24. Multiple Arguments

```python
import multiprocessing

def task(name, age):
    print("Name:", name)
    print("Age:", age)

if __name__ == "__main__":
    process = multiprocessing.Process(
        target=task,
        args=("Faruk", 25)
    )

    process.start()
    process.join()
```

---

# 25. kwargs

Keyword arguments পাঠানোর জন্য:

```python
kwargs=
```

ব্যবহার করা যায়।

Example:

```python
import multiprocessing

def task(name, age):
    print("Name:", name)
    print("Age:", age)

if __name__ == "__main__":

    process = multiprocessing.Process(
        target=task,
        kwargs={
            "name": "Faruk",
            "age": 25
        }
    )

    process.start()
    process.join()
```

---

# 26. terminate()

কোনো running process manually terminate করতে:

```python
process.terminate()
```

ব্যবহার করা যায়।

### Example

```python
import multiprocessing
import time

def task():
    while True:
        print("Running...")
        time.sleep(1)

if __name__ == "__main__":

    process = multiprocessing.Process(target=task)

    process.start()

    time.sleep(3)

    process.terminate()
    process.join()

    print("Process terminated")
```

---

# 27. kill()

Process forcefully kill করার জন্য:

```python
process.kill()
```

ব্যবহার করা যায়।

```python
process.kill()
```

`terminate()` এবং `kill()` দুটিই process বন্ধ করার জন্য ব্যবহৃত হয়।

---

# 28. exitcode

Process শেষ হওয়ার পরে তার exit code পাওয়া যায়:

```python
process.exitcode
```

### Example

```python
import multiprocessing

def task():
    print("Child process")

if __name__ == "__main__":

    process = multiprocessing.Process(target=task)

    process.start()
    process.join()

    print("Exit Code:", process.exitcode)
```

সাধারণভাবে successful completion-এর জন্য:

```text
0
```

পাওয়া যায়।

---

# 29. Process Lifecycle

একটি process-এর সাধারণ lifecycle:

```text
Created
   |
   v
Started
   |
   v
Running
   |
   v
Finished
```

আরও সহজভাবে:

```text
Process()
   ↓
start()
   ↓
Running
   ↓
Finished
   ↓
join()
```

---

# 30. start() একবারই ব্যবহার করা যায়

একটি process object-এ `start()` একবার call করতে হয়।

Example:

```python
process.start()
process.start()
```

এভাবে একই process আবার start করা যাবে না।

---

# 31. join() Process বন্ধ করে না

এটি খুব important।

```python
process.join()
```

process বন্ধ করে না।

এটি শুধু main process-কে অপেক্ষা করায় যতক্ষণ child process শেষ না হয়।

```text
start() → process চালু করে

join() → process শেষ হওয়া পর্যন্ত wait করে
```

---

# 32. কেন Multiprocessing ব্যবহার করব?

Multiprocessing ব্যবহার করা হয় বিশেষ করে CPU-intensive কাজের জন্য।

Examples:

```text
Image Processing
Video Processing
Machine Learning Computation
Large Mathematical Calculation
Data Processing
Scientific Computation
CPU-heavy Algorithms
```

---

# 33. CPU-Bound Task

যে কাজ CPU-এর উপর বেশি নির্ভর করে তাকে:

```text
CPU-bound task
```

বলা হয়।

Examples:

```text
Large calculations
Image processing
Video encoding
Scientific calculations
Complex algorithms
```

এ ধরনের কাজের জন্য multiprocessing ভালো option হতে পারে।

---

# 34. I/O-Bound Task

I/O-bound task হলো যে কাজে I/O operation (যেমন: file read/write, network request, database query) বেশি নির্ভর করে।
"""