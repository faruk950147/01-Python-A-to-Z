"""
# Python Multiprocessing — Full Notes

## 1. What is Processing?

**Processing** হলো কোনো input/data-এর উপর বিভিন্ন operation প্রয়োগ করে সেটিকে পরিবর্তন, বিশ্লেষণ বা useful output-এ রূপান্তর করার প্রক্রিয়া।

Python-এ processing করার বিভিন্ন উপায় আছে:

* Single Processing
* Multithreading
* Multiprocessing
* Asynchronous Programming

---

# 2. What is Multiprocessing?

**Multiprocessing** হলো এমন একটি technique যেখানে একটি Python program-এর কাজ একাধিক **independent process**-এর মাধ্যমে execute করা হয়।

প্রতিটি process-এর সাধারণত **নিজস্ব memory space** থাকে এবং multiprocessing ব্যবহার করে একাধিক CPU core-এ কাজ parallelভাবে চালানো সম্ভব।

Multiprocessing বিশেষভাবে **CPU-bound tasks**-এর জন্য useful।

### Examples

* Image Processing
* Video Processing
* Large Mathematical Calculation
* Scientific Computation
* Data Processing
* Machine Learning Computation
* CPU-heavy Algorithms

### Basic Example

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

# 3. What is a Process?

**Process** হলো একটি program-এর বর্তমানে চলমান instance।

যখন আমরা Python program run করি, operating system সেটিকে একটি process হিসেবে চালায়।

একটি program থেকে একাধিক process তৈরি করা যেতে পারে।

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

# 4. Main Process

যে process থেকে Python program-এর execution শুরু হয় তাকে সাধারণত **Main Process** বলা হয়।

```python
import multiprocessing


process = multiprocessing.current_process()

print(process)
```

Possible Output:

```text
<_MainProcess name='MainProcess' parent=None started>
```

---

# 5. multiprocessing.current_process()

বর্তমানে যে process code execute করছে তার `Process` object পাওয়ার জন্য:

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

# 6. Process Name

Process-এর নাম দেখতে:

```python
process.name
```

ব্যবহার করা হয়।

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

Child process-এর default name সাধারণত এমন হতে পারে:

```text
Process-1
Process-2
Process-3
```

---

# 7. Process ID — PID

প্রতিটি running process-এর একটি **Process ID (PID)** থাকে।

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

# 8. Process `ident`

`multiprocessing.Process` object-এর `ident` attribute process-এর identifier দেয়।

```python
import multiprocessing


process = multiprocessing.current_process()

print(process.ident)
```

### Important

`ident` এবং OS-এর PID একই concept নয়।

OS-level process ID দেখতে:

```python
os.getpid()
```

ব্যবহার করা যায়।

---

# 9. `is_alive()`

কোনো process বর্তমানে running অবস্থায় আছে কিনা জানতে:

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

Possible Output:

```text
True
False
```

---

# 10. Child Process

Main/Parent process থেকে তৈরি হওয়া process-কে **Child Process** বলা হয়।

```text
Parent Process
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

---

# 11. `multiprocessing.Process()`

নতুন process তৈরি করার জন্য:

```python
multiprocessing.Process()
```

ব্যবহার করা হয়।

### Basic Syntax

```python
process = multiprocessing.Process(target=task)
```

### Common Parameters

```python
multiprocessing.Process(
    group=None,
    target=None,
    name=None,
    args=(),
    kwargs={},
    daemon=None
)
```

সবচেয়ে বেশি ব্যবহৃত parameters:

```text
target
args
kwargs
name
daemon
```

---

# 12. `target`

`target` হলো সেই **callable/function**, যেটি child process-এ execute হবে।

### Example

```python
def task():
    print("Hello from child process")


process = multiprocessing.Process(target=task)
```

এখানে:

```python
target=task
```

মানে child process `task` function execute করবে।

---

# 13. `target=task` vs `target=task()`

এটি খুব গুরুত্বপূর্ণ।

### Correct

```python
process = multiprocessing.Process(target=task)
```

এখানে `task` function-এর reference দেওয়া হচ্ছে।

### Incorrect

```python
process = multiprocessing.Process(target=task())
```

এখানে `task()` আগে execute হয়ে যাবে এবং তার return value `target` হিসেবে চলে যাবে।

তাই সাধারণভাবে:

```python
target=task
```

ব্যবহার করতে হবে।

---

# 14. `start()`

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

`start()` call করার পর নতুন process তৈরি হয়ে target function execute করার জন্য শুরু হয়।

---

# 15. `join()`

কোনো child process শেষ না হওয়া পর্যন্ত calling process-কে অপেক্ষা করানোর জন্য:

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

এখানে:

```python
process.join()
```

এর কারণে main process child process শেষ হওয়া পর্যন্ত অপেক্ষা করবে।

---

# 16. `start()` vs `join()`

### `start()`

```python
process.start()
```

কাজ:

```text
নতুন process শুরু করে
```

### `join()`

```python
process.join()
```

কাজ:

```text
Process শেষ হওয়া পর্যন্ত wait করে
```

সহজভাবে:

```text
start() = Start the process

join() = Wait for the process to finish
```

---

# 17. Windows-এ `if __name__ == "__main__":`

Windows-এ multiprocessing ব্যবহার করার সময় **main guard** ব্যবহার করা অত্যন্ত গুরুত্বপূর্ণ।

### Recommended Structure

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

# 18. Main Guard কেন দরকার?

বিশেষ করে Windows-এর `spawn` start method-এর ক্ষেত্রে child process একটি নতুন Python interpreter দিয়ে শুরু হয়।

যদি process creation code module-এর top level-এ থাকে, child process আবার সেই code execute করার চেষ্টা করতে পারে।

ফলে unwanted recursive process creation হতে পারে।

তাই:

```python
if __name__ == "__main__":
```

ব্যবহার করা recommended।

### Incorrect

```python
import multiprocessing


def task():
    print("Running")


process = multiprocessing.Process(target=task)
process.start()
```

### Correct

```python
import multiprocessing


def task():
    print("Running")


if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()
```

---

# 19. Complete Basic Multiprocessing Program

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

### Flow

```text
Program Start
     ↓
Main Process
     ↓
Create Process
     ↓
start()
     ↓
Child Process
     ↓
task()
     ↓
Child Finished
     ↓
join() returns
     ↓
Main Process continues
```

---

# 20. Parent and Child Process

একটি process যখন অন্য process তৈরি করে:

```text
Parent Process
       |
       v
Child Process
```

### Example

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

এখানে:

```python
os.getpid()
```

বর্তমান process-এর PID দেয়।

এবং:

```python
os.getppid()
```

parent process-এর PID দেয়।

---

# 21. Child Process-এর Name

Child process-এর default name সাধারণত:

```text
Process-1
```

এর মতো হতে পারে।

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

# 22. Custom Process Name

নিজের মতো process name দেওয়া যায়।

```python
process = multiprocessing.Process(
    target=task,
    name="Worker-1"
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

Output:

```text
Process Name: Worker-1
```

---

# 23. Multiple Child Processes

একাধিক child process তৈরি করা যায়।

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

Output-এর order fixed নয়:

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

কারণ process scheduling operating system-এর উপর নির্ভর করে।

---

# 24. `args`

Child process-এর target function-এ positional arguments পাঠাতে:

```python
args=
```

ব্যবহার করা হয়।

### Example

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

একটি argument হলেও tuple-এ comma দিতে হবে:

```python
args=("Faruk",)
```

কারণ:

```python
("Faruk")
```

এটি tuple নয়; এটি string।

---

# 25. Multiple Arguments

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

# 26. `kwargs`

Keyword arguments পাঠানোর জন্য:

```python
kwargs=
```

ব্যবহার করা যায়।

### Example

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

# 27. `terminate()`

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

### Important

`terminate()` process-কে graceful cleanup করার সুযোগ নাও দিতে পারে।

তাই files, locks, resources ইত্যাদি ব্যবহার করলে সতর্ক থাকতে হবে।

---

# 28. `kill()`

Process forcefully terminate করার জন্য:

```python
process.kill()
```

ব্যবহার করা যায়।

### Example

```python
process.kill()
```

### `terminate()` vs `kill()`

```text
terminate() → Process terminate করে

kill() → আরও forceful ভাবে Process terminate করে
```

---

# 29. `exitcode`

Process শেষ হওয়ার পরে তার exit code:

```python
process.exitcode
```

দিয়ে পাওয়া যায়।

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

সফলভাবে শেষ হলে সাধারণত:

```text
0
```

পাওয়া যায়।

Error-এর কারণে process শেষ হলে non-zero exit code পাওয়া যেতে পারে।

---

# 30. Process Lifecycle

একটি process-এর সাধারণ lifecycle:

```text
Process Object Created
          |
          v
       start()
          |
          v
       Running
          |
          v
       Finished
          |
          v
       join()
```

সহজভাবে:

```text
Process()
   ↓
start()
   ↓
Running
   ↓
Finished
   ↓
join() returns
```

---

# 31. `start()` একবারই ব্যবহার করা যায়

একটি `Process` object-এর উপর `start()` সাধারণভাবে একবারই call করা যায়।

### Incorrect

```python
process.start()
process.start()
```

একই process object পুনরায় start করা যাবে না।

আবার process চালাতে হলে নতুন `Process` object তৈরি করতে হবে।

---

# 32. `join()` Process বন্ধ করে না

এটি খুব important।

```python
process.join()
```

Process terminate করে না।

`join()` শুধু calling process-কে অপেক্ষা করায় যতক্ষণ না target process শেষ হয়।

```text
start() → Process শুরু করে

join() → Process শেষ হওয়া পর্যন্ত wait করে
```

---

# 33. CPU-Bound Task

যে task-এর execution time মূলত CPU computation-এর উপর নির্ভর করে তাকে **CPU-bound task** বলা হয়।

### Examples

```text
Large Mathematical Calculations
Image Processing
Video Encoding
Scientific Calculations
Complex Algorithms
CPU-heavy Data Processing
```

CPU-bound কাজের জন্য multiprocessing ভালো option হতে পারে।

---

# 34. I/O-Bound Task

যে task-এ execution-এর বড় অংশ input/output operation-এর জন্য অপেক্ষা করে তাকে **I/O-bound task** বলা হয়।

### Examples

```text
File Read/Write
Network Request
Database Query
API Request
Waiting for External Service
```

I/O-bound কাজের জন্য অনেক ক্ষেত্রে:

```text
Threading
Asyncio
```

বেশি উপযোগী হতে পারে।

তবে multiprocessing দিয়েও I/O-bound কাজ করা সম্ভব।

---

# 35. Multiprocessing কেন ব্যবহার করব?

Multiprocessing বিশেষভাবে **CPU-bound workload**-এর জন্য useful।

### Examples

```text
Image Processing
Video Processing
Large Mathematical Calculation
Scientific Computation
Machine Learning Computation
CPU-heavy Algorithms
Data Processing
```

---

# 36. Multiprocessing এবং Python GIL

Python-এর **CPython** implementation-এ **GIL (Global Interpreter Lock)** একই process-এর মধ্যে একাধিক thread-এর Python bytecode execution-কে একই সময়ে চালাতে সীমাবদ্ধ করে।

Multiprocessing-এর ক্ষেত্রে প্রতিটি process-এর আলাদা Python interpreter এবং সাধারণত আলাদা memory space থাকে।

তাই CPU-bound কাজের ক্ষেত্রে multiple processes একাধিক CPU core ব্যবহার করতে পারে।

সহজভাবে:

```text
Threading
   ↓
Same Process
   ↓
Shared Memory
   ↓
GIL consideration


Multiprocessing
   ↓
Multiple Processes
   ↓
Separate Memory
   ↓
Multiple CPU Cores
```

---

# 37. Multiprocessing vs Multithreading

| Feature           | Multiprocessing   | Multithreading           |
| ----------------- | ----------------- | ------------------------ |
| Unit              | Process           | Thread                   |
| Memory            | Separate          | Shared                   |
| CPU-bound         | ভালো choice       | CPython-এ GIL limitation |
| I/O-bound         | Possible          | Often suitable           |
| Communication     | তুলনামূলক complex | তুলনামূলক easy           |
| Memory usage      | বেশি              | কম                       |
| Isolation         | বেশি              | কম                       |
| Creation overhead | বেশি              | কম                       |

### General Rule

```text
CPU-bound
    ↓
Multiprocessing

I/O-bound
    ↓
Threading / Asyncio
```

এটি একটি general guideline, absolute rule নয়।

---

# 38. Process-এর আলাদা Memory

Multiprocessing-এর গুরুত্বপূর্ণ বৈশিষ্ট্য হলো process-গুলোর memory সাধারণভাবে আলাদা থাকে।

### Example

```python
import multiprocessing


number = 10


def task():
    print("Child:", number)


if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()
```

Child process variable-এর একটি process-specific copy পেতে পারে।

Child process-এর পরিবর্তন সরাসরি parent process-এর ordinary Python variable পরিবর্তন করে না।

---

# 39. Process-এর মধ্যে Data Sharing

Process-গুলোর memory আলাদা হওয়ায় ordinary Python variable সরাসরি share করা যায় না।

Python `multiprocessing` কিছু IPC/data-sharing mechanism দেয়:

```text
Queue
Pipe
Value
Array
Manager
Shared Memory
```

---

# 40. `multiprocessing.Queue`

এক process থেকে অন্য process-এ data/message পাঠানোর জন্য:

```python
multiprocessing.Queue()
```

ব্যবহার করা যায়।

### Example

```python
import multiprocessing


def worker(queue):
    queue.put("Hello from child")


if __name__ == "__main__":

    queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=worker,
        args=(queue,)
    )

    process.start()

    print(queue.get())

    process.join()
```

Output:

```text
Hello from child
```

---

# 41. `multiprocessing.Pipe`

দুই process-এর মধ্যে communication-এর জন্য:

```python
multiprocessing.Pipe()
```

ব্যবহার করা যায়।

### Basic Idea

```text
Process A
    |
    | Pipe
    |
Process B
```

### Example

```python
import multiprocessing


def worker(connection):
    connection.send("Hello from child")
    connection.close()


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=worker,
        args=(child_conn,)
    )

    process.start()

    print(parent_conn.recv())

    process.join()
```

Output:

```text
Hello from child
```

---

# 42. `multiprocessing.Pool`

অনেকগুলো একই ধরনের task worker processes-এর মধ্যে distribute করার জন্য:

```python
multiprocessing.Pool
```

ব্যবহার করা যায়।

### Example

```python
import multiprocessing


def square(number):
    return number * number


if __name__ == "__main__":

    with multiprocessing.Pool() as pool:

        results = pool.map(
            square,
            [1, 2, 3, 4, 5]
        )

    print(results)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

# 43. `Pool.map()`

একটি iterable-এর প্রতিটি item-এর উপর একই function চালাতে:

```python
pool.map(function, iterable)
```

ব্যবহার করা হয়।

### Example

```python
results = pool.map(
    square,
    [1, 2, 3, 4, 5]
)
```

Conceptually:

```text
1 → square()
2 → square()
3 → square()
4 → square()
5 → square()
```

Result হিসেবে একটি list পাওয়া যায়।

---

# 44. Pool কেন ব্যবহার করব?

যদি অনেকগুলো একই ধরনের independent task থাকে, তাহলে manually:

```python
p1 = Process(...)
p2 = Process(...)
p3 = Process(...)
p4 = Process(...)
```

লেখার পরিবর্তে `Pool` ব্যবহার করা সহজ হতে পারে।

```text
Many Tasks
    ↓
Process Pool
    ↓
Worker Processes
    ↓
Results
```

---

# 45. Multiprocessing-এর সুবিধা

### 1. CPU-bound Performance

CPU-intensive workload parallelize করতে সাহায্য করে।

### 2. Multiple CPU Cores

একাধিক process একাধিক CPU core ব্যবহার করতে পারে।

### 3. Process Isolation

একটি process-এর memory সাধারণত অন্য process-এর memory থেকে আলাদা।

### 4. Fault Isolation

একটি child process crash করলেও parent process সবসময় crash করবে এমন নয়।

### 5. Parallel Execution

Independent tasks একই সময়ে execute করা যায়।

---

# 46. Multiprocessing-এর অসুবিধা

### 1. বেশি Memory Usage

প্রতিটি process-এর আলাদা memory space থাকে।

### 2. Process Creation Overhead

Thread-এর তুলনায় process তৈরি করা তুলনামূলক expensive।

### 3. Communication Complexity

Process-এর মধ্যে data share করতে IPC mechanism প্রয়োজন হতে পারে।

### 4. Serialization Overhead

Process-এর মধ্যে data পাঠানোর সময় অনেক ক্ষেত্রে object serialization/pickling-এর overhead হয়।

### 5. Debugging Complexity

একাধিক process একসাথে চলায় debugging তুলনামূলক কঠিন হতে পারে।

---

# 47. কখন Multiprocessing ব্যবহার করব?

Multiprocessing ব্যবহার করার কথা ভাবতে পারো যখন:

```text
✓ Task CPU-intensive
✓ Tasks independent
✓ Multiple CPU cores available
✓ Parallel execution beneficial
✓ Large computation করতে হবে
```

Examples:

```text
Image Processing
Video Processing
Scientific Computation
Large Mathematical Operations
CPU-heavy Data Processing
```

---

# 48. কখন Multiprocessing ব্যবহার না করাই ভালো?

যদি task খুব ছোট হয় এবং process তৈরির overhead task-এর computation-এর চেয়ে বেশি হয়, তাহলে multiprocessing performance improve করার পরিবর্তে slow করতে পারে।

Examples:

```text
Very Small Calculations
Simple Print Operations
Tiny Tasks
Tasks Requiring Frequent Shared-State Access
```

---

# 49. Important Process Methods

| Method              | Purpose                                 |
| ------------------- | --------------------------------------- |
| `start()`           | Process শুরু করে                        |
| `join()`            | Process শেষ হওয়া পর্যন্ত wait করে       |
| `is_alive()`        | Process alive কিনা check করে            |
| `terminate()`       | Process terminate করে                   |
| `kill()`            | Process forcefully terminate করে        |
| `close()`           | Process object-এর resources release করে |
| `run()`             | Target callable execute করার method     |
| `current_process()` | Current process-এর object দেয়           |

---

# 50. Important Process Attributes

| Attribute    | Purpose                |
| ------------ | ---------------------- |
| `name`       | Process-এর নাম         |
| `pid`        | OS Process ID          |
| `ident`      | Process identifier     |
| `exitcode`   | Process-এর exit status |
| `daemon`     | Daemon process কিনা    |
| `is_alive()` | Process running কিনা   |

### PID

`Process` object থেকেও PID পাওয়া যায়:

```python
process.pid
```

---

# 51. Complete Multiprocessing Example

```python
import multiprocessing
import os
import time


def worker(number):

    process = multiprocessing.current_process()

    print(
        f"Name: {process.name}, "
        f"PID: {os.getpid()}, "
        f"Task: {number}"
    )

    time.sleep(2)

    print(f"Task {number} finished")


if __name__ == "__main__":

    processes = []

    for i in range(3):

        process = multiprocessing.Process(
            target=worker,
            args=(i,),
            name=f"Worker-{i}"
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes finished")
```

Possible output:

```text
Name: Worker-0, PID: 1234, Task: 0
Name: Worker-1, PID: 1235, Task: 1
Name: Worker-2, PID: 1236, Task: 2

Task 0 finished
Task 1 finished
Task 2 finished

All processes finished
```

Output-এর exact order guaranteed নয়।

---

# 52. Multiprocessing Mental Model

সবচেয়ে সহজভাবে:

```text
                 Python Program
                       |
                       v
                  Main Process
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Process 1    Process 2    Process 3
          |            |            |
          v            v            v
       CPU Core     CPU Core     CPU Core
```

প্রতিটি process-এর থাকে:

```text
নিজস্ব execution
       +
নিজস্ব memory space
       +
নিজস্ব process ID
```

---

# 53. Multiprocessing Short Revision

### Process কী?

Running program-এর একটি instance।

### Multiprocessing কী?

একাধিক process ব্যবহার করে task execute করার technique।

### `Process()` কী?

নতুন process তৈরি করে।

### `start()` কী?

Process শুরু করে।

### `join()` কী?

Process শেষ হওয়া পর্যন্ত wait করে।

### `target` কী?

Child process-এ execute হওয়া callable।

### `args` কী?

Positional arguments পাঠায়।

### `kwargs` কী?

Keyword arguments পাঠায়।

### `terminate()` কী?

Process terminate করে।

### `kill()` কী?

Process forcefully terminate করে।

### `is_alive()` কী?

Process বর্তমানে alive কিনা check করে।

### `exitcode` কী?

Process শেষ হওয়ার status code।

### `pid` কী?

Process-এর OS-level Process ID।

### `current_process()` কী?

Current process-এর object দেয়।

### `Queue` কী?

Process-এর মধ্যে data/message exchange করতে সাহায্য করে।

### `Pipe` কী?

Process-to-process communication-এর জন্য ব্যবহৃত হয়।

### `Pool` কী?

অনেকগুলো task worker processes-এর মধ্যে distribute করতে সাহায্য করে।

---

# 54. Most Important Topics for Exam & Interview

```text
1. Process
2. Main Process
3. Child Process
4. multiprocessing.Process
5. target
6. args
7. kwargs
8. start()
9. join()
10. is_alive()
11. terminate()
12. kill()
13. PID
14. current_process()
15. Process Lifecycle
16. Multiprocessing vs Multithreading
17. CPU-bound vs I/O-bound
18. GIL
19. Queue
20. Pipe
21. Pool
22. Process Memory
23. if __name__ == "__main__":
```

# Final Quick Revision

```text
Multiprocessing
       ↓
Multiple Processes
       ↓
Separate Memory
       ↓
Multiple CPU Cores
       ↓
Best for CPU-bound Tasks
```

```text
Process()
    ↓
start()
    ↓
Running
    ↓
Task Execution
    ↓
Finished
    ↓
join()
```

```text
CPU-bound
    ↓
Multiprocessing

I/O-bound
    ↓
Threading / Asyncio
```

"""