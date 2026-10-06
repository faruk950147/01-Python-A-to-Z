"""
# Python Threading & Multithreading — Complete Notes

---

# 1. What is a Thread?

A **thread** is the smallest unit of execution within a process.

A process can contain one or more threads.

A typical Python program starts with a **Main Thread**.

```text
Process
│
├── Main Thread
├── Worker Thread 1 → Task A
├── Worker Thread 2 → Task B
└── Worker Thread 3 → Task C
```

All threads within the same process generally share the process's memory and resources.

### Simple Definition

> A thread is an execution path within a process.

---

# 2. What is Threading?

**Threading** means using multiple threads within a single process so that multiple tasks can make progress concurrently.

Python's built-in `threading` module provides support for creating and managing threads.

```python
import threading
```

Threading is particularly useful for **I/O-bound tasks**, where threads spend significant time waiting for external operations.

Examples:

```text
API Requests
Network Requests
File I/O
Database Operations
Web Scraping
HTTP Requests
Waiting for External Services
```

---

# 3. Concurrency

**Concurrency** means managing multiple tasks so that their execution can overlap in time.

For example:

```text
Task A ─────────────
Task B ─────────
Task C ────────────
```

The tasks may make progress during overlapping periods.

### Important

**Concurrency is not the same as parallelism.**

```text
Concurrency
→ Multiple tasks make progress during overlapping time periods.

Parallelism
→ Multiple tasks actually execute simultaneously,
  typically on different CPU cores.
```

A concurrent program does not necessarily execute multiple operations at exactly the same instant.

---

# 4. Why Use Threading?

Suppose we have three I/O-bound tasks:

```text
Task A → 3 seconds
Task B → 3 seconds
Task C → 3 seconds
```

Sequential execution might take approximately:

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

However, this is only an illustration.

Actual execution time depends on:

* Network speed
* Server response time
* Operating system scheduling
* Number of threads
* I/O latency
* CPU overhead
* Application architecture

Threading does not guarantee a specific speedup.

---

# 5. The `threading` Module

Python provides the built-in `threading` module for working with threads.

```python
import threading
```

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

creates a `Thread` object.

And:

```python
thread.start()
```

starts the thread.

### Important

The function is passed without parentheses:

```python
target=task
```

Not:

```python
target=task()
```

because `task()` would execute immediately while creating the `Thread` object.

---

# 7. `start()` vs `run()`

## `start()`

```python
thread.start()
```

`start()` starts the thread's execution.

It causes the thread's `run()` method to be invoked in a separate thread of execution.

A thread can normally be started **only once**.

---

## `run()`

```python
thread.run()
```

`run()` contains the actual execution logic for the thread.

If you call `run()` directly, it does **not** start a new thread.

Instead, the target function runs in the current thread.

### Example

```python
import threading


def task():
    print("Task is running")


thread = threading.Thread(target=task)

thread.run()
```

The task runs in the current thread.

Normally, use:

```python
thread.start()
```

rather than calling `run()` directly.

---

# 8. `join()`

`join()` makes the calling thread wait until another thread finishes.

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

causes the Main Thread to wait until `thread` completes.

### Important

`join()` does **not** stop the thread.

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

The exact output order is not guaranteed.

For example:

```text
Thread 1 started
Thread 2 started
Thread 3 started
Thread 2 finished
Thread 1 finished
Thread 3 finished
```

Another execution may produce a different order.

This is because thread scheduling is controlled by the operating system and Python runtime.

---

# 10. Passing Arguments with `args`

The `args` parameter is used to pass positional arguments to the target function.

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

### Why the comma?

For one positional argument:

```python
args=("Faruk",)
```

This is a tuple.

But:

```python
("Faruk")
```

is simply a string surrounded by parentheses.

Therefore:

```python
args=("Faruk",)
```

is correct.

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

A thread can have a custom name.

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

The currently executing thread can be obtained using:

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

Important attributes include:

```python
current.name
current.ident
```

---

# 14. `active_count()`

To get the approximate number of currently active threads:

```python
threading.active_count()
```

Example:

```python
import threading

print(threading.active_count())
```

The count includes the calling thread and other currently active threads managed by the threading module.

---

# 15. Thread Lifecycle

A simplified thread lifecycle can be represented as:

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

↓

```python
thread.start()
```

↓

The thread executes its target.

↓

The thread finishes.

### Note

The actual operating-system scheduling states are more detailed than this simplified diagram.

---

# 16. Daemon Threads

A **daemon thread** is a background thread that does not prevent the Python program from exiting when only daemon threads remain.

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

When the Python process exits, daemon threads are not guaranteed to finish their work.

### Important

Do not use daemon threads for work that must be completed or cleaned up reliably.

For example:

```text
Important database update
Important file write
Financial transaction
Critical data processing
```

For such tasks, a controlled shutdown mechanism is usually better.

---

# 17. Non-Daemon Threads

Threads are non-daemon by default unless configured otherwise.

```python
thread = threading.Thread(target=task)
```

A non-daemon thread can keep the Python program alive until it finishes.

Conceptually:

```text
Main Thread finishes
        │
        ▼
Non-daemon worker still running?
        │
       Yes
        │
        ▼
Process remains alive
```

---

# 18. Shared Resources

A **shared resource** is data or a resource that can be accessed by multiple threads.

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

If multiple threads modify shared state, synchronization may be required.

---

# 19. Race Condition

A **race condition** occurs when the correctness of a program depends on the timing or ordering of concurrent operations.

For example:

```python
counter += 1
```

Conceptually, this involves:

```text
Read counter
      ↓
Calculate new value
      ↓
Write new value
```

Multiple threads accessing shared state without appropriate synchronization can cause lost updates or inconsistent results.

Conceptual example:

```text
Initial counter = 0

Thread 1 → Read 0
Thread 2 → Read 0

Thread 1 → Write 1
Thread 2 → Write 1

Expected logical result → 2
Possible result          → 1
```

### Solution

Protect the critical section with an appropriate synchronization mechanism.

```python
with lock:
    counter += 1
```

---

# 20. Critical Section

A **critical section** is a section of code that accesses or modifies shared state and therefore may require synchronization.

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

The goal is to ensure that shared state is accessed safely.

---

# 21. Lock

A `Lock` is a synchronization primitive used to protect a critical section.

```python
import threading

lock = threading.Lock()
```

A normal `Lock` can be acquired by only one thread at a time.

If another thread attempts to acquire the same lock while it is already held, that thread waits until the lock becomes available.

---

# 22. `acquire()` and `release()`

A lock can be manually controlled:

```python
lock.acquire()

# Critical Section

lock.release()
```

`acquire()` attempts to obtain the lock.

`release()` releases the lock.

### Warning

Manual lock management can be dangerous if an exception occurs before `release()`.

---

# 23. Safe Manual Lock Management

If manually managing a lock, `try/finally` is safer:

```python
lock.acquire()

try:
    counter += 1

finally:
    lock.release()
```

Even if an exception occurs inside the critical section, the `finally` block executes and releases the lock.

---

# 24. `with lock` — Recommended

The cleaner approach is:

```python
with lock:
    counter += 1
```

The context manager handles acquiring and releasing the lock.

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

Because the update is protected by the lock.

---

# 25. Real-Life Lock Example

Imagine a bathroom with one key:

```text
Bathroom
   │
  LOCK
   │
Person A → Inside
Person B → Waiting
Person C → Waiting
```

Similarly:

```text
Thread A → Lock → Critical Section
Thread B → Wait
Thread C → Wait
```

The lock provides mutual exclusion.

---

# 26. RLock

`RLock` means **Reentrant Lock**.

A thread that already owns an `RLock` can acquire the same lock again.

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

This works because the same thread can re-enter the lock.

### Lock vs RLock

```text
Lock
→ A normal mutual-exclusion lock.

RLock
→ The owning thread can acquire it repeatedly.
```

An `RLock` keeps track of the number of acquisitions by the owning thread.

The lock must be released the corresponding number of times.

---

# 27. Semaphore

A `Semaphore` limits the number of threads that can simultaneously enter a protected section or acquire a particular resource.

```python
import threading

semaphore = threading.Semaphore(3)
```

This means up to three threads can acquire the semaphore at the same time.

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

At most two threads can be inside the `with semaphore:` section at a time.

---

# 28. Lock vs Semaphore

## Lock

```python
lock = threading.Lock()
```

Normally:

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

Remember:

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

`Event` is a simple signaling mechanism for communication between threads.

```python
event = threading.Event()
```

One thread can wait:

```python
event.wait()
```

Another thread can signal:

```python
event.set()
```

This is useful when one thread needs to wait until another thread announces that something has happened.

---

# 30. Event Methods

## `set()`

```python
event.set()
```

Sets the internal event flag.

Threads waiting on the event can proceed.

---

## `clear()`

```python
event.clear()
```

Clears the event flag.

---

## `wait()`

```python
event.wait()
```

Waits until the event is set.

---

## `is_set()`

```python
event.is_set()
```

Checks whether the event is currently set.

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

`Condition` is a synchronization primitive used when threads need to wait for a particular state or condition and another thread needs to notify them.

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

In real producer-consumer code, `Condition.wait()` should normally be used in a loop that checks the required state:

```python
with condition:
    while not data_available:
        condition.wait()
```

This protects against waking up when the required condition is not actually satisfied.

---

# 33. Event vs Condition

## Event

Useful for simple signaling:

```text
"Something has happened."
```

## Condition

Useful for waiting for a particular state and coordinating access to shared state:

```text
"Notify me when data becomes available."
```

Remember:

```text
Event
→ Simple signaling

Condition
→ Wait for a condition + notification
```

---

# 34. Queue

Python provides a thread-safe queue through:

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

Retrieve data:

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

`Queue` is particularly useful for communication between producer and consumer threads.

---

# 35. Producer-Consumer Pattern

The **Producer-Consumer pattern** is a common concurrency design.

The producer creates tasks or data.

The consumer processes them.

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

This pattern is highly useful in backend systems, task processing, web applications, and data pipelines.

---

# 36. `ThreadPoolExecutor`

When many small or similar tasks need to be executed concurrently, manually creating a large number of threads can be inconvenient.

`ThreadPoolExecutor` provides a higher-level interface for managing a pool of worker threads.

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

With `max_workers=3`, the executor uses up to three worker threads concurrently.

---

# 37. `submit()` and `Future`

`submit()` schedules a callable and returns a `Future`.

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

A `Future` represents the eventual result of an asynchronous operation.

Useful methods include:

```python
future.result()
future.done()
future.exception()
future.cancel()
```

### Important

Calling:

```python
future.result()
```

waits until the task completes if the result is not ready yet.

---

# 38. Thread Exception Handling

Exceptions raised inside a thread should be handled appropriately.

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

If an exception escapes a normal `threading.Thread` target, Python reports the exception through the thread's exception handling mechanism, but it does not automatically propagate the exception to the thread that called `start()`.

With `ThreadPoolExecutor`, exceptions are associated with the returned `Future` and are raised when calling:

```python
future.result()
```

---

# 39. Getting a Return Value from a Thread

A normal `threading.Thread` does not directly provide the return value of its target function.

For example:

```python
def task():
    return 100
```

If you use:

```python
thread = threading.Thread(target=task)
```

you cannot simply do:

```python
result = thread.result()
```

because `Thread` has no such method.

One convenient solution is `ThreadPoolExecutor`:

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

Other approaches include:

* `queue.Queue`
* Shared state with synchronization
* Callback functions
* Custom thread classes

---

# 40. Thread Information

Information about the current thread can be obtained using:

```python
import threading


current = threading.current_thread()

print(current.name)
print(current.ident)
print(current.is_alive())
```

### Important

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

Returns the thread identifier, which can be `None` before the thread has started.

```python
current.is_alive()
```

Returns whether the thread is currently alive.

---

# 41. Thread-Safe

Code or a resource is **thread-safe** if it behaves correctly when accessed concurrently by multiple threads according to its documented guarantees.

Example:

```python
with lock:
    shared_data.append(item)
```

The lock can protect the shared operation from conflicting access.

### Important

Thread-safe does not necessarily mean "fast".

Synchronization can introduce overhead, but it can provide correctness.

---

# 42. Deadlock

A **deadlock** occurs when two or more threads wait indefinitely for resources held by each other.

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

Neither thread can continue.

---

# 43. Preventing Deadlocks

## 1. Use Consistent Lock Ordering

Make all threads acquire multiple locks in the same order.

For example:

```text
Lock A
   ↓
Lock B
```

Avoid another thread doing:

```text
Lock B
   ↓
Lock A
```

---

## 2. Keep Lock Scope Small

Hold a lock only for the minimum amount of time required.

Bad design:

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

Do not use synchronization where it is not needed.

---

## 4. Use Timeouts When Appropriate

Some synchronization operations support timeouts.

For example:

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

Timeouts do not automatically solve all deadlocks, but they can prevent indefinite waiting in some designs.

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

Here, each URL is processed by a separate thread.

### Important

For production applications, consider:

* Connection pooling
* Request timeouts
* Exception handling
* Rate limits
* Resource limits
* A thread pool instead of unlimited thread creation

For example, with `requests`:

```python
requests.get(url, timeout=10)
```

is generally safer than making a request without a timeout.

---

# 45. Creating a Thread Using a Class

You can create a custom thread class by inheriting from `threading.Thread`.

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

The thread's main work is implemented in:

```python
run()
```

Calling:

```python
thread.start()
```

causes `run()` to execute in the new thread.

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

The three uploader threads can run concurrently.

---

# 47. CPU-Bound vs I/O-Bound

## CPU-Bound Tasks

A CPU-bound task spends most of its time performing computation.

Examples:

```text
Large Mathematical Calculations
Image Processing
Heavy Computation
Data Processing
CPU-intensive Algorithms
```

For CPU-bound Python code in standard CPython, regular threads generally do not provide parallel execution of Python bytecode across multiple CPU cores because of the GIL.

In such cases, `multiprocessing` or other parallel-computation approaches may be more suitable.

---

# 48. I/O-Bound Tasks

An I/O-bound task spends significant time waiting for external operations.

Examples:

```text
API Requests
Network Requests
Database Operations
File I/O
Web Scraping
HTTP Requests
```

While one thread is waiting for I/O, another thread can potentially make progress.

Therefore, threading can be very useful for I/O-bound workloads.

---

# 49. What is the GIL?

**GIL = Global Interpreter Lock**

In standard CPython, the GIL is a mechanism that protects the interpreter's internal state and, in the traditional CPython execution model, allows only one thread at a time to execute Python bytecode within a given interpreter.

Therefore, CPU-bound pure-Python code generally does not achieve multi-core parallelism simply by creating multiple threads.

Conceptually:

```text
CPU-bound Python code
        ↓
GIL limitation in traditional CPython
        ↓
Threads generally do not provide
multi-core Python-bytecode parallelism
        ↓
Multiprocessing may be more suitable
```

For I/O-bound workloads:

```text
I/O-bound
    ↓
Threads can spend time waiting on I/O
    ↓
Other threads can make progress
    ↓
Threading can be useful
```

### Important Modern Note

Modern Python versions have additional interpreter configurations and implementations, including free-threaded CPython builds that can run without the traditional GIL.

Therefore, the statement:

> "Python has a GIL"

should be understood primarily in the context of traditional CPython execution.

For ordinary CPython builds, the GIL remains an important consideration.

---

# 50. Threading vs Multiprocessing

| Feature               | Threading                                                        | Multiprocessing                       |
| --------------------- | ---------------------------------------------------------------- | ------------------------------------- |
| Basic unit            | Thread                                                           | Process                               |
| Memory                | Threads in a process share memory                                | Processes have separate memory spaces |
| Creation overhead     | Usually lower                                                    | Usually higher                        |
| I/O-bound tasks       | Often very useful                                                | Can also be useful                    |
| CPU-bound Python code | Limited by traditional CPython GIL                               | Can use multiple CPU cores            |
| Communication         | Often easier through shared memory, but requires synchronization | Usually requires IPC mechanisms       |
| Synchronization       | Locks, Events, Conditions, etc.                                  | Process synchronization / IPC         |
| Memory usage          | Usually lower                                                    | Usually higher                        |
| Isolation             | Lower                                                            | Higher                                |

### Simple Starting Rule

```text
I/O-bound
    ↓
Threading

CPU-bound
    ↓
Multiprocessing
```

This is a useful starting point, not an absolute rule.

The best choice depends on:

* Workload
* Python implementation
* Deployment environment
* Memory requirements
* Communication requirements
* CPU count
* External services
* Application architecture

---

# 51. Important Threading Methods

| Method       | Purpose                                            |
| ------------ | -------------------------------------------------- |
| `start()`    | Start a thread                                     |
| `run()`      | Execute the thread's target logic                  |
| `join()`     | Wait for a thread to finish                        |
| `is_alive()` | Check whether a thread is alive                    |
| `acquire()`  | Acquire a synchronization primitive such as a lock |
| `release()`  | Release a lock                                     |
| `wait()`     | Wait on an Event or Condition                      |
| `set()`      | Set an Event                                       |
| `clear()`    | Clear an Event                                     |
| `is_set()`   | Check whether an Event is set                      |

---

# 52. Important Threading Classes and Tools

Important synchronization and threading-related classes include:

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

Higher-level concurrency tools include:

```text
ThreadPoolExecutor
Future
```

For thread-safe task/data communication:

```text
Queue
```

---

# 53. Lock vs RLock vs Semaphore vs Event vs Condition vs Queue

| Tool        | Main Purpose                                                |
| ----------- | ----------------------------------------------------------- |
| `Lock`      | Protect a critical section using mutual exclusion           |
| `RLock`     | Allow the owning thread to acquire the same lock repeatedly |
| `Semaphore` | Limit the number of concurrent users of a resource          |
| `Event`     | Simple signaling between threads                            |
| `Condition` | Wait for a state and notify waiting threads                 |
| `Queue`     | Thread-safe communication and task exchange                 |

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
├── Concurrency Issues
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

A thread is an execution path within a process.

---

## Q2. What is Threading?

Threading is the use of multiple threads within a process to perform tasks concurrently.

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

`start()` starts the thread and causes its `run()` method to execute in a separate thread of execution.

A thread can normally be started only once.

---

## Q5. What does `run()` do?

`run()` contains the code executed by the thread.

Calling it directly does not create a new thread.

---

## Q6. What does `join()` do?

`join()` causes the calling thread to wait until the target thread terminates.

---

## Q7. What is a Race Condition?

A race condition occurs when the result of concurrent operations depends on their timing or ordering.

---

## Q8. How can Race Conditions be prevented?

Use appropriate synchronization mechanisms such as:

```python
threading.Lock()
```

Other tools may include:

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

A critical section is a part of code that accesses or modifies shared state and may require synchronization.

---

## Q10. What is a Lock?

A lock provides mutual exclusion so that only one thread at a time can hold the lock.

---

## Q11. What is the difference between Lock and RLock?

```text
Lock
→ Normal mutual-exclusion lock.

RLock
→ The same thread can acquire the lock repeatedly.
```

---

## Q12. What is a Semaphore?

A semaphore limits how many threads can acquire a resource concurrently.

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

A Condition allows threads to wait for a particular state and allows another thread to notify waiting threads.

---

## Q15. Why is Queue used?

`Queue` provides thread-safe communication and is commonly used to implement producer-consumer systems.

---

## Q16. What is a Daemon Thread?

A daemon thread is a background thread that does not prevent the Python process from exiting when no non-daemon threads remain.

---

## Q17. What is the GIL?

The GIL, or Global Interpreter Lock, is a mechanism in traditional CPython that allows only one thread at a time to execute Python bytecode within an interpreter.

It limits multi-core parallelism for CPU-bound pure-Python code in traditional CPython.

---

## Q18. When should Threading be used?

Threading is often useful for I/O-bound workloads such as:

```text
Network Requests
API Calls
File I/O
Database Operations
Web Scraping
```

---

## Q19. Is Threading ideal for CPU-bound tasks?

For CPU-bound pure-Python code in traditional CPython, threading generally does not provide multi-core Python-bytecode parallelism because of the GIL.

Multiprocessing may be more suitable.

---

## Q20. What is Deadlock?

Deadlock occurs when threads wait indefinitely for resources held by one another.

---

## Q21. What is Thread-Safe Code?

Thread-safe code behaves correctly when accessed concurrently by multiple threads according to its intended synchronization guarantees.

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

executes the thread's target in the current thread.

Use:

```python
thread.start()
```

to start a separate thread.

---

## Q24. Can a Thread be started more than once?

No.

A `Thread` object can normally be started only once.

This is invalid:

```python
thread.start()
thread.start()
```

Instead, create a new `Thread` object.

---

## Q25. Does a normal `Thread` return the target function's result?

No.

For convenient result handling, use:

```python
ThreadPoolExecutor
```

and:

```python
Future
```

---

# 57. Quick Revision

```text
Thread
  ↓
Execution path within a Process

Threading
  ↓
Concurrent execution of multiple tasks

start()
  ↓
Start a new thread of execution

run()
  ↓
Execute the thread's target logic

join()
  ↓
Wait for a thread to finish

Shared Resource
  ↓
Data/resource accessed by multiple threads

Race Condition
  ↓
Result depends on concurrent timing/order

Critical Section
  ↓
Code that accesses shared state

Lock
  ↓
Mutual exclusion

RLock
  ↓
Same thread can re-enter the lock

Semaphore
  ↓
Limit concurrent access

Event
  ↓
Simple signaling

Condition
  ↓
Wait for state + Notify

Queue
  ↓
Thread-safe Producer → Consumer communication

ThreadPoolExecutor
  ↓
Manage a pool of worker threads

Future
  ↓
Handle an asynchronous result

Daemon
  ↓
Background thread that does not keep the process alive

GIL
  ↓
Traditional CPython limitation on concurrent Python-bytecode execution

I/O-bound
  ↓
Threading is often useful

CPU-bound
  ↓
Multiprocessing is often useful in traditional CPython
```

---

# 58. Final Important Topics

When learning Python Threading, make sure you understand these topics:

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
→ Execution path within a process

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
→ Same thread can re-enter

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
→ Handle an asynchronous result

GIL
→ Traditional CPython limitation on simultaneous Python-bytecode execution

I/O-bound
→ Threading is often useful

CPU-bound
→ Multiprocessing is often useful in traditional CPython
```

---

# Final Summary

The most important ideas are:

```text
Thread
    ↓
Multiple execution paths inside one process
    ↓
Shared memory/resources
    ↓
Potential synchronization problems
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
In traditional CPython
    ↓
Consider Multiprocessing or another
parallel-computation approach
```

But always choose the concurrency model based on the actual workload, performance requirements, resource usage, and application architecture.


"""