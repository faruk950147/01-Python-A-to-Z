"""
# Python Threading & Multithreading — Easy English Notes

---

# 1. What is a Thread?

A **thread** is a small unit of execution inside a process.

A process can have one or many threads.

When a Python program starts, it normally has a **Main Thread**.

```text
Process
│
├── Main Thread
├── Worker Thread 1 → Task A
├── Worker Thread 2 → Task B
└── Worker Thread 3 → Task C
```

Threads inside the same process usually share the same memory and resources.

### Simple Definition

> A thread is an execution path inside a process.

---

# 2. What is Threading?

**Threading** means using multiple threads in one process so that multiple tasks can make progress at the same time.

Python provides the built-in `threading` module.

```python
import threading
```

Threading is especially useful for **I/O-bound tasks**.

Examples:

```text
API Requests
Network Requests
File Operations
Database Operations
Web Scraping
HTTP Requests
Waiting for External Services
```

---

# 3. What is Concurrency?

**Concurrency** means handling multiple tasks so their execution can overlap in time.

Example:

```text
Task A ─────────────
Task B ─────────
Task C ────────────
```

The tasks can make progress during overlapping time periods.

### Concurrency vs Parallelism

**Concurrency**

> Multiple tasks make progress during overlapping time periods.

**Parallelism**

> Multiple tasks actually execute at the same time, usually on different CPU cores.

So:

```text
Concurrency
→ Tasks overlap in progress.

Parallelism
→ Tasks execute simultaneously.
```

Concurrency does not always mean that tasks run at exactly the same moment.

---

# 4. Why Use Threading?

Suppose we have three I/O tasks:

```text
Task A → 3 seconds
Task B → 3 seconds
Task C → 3 seconds
```

Without concurrency:

```text
Task A → 3 sec
Task B → 3 sec
Task C → 3 sec

Total ≈ 9 sec
```

With suitable concurrency:

```text
Task A ─────────
Task B ─────────
Task C ─────────

Total may be closer to ≈ 3 sec
```

This is only an example.

Actual performance depends on:

* Network speed
* Server response time
* Operating system
* Number of threads
* I/O speed
* CPU overhead
* Application design

Threading does **not guarantee** a specific speed improvement.

---

# 5. The `threading` Module

Python has a built-in module called `threading`.

```python
import threading
```

It provides classes and functions for creating and controlling threads.

---

# 6. Creating a Basic Thread

```python
import threading


def task():
    print("Task is running")


thread = threading.Thread(target=task)

thread.start()
```

Here:

```python
threading.Thread(target=task)
```

creates a thread object.

And:

```python
thread.start()
```

starts the thread.

### Important

Use:

```python
target=task
```

Not:

```python
target=task()
```

Why?

Because:

```python
task()
```

calls the function immediately.

But:

```python
target=task
```

passes the function to the thread.

---

# 7. `start()` vs `run()`

## `start()`

```python
thread.start()
```

`start()` starts a new thread of execution.

It causes the thread's `run()` method to execute in that new thread.

A thread can normally be started only once.

---

## `run()`

```python
thread.run()
```

`run()` contains the actual work performed by the thread.

But if you call `run()` directly, it does **not** create a new thread.

The target function runs in the current thread.

Example:

```python
import threading


def task():
    print("Task is running")


thread = threading.Thread(target=task)

thread.run()
```

Here, no new thread is created.

Normally use:

```python
thread.start()
```

instead of:

```python
thread.run()
```

### Easy Rule

```text
start()
→ Creates/starts a new thread

run()
→ Runs the thread's work directly in the current execution context
```

---

# 8. `join()`

`join()` makes the current thread wait until another thread finishes.

Example:

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

Here:

```python
thread.join()
```

makes the Main Thread wait for `thread`.

### Important

`join()` does **not stop** the thread.

It only waits for the thread to finish.

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

The three threads can make progress concurrently.

### Important

The output order is **not guaranteed**.

For example:

```text
Thread 1 started
Thread 2 started
Thread 3 started
Thread 2 finished
Thread 1 finished
Thread 3 finished
```

Another execution may have a different order.

This happens because thread scheduling is controlled by the operating system and Python runtime.

---

# 10. Passing Arguments with `args`

The `args` parameter is used to pass positional arguments to a thread's target function.

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

### Why is there a comma?

This:

```python
("Faruk",)
```

is a tuple with one element.

But:

```python
("Faruk")
```

is just a string inside parentheses.

So this is correct:

```python
args=("Faruk",)
```

---

# 11. Using `kwargs`

`kwargs` is used to pass keyword arguments.

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

We can give a custom name to a thread.

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

Possible output:

```text
Worker-1
```

---

# 13. `current_thread()`

We can get the currently running thread using:

```python
threading.current_thread()
```

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

Useful attributes:

```python
current.name
current.ident
```

---

# 14. `active_count()`

To get the approximate number of active threads:

```python
threading.active_count()
```

Example:

```python
import threading

print(threading.active_count())
```

The result includes the current thread and other active threads managed by the threading system.

---

# 15. Thread Lifecycle

A simple thread lifecycle is:

```text
Thread Object Created
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

Example:

```python
thread = threading.Thread(target=task)
```

Then:

```python
thread.start()
```

Then the thread runs the target function.

Finally, the thread finishes.

This is a simplified model. Real operating-system thread states are more detailed.

---

# 16. Daemon Threads

A **daemon thread** is a background thread that does not keep the Python program alive when no non-daemon threads remain.

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

When the Python process exits, daemon threads are **not guaranteed to finish** their work.

### Do not use daemon threads for important work

For example:

```text
Important Database Update
Important File Write
Financial Transaction
Critical Data Processing
```

For important work, use a controlled shutdown method.

---

# 17. Non-Daemon Threads

Threads are normally **non-daemon** by default.

Example:

```python
thread = threading.Thread(target=task)
```

A non-daemon thread can keep the Python program alive until it finishes.

Conceptually:

```text
Main Thread finishes
        │
        ▼
Non-daemon thread still running?
        │
       Yes
        │
        ▼
Process remains alive
```

---

# 18. Shared Resources

A **shared resource** is data or a resource that multiple threads can access.

Examples:

```text
Shared Resource
│
├── Counter
├── Bank Balance
├── Available Seats
├── File
├── Database Record
└── Shared Data Structure
```

Example:

```python
counter = 0
```

If multiple threads change the same data, synchronization may be needed.

---

# 19. Race Condition

A **race condition** happens when the result of a program depends on the timing or order of concurrent operations.

Example:

```python
counter += 1
```

Conceptually, this means:

```text
Read counter
      ↓
Calculate new value
      ↓
Write new value
```

Suppose:

```text
Initial counter = 0

Thread 1 → Read 0
Thread 2 → Read 0

Thread 1 → Write 1
Thread 2 → Write 1
```

Expected:

```text
2
```

Possible result:

```text
1
```

This can happen because both threads access shared data without proper synchronization.

### Solution

Use a synchronization mechanism:

```python
with lock:
    counter += 1
```

---

# 20. Critical Section

A **critical section** is a part of code that accesses or changes shared data and may need synchronization.

Example:

```python
with lock:
    counter += 1
```

Here:

```python
counter += 1
```

is the critical operation.

The goal is to protect shared data from conflicting access.

---

# 21. Lock

A `Lock` is used to protect a critical section.

```python
import threading

lock = threading.Lock()
```

Only one thread can hold a normal `Lock` at a time.

If another thread tries to acquire the same locked lock, it waits.

---

# 22. `acquire()` and `release()`

A lock can be controlled manually:

```python
lock.acquire()

# Critical Section

lock.release()
```

`acquire()` gets the lock.

`release()` gives the lock back.

### Problem

If an exception happens before `release()`, the lock may remain locked.

So manual lock management can be risky.

---

# 23. Safe Manual Lock Management

Use `try/finally` when manually managing a lock:

```python
lock.acquire()

try:
    counter += 1

finally:
    lock.release()
```

Even if an error occurs, the `finally` block releases the lock.

---

# 24. `with lock` — Recommended

A cleaner method is:

```python
with lock:
    counter += 1
```

Python automatically handles acquiring and releasing the lock.

Complete example:

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

Because the shared update is protected by the lock.

---

# 25. Real-Life Lock Example

Imagine a bathroom with only one key:

```text
Bathroom
   │
  LOCK
   │
Person A → Inside
Person B → Waiting
Person C → Waiting
```

The same idea applies to threads:

```text
Thread A → Lock → Critical Section
Thread B → Wait
Thread C → Wait
```

A lock provides **mutual exclusion**.

That means only one thread can enter the protected section at a time.

---

# 26. RLock

`RLock` means **Reentrant Lock**.

A thread that already owns an `RLock` can acquire the same lock again.

Example:

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

This works because the same thread can acquire the `RLock` again.

### Lock vs RLock

```text
Lock
→ Normal mutual-exclusion lock.

RLock
→ The same thread can acquire it repeatedly.
```

An `RLock` keeps track of how many times the owning thread acquired it.

Therefore, it must be released the same number of times.

---

# 27. Semaphore

A **Semaphore** controls how many threads can use a resource at the same time.

```python
import threading

semaphore = threading.Semaphore(3)
```

This allows up to **3 threads** to acquire it at the same time.

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

At most two threads can be inside the protected section at the same time.

---

# 28. Lock vs Semaphore

## Lock

```python
lock = threading.Lock()
```

Usually:

```text
Maximum 1 thread
```

## Semaphore

```python
semaphore = threading.Semaphore(3)
```

Means:

```text
Maximum 3 threads
```

Easy rule:

```text
Lock
↓
1 thread at a time

Semaphore(3)
↓
Maximum 3 threads at a time
```

---

# 29. Event

`Event` is a simple way for threads to communicate using a signal.

```python
event = threading.Event()
```

One thread can wait:

```python
event.wait()
```

Another thread can send a signal:

```python
event.set()
```

Useful when one thread needs to wait until another thread says that something has happened.

---

# 30. Event Methods

### `set()`

```python
event.set()
```

Sets the event.

Waiting threads can continue.

### `clear()`

```python
event.clear()
```

Clears the event.

### `wait()`

```python
event.wait()
```

Waits until the event is set.

### `is_set()`

```python
event.is_set()
```

Checks whether the event is set.

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

`Condition` is useful when threads need to wait for a particular state.

One thread waits, and another thread sends a notification.

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

### Important

In real producer-consumer code, normally check the required state in a loop:

```python
with condition:
    while not data_available:
        condition.wait()
```

This is safer because a thread can wake up even when the required state is not actually ready.

---

# 33. Event vs Condition

## Event

Used for simple signaling:

```text
"Something happened."
```

## Condition

Used when a thread needs to wait for a specific state:

```text
"Tell me when data is available."
```

Easy rule:

```text
Event
→ Simple signaling

Condition
→ Wait for a condition + notification
```

---

# 34. Queue

Python provides a thread-safe queue:

```python
from queue import Queue
```

Create a queue:

```python
queue = Queue()
```

Add data:

```python
queue.put("Task 1")
```

Get data:

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

`Queue` is very useful for communication between producer and consumer threads.

---

# 35. Producer-Consumer Pattern

The **Producer-Consumer pattern** is a common concurrency design.

The producer creates tasks.

The consumer processes tasks.

```text
Producer
    │
    │ Creates Task
    ▼
  Queue
    │
    │ Gets Task
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

This pattern is useful in:

* Backend systems
* Web applications
* Task processing
* Data pipelines

---

# 36. ThreadPoolExecutor

When there are many small or similar tasks, manually creating many threads can be difficult.

`ThreadPoolExecutor` provides an easier way to manage a group of worker threads.

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

Here:

```python
max_workers=3
```

means the executor can use up to 3 worker threads at the same time.

---

# 37. `submit()` and `Future`

`submit()` sends a task to the thread pool.

It returns a `Future`.

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

A `Future` represents the result of an asynchronous task.

Useful methods:

```python
future.result()
future.done()
future.exception()
future.cancel()
```

### Important

```python
future.result()
```

waits until the task is finished if the result is not ready yet.

---

# 38. Thread Exception Handling

Exceptions inside threads should be handled properly.

Example:

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

### Important

If an exception escapes from a normal `Thread` target, Python reports the exception for that thread.

It does **not automatically send the exception** to the thread that called `start()`.

With `ThreadPoolExecutor`, the exception is stored in the `Future` and is raised when:

```python
future.result()
```

is called.

---

# 39. Getting a Return Value from a Thread

A normal `threading.Thread` does not directly provide the return value of its target function.

Example:

```python
def task():
    return 100
```

If we create:

```python
thread = threading.Thread(target=task)
```

we cannot do:

```python
result = thread.result()
```

because `Thread` does not have a `result()` method.

A convenient solution is `ThreadPoolExecutor`:

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

Other solutions include:

* `queue.Queue`
* Shared data with synchronization
* Callback functions
* Custom thread classes

---

# 40. Thread Information

We can get information about a thread using:

```python
import threading


current = threading.current_thread()

print(current.name)
print(current.ident)
print(current.is_alive())
```

Important:

```python
threading.current_thread()
```

Returns the current thread.

```python
current.name
```

Returns the thread name.

```python
current.ident
```

Returns the thread ID.

It can be `None` before a thread starts.

```python
current.is_alive()
```

Checks whether the thread is currently running/alive.

---

# 41. Thread-Safe

Code or a resource is **thread-safe** when it works correctly when multiple threads access it concurrently according to its synchronization guarantees.

Example:

```python
with lock:
    shared_data.append(item)
```

The lock can protect the shared operation.

### Important

Thread-safe does not mean "fast".

Synchronization can add some overhead, but it helps keep the program correct.

---

# 42. Deadlock

A **deadlock** happens when two or more threads wait forever for resources held by each other.

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

Result:

```text
Thread A waits for Thread B
Thread B waits for Thread A
```

Neither can continue.

---

# 43. How to Prevent Deadlocks

## 1. Use the Same Lock Order

Make all threads acquire multiple locks in the same order.

For example:

```text
Lock A
   ↓
Lock B
```

Do not let another thread do:

```text
Lock B
   ↓
Lock A
```

---

## 2. Keep Lock Scope Small

Hold a lock only for the time you really need it.

Bad:

```python
with lock:
    perform_expensive_network_request()
    perform_large_computation()
    update_shared_data()
```

Better:

```python
data = perform_expensive_operation()

with lock:
    update_shared_data(data)
```

The exact design depends on the application.

---

## 3. Avoid Unnecessary Locks

Do not use synchronization when it is not needed.

---

## 4. Use Timeouts

Some synchronization operations support timeouts.

Example:

```python
if lock.acquire(timeout=2):

    try:
        # Critical section
        pass

    finally:
        lock.release()

else:
    print("Could not acquire lock")
```

Timeouts do not solve every deadlock, but they can prevent waiting forever in some situations.

---

# 44. Web Request Example

Threading is often useful for independent I/O-bound requests.

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

Each URL is handled by a separate thread.

### Production considerations

For real applications, consider:

* Connection pooling
* Request timeouts
* Exception handling
* Rate limits
* Resource limits
* Thread pools

For example:

```python
requests.get(url, timeout=10)
```

is safer than making a request without a timeout.

---

# 45. Creating a Thread Using a Class

We can create a custom thread class by inheriting from `threading.Thread`.

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

The main work is written inside:

```python
run()
```

When we call:

```python
thread.start()
```

Python runs `run()` in the new thread.

---

# 46. Multiple Threads with a Custom Class

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

The three uploader threads can make progress concurrently.

---

# 47. CPU-Bound vs I/O-Bound

## CPU-Bound Tasks

A CPU-bound task spends most of its time doing calculations.

Examples:

```text
Large Mathematical Calculations
Image Processing
Heavy Computation
Data Processing
CPU-intensive Algorithms
```

In traditional CPython, normal Python threads generally cannot execute Python bytecode on multiple CPU cores at the same time because of the GIL.

For these tasks, `multiprocessing` or other parallel-computation methods may be better.

---

# 48. I/O-Bound Tasks

An I/O-bound task spends a lot of time waiting for external operations.

Examples:

```text
API Requests
Network Requests
Database Operations
File I/O
Web Scraping
HTTP Requests
```

While one thread waits for I/O, another thread can often continue working.

Therefore, threading is often very useful for I/O-bound tasks.

---

# 49. What is the GIL?

**GIL = Global Interpreter Lock**

In traditional CPython, the GIL is a mechanism that protects the interpreter's internal state and allows only one thread at a time to execute Python bytecode within an interpreter.

Because of this, CPU-bound pure-Python code usually does not get true multi-core parallelism simply by creating more threads.

Conceptually:

```text
CPU-bound Python code
        ↓
Traditional CPython GIL
        ↓
Threads do not normally give
multi-core Python-bytecode execution
        ↓
Multiprocessing may be better
```

For I/O-bound tasks:

```text
I/O-bound
    ↓
Thread waits for I/O
    ↓
Another thread can make progress
    ↓
Threading can be useful
```

### Modern Python Note

Modern Python also has free-threaded CPython builds that can run without the traditional GIL.

So the statement:

> "Python has a GIL"

is mainly a statement about traditional CPython execution.

For ordinary CPython builds, the GIL is still an important concept.

---

# 50. Threading vs Multiprocessing

| Feature               | Threading                                                         | Multiprocessing                |
| --------------------- | ----------------------------------------------------------------- | ------------------------------ |
| Basic unit            | Thread                                                            | Process                        |
| Memory                | Threads share process memory                                      | Processes have separate memory |
| Creation cost         | Usually lower                                                     | Usually higher                 |
| I/O-bound tasks       | Often very useful                                                 | Can also be useful             |
| CPU-bound Python code | Limited by traditional CPython GIL                                | Can use multiple CPU cores     |
| Communication         | Often easier through shared memory, but synchronization is needed | Usually uses IPC mechanisms    |
| Synchronization       | Locks, Events, Conditions, etc.                                   | Process synchronization / IPC  |
| Memory usage          | Usually lower                                                     | Usually higher                 |
| Isolation             | Lower                                                             | Higher                         |

### Simple Starting Rule

```text
I/O-bound
    ↓
Threading

CPU-bound
    ↓
Multiprocessing
```

This is only a starting rule.

The best choice depends on:

* Workload
* Python implementation
* Deployment environment
* Memory requirements
* Communication needs
* CPU count
* External services
* Application architecture

---

# 51. Important Threading Methods

| Method       | Purpose                         |
| ------------ | ------------------------------- |
| `start()`    | Start a thread                  |
| `run()`      | Execute thread logic            |
| `join()`     | Wait for a thread               |
| `is_alive()` | Check whether a thread is alive |
| `acquire()`  | Acquire a lock                  |
| `release()`  | Release a lock                  |
| `wait()`     | Wait for an Event or Condition  |
| `set()`      | Set an Event                    |
| `clear()`    | Clear an Event                  |
| `is_set()`   | Check whether an Event is set   |

---

# 52. Important Threading Classes and Tools

Important classes include:

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

Higher-level tools:

```text
ThreadPoolExecutor
Future
```

Thread-safe communication:

```text
Queue
```

---

# 53. Lock vs RLock vs Semaphore vs Event vs Condition vs Queue

| Tool        | Main Purpose                                         |
| ----------- | ---------------------------------------------------- |
| `Lock`      | Protect a critical section                           |
| `RLock`     | Allow the same thread to acquire the lock repeatedly |
| `Semaphore` | Limit the number of concurrent users                 |
| `Event`     | Simple communication/signaling                       |
| `Condition` | Wait for a state and notify waiting threads          |
| `Queue`     | Thread-safe communication and task exchange          |

---

# 54. Complete Threading Example

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

# 55. Threading Concept Map

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
├── Thread Information
│   ├── current_thread()
│   ├── name
│   ├── ident
│   └── is_alive()
│
├── Shared Resources
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
├── Background Work
│   └── daemon=True
│
├── Thread Pools
│   ├── ThreadPoolExecutor
│   └── Future
│
├── Concurrency Problems
│   ├── Race Condition
│   └── Deadlock
│
└── CPU / I/O
    ├── GIL
    ├── I/O-bound
    └── CPU-bound
```

---

# 56. Interview Questions

## Q1. What is a Thread?

A thread is an execution path inside a process.

---

## Q2. What is Threading?

Threading means using multiple threads in a process so that multiple tasks can make progress concurrently.

---

## Q3. How do you create a thread in Python?

```python
import threading

thread = threading.Thread(target=function)
```

Then:

```python
thread.start()
```

starts the thread.

---

## Q4. What does `start()` do?

`start()` starts a new thread of execution and causes its `run()` method to execute.

A thread can normally be started only once.

---

## Q5. What does `run()` do?

`run()` contains the work performed by the thread.

Calling it directly does not create a new thread.

---

## Q6. What does `join()` do?

`join()` makes the calling thread wait until the target thread finishes.

---

## Q7. What is a Race Condition?

A race condition occurs when the result of concurrent operations depends on their timing or order.

---

## Q8. How can Race Conditions be prevented?

Use appropriate synchronization tools such as:

```python
threading.Lock()
```

Other tools include:

```text
RLock
Semaphore
Condition
Event
Queue
```

depending on the problem.

---

## Q9. What is a Critical Section?

A critical section is a part of code that accesses or changes shared data and may need synchronization.

---

## Q10. What is a Lock?

A lock provides mutual exclusion.

It allows only one thread to hold the lock at a time.

---

## Q11. What is the difference between Lock and RLock?

```text
Lock
→ Normal mutual-exclusion lock.

RLock
→ The same thread can acquire it repeatedly.
```

---

## Q12. What is a Semaphore?

A semaphore limits how many threads can use a resource at the same time.

Example:

```python
threading.Semaphore(3)
```

allows up to three threads to acquire it simultaneously.

---

## Q13. What is an Event?

An Event is a simple signaling mechanism between threads.

---

## Q14. What is a Condition?

A Condition allows threads to wait for a particular state and allows another thread to notify them.

---

## Q15. Why is Queue used?

`Queue` provides thread-safe communication.

It is commonly used for producer-consumer systems.

---

## Q16. What is a Daemon Thread?

A daemon thread is a background thread that does not keep the Python process alive when no non-daemon threads remain.

---

## Q17. What is the GIL?

GIL means **Global Interpreter Lock**.

In traditional CPython, it allows only one thread at a time to execute Python bytecode within an interpreter.

It limits multi-core parallelism for CPU-bound pure-Python code.

---

## Q18. When should Threading be used?

Threading is often useful for I/O-bound tasks:

```text
Network Requests
API Calls
File I/O
Database Operations
Web Scraping
```

---

## Q19. Is Threading ideal for CPU-bound tasks?

Usually not for CPU-bound pure-Python code in traditional CPython because of the GIL.

`multiprocessing` may be more suitable.

---

## Q20. What is Deadlock?

Deadlock happens when threads wait forever for resources held by each other.

---

## Q21. What is Thread-Safe Code?

Thread-safe code behaves correctly when multiple threads access it concurrently according to its intended synchronization guarantees.

---

## Q22. Does `join()` stop a thread?

No.

```python
thread.join()
```

only waits for the thread to finish.

---

## Q23. Does calling `run()` create a new thread?

No.

```python
thread.run()
```

runs the target in the current execution context.

Use:

```python
thread.start()
```

to start a new thread.

---

## Q24. Can a Thread be started more than once?

No.

A `Thread` object can normally be started only once.

This is invalid:

```python
thread.start()
thread.start()
```

Create a new thread object instead.

---

## Q25. Does a normal Thread return the target function's result?

No.

For easy result handling, use:

```python
ThreadPoolExecutor
```

with:

```python
Future
```

---

# 57. Quick Revision

```text
Thread
  ↓
Execution path inside a Process

Threading
  ↓
Using multiple threads concurrently

start()
  ↓
Start a new thread

run()
  ↓
Run thread logic directly when called

join()
  ↓
Wait for a thread to finish

Shared Resource
  ↓
Data/resource used by multiple threads

Race Condition
  ↓
Result depends on concurrent timing/order

Critical Section
  ↓
Code that accesses shared data

Lock
  ↓
Mutual exclusion

RLock
  ↓
Same thread can acquire the lock again

Semaphore
  ↓
Limit concurrent access

Event
  ↓
Simple signal

Condition
  ↓
Wait for a state + notify

Queue
  ↓
Thread-safe Producer → Consumer communication

ThreadPoolExecutor
  ↓
Manage a pool of worker threads

Future
  ↓
Represent an asynchronous result

Daemon
  ↓
Background thread that does not keep the process alive

GIL
  ↓
Traditional CPython limitation on Python-bytecode execution

I/O-bound
  ↓
Threading is often useful

CPU-bound
  ↓
Multiprocessing is often useful in traditional CPython
```

---

# 58. Final Important Topics

When learning Python Threading, understand these topics:

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
12. active_count()
13. is_alive()
14. Shared Resource
15. Race Condition
16. Critical Section
17. Lock
18. acquire()
19. release()
20. with lock
21. RLock
22. Semaphore
23. Event
24. Condition
25. Queue
26. Producer-Consumer
27. Daemon Thread
28. Thread Exception Handling
29. ThreadPoolExecutor
30. Future
31. GIL
32. I/O-bound
33. CPU-bound
34. Threading vs Multiprocessing
35. Deadlock
36. Thread-Safe Code
37. Lock Ordering
38. Timeouts
39. Custom Thread Class
40. Thread Lifecycle
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
             │                           │
             └─────────────┬─────────────┘
                           ↓
                    Shared Resources
                           │
                           ↓
                     Race Condition
                           │
                           ↓
                    Synchronization
                  ┌────────┼────────┐
                  ↓        ↓        ↓
                Lock     RLock   Semaphore
                  │
                  ↓
             Communication
             ┌────┼────┐
             ↓    ↓    ↓
           Event Condition Queue
                           │
                           ↓
                  Producer → Consumer
                           │
                           ↓
                   ThreadPoolExecutor
                           │
                           ↓
                      I/O-bound
                           │
                           ↓
                    Threading Useful
```

---

# One-Line Revision

```text
Thread
→ Execution path inside a process

Threading
→ Concurrent task execution

start()
→ Start a new thread

run()
→ Execute thread logic in the current execution context when called directly

join()
→ Wait for a thread to finish

Shared Resource
→ Common data/resource

Race Condition
→ Timing-dependent unsafe concurrent access

Critical Section
→ Shared-state code requiring synchronization

Lock
→ Mutual exclusion

RLock
→ Same thread can acquire it again

Semaphore
→ Limit concurrent access

Event
→ Simple signal

Condition
→ Wait for a state + notify

Queue
→ Thread-safe Producer → Consumer communication

Daemon
→ Background thread that does not keep the process alive

ThreadPoolExecutor
→ Manage a pool of worker threads

Future
→ Represent an asynchronous result

GIL
→ Traditional CPython limitation on simultaneous Python-bytecode execution

I/O-bound
→ Threading is often useful

CPU-bound
→ Multiprocessing is often useful in traditional CPython
```

---

# Final Summary

The main idea of Python threading is:

```text
Thread
    ↓
Multiple execution paths inside one process
    ↓
Shared memory/resources
    ↓
Possible synchronization problems
    ↓
Race Condition
    ↓
Lock / RLock / Semaphore
    ↓
Communication
    ↓
Event / Condition / Queue
    ↓
Thread Pool
    ↓
ThreadPoolExecutor / Future
    ↓
I/O-bound workloads
    ↓
Threading is often useful
```

The most important practical rule is:

```text
I/O-bound
    ↓
Consider Threading / ThreadPoolExecutor

CPU-bound pure-Python code
    ↓
Traditional CPython
    ↓
Consider Multiprocessing or another
parallel-computation approach
```

But this is only a starting rule.

Always choose the concurrency method based on:

* Actual workload
* Performance requirements
* Python implementation
* Memory usage
* Communication needs
* CPU resources
* External services
* Application architecture

## Most Important Things to Remember

```text
1. Thread = execution path inside a process.

2. Threading = using multiple threads concurrently.

3. start() = starts a new thread.

4. run() = runs the thread's work directly if called manually.

5. join() = waits for a thread to finish.

6. Lock = protects shared data.

7. Race Condition = unsafe result caused by concurrent access.

8. RLock = same thread can acquire the lock again.

9. Semaphore = allows a limited number of threads.

10. Event = simple thread signaling.

11. Condition = wait for a specific state.

12. Queue = safe communication between threads.

13. ThreadPoolExecutor = easier thread-pool management.

14. Future = represents a task's eventual result.

15. Daemon = background thread that does not keep the process alive.

16. I/O-bound → Threading is often useful.

17. CPU-bound pure Python → Multiprocessing is often better in traditional CPython.

18. GIL is an important limitation of traditional CPython threading.
```

"""