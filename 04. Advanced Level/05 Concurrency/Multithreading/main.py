"""
# Python Multithreading

## 1. What is Multithreading?

**Multithreading** is a technique in which a program uses multiple **threads** to perform multiple tasks concurrently.

A **thread** is the smallest unit of execution within a process.

In Python, multithreading is mainly implemented using the:

```python
import threading
```

module.

### Basic Idea

```text
Program
   │
   ├── Main Thread
   │
   ├── Thread 1
   │
   ├── Thread 2
   │
   └── Thread 3
```

---

# 2. Creating and Running Threads

Python provides `threading.Thread()` for creating threads.

## Example

```python
import threading
import time


def first_program():
    for i in range(5):
        print("First Program:", i)
        time.sleep(1)


def second_program():
    for i in range(5):
        print("Second Program:", i)
        time.sleep(1)


# Create threads
t1 = threading.Thread(target=first_program)
t2 = threading.Thread(target=second_program)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Program Finished")
```

### Important Methods

```python
thread.start()
```

Starts the thread's execution.

```python
thread.join()
```

Makes the calling thread wait until the specified thread finishes.

### Basic Flow

```text
Create Thread
      ↓
   start()
      ↓
Thread Runs
      ↓
   join()
      ↓
Wait Until Finished
```

---

# 3. Race Condition

## What is a Race Condition?

A **race condition** occurs when multiple threads access and modify the same **shared resource** concurrently, and the final result depends on the timing or order of execution.

### Example

Suppose several buses are trying to book seats from the same seat counter.

```python
import threading
import time


available_seats = 5


class Bus(threading.Thread):

    def __init__(self, name, move_time):
        super().__init__()
        self.name = name
        self.move_time = move_time

    def run(self):
        global available_seats

        for _ in range(3):

            print(f"{self.name} is checking seat availability...")
            time.sleep(self.move_time)

            if available_seats > 0:

                print(f"{self.name} found a seat! Booking now...")

                time.sleep(0.1)

                available_seats -= 1

                print(
                    f"{self.name} booked a seat. "
                    f"Remaining seats: {available_seats}"
                )

            else:
                print(f"{self.name} found no seat available!")


bus1 = Bus("Bus-1", 0.2)
bus2 = Bus("Bus-2", 0.2)
bus3 = Bus("Bus-3", 0.2)

bus1.start()
bus2.start()
bus3.start()

bus1.join()
bus2.join()
bus3.join()

print("All buses finished checking!")
```

### Problem

Multiple threads can reach:

```python
if available_seats > 0:
```

before one of them updates:

```python
available_seats -= 1
```

Therefore, multiple threads may make decisions based on the same old value.

This is the basic idea behind a race condition.

---

# 4. Shared Resource

A **shared resource** is data or a resource that can be accessed by multiple threads.

Examples:

```text
Shared Resource
├── Bank Balance
├── Available Seats
├── File
├── Database Record
├── Counter
└── Shared Variable
```

Example:

```python
available_seats = 5
```

Here, `available_seats` is a shared variable.

If multiple threads modify it, synchronization may be required.

---

# 5. Lock

## What is a Lock?

A **Lock** is a synchronization mechanism used to ensure that only one thread at a time enters a protected section of code.

Python provides:

```python
lock = threading.Lock()
```

A Lock is commonly used to protect a **critical section**.

---

# 6. Critical Section

A **critical section** is a part of a program that accesses or modifies a shared resource and therefore needs synchronization.

Example:

```python
with lock:
    available_seats -= 1
```

Here:

```text
Thread
   ↓
Acquire Lock
   ↓
Critical Section
   ↓
Modify Shared Resource
   ↓
Release Lock
```

---

# 7. Using `with lock`

The recommended way to use a lock is often:

```python
with lock:
    # Critical Section
```

Example:

```python
import threading
import time


available_seats = 5

lock = threading.Lock()


class Bus(threading.Thread):

    def __init__(self, name, move_time, lock):
        super().__init__()
        self.name = name
        self.move_time = move_time
        self.lock = lock

    def run(self):
        global available_seats

        for _ in range(3):

            print(f"{self.name} is checking seat availability...")
            time.sleep(self.move_time)

            with self.lock:

                if available_seats > 0:

                    print(f"{self.name} found a seat! Booking now...")

                    time.sleep(0.1)

                    available_seats -= 1

                    print(
                        f"{self.name} booked a seat. "
                        f"Remaining seats: {available_seats}"
                    )

                else:
                    print(f"{self.name} found no seat available!")


bus1 = Bus("Bus-A", 0.2, lock)
bus2 = Bus("Bus-B", 0.3, lock)
bus3 = Bus("Bus-C", 0.1, lock)

bus1.start()
bus2.start()
bus3.start()

bus1.join()
bus2.join()
bus3.join()

print("Final available seats:", available_seats)
```

Using:

```python
with lock:
```

automatically acquires the lock when entering the block and releases it when leaving the block, including when an exception occurs.

---

# 8. `acquire()` and `release()`

A lock can also be managed manually.

```python
lock.acquire()

# Critical Section

lock.release()
```

### `acquire()`

Attempts to acquire the lock.

If another thread already holds the lock, the calling thread normally waits until the lock becomes available.

### `release()`

Releases the lock so another thread can acquire it.

---

# 9. Manual Lock vs `with lock`

## Method 1 — Manual

```python
lock.acquire()

try:
    balance -= amount
finally:
    lock.release()
```

The `try/finally` structure is important when manually managing locks because it ensures the lock is released even if an exception occurs.

## Method 2 — Context Manager

```python
with lock:
    balance -= amount
```

This is usually cleaner and safer.

---

# 10. Bank Account Example with Lock

```python
import threading


balance = 100
lock = threading.Lock()


def withdraw(amount):
    global balance

    for _ in range(100000):

        with lock:
            balance -= amount


def deposit(amount):
    global balance

    for _ in range(100000):

        with lock:
            balance += amount


t1 = threading.Thread(target=withdraw, args=(1,))
t2 = threading.Thread(target=deposit, args=(1,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", balance)
```

Here:

```text
Thread 1 → Withdraw
Thread 2 → Deposit
             ↓
          balance
             ↑
            Lock
```

`balance` is the shared resource.

---

# 11. Object-Level Lock

Each object can have its own lock.

```python
import threading


class Account:

    def __init__(self, balance):
        self._balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            self._balance -= amount

    def deposit(self, amount):
        with self.lock:
            self._balance += amount

    def get_balance(self):
        with self.lock:
            return self._balance
```

Here:

```python
self.lock
```

is a separate lock for each `Account` object.

For example:

```text
Account A → Lock A
Account B → Lock B
Account C → Lock C
```

This can allow independent account objects to be operated on concurrently.

---

# 12. Thread-Safe Transfer

When transferring money between two accounts, both accounts may need to be locked.

A common technique is to always acquire the two locks in a consistent order.

```python
def transfer(self, amount, other_account):

    first, second = (
        (self, other_account)
        if id(self) < id(other_account)
        else (other_account, self)
    )

    with first.lock:

        with second.lock:

            if self._balance >= amount:

                self._balance -= amount
                other_account._balance += amount

            else:
                print("Insufficient balance for transfer")
```

### Why use a consistent lock order?

Consider:

```text
Thread 1:
Lock A → waiting for Lock B

Thread 2:
Lock B → waiting for Lock A
```

Both threads could wait forever.

This situation is called a **deadlock**.

Using a consistent lock-acquisition order helps prevent this particular type of deadlock.

---

# 13. `@property` with Lock

Python's `@property` can be used to expose an object's balance through a getter.

```python
import threading


class Account:

    def __init__(self, balance):
        self._balance = balance
        self.lock = threading.Lock()

    @property
    def balance(self):

        with self.lock:
            return self._balance

    def withdraw(self, amount):

        with self.lock:
            self._balance -= amount

    def deposit(self, amount):

        with self.lock:
            self._balance += amount
```

Access:

```python
account.balance
```

Using the lock inside the getter is useful when the value needs synchronized access.

---

# 14. RLock — Reentrant Lock

`RLock` stands for **Reentrant Lock**.

It allows the **same thread** to acquire the same lock multiple times.

```python
lock = threading.RLock()
```

Example:

```python
import threading


lock = threading.RLock()


def task(lock):

    lock.acquire()
    print("First lock acquired")

    lock.acquire()
    print("Second lock acquired")

    lock.release()
    lock.release()

    print("Lock released")


t1 = threading.Thread(target=task, args=(lock,))
t2 = threading.Thread(target=task, args=(lock,))

t1.start()
t2.start()

t1.join()
t2.join()
```

### Important

```text
Lock
    → Same thread cannot safely acquire it again
      while already holding it.

RLock
    → Same thread can acquire it multiple times.
```

The same thread must release an `RLock` the corresponding number of times.

---

# 15. Semaphore

A **Semaphore** controls how many threads can enter a protected section at the same time.

```python
semaphore = threading.Semaphore(2)
```

This means up to **2 threads** can acquire the semaphore simultaneously.

## Example

```python
import threading
import time


semaphore = threading.Semaphore(2)


def task(semaphore):

    semaphore.acquire()

    try:
        print(
            "Thread",
            threading.current_thread().name,
            "acquired semaphore"
        )

        time.sleep(2)

    finally:
        semaphore.release()

        print(
            "Thread",
            threading.current_thread().name,
            "released semaphore"
        )


threads = []

for _ in range(4):

    thread = threading.Thread(
        target=task,
        args=(semaphore,)
    )

    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()
```

### Concept

```text
Semaphore(2)

Thread 1 ──┐
           ├── Access
Thread 2 ──┘

Thread 3 ──┐
           └── Wait

Thread 4 ──┐
           └── Wait

After a thread releases:
        ↓
Another waiting thread can enter
```

---

# 16. Lock vs Semaphore

### Lock

```python
lock = threading.Lock()
```

Normally allows:

```text
One thread at a time
```

### Semaphore

```python
semaphore = threading.Semaphore(3)
```

Allows:

```text
Up to three threads at a time
```

---

# 17. Thread Communication

Threads sometimes need to communicate or coordinate with each other.

Common mechanisms include:

```text
Thread Communication
│
├── Event
├── Condition
├── Queue
└── Semaphore
```

Each mechanism has a different purpose.

---

# 18. Event

`Event` is used for simple signaling between threads.

```python
event = threading.Event()
```

### Important Methods

```python
event.set()
```

Sets the event.

```python
event.clear()
```

Clears the event.

```python
event.wait()
```

Waits until the event is set.

```python
event.is_set()
```

Checks whether the event is currently set.

---

# 19. Event Example

```python
import threading
import time


def task(event):

    print("Thread is waiting for the event.")

    event.wait()

    print("Thread received the signal and is processing.")


event = threading.Event()

thread = threading.Thread(
    target=task,
    args=(event,)
)

thread.start()

time.sleep(2)

event.set()

thread.join()
```

### Flow

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

# 20. Condition

A `Condition` is a synchronization primitive that allows threads to wait for a particular condition and notify other waiting threads when the condition changes.

```python
condition = threading.Condition()
```

Common methods:

```python
condition.acquire()
condition.wait()
condition.notify()
condition.notify_all()
condition.release()
```

### Basic Structure

Producer:

```python
with condition:

    # Update shared state

    condition.notify_all()
```

Consumer:

```python
with condition:

    condition.wait()

    # Continue working
```

A `Condition` is commonly used in producer-consumer style problems.

---

# 21. Producer / Consumer Communication

The basic idea is:

```text
Producer Thread
       │
       │ Produces Data
       ▼
     Queue
       │
       │ Consumes Data
       ▼
Consumer Thread
```

A `Condition` can be used when the consumer needs to wait until some condition becomes true.

---

# 22. Queue

`Queue` is useful for safely exchanging data between threads.

Python provides:

```python
from queue import Queue

queue = Queue()
```

Concept:

```text
Producer
   │
   ▼
 Queue
   │
   ▼
Consumer
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

# 23. Thread Exception Handling

Exceptions raised inside a thread should be handled appropriately within the thread's target function when you want to control the error.

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

---

# 24. Thread Information

Python provides several ways to get information about threads.

```python
import threading


current = threading.current_thread()

print(current)
print(current.name)
print(current.ident)
print(current.is_alive())
```

### Important

```python
threading.current_thread()
```

Returns the currently executing thread.

```python
current.name
```

Returns the thread's name.

```python
current.ident
```

Returns the thread identifier.

```python
current.is_alive()
```

Checks whether the thread is alive.

---

# 25. Daemon Thread

A **daemon thread** is a background thread that does not keep the Python program running by itself when all non-daemon threads have finished.

Example:

```python
thread = threading.Thread(
    target=traffic_message,
    args=(event,),
    daemon=True
)
```

Here:

```python
daemon=True
```

creates a daemon thread.

Daemon threads are useful for background tasks such as:

```text
Monitoring
Logging
Background polling
Periodic status checks
```

---

# 26. Traffic Light Example Using Event

```python
import threading
import time


event = threading.Event()


def light_switch(event):

    while True:

        # GREEN
        print("Green Light ON")
        event.set()

        time.sleep(5)

        # YELLOW
        print("Yellow Light ON")

        time.sleep(2)

        # RED
        print("Red Light ON")
        event.clear()

        time.sleep(5)


def traffic_message(event):

    while True:

        if event.is_set():
            print("You can cross the road")
        else:
            print("You cannot cross the road")

        time.sleep(1)


t1 = threading.Thread(
    target=light_switch,
    args=(event,)
)

t2 = threading.Thread(
    target=traffic_message,
    args=(event,),
    daemon=True
)

t1.start()
t2.start()

t1.join()
```

### Concept

```text
Green
  ↓
event.set()
  ↓
"You can cross the road"


Red
  ↓
event.clear()
  ↓
"You cannot cross the road"
```

---

# 27. Multithreading with a Class

You can create a custom thread by inheriting from `threading.Thread`.

```python
import threading
import time


class VideoUploader(threading.Thread):

    def __init__(self, video):
        super().__init__()
        self.video = video

    def run(self):

        print(f"Started uploading {self.video}")

        time.sleep(0.5)

        print(f"Video uploaded {self.video}")
```

Create and start the thread:

```python
thread = VideoUploader("video1.mp4")

thread.start()
thread.join()
```

---

# 28. Multiple Video Upload Threads

```python
import threading
import time


class VideoUploader(threading.Thread):

    def __init__(self, video):
        super().__init__()
        self.video = video

    def run(self):

        print(f"Started uploading {self.video}")

        time.sleep(0.5)

        print(f"Video uploaded {self.video}")


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


print("All videos uploaded successfully!")
```

### Flow

```text
Main Thread
    │
    ├── VideoUploader 1
    ├── VideoUploader 2
    └── VideoUploader 3
```

---

# 29. Important Threading Methods

| Method       | Purpose                          |
| ------------ | -------------------------------- |
| `start()`    | Starts a thread                  |
| `run()`      | Contains the thread's task       |
| `join()`     | Waits for a thread to finish     |
| `acquire()`  | Acquires a lock/semaphore        |
| `release()`  | Releases a lock/semaphore        |
| `wait()`     | Waits for a condition/event      |
| `set()`      | Sets an event                    |
| `clear()`    | Clears an event                  |
| `is_set()`   | Checks whether an event is set   |
| `is_alive()` | Checks whether a thread is alive |

---

# 30. Lock vs RLock vs Semaphore vs Event vs Condition vs Queue

| Tool        | Main Purpose                                                  |
| ----------- | ------------------------------------------------------------- |
| `Lock`      | Protect a critical section                                    |
| `RLock`     | Allow the same thread to acquire the same lock multiple times |
| `Semaphore` | Limit the number of concurrent threads                        |
| `Event`     | Send a simple signal between threads                          |
| `Condition` | Wait for and notify about a shared state                      |
| `Queue`     | Safely exchange data/tasks between threads                    |

---

# 31. Complete Concept Map

```text
Python Multithreading
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
├── Thread Communication
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
└── Background Thread
    └── daemon=True
```

---

# 32. Easy Way to Remember

### Race Condition

```text
Multiple Threads
       ↓
Shared Resource
       ↓
Unsafe Concurrent Access
       ↓
Race Condition
```

### Lock

```text
Lock
  ↓
One thread at a time
```

### Semaphore

```text
Semaphore(3)
  ↓
Up to 3 threads at a time
```

### RLock

```text
RLock
  ↓
Same thread can acquire
the same lock multiple times
```

### Event

```text
Event
  ↓
"Wait until I send a signal."
```

### Condition

```text
Condition
  ↓
"Wait until the required condition is true."
```

### Queue

```text
Queue
  ↓
Producer → Data → Consumer
```

---

# 33. Important Interview Questions

## Q1. What is Multithreading?

Multithreading is a programming technique in which multiple threads execute tasks concurrently within a process.

---

## Q2. What is a Race Condition?

A race condition occurs when multiple threads access or modify shared data concurrently and the result depends on the timing or order of execution.

---

## Q3. How can you prevent a Race Condition?

Synchronization mechanisms such as:

```python
threading.Lock()
```

can be used to protect shared resources.

---

## Q4. What is the difference between Lock and RLock?

```text
Lock
→ A normal mutual-exclusion lock.

RLock
→ A reentrant lock that can be acquired
  multiple times by the same thread.
```

---

## Q5. What is a Semaphore?

A Semaphore controls how many threads can access a resource or critical section concurrently.

Example:

```python
threading.Semaphore(3)
```

allows up to three threads to hold the semaphore simultaneously.

---

## Q6. What is an Event?

An Event is a signaling mechanism that allows one thread to notify other threads that something has happened.

---

## Q7. What is `join()`?

`join()` makes the calling thread wait until the specified thread terminates.

---

## Q8. What is a Daemon Thread?

A daemon thread is a background thread that does not keep the Python interpreter alive after all non-daemon threads have finished.

---

## Q9. What is a Critical Section?

A critical section is a part of code that accesses or modifies shared state and therefore may require synchronization.

---

## Q10. What is the difference between `start()` and `run()`?

```text
start()
→ Starts execution in a new thread.

run()
→ Contains the code executed by that thread.
```

Normally, you should call:

```python
thread.start()
```

rather than directly calling:

```python
thread.run()
```

because calling `run()` directly does not create a new thread.

---

# 34. Important Note About Python's GIL

In standard CPython, the **Global Interpreter Lock (GIL)** means that only one thread executes Python bytecode at a time within a process.

Therefore, Python threads are especially useful for **I/O-bound tasks**, such as:

```text
Network requests
File I/O
Database operations
Waiting for external services
```

For CPU-heavy Python code, threads generally do not provide the same parallel execution benefit as processes.

For CPU-bound work, alternatives such as:

```python
multiprocessing
```

or other parallelism approaches may be more appropriate.

---

# 35. Multithreading vs Multiprocessing

| Feature               | Multithreading         | Multiprocessing            |
| --------------------- | ---------------------- | -------------------------- |
| Unit                  | Thread                 | Process                    |
| Memory                | Shared within process  | Separate process memory    |
| Communication         | Easier                 | More overhead              |
| I/O-bound tasks       | Often useful           | Useful                     |
| CPU-bound Python code | Limited by CPython GIL | Can use multiple CPU cores |
| Creation overhead     | Lower                  | Higher                     |

### Simple Rule

```text
I/O-bound
    ↓
Threading can be useful

CPU-bound
    ↓
Multiprocessing may be more suitable
```

---

# 36. Final Summary

The most important concepts in Python Multithreading are:

```text
1. Thread
2. threading.Thread()
3. start()
4. run()
5. join()
6. Shared Resource
7. Race Condition
8. Critical Section
9. Lock
10. RLock
11. Semaphore
12. Event
13. Condition
14. Queue
15. Thread Exception Handling
16. Thread Information
17. Daemon Thread
18. GIL
19. Thread vs Process
```

### Core Relationship

```text
Multiple Threads
       ↓
Shared Resource
       ↓
Race Condition
       ↓
Synchronization
       ↓
Lock / RLock / Semaphore
```

### Thread Communication

```text
Event
  ↓
Simple Signaling

Condition
  ↓
Wait + Notify

Queue
  ↓
Safe Data/Task Exchange
```

### Final Mental Model

```text
                Python Multithreading
                        │
          ┌─────────────┴─────────────┐
          ↓                           ↓
     Thread Creation             Thread Control
          │                           │
   Thread() / Class             start() / join()
          │
          ↓
    Shared Resources
          │
          ↓
    Race Conditions
          │
          ↓
    Synchronization
     ┌────┼────┐
     ↓    ↓    ↓
   Lock RLock Semaphore
     
          ↓
   Thread Communication
      ┌────┼────┐
      ↓    ↓    ↓
    Event Condition Queue
```
"""