"""
# Python Threading & Multithreading — Full Notes

## 1. What Is a Thread?

A **Thread** is a separate path of execution within a process. A process can contain one or more threads.

Threads within the same process generally share memory and resources.

## 2. What Is Threading?

**Threading** is a technique for allowing multiple threads to make progress concurrently within a process.

Python provides the built-in `threading` module.

```python
import threading
```

Threading is particularly useful for I/O-bound tasks, such as:

- API requests
- Network requests
- File operations
- Database operations
- Web scraping

## 3. Concurrency vs. Parallelism

**Concurrency:** Multiple tasks make progress during overlapping periods. When one task waits for I/O, another task can make progress.

**Parallelism:** Multiple tasks execute at the same time, such as on separate CPU cores.

Concurrency does not necessarily mean parallelism.

## 4. Why Use Threading?

Suppose three I/O tasks each require approximately three seconds of waiting.

**Sequential execution:**

```text
Task A → 3 seconds
Task B → 3 seconds
Task C → 3 seconds
Total ≈ 9 seconds
```

**Concurrent execution:**

```text
Task A ──────────────┐
Task B ──────────────┼── Progress concurrently
Task C ──────────────┘

Total ≈ 3 seconds
```

This is an approximation. Actual execution time depends on I/O behavior, network conditions, scheduling, and thread overhead.

## 5. Creating a Thread

```python
import threading

def task():
    print("Task is running")

thread = threading.Thread(target=task)
thread.start()
```

- `threading.Thread()` creates a thread object.
- `target=task` specifies the function to execute.
- `start()` starts the new thread.

**Correct:**

```python
thread = threading.Thread(target=task)
```

**Incorrect:**

```python
thread = threading.Thread(target=task())
```

Calling `task()` executes the function immediately and passes its return value to `target`. Using `target=task` passes the function itself.

## 6. start() vs. run()

**start():**

```python
thread.start()
```

Starts a new thread and arranges for its `run()` method to execute in that thread.

**run():**

```python
thread.run()
```

Calling `run()` directly does not create a new thread. It executes in the current execution context.

A thread object can normally be started only once.

## 7. join()

The `join()` method makes the calling thread wait until another thread finishes.

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

**Output:**

```text
Task completed
Main thread finished
```

`join()` does not stop a thread. It waits for that thread to finish.

## 8. Multiple Threads

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

The threads can make progress concurrently. Their completion order is not guaranteed.

## 9. args and kwargs

`args` passes positional arguments to the target function.

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

The trailing comma is necessary when creating a tuple with one element.

`kwargs` passes keyword arguments.

```python
import threading

def student(name, age):
    print(name, age)

thread = threading.Thread(
    target=student,
    kwargs={"name": "Faruk", "age": 25}
)

thread.start()
thread.join()
```

## 10. Thread Names and Information

```python
import threading

def task():
    current = threading.current_thread()

    print("Name:", current.name)
    print("ID:", current.ident)

thread = threading.Thread(
    target=task,
    name="Worker-1"
)

thread.start()
thread.join()
```

- `current_thread()`: Returns the current thread object.
- `name`: The thread's name.
- `ident`: The thread identifier.
- `is_alive()`: Checks whether the thread is alive.
- `threading.active_count()`: Returns the number of active thread objects.

## 11. Thread Lifecycle

```text
Thread Object Created
        ↓
      start()
        ↓
Runnable / Running
        ↓
     Finished
```

This is a simplified conceptual lifecycle.

## 12. Daemon Thread

A **daemon thread** is a thread that does not keep the Python process alive by itself.

```python
thread = threading.Thread(
    target=task,
    daemon=True
)
```

When all non-daemon threads finish, the Python process can exit even if daemon threads have unfinished work.

### Common Use Cases

Daemon threads may be appropriate for non-critical background tasks, including:

1. Background monitoring
2. Periodic status checking
3. Non-critical logging
4. System health monitoring
5. Temporary background tasks
6. GUI background tasks
7. Progress monitoring
8. Debugging information collection
9. Temporary statistics collection
10. Non-critical notifications

Use daemon threads only when abruptly abandoning the work is acceptable.

### Example

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

When the main thread finishes and no non-daemon threads remain, the process may exit and the daemon thread may stop before completing its work.

Daemon threads do not guarantee that important data will be saved or cleanup will finish.

## 13. Sending Email with a Daemon Thread

```python
import threading
import time

def send_email():
    print("Email sending started...")
    time.sleep(5)
    print("Email sent successfully!")

thread = threading.Thread(
    target=send_email,
    daemon=True
)

thread.start()

print("User registration completed!")
```

Possible output:

```text
Email sending started...
User registration completed!
```

The process may exit before the email is sent.

Therefore, do not rely solely on daemon threads for important operations such as password reset emails, OTP delivery, or registration confirmation.

For production applications, a durable task queue or background job system is often a better choice.

## 14. Non-Daemon Thread

A **non-daemon thread** generally keeps the Python process alive until its execution finishes.

The default is `daemon=False`.

```python
thread = threading.Thread(
    target=task,
    daemon=False
)
```

### Example

```python
import threading
import time

def save_data():
    print("Saving important data...")
    time.sleep(3)
    print("Data saved successfully!")

thread = threading.Thread(
    target=save_data,
    daemon=False
)

thread.start()

print("Main task completed!")
```

Possible output:

```text
Saving important data...
Main task completed!
Data saved successfully!
```

### Common Use Cases

Non-daemon threads can be useful for:

1. Important email sending
2. Database operations
3. Order processing
4. File uploads
5. Data saving
6. Background jobs that must finish before normal process exit

A non-daemon thread provides an opportunity for work to finish, but it does not guarantee success. Error handling, transaction management, and verification are still necessary.

## 15. Daemon vs. Non-Daemon

**Daemon thread:**

- Does not keep the process alive by itself.
- May be abandoned when the process exits.
- Can be suitable for non-critical background work.

**Non-daemon thread:**

- Normally keeps the process alive while running.
- Allows work to finish before normal process exit.
- Is the default thread type.

A background thread can be either daemon or non-daemon.

## 16. Shared Resources

A **shared resource** is data or a resource accessed by multiple threads.

Examples include:

- Bank balances
- Available seats
- Shared files
- Database records
- Shared data structures

Synchronization may be necessary when multiple threads modify the same data.

## 17. Race Condition

A **race condition** occurs when the result of concurrent operations depends on their timing or execution order.

Suppose `counter = 0`.

```text
Thread 1 → Read 0
Thread 2 → Read 0
Thread 1 → Write 1
Thread 2 → Write 1
```

Two increments should produce `2`, but the final result can be `1`. This is called a lost update.

## 18. Solving a Race Condition with Lock

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

Expected output:

```text
200000
```

The lock protects the increment operation so that only one thread at a time can execute that protected section.

## 19. Critical Section

A **critical section** is a section of code that accesses or modifies shared resources and may require synchronization.

```python
with lock:
    counter += 1
```

Here, `counter += 1` is the critical section.

## 20. Lock

A lock provides mutual exclusion, allowing only one thread at a time to hold the lock.

```python
import threading

lock = threading.Lock()
```

- `acquire()`: Acquires the lock.
- `release()`: Releases the lock.

```python
lock.acquire()

try:
    # Critical section
    pass
finally:
    lock.release()
```

**Recommended approach:**

```python
with lock:
    counter += 1
```

The context manager handles acquiring and releasing the lock.

## 21. RLock

`RLock` stands for **Reentrant Lock**.

The thread that owns an RLock can acquire it again without blocking itself.

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

With a regular `Lock`, attempting to acquire the same lock again from the same thread can cause that thread to block. An RLock allows re-entry by its owning thread.

An RLock must be released as many times as it has been acquired.

## 22. Semaphore

A semaphore limits how many threads can acquire a resource at the same time.

```python
import threading

semaphore = threading.Semaphore(3)
```

Here, up to three threads can acquire the semaphore simultaneously.

### Example

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

Five threads are created, but at most two can enter the protected section simultaneously.

## 23. Lock vs. Semaphore

**Lock:**

- Provides mutual exclusion.
- Typically allows one thread at a time to hold the lock.
- Useful for protecting critical sections.

**Semaphore(3):**

- Allows up to three threads to acquire it simultaneously.
- Useful for limiting concurrent access to a resource.

## 24. Event

An `Event` is a simple signaling mechanism between threads.

```python
event = threading.Event()
```

Methods:

- `set()`: Sets the event.
- `clear()`: Clears the event.
- `wait()`: Waits until the event is set.
- `is_set()`: Checks whether the event is set.

### Example

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
      ↓
  event.wait()
      ↓
    Waiting
      ↓
   event.set()
      ↓
Continue Execution
```

## 25. Condition

A `Condition` is useful when a thread needs to wait until a particular state becomes true.

```python
condition = threading.Condition()
```

Methods:

- `wait()`
- `notify()`
- `notify_all()`

### Example

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

In production code, check the required condition in a loop. Receiving a notification does not guarantee that the desired state is true.

```python
with condition:
    while not data_available:
        condition.wait()
```

The shared state must be checked and modified using appropriate synchronization.

## 26. Event vs. Condition

**Event:**

- Provides simple signaling.
- Uses `set()` to signal.
- Uses `wait()` to wait for the signal.
- Remains set until cleared.

**Condition:**

- Supports waiting for a state and notifying waiters.
- Uses `notify()` or `notify_all()`.
- Is useful when threads coordinate around shared state.

## 27. Queue

Python's `queue` module provides thread-safe queues for communication between threads.

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

Important methods:

- `put()`: Adds an item to the queue.
- `get()`: Retrieves an item.
- `task_done()`: Signals that a retrieved task has been processed.
- `join()`: Waits until all queued tasks have been marked as complete.

`queue.join()` and `thread.join()` are different operations.

## 28. Producer-Consumer Pattern

The producer creates tasks, the queue stores them, and consumers retrieve and process them.

```text
Producer → Queue → Consumer → Process Task
```

Common applications:

- Backend systems
- Web applications
- Task processing
- Data pipelines

## 29. ThreadPoolExecutor

`ThreadPoolExecutor` manages a pool of worker threads.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(number):
    time.sleep(1)
    return number * number

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])

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

`max_workers=3` means that at most three worker threads can execute tasks concurrently.

## 30. submit() and Future

`submit()` schedules a task and returns a `Future` object.

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

A Future represents the eventual result of an asynchronous computation.

Important methods:

- `result()`: Returns the result, waiting if necessary.
- `done()`: Checks whether the task has finished.
- `exception()`: Returns the task's exception, if any.
- `cancel()`: Attempts to cancel a task that has not started.

## 31. Thread Exception Handling

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

If an exception escapes a normal thread's target function, Python reports the exception for that thread. It is not automatically propagated to the thread that called `start()`.

With `ThreadPoolExecutor`, an exception is stored in the Future and can be raised when `future.result()` is called.

## 32. Returning a Value from a Thread

A regular `threading.Thread` does not directly expose the target function's return value.

One convenient solution is `ThreadPoolExecutor`.

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

## 33. Thread-Safe Code

Code or a resource is **thread-safe** when concurrent access is handled correctly according to its synchronization requirements.

```python
with lock:
    shared_data.append(item)
```

Thread safety does not necessarily mean high performance. Synchronization introduces overhead but helps preserve correctness.

## 34. Deadlock

A **deadlock** occurs when two or more threads wait indefinitely for resources held by one another, preventing progress.

Example:

```text
Thread A:
    Acquires Lock 1
    Waits for Lock 2

Thread B:
    Acquires Lock 2
    Waits for Lock 1
```

Neither thread can proceed.

## 35. Deadlock Prevention

1. Acquire locks in a consistent order.
2. Keep critical sections small.
3. Avoid unnecessary locks.
4. Use timeouts where appropriate.
5. Avoid calling unknown or blocking code while holding locks.

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

A timeout does not solve every deadlock, but it can prevent indefinite waiting at that acquisition point.

## 36. Web Request Example

```python
import threading
import requests

def download(url):
    try:
        response = requests.get(url, timeout=10)
        print(url, response.status_code)

    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")

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

Threading can improve performance for independent I/O-bound requests.

Production applications should consider connection pooling, request timeouts, exception handling, rate limits, and bounded thread pools.

Install the third-party dependency if necessary:

```bash
pip install requests
```

## 37. Custom Thread Class

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

The `run()` method contains the thread's work. Calling `start()` executes it in the new thread.

## 38. CPU-Bound vs. I/O-Bound Tasks

**CPU-bound tasks:**

- Large mathematical calculations
- Image processing
- Heavy computation
- CPU-intensive algorithms

**I/O-bound tasks:**

- API requests
- Network requests
- Database operations
- File I/O
- Web scraping

In traditional GIL-enabled CPython, ordinary threading usually does not provide multi-core parallelism for pure-Python CPU-bound tasks. Multiprocessing may be more appropriate.

Threading is often beneficial for I/O-bound workloads.

## 39. GIL

GIL stands for **Global Interpreter Lock**.

In traditional CPython builds, the GIL generally allows only one thread at a time to execute Python bytecode within an interpreter.

As a result, adding threads does not necessarily provide multi-core parallelism for CPU-bound pure-Python code.

Threading can still be useful for I/O-bound work.

Modern Python also offers free-threaded CPython builds that can run without the GIL. Therefore, consider the Python implementation and build when reasoning about performance.

## 40. Threading vs. Multiprocessing

| Feature | Threading | Multiprocessing |
|---|---|---|
| Basic unit | Thread | Process |
| Memory | Shared within a process | Generally separate address spaces |
| Creation overhead | Usually lower | Usually higher |
| I/O-bound tasks | Often useful | Can be useful |
| CPU-bound pure Python | Limited by the GIL in traditional CPython | Can use multiple CPU cores |
| Communication | Shared data and synchronization | IPC and process-safe communication |
| Isolation | Threads share process resources | Processes provide stronger isolation |

**General guideline:**

- I/O-bound tasks → Consider threading.
- CPU-bound pure-Python tasks in traditional CPython → Consider multiprocessing.

The best choice depends on the workload, runtime, and implementation requirements.

## 41. Important Threading Methods

- `start()`: Starts a new thread.
- `run()`: Contains the thread's execution logic.
- `join()`: Waits for a thread to finish.
- `is_alive()`: Checks whether a thread is alive.
- `acquire()`: Acquires a lock.
- `release()`: Releases a lock.
- `wait()`: Waits for an event or condition notification.
- `set()`: Sets an event.
- `clear()`: Clears an event.
- `is_set()`: Checks whether an event is set.

## 42. Important Threading Classes

```python
threading.Thread
threading.Lock
threading.RLock
threading.Semaphore
threading.BoundedSemaphore
threading.Event
threading.Condition
threading.Barrier
threading.Timer
```

Higher-level tools:

```python
ThreadPoolExecutor
Future
Queue
```

`Queue` is provided by the separate `queue` module, while `ThreadPoolExecutor` and `Future` are provided by `concurrent.futures`.

## 43. Synchronization Tools Summary

- **Lock:** Protects a critical section.
- **RLock:** Allows the owning thread to acquire the same lock recursively.
- **Semaphore:** Limits concurrent access.
- **Event:** Provides simple signaling.
- **Condition:** Supports waiting for a state and notifying waiters.
- **Queue:** Provides thread-safe communication.

## 44. Complete Threading Example

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
    ↓
Thread-0, Thread-1, Thread-2
    ↓
All Tasks Complete
    ↓
Main Thread Continues
```

## 45. Threading Concept Map

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
│   ├── Daemon Thread
│   └── Non-Daemon Thread
│
├── Thread Pools
│   ├── ThreadPoolExecutor
│   └── Future
│
├── Concurrency Problems
│   ├── Race Condition
│   └── Deadlock
│
└── CPU and I/O
    ├── GIL
    ├── I/O-bound
    └── CPU-bound
```

## 46. Interview Questions and Answers

**Q1. What is a thread?**

A thread is a path of execution within a process.

**Q2. What is threading?**

Threading allows multiple threads to make progress concurrently.

**Q3. How do you create a thread in Python?**

```python
import threading

thread = threading.Thread(target=function)
thread.start()
```

**Q4. What does `start()` do?**

It starts a new thread and arranges for its `run()` method to execute there.

**Q5. What does `run()` do?**

It contains the thread's execution logic. Calling it directly does not create a new thread.

**Q6. What does `join()` do?**

It makes the calling thread wait for another thread to finish.

**Q7. What is a race condition?**

It occurs when concurrent operations produce results that depend on their timing or execution order.

**Q8. How can you prevent race conditions?**

Use appropriate synchronization mechanisms, such as locks, semaphores, or other thread-safe operations.

**Q9. What is a critical section?**

A section of code that accesses or modifies shared resources and may require synchronization.

**Q10. What is a lock?**

A synchronization primitive that provides mutual exclusion.

**Q11. What is the difference between Lock and RLock?**

A regular Lock is non-reentrant, while an RLock allows its owning thread to acquire it multiple times.

**Q12. What is a semaphore?**

A synchronization primitive that limits the number of simultaneous acquisitions.

**Q13. What is an event?**

A simple mechanism for signaling between threads.

**Q14. What is a condition?**

A synchronization mechanism that supports waiting for a state and notifying waiting threads.

**Q15. Why use a queue?**

A queue provides thread-safe communication and supports producer-consumer patterns.

**Q16. What is a daemon thread?**

A thread that does not keep the Python process alive by itself.

**Q17. What is a non-daemon thread?**

A thread that normally keeps the process alive while it is running.

**Q18. Is a daemon thread suitable for sending important emails?**

Not by itself. The process may exit before the email is sent.

**Q19. What is the GIL?**

The Global Interpreter Lock, which limits simultaneous Python bytecode execution in traditional GIL-enabled CPython.

**Q20. When should you use threading?**

Threading is often useful for I/O-bound work, including network requests, file I/O, and web scraping.

**Q21. Is threading ideal for CPU-bound tasks?**

In traditional GIL-enabled CPython, multiprocessing is often more appropriate for CPU-bound pure-Python work.

**Q22. What is a deadlock?**

A situation in which threads wait for resources held by one another and cannot make progress.

**Q23. What is thread-safe code?**

Code that behaves correctly under concurrent access according to its synchronization requirements.

**Q24. Does `join()` stop a thread?**

No. It waits for the thread to finish.

**Q25. Can a thread object be started multiple times?**

Normally, no. Create a new thread object for another execution.

**Q26. Does a normal Thread return the target function's result?**

Not directly. You can use `ThreadPoolExecutor` and `Future.result()` to retrieve a return value.

## 47. Quick Revision

- **Thread:** A path of execution within a process.
- **Threading:** Concurrent progress using multiple threads.
- **start():** Starts a new thread.
- **run():** Contains the thread's execution logic.
- **join():** Waits for a thread to finish.
- **Shared resource:** Data or resources used by multiple threads.
- **Race condition:** An incorrect or unexpected result caused by execution timing or order.
- **Critical section:** Protected code that accesses shared resources.
- **Lock:** Provides mutual exclusion.
- **RLock:** Allows recursive acquisition by the owning thread.
- **Semaphore:** Limits concurrent access.
- **Event:** Simple signaling mechanism.
- **Condition:** Supports state-based waiting and notification.
- **Queue:** Thread-safe communication mechanism.
- **Daemon thread:** Does not keep the process alive by itself.
- **Non-daemon thread:** Normally keeps the process alive while running.
- **ThreadPoolExecutor:** Manages a pool of worker threads.
- **Future:** Represents an asynchronous computation's result.
- **GIL:** Limits simultaneous Python bytecode execution in traditional CPython.
- **I/O-bound tasks:** Often benefit from threading.
- **CPU-bound pure-Python tasks:** Often benefit from multiprocessing in traditional CPython.

## 48. Practice Checklist

1. Understand threads and processes.
2. Create threads using `threading.Thread()`.
3. Understand `start()` versus `run()`.
4. Practice `join()` and multiple threads.
5. Use `args` and `kwargs`.
6. Compare daemon and non-daemon threads.
7. Understand shared resources and race conditions.
8. Practice Lock and RLock.
9. Practice Semaphore.
10. Understand Event and Condition.
11. Implement Queue and producer-consumer patterns.
12. Use ThreadPoolExecutor and Future.
13. Handle thread exceptions.
14. Understand and prevent deadlocks.
15. Compare the GIL, threading, and multiprocessing.

**Recommended learning order:** First master Thread, `start()`, `join()`, and daemon versus non-daemon threads. Then practice race conditions, locks, queues, and ThreadPoolExecutor with small Python programs.
"""