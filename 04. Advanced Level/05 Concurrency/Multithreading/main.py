"""
# Python Threading & Multithreading — বাংলা নোট

---

# 1. Thread কী?

**Thread** হলো একটি Process-এর ভিতরে execution-এর একটি ছোট unit।

সহজভাবে:

```text
Process
│
├── Main Thread
├── Thread 1 → Task A
├── Thread 2 → Task B
└── Thread 3 → Task C
```

একটি Python program শুরু হলে সাধারণত একটি **Main Thread** থাকে।

---

# 2. Threading কী?

Python-এ **Threading** হলো একটি Process-এর মধ্যে একাধিক Thread ব্যবহার করে একাধিক কাজকে **concurrently** execute করার পদ্ধতি।

Threading বিশেষ করে **I/O-bound task**-এর জন্য useful।

উদাহরণ:

* API Request
* Network Request
* File Read/Write
* Database Operation
* Web Scraping
* Waiting-based Tasks

---

# 3. Concurrency কী?

**Concurrency** হলো একাধিক কাজের execution এমনভাবে পরিচালনা করা যাতে কাজগুলো overlapping করতে পারে।

উদাহরণ:

```text
Task A ─────────────
Task B ─────────
Task C ────────────
```

এখানে Task A, B এবং C-এর execution overlap করতে পারে।

### গুরুত্বপূর্ণ

**Concurrency মানেই Parallelism নয়।**

```text
Concurrency
→ একাধিক কাজের progress overlapping

Parallelism
→ একাধিক কাজ সত্যিকার অর্থে একই সময়ে execute হওয়া
```

---

# 4. Threading কেন ব্যবহার করব?

ধরা যাক ৩টি I/O task আছে:

```text
Task A → 3 seconds
Task B → 3 seconds
Task C → 3 seconds
```

Sequential execution:

```text
Task A → 3 sec
Task B → 3 sec
Task C → 3 sec

Total ≈ 9 sec
```

Threading ব্যবহার করলে I/O অপেক্ষার সময় অন্য Thread কাজ করতে পারে:

```text
Task A ─────────
Task B ─────────
Task C ─────────

Total ≈ 3 sec
```

তবে exact execution time সবসময় এমন হবে না। এটি task, network, system এবং scheduling-এর উপর নির্ভর করে।

---

# 5. threading Module

Python-এ Thread তৈরি করার জন্য built-in `threading` module ব্যবহার করা হয়।

```python
import threading
```

---

# 6. Basic Thread তৈরি

```python
import threading


def task():
    print("Task is running")


thread = threading.Thread(target=task)

thread.start()
```

এখানে:

```python
threading.Thread(target=task)
```

একটি Thread object তৈরি করে।

আর:

```python
thread.start()
```

Thread-এর execution শুরু করে।

---

# 7. start() বনাম run()

## start()

```python
thread.start()
```

`start()` নতুন Thread-এর execution শুরু করে।

## run()

```python
thread.run()
```

`run()` Thread-এর target কাজ execute করে।

কিন্তু `run()` সরাসরি call করলে নতুন OS-level Thread শুরু হয় না; এটি current Thread-এর execution context-এ চলে।

### সাধারণভাবে ব্যবহার:

```python
thread.start()
```

---

# 8. join() কী?

`join()` ব্যবহার করা হয় কোনো Thread শেষ হওয়া পর্যন্ত calling Thread-কে অপেক্ষা করানোর জন্য।

```python
import threading
import time


def task():
    time.sleep(2)
    print("Task completed")


thread = threading.Thread(target=task)

thread.start()
thread.join()

print("Main thread finished")
```

এখানে:

```python
thread.join()
```

এর কারণে Main Thread অপেক্ষা করবে যতক্ষণ না `thread` শেষ হয়।

---

# 9. Multiple Threads

```python
import threading
import time


def task(name):
    print(f"{name} started")

    time.sleep(2)

    print(f"{name} finished")


t1 = threading.Thread(
    target=task,
    args=("Thread 1",)
)

t2 = threading.Thread(
    target=task,
    args=("Thread 2",)
)

t3 = threading.Thread(
    target=task,
    args=("Thread 3",)
)


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


print("All tasks completed")
```

### গুরুত্বপূর্ণ

Output-এর exact order সবসময় একই নাও হতে পারে।

কারণ Thread scheduling-এর order নির্দিষ্ট নয়।

---

# 10. args দিয়ে Argument পাঠানো

Thread function-এ positional argument পাঠাতে `args` ব্যবহার করা হয়।

```python
import threading


def greet(name):
    print(f"Hello {name}")


thread = threading.Thread(
    target=greet,
    args=("Faruk",)
)

thread.start()
thread.join()
```

Output:

```text
Hello Faruk
```

একটি argument হলেও comma দিতে হয়:

```python
args=("Faruk",)
```

কারণ:

```python
("Faruk",)
```

একটি Tuple।

কিন্তু:

```python
("Faruk")
```

একটি String।

---

# 11. kwargs ব্যবহার

Keyword argument পাঠানোর জন্য `kwargs` ব্যবহার করা যায়।

```python
import threading


def student(name, age):
    print(name, age)


thread = threading.Thread(
    target=student,
    kwargs={
        "name": "Faruk",
        "age": 25
    }
)

thread.start()
thread.join()
```

---

# 12. Thread Name

Thread-এর নাম দেওয়া যায়।

```python
import threading


def task():
    print(threading.current_thread().name)


thread = threading.Thread(
    target=task,
    name="Worker-1"
)

thread.start()
thread.join()
```

Output:

```text
Worker-1
```

---

# 13. current_thread()

বর্তমানে যে Thread execute করছে সেটি পাওয়ার জন্য:

```python
threading.current_thread()
```

ব্যবহার করা হয়।

Example:

```python
import threading


def task():

    current = threading.current_thread()

    print("Name:", current.name)
    print("ID:", current.ident)


thread = threading.Thread(target=task)

thread.start()
thread.join()
```

---

# 14. active_count()

বর্তমানে active Thread-এর সংখ্যা জানার জন্য:

```python
threading.active_count()
```

ব্যবহার করা হয়।

Example:

```python
import threading

print(threading.active_count())
```

---

# 15. Thread Lifecycle

Thread-এর lifecycle সহজভাবে:

```text
New
 │
 ▼
start()
 │
 ▼
Runnable / Running
 │
 ▼
Finished
```

Python-এ:

```python
thread = threading.Thread(...)
```

↓

```python
thread.start()
```

↓

Thread কাজ করে

↓

Thread শেষ হয়।

---

# 16. Daemon Thread

**Daemon Thread** হলো এমন Thread যা background-এ কাজ করে এবং কোনো non-daemon Thread আর না থাকলে Python process-কে alive রাখে না।

Daemon Thread তৈরি:

```python
thread = threading.Thread(
    target=task,
    daemon=True
)
```

Example:

```python
import threading
import time


def background_task():

    while True:
        print("Background running...")
        time.sleep(1)


thread = threading.Thread(
    target=background_task,
    daemon=True
)

thread.start()

time.sleep(3)

print("Main program finished")
```

Main program shutdown হলে daemon Thread-ও process-এর সাথে শেষ হয়ে যেতে পারে।

### Important

Daemon Thread-এর কাজ program shutdown-এর সময় gracefully complete নাও হতে পারে।

তাই important data save করার মতো কাজের জন্য daemon Thread ব্যবহারে সতর্ক থাকতে হবে।

---

# 17. Non-Daemon Thread

Defaultভাবে Python Thread সাধারণত non-daemon।

```python
thread = threading.Thread(target=task)
```

Main Thread শেষ হলেও non-daemon Thread running থাকলে Python process সাধারণত সেই Thread শেষ হওয়া পর্যন্ত alive থাকে।

---

# 18. Shared Resource

যে data বা resource একাধিক Thread access করতে পারে তাকে **Shared Resource** বলে।

Examples:

```text
Shared Resource
│
├── Counter
├── Bank Balance
├── Available Seats
├── File
├── Database Record
└── Shared Variable
```

Example:

```python
counter = 0
```

যদি একাধিক Thread `counter` modify করে, synchronization প্রয়োজন হতে পারে।

---

# 19. Race Condition

যখন একাধিক Thread একই Shared Resource access বা modify করে এবং final result execution timing/order-এর উপর নির্ভর করে, তখন তাকে **Race Condition** বলে।

ধরা যাক:

```python
counter += 1
```

ধারণাগতভাবে:

```text
Read counter
      ↓
Calculate new value
      ↓
Write counter
```

দুই Thread একই সময়ে কাজ করলে update হারিয়ে যেতে পারে।

```text
Thread 1 → Read 0
Thread 2 → Read 0
Thread 1 → Write 1
Thread 2 → Write 1

Expected → 2
Possible result → 1
```

### Solution

Shared resource access করার সময় synchronization ব্যবহার করা যায়।

```python
with lock:
    counter += 1
```

---

# 20. Critical Section

যে code অংশ Shared Resource access বা modify করে এবং synchronization প্রয়োজন হতে পারে তাকে **Critical Section** বলে।

Example:

```python
with lock:
    counter += 1
```

এখানে:

```python
counter += 1
```

হলো critical operation।

---

# 21. Lock

`Lock` হলো একটি synchronization mechanism যা একই সময়ে critical section-এ একাধিক Thread ঢোকা থেকে বাধা দেয়।

```python
import threading

lock = threading.Lock()
```

---

# 22. acquire() এবং release()

Lock manually ব্যবহার করা যায়:

```python
lock.acquire()

# Critical Section

lock.release()
```

`acquire()` Lock নেওয়ার চেষ্টা করে।

`release()` Lock ছেড়ে দেয়।

---

# 23. Manual Lock — Safe Version

Manual Lock ব্যবহার করলে `try/finally` ব্যবহার করা ভালো:

```python
lock.acquire()

try:
    counter += 1

finally:
    lock.release()
```

কারণ exception হলেও `finally` block execute হবে এবং Lock release হবে।

---

# 24. with lock — Recommended

Lock ব্যবহারের সবচেয়ে clean উপায়:

```python
with lock:
    counter += 1
```

Python automatically Lock acquire এবং release করার ব্যবস্থা করে।

Complete Example:

```python
import threading


counter = 0
lock = threading.Lock()


def increment():

    global counter

    for _ in range(100000):

        with lock:
            counter += 1


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)


t1.start()
t2.start()


t1.join()
t2.join()


print(counter)
```

Expected result:

```text
200000
```

---

# 25. Lock-এর Real-Life Example

একটি bathroom-এর দরজা চিন্তা করো:

```text
Bathroom
   │
  LOCK
   │
Person A → ভিতরে
Person B → অপেক্ষা
Person C → অপেক্ষা
```

একইভাবে:

```text
Thread A → Lock → Critical Section
Thread B → Wait
Thread C → Wait
```

---

# 26. RLock

`RLock` = **Reentrant Lock**

একই Thread একই Lock একাধিকবার acquire করতে পারে।

```python
import threading

lock = threading.RLock()


def function_a():

    with lock:
        function_b()


def function_b():

    with lock:
        print("Running")


function_a()
```

### Lock বনাম RLock

```text
Lock
→ সাধারণ mutual exclusion

RLock
→ একই Thread একই Lock multiple times acquire করতে পারে
```

একই Thread যতবার `RLock` acquire করবে, ততবার release করতে হবে।

---

# 27. Semaphore

`Semaphore` ব্যবহার করা হয় একই সময়ে কতগুলো Thread resource ব্যবহার করতে পারবে তা সীমাবদ্ধ করার জন্য।

```python
import threading

semaphore = threading.Semaphore(3)
```

এর অর্থ সর্বোচ্চ ৩টি Thread একই সময়ে Semaphore acquire করতে পারবে।

Example:

```python
import threading
import time


semaphore = threading.Semaphore(2)


def task(number):

    with semaphore:

        print(f"Thread {number} entered")

        time.sleep(2)

        print(f"Thread {number} leaving")


threads = []


for i in range(5):

    t = threading.Thread(
        target=task,
        args=(i,)
    )

    threads.append(t)
    t.start()


for t in threads:
    t.join()
```

---

# 28. Lock বনাম Semaphore

## Lock

```python
lock = threading.Lock()
```

সাধারণভাবে:

```text
একবারে ১ Thread
```

## Semaphore

```python
semaphore = threading.Semaphore(3)
```

মানে:

```text
একবারে সর্বোচ্চ ৩ Thread
```

মনে রাখো:

```text
Lock
↓
1 Thread

Semaphore(3)
↓
Maximum 3 Threads
```

---

# 29. Event

`Event` হলো Thread-এর মধ্যে simple signal communication mechanism।

```python
event = threading.Event()
```

Worker Thread বলতে পারে:

> "আমি signal-এর জন্য অপেক্ষা করছি।"

```python
event.wait()
```

অন্য Thread signal দিতে পারে:

```python
event.set()
```

---

# 30. Event-এর গুরুত্বপূর্ণ Methods

## set()

```python
event.set()
```

Event set করে।

## clear()

```python
event.clear()
```

Event reset করে।

## wait()

```python
event.wait()
```

Event set হওয়া পর্যন্ত অপেক্ষা করে।

## is_set()

```python
event.is_set()
```

Event set আছে কিনা check করে।

---

# 31. Event Example

```python
import threading
import time


def worker(event):

    print("Thread is waiting...")

    event.wait()

    print("Thread received the signal!")


event = threading.Event()


thread = threading.Thread(
    target=worker,
    args=(event,)
)

thread.start()

time.sleep(2)

print("Sending signal...")

event.set()

thread.join()
```

Flow:

```text
Worker Thread
      │
      ▼
event.wait()
      │
      │ Waiting
      ▼
event.set()
      │
      ▼
Continue Execution
```

---

# 32. Condition

`Condition` এমন একটি synchronization mechanism যা Thread-কে কোনো state/condition-এর জন্য wait করতে এবং অন্য Thread-কে notify করতে সাহায্য করে।

```python
condition = threading.Condition()
```

Common methods:

```python
condition.wait()
condition.notify()
condition.notify_all()
```

Example:

```python
import threading
import time


condition = threading.Condition()


def consumer():

    with condition:

        print("Consumer waiting...")

        condition.wait()

        print("Consumer received signal")


def producer():

    time.sleep(2)

    with condition:

        print("Producer sending signal")

        condition.notify()


t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)


t1.start()
t2.start()


t1.join()
t2.join()
```

---

# 33. Event বনাম Condition

## Event

Simple signal:

```text
"Signal দেওয়া হয়েছে!"
```

## Condition

State/condition-এর জন্য wait এবং notify:

```text
"Data available হলে আমাকে জানাও।"
```

মনে রাখো:

```text
Event
→ Simple Signaling

Condition
→ Wait + Notify
```

---

# 34. Queue

Thread-এর মধ্যে safely data/task exchange করার জন্য Python-এর:

```python
from queue import Queue
```

ব্যবহার করা যায়।

```python
queue = Queue()
```

Data যোগ:

```python
queue.put("Task 1")
```

Data নেওয়া:

```python
queue.get()
```

Example:

```python
from queue import Queue


queue = Queue()

queue.put("Task 1")
queue.put("Task 2")

print(queue.get())
print(queue.get())
```

Output:

```text
Task 1
Task 2
```

---

# 35. Producer-Consumer Pattern

Producer data তৈরি করে।

Consumer data ব্যবহার করে।

```text
Producer
    │
    │ Produces Task
    ▼
  Queue
    │
    │ Consumes Task
    ▼
Consumer
```

Example:

```text
Customer Order
      ↓
Producer
      ↓
Queue
      ↓
Worker
      ↓
Process Order
```

Backend development-এ এই pattern খুব গুরুত্বপূর্ণ।

---

# 36. ThreadPoolExecutor

অনেকগুলো ছোট Task থাকলে manually অনেক Thread তৈরি করার পরিবর্তে `ThreadPoolExecutor` ব্যবহার করা সুবিধাজনক।

```python
from concurrent.futures import ThreadPoolExecutor
```

Example:

```python
from concurrent.futures import ThreadPoolExecutor
import time


def task(number):

    time.sleep(1)

    return number * number


with ThreadPoolExecutor(max_workers=3) as executor:

    results = executor.map(
        task,
        [1, 2, 3, 4, 5]
    )

    for result in results:
        print(result)
```

Output:

```text
1
4
9
16
25
```

---

# 37. submit() এবং Future

```python
from concurrent.futures import ThreadPoolExecutor
import time


def task(x):

    time.sleep(2)

    return x * x


with ThreadPoolExecutor(max_workers=3) as executor:

    future = executor.submit(task, 5)

    print("Task submitted")

    result = future.result()

    print(result)
```

Output:

```text
Task submitted
25
```

`Future` হলো একটি asynchronous operation-এর result handle।

---

# 38. Thread Exception Handling

Thread-এর ভিতরের exception handle করা যায়:

```python
import threading


def task():

    try:

        result = 10 / 0

        print(result)

    except Exception as e:

        print("Error:", e)


thread = threading.Thread(target=task)

thread.start()
thread.join()
```

Output:

```text
Error: division by zero
```

---

# 39. Thread-এর ভিতরের Return Value

সাধারণ `threading.Thread` থেকে সরাসরি function-এর return value পাওয়া যায় না।

Example:

```python
def task():
    return 100
```

Thread দিয়ে চালালে:

```python
thread = threading.Thread(target=task)
```

`thread` object থেকে সরাসরি `100` পাওয়া যাবে না।

Result প্রয়োজন হলে `ThreadPoolExecutor` এবং `Future` ব্যবহার করা সুবিধাজনক।

```python
from concurrent.futures import ThreadPoolExecutor


def task():
    return 100


with ThreadPoolExecutor(max_workers=1) as executor:

    future = executor.submit(task)

    result = future.result()

    print(result)
```

Output:

```text
100
```

---

# 40. Thread Information

বর্তমান Thread সম্পর্কে information:

```python
import threading


current = threading.current_thread()

print(current.name)
print(current.ident)
print(current.is_alive())
```

### গুরুত্বপূর্ণ

```python
threading.current_thread()
```

Current Thread return করে।

```python
current.name
```

Thread-এর নাম।

```python
current.ident
```

Thread identifier।

```python
current.is_alive()
```

Thread alive কিনা check করে।

---

# 41. Thread-safe কী?

যে code বা resource একাধিক Thread থেকে safely ব্যবহার করা যায় তাকে **Thread-safe** বলা হয়।

Example:

```python
with lock:
    shared_data.append(item)
```

এখানে Lock shared data access synchronize করছে।

---

# 42. Deadlock

যখন দুই বা তার বেশি Thread একে অপরের Lock/resource-এর জন্য অপেক্ষা করতে থাকে এবং কেউ এগোতে পারে না, তখন **Deadlock** হয়।

Example:

```text
Thread A
   │
   ├── Lock 1 ✓
   │
   └── Waiting for Lock 2


Thread B
   │
   ├── Lock 2 ✓
   │
   └── Waiting for Lock 1
```

ফলে:

```text
A waits for B
B waits for A
```

Program আটকে যায়।

---

# 43. Deadlock Prevent করার উপায়

### 1. Consistent Lock Ordering

সব Thread যেন একই order-এ Lock নেয়।

```text
Lock A
   ↓
Lock B
```

কেউ যেন:

```text
Lock B
   ↓
Lock A
```

না নেয়।

### 2. Lock-এর Scope ছোট রাখা

প্রয়োজনের চেয়ে বেশি সময় Lock ধরে রাখা উচিত নয়।

### 3. অপ্রয়োজনীয় Lock এড়িয়ে চলা

যেখানে synchronization প্রয়োজন নেই সেখানে Lock ব্যবহার না করা।

### 4. Timeout ব্যবহার করা

প্রয়োজনে Lock acquisition-এ timeout ব্যবহার করা যায়।

---

# 44. Web Request-এর Example

Threading I/O-bound কাজের একটি common example:

```python
import threading
import requests


def download(url):

    response = requests.get(url)

    print(url, response.status_code)


urls = [
    "https://example.com",
    "https://python.org",
    "https://github.com"
]


threads = []


for url in urls:

    thread = threading.Thread(
        target=download,
        args=(url,)
    )

    threads.append(thread)

    thread.start()


for thread in threads:

    thread.join()
```

এখানে প্রতিটি URL-এর জন্য একটি Thread ব্যবহার করা হয়েছে।

---

# 45. Class দিয়ে Thread তৈরি

`threading.Thread` inherit করে custom Thread class তৈরি করা যায়।

```python
import threading
import time


class VideoUploader(threading.Thread):

    def __init__(self, video):
        super().__init__()
        self.video = video

    def run(self):

        print(f"Started uploading {self.video}")

        time.sleep(1)

        print(f"Video uploaded: {self.video}")


thread = VideoUploader("video1.mp4")

thread.start()
thread.join()
```

এখানে:

```python
run()
```

এর ভিতরে Thread-এর কাজ লেখা হয়েছে।

---

# 46. Multiple Threads with Class

```python
import threading
import time


class VideoUploader(threading.Thread):

    def __init__(self, video):
        super().__init__()
        self.video = video

    def run(self):

        print(f"Started uploading {self.video}")

        time.sleep(1)

        print(f"Video uploaded: {self.video}")


videos = [
    "video1.mp4",
    "video2.mp4",
    "video3.mp4"
]


threads = []


for video in videos:

    thread = VideoUploader(video)

    thread.start()

    threads.append(thread)


for thread in threads:

    thread.join()


print("All videos uploaded!")
```

---

# 47. CPU-bound বনাম I/O-bound

## CPU-bound

যেখানে CPU বেশি কাজ করে।

Examples:

```text
Large Mathematical Calculation
Heavy Computation
CPU-intensive Processing
```

Standard CPython-এ এই ধরনের Python code-এর ক্ষেত্রে Threading সাধারণত multiple CPU cores-এর full parallel execution দেয় না।

এক্ষেত্রে অনেক সময়:

```python
multiprocessing
```

বেশি suitable।

---

# 48. I/O-bound

যেখানে program-এর অনেক সময় external I/O-এর জন্য অপেক্ষা করতে হয়।

Examples:

```text
API Request
Network Request
Database Operation
File I/O
Web Scraping
HTTP Request
```

একটি Thread I/O-এর জন্য অপেক্ষা করার সময় অন্য Thread কাজ করতে পারে।

তাই I/O-bound task-এর ক্ষেত্রে Threading useful হতে পারে।

---

# 49. GIL কী?

**GIL = Global Interpreter Lock**

CPython-এর traditional execution model-এ GIL একই সময়ে একটি Thread-কে Python bytecode execution-এর জন্য interpreter lock ধরে রাখতে দেয়।

তাই CPU-bound Python code-এর ক্ষেত্রে একাধিক Thread ব্যবহার করে সাধারণত multiple CPU core-এ একই সময়ে Python bytecode execute করা যায় না।

তবে I/O-bound কাজের ক্ষেত্রে Threading এখনও খুব useful।

### সহজভাবে:

```text
CPU-bound
   ↓
GIL limitation
   ↓
Threading → সাধারণত ideal নয়


I/O-bound
   ↓
I/O waiting
   ↓
Threading → Useful
```

---

# 50. Threading বনাম Multiprocessing

| Feature           | Threading                   | Multiprocessing         |
| ----------------- | --------------------------- | ----------------------- |
| Unit              | Thread                      | Process                 |
| Memory            | একই Process-এর মধ্যে shared | Separate                |
| Creation Overhead | কম                          | বেশি                    |
| I/O-bound         | ভালো                        | ভালো                    |
| CPU-bound Python  | GIL-এর কারণে limited        | ভালো                    |
| Communication     | তুলনামূলক সহজ               | তুলনামূলক বেশি overhead |
| Memory Usage      | তুলনামূলক কম                | তুলনামূলক বেশি          |

### Simple Rule

```text
I/O-bound
    ↓
Threading

CPU-bound
    ↓
Multiprocessing
```

এটি একটি useful starting rule; actual architecture task-এর requirements-এর উপর নির্ভর করে।

---

# 51. Important Threading Methods

| Method       | কাজ                              |
| ------------ | -------------------------------- |
| `start()`    | Thread শুরু করে                  |
| `run()`      | Thread-এর কাজ execute করে        |
| `join()`     | Thread শেষ হওয়া পর্যন্ত wait করে |
| `is_alive()` | Thread alive কিনা check করে      |
| `acquire()`  | Lock/Semaphore acquire করে       |
| `release()`  | Lock release করে                 |
| `wait()`     | Event/Condition-এর জন্য wait করে |
| `set()`      | Event set করে                    |
| `clear()`    | Event clear করে                  |
| `is_set()`   | Event set আছে কিনা check করে     |

---

# 52. Important Threading Classes

Python-এর গুরুত্বপূর্ণ threading classes:

```text
Thread
Lock
RLock
Semaphore
BoundedSemaphore
Event
Condition
Barrier
Timer
```

Thread-related task management-এর জন্য:

```text
ThreadPoolExecutor
Future
Queue
```

খুব গুরুত্বপূর্ণ।

---

# 53. Lock vs RLock vs Semaphore vs Event vs Condition vs Queue

| Tool        | Main Purpose                                              |
| ----------- | --------------------------------------------------------- |
| `Lock`      | Critical Section protect করা                              |
| `RLock`     | Same Thread-কে একই Lock multiple times acquire করতে দেওয়া |
| `Semaphore` | Concurrent access limit করা                               |
| `Event`     | Simple signal পাঠানো                                      |
| `Condition` | Wait + Notify                                             |
| `Queue`     | Thread-safe data/task exchange                            |

---

# 54. Threading-এর Complete Example

```python
import threading
import time


def task(name):

    print(f"{name} started")

    time.sleep(2)

    print(f"{name} finished")


threads = []


for i in range(3):

    thread = threading.Thread(
        target=task,
        args=(f"Thread-{i}",)
    )

    threads.append(thread)

    thread.start()


for thread in threads:

    thread.join()


print("All threads completed")
```

Flow:

```text
Main Thread
    │
    ├── Thread-0
    │
    ├── Thread-1
    │
    └── Thread-2
           │
           ▼
        Complete
           │
           ▼
    Main Thread continues
```

---

# 55. Python Threading Concept Map

```text
Python Threading
│
├── Thread Creation
│   ├── threading.Thread()
│   └── Custom Thread Class
│
├── Thread Control
│   ├── start()
│   ├── run()
│   └── join()
│
├── Shared Resource
│   └── Race Condition
│
├── Synchronization
│   ├── Lock
│   ├── RLock
│   └── Semaphore
│
├── Communication
│   ├── Event
│   ├── Condition
│   └── Queue
│
├── Thread Information
│   ├── current_thread()
│   ├── name
│   ├── ident
│   └── is_alive()
│
├── Background Thread
│   └── daemon=True
│
└── Concurrency
    ├── GIL
    ├── ThreadPoolExecutor
    └── Multiprocessing
```

---

# 56. Interview Questions

## Q1. Thread কী?

Thread হলো একটি Process-এর ভিতরে execution-এর একটি ছোট unit।

---

## Q2. Threading কী?

একটি Process-এর মধ্যে একাধিক Thread ব্যবহার করে একাধিক কাজ concurrently execute করার technique।

---

## Q3. Python-এ Thread কীভাবে তৈরি করা হয়?

```python
threading.Thread(target=function)
```

---

## Q4. `start()` কী করে?

নতুন Thread-এর execution শুরু করে।

---

## Q5. `run()` কী করে?

Thread-এর target কাজ execute করে।

তবে সরাসরি `run()` call করলে নতুন Thread তৈরি হয় না।

---

## Q6. `join()` কী করে?

Calling Thread-কে নির্দিষ্ট Thread শেষ হওয়া পর্যন্ত অপেক্ষা করায়।

---

## Q7. Race Condition কী?

Multiple Thread একই Shared Resource concurrently access বা modify করার কারণে execution timing/order-এর উপর নির্ভরশীল unexpected result হওয়া।

---

## Q8. Race Condition কীভাবে prevent করা যায়?

Synchronization mechanism ব্যবহার করে।

যেমন:

```python
threading.Lock()
```

---

## Q9. Critical Section কী?

Shared Resource access বা modify করা code-এর sensitive অংশ।

---

## Q10. Lock কী?

Lock critical section-এ একই সময়ে একাধিক Thread ঢোকা থেকে বাধা দেয়।

---

## Q11. Lock এবং RLock-এর পার্থক্য কী?

```text
Lock
→ সাধারণ mutual exclusion

RLock
→ একই Thread একই Lock multiple times acquire করতে পারে
```

---

## Q12. Semaphore কী?

Semaphore concurrent access-এর সংখ্যা সীমাবদ্ধ করে।

```python
threading.Semaphore(3)
```

সর্বোচ্চ ৩টি Thread একই সময়ে Semaphore acquire করতে পারবে।

---

## Q13. Event কী?

Event হলো Thread-এর মধ্যে simple signaling mechanism।

---

## Q14. Condition কী?

Condition Thread-কে কোনো state/condition-এর জন্য wait এবং অন্য Thread-কে notify করতে সাহায্য করে।

---

## Q15. Queue কেন ব্যবহার করা হয়?

Thread-safe data/task exchange এবং Producer-Consumer pattern implement করার জন্য।

---

## Q16. Daemon Thread কী?

Daemon Thread হলো background Thread যা non-daemon Thread শেষ হওয়ার পর Python process-কে alive রাখে না।

---

## Q17. GIL কী?

GIL বা Global Interpreter Lock হলো CPython-এর একটি mechanism যা একই সময়ে Python bytecode execution-এর জন্য Thread access সীমাবদ্ধ করে।

---

## Q18. Threading কখন ব্যবহার করা উচিত?

মূলত I/O-bound task-এর ক্ষেত্রে।

---

## Q19. CPU-bound task-এর জন্য Threading কি ideal?

Standard CPython-এ সাধারণত নয়। CPU-bound Python code-এর ক্ষেত্রে GIL-এর কারণে multiprocessing অনেক সময় বেশি suitable।

---

## Q20. Deadlock কী?

দুই বা তার বেশি Thread একে অপরের Lock/resource-এর জন্য অপেক্ষা করতে থাকলে এবং কেউ এগোতে না পারলে Deadlock হয়।

---

# 57. Quick Revision

```text
Thread
  ↓
Process-এর ভিতরের execution unit

Threading
  ↓
Multiple concurrent tasks

start()
  ↓
Thread শুরু

run()
  ↓
Thread-এর কাজ

join()
  ↓
Thread শেষ হওয়া পর্যন্ত wait

Shared Resource
  ↓
একাধিক Thread-এর common data/resource

Race Condition
  ↓
Unsafe concurrent access

Critical Section
  ↓
Shared resource access-এর sensitive code

Lock
  ↓
একবারে একটি Thread

RLock
  ↓
Same Thread একই Lock multiple times নিতে পারে

Semaphore
  ↓
Concurrent access limit

Event
  ↓
Simple Signal

Condition
  ↓
Wait + Notify

Queue
  ↓
Producer → Queue → Consumer

ThreadPoolExecutor
  ↓
Thread pool management

Daemon
  ↓
Background Thread

GIL
  ↓
CPython Python-bytecode execution limitation

I/O-bound
  ↓
Threading useful

CPU-bound
  ↓
Multiprocessing often useful
```

---

# 58. Final Important Topics

Python Threading শেখার সময় এই Topics অবশ্যই ভালোভাবে শিখতে হবে:

```text
1. Process
2. Thread
3. Threading
4. threading.Thread
5. start()
6. run()
7. join()
8. args
9. kwargs
10. Thread Name
11. current_thread()
12. is_alive()
13. Shared Resource
14. Race Condition
15. Critical Section
16. Lock
17. acquire()
18. release()
19. with lock
20. RLock
21. Semaphore
22. Event
23. Condition
24. Queue
25. Producer-Consumer
26. Daemon Thread
27. Thread Exception Handling
28. ThreadPoolExecutor
29. Future
30. GIL
31. I/O-bound
32. CPU-bound
33. Threading vs Multiprocessing
34. Deadlock
35. Thread-safe Code
```

---

# Final Mental Model

```text
                  Python Threading
                        │
          ┌─────────────┴─────────────┐
          ↓                           ↓
   Thread Creation              Thread Control
          │                           │
   Thread() / Class             start() / join()
          │
          ↓
    Shared Resources
          │
          ↓
    Race Condition
          │
          ↓
    Synchronization
       ┌──┼────┐
       ↓  ↓    ↓
     Lock RLock Semaphore
       
          ↓
   Thread Communication
      ┌────┼────┐
      ↓    ↓    ↓
    Event Condition Queue
```

# One-Line Revision

```text
Thread
→ Worker

Threading
→ Concurrent task execution

start()
→ Start Thread

run()
→ Execute Thread task

join()
→ Wait for Thread

Shared Resource
→ Common data/resource

Race Condition
→ Unsafe concurrent access

Critical Section
→ Sensitive shared-data code

Lock
→ One Thread at a time

RLock
→ Same Thread can re-enter

Semaphore
→ Limited concurrent access

Event
→ Simple signal

Condition
→ Wait + Notify

Queue
→ Producer → Consumer

Daemon
→ Background Thread

ThreadPoolExecutor
→ Manage worker threads

GIL
→ CPython Python-bytecode execution limitation

I/O-bound
→ Threading is often useful

CPU-bound
→ Multiprocessing is often useful
```

"""