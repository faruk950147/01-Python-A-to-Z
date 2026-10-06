"""
# Python Processing & Multiprocessing — Easy English Notes

## 1. What is Processing?

**Processing** means doing some work on input/data to produce useful output.

In Python, we can process tasks in different ways:

* Single Processing
* Multithreading
* Multiprocessing
* Asynchronous Programming

---

# 2. What is Multiprocessing?

**Multiprocessing** means using multiple **processes** to perform tasks.

Each process usually has its **own memory space**.

Multiprocessing is very useful for **CPU-heavy tasks** because different processes can run on different CPU cores.

### Examples

* Image Processing
* Video Processing
* Large Mathematical Calculations
* Scientific Calculations
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

A **process** is a running instance of a program.

When we run a Python program, the operating system creates a process for it.

One program can create multiple child processes.

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

The process where the Python program starts is called the **Main Process**.

```python
import multiprocessing

process = multiprocessing.current_process()

print(process)
```

Possible output:

```text
<_MainProcess name='MainProcess' parent=None started>
```

---

# 5. `multiprocessing.current_process()`

This function returns the process that is currently running the code.

```python
multiprocessing.current_process()
```

### Example

```python
import multiprocessing

process = multiprocessing.current_process()

print(process)
```

---

# 6. Process Name

To get the name of a process:

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

Child processes may have names like:

```text
Process-1
Process-2
Process-3
```

---

# 7. Process ID — PID

Every running process has a unique **Process ID**, called **PID**.

Python can get the PID using:

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

The `ident` attribute gives the identifier of a `multiprocessing.Process` object.

```python
import multiprocessing

process = multiprocessing.current_process()

print(process.ident)
```

### Important

`ident` and OS-level PID are related but are not exactly the same concept.

For the OS process ID, use:

```python
os.getpid()
```

You can also get a process's PID using:

```python
process.pid
```

---

# 9. `is_alive()`

The `is_alive()` method checks whether a process is currently running.

```python
process.is_alive()
```

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

Possible output:

```text
True
False
```

---

# 10. Child Process

A process created by another process is called a **Child Process**.

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

To create a new process, use:

```python
multiprocessing.Process()
```

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

The most important parameters are:

```text
target
args
kwargs
name
daemon
```

---

# 12. `target`

`target` tells the child process **which function to run**.

### Example

```python
def task():
    print("Hello from child process")


process = multiprocessing.Process(target=task)
```

Here:

```python
target=task
```

means the child process will run the `task()` function.

---

# 13. `target=task` vs `target=task()`

This is very important.

### Correct

```python
process = multiprocessing.Process(target=task)
```

Here, we pass the function itself.

### Incorrect

```python
process = multiprocessing.Process(target=task())
```

Here, `task()` runs immediately.

Its return value is then given to `target`.

So normally use:

```python
target=task
```

Think:

```text
target=task
      ↓
"Run this function later"
```

---

# 14. `start()`

The `start()` method starts a new process.

```python
process.start()
```

### Example

```python
import multiprocessing


def task():
    print("Child process is running")


if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
```

After `start()` is called, the child process starts running the target function.

---

# 15. `join()`

The `join()` method makes the calling process **wait until another process finishes**.

```python
process.join()
```

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

Here:

```python
process.join()
```

makes the main process wait for the child process.

---

# 16. `start()` vs `join()`

### `start()`

```python
process.start()
```

Purpose:

```text
Starts the process
```

### `join()`

```python
process.join()
```

Purpose:

```text
Waits for the process to finish
```

Easy way to remember:

```text
start() = Start the process

join() = Wait for the process
```

---

# 17. Windows and Main Guard

When using multiprocessing, especially on **Windows**, use:

```python
if __name__ == "__main__":
```

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

# 18. Why is the Main Guard Important?

On systems using the `spawn` start method, a child process starts a fresh Python interpreter.

Without the main guard, the child may run the process-creation code again.

This can create unwanted new processes repeatedly.

Therefore, use:

```python
if __name__ == "__main__":
```

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

### Program Flow

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

When one process creates another process:

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

### Important Functions

```python
os.getpid()
```

Returns the PID of the current process.

```python
os.getppid()
```

Returns the PID of the parent process.

---

# 21. Child Process Name

A child process may have a default name like:

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

# 22. Custom Process Name

We can give a process our own name.

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

We can create multiple child processes.

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

The output order is **not fixed**.

For example:

```text
Task: 2
Task: 1
Task: 3
```

or:

```text
Task: 1
Task: 3
Task: 2
```

The operating system decides which process gets CPU time.

---

# 24. `args`

Use `args` to pass **positional arguments** to a child process.

```python
args=
```

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

For one argument, we need a comma:

```python
args=("Faruk",)
```

Because:

```python
("Faruk")
```

is a string.

But:

```python
("Faruk",)
```

is a tuple.

---

# 25. Multiple Arguments

We can pass multiple positional arguments.

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

Use `kwargs` to pass **keyword arguments**.

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

Use:

```python
process.terminate()
```

to request termination of a running process.

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

`terminate()` does not give the process a normal cleanup opportunity.

So be careful if the process is using:

* Files
* Locks
* Database connections
* Other resources

---

# 28. `kill()`

Use:

```python
process.kill()
```

to forcefully stop a process.

### Example

```python
process.kill()
```

### `terminate()` vs `kill()`

```text
terminate() → Stops the process

kill() → Forcefully stops the process
```

---

# 29. `exitcode`

After a process finishes, we can check its exit status using:

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

Normally:

```text
0
```

means the process finished successfully.

A non-zero exit code usually means that the process ended because of an error or another abnormal condition.

---

# 30. Process Lifecycle

The basic lifecycle is:

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
       join() returns
```

Easy version:

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

# 31. `start()` Can Normally Be Used Only Once

A `Process` object can normally be started only once.

### Incorrect

```python
process.start()
process.start()
```

You cannot restart the same `Process` object.

If you need another process, create a new `Process` object.

---

# 32. `join()` Does Not Stop a Process

This is very important.

```python
process.join()
```

does **not** stop the process.

It only makes the calling process wait until the target process finishes.

Remember:

```text
start() → Starts the process

join() → Waits for the process to finish
```

---

# 33. CPU-Bound Task

A **CPU-bound task** spends most of its time doing calculations.

### Examples

* Large mathematical calculations
* Image processing
* Video encoding
* Scientific calculations
* Complex algorithms
* CPU-heavy data processing

Multiprocessing is often a good choice for these tasks.

---

# 34. I/O-Bound Task

An **I/O-bound task** spends much of its time waiting for input/output operations.

### Examples

* Reading/writing files
* Network requests
* Database queries
* API requests
* Waiting for external services

For many I/O-bound tasks:

```text
Threading
Asyncio
```

may be better choices.

But multiprocessing can also be used for I/O-bound tasks in some situations.

---

# 35. Why Use Multiprocessing?

Multiprocessing is especially useful for **CPU-bound work**.

Examples:

```text
Image Processing
Video Processing
Large Mathematical Calculations
Scientific Computation
Machine Learning Computation
CPU-heavy Algorithms
Data Processing
```

---

# 36. Multiprocessing and Python GIL

In **CPython**, the **GIL (Global Interpreter Lock)** prevents multiple threads in the same process from executing Python bytecode at the same time in the usual way.

Multiprocessing uses separate processes.

Each process has its own Python interpreter and normally its own memory space.

Therefore, CPU-bound programs can use multiple CPU cores through multiple processes.

### Easy Idea

```text
Multithreading
      ↓
Same Process
      ↓
Shared Memory
      ↓
GIL matters in CPython
```

```text
Multiprocessing
      ↓
Multiple Processes
      ↓
Separate Memory
      ↓
Can use multiple CPU cores
```

---

# 37. Multiprocessing vs Multithreading

| Feature           | Multiprocessing     | Multithreading            |
| ----------------- | ------------------- | ------------------------- |
| Unit              | Process             | Thread                    |
| Memory            | Separate            | Shared within a process   |
| CPU-bound         | Often a good choice | GIL limitation in CPython |
| I/O-bound         | Possible            | Often suitable            |
| Communication     | More complex        | Easier                    |
| Memory usage      | Higher              | Lower                     |
| Isolation         | Higher              | Lower                     |
| Creation overhead | Higher              | Lower                     |

### General Rule

```text
CPU-bound
    ↓
Multiprocessing

I/O-bound
    ↓
Threading / Asyncio
```

This is a general rule, not a strict rule.

---

# 38. Separate Memory in Processes

Processes normally have separate memory spaces.

Example:

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

The child process gets its own process-specific view/copy of ordinary Python data.

If the child changes a normal Python variable, that change does not directly change the parent's variable.

---

# 39. Sharing Data Between Processes

Because processes normally have separate memory spaces, ordinary Python variables are not directly shared.

The `multiprocessing` module provides different ways to communicate and share data:

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

A `Queue` can be used to send messages/data between processes.

```python
multiprocessing.Queue()
```

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

### Easy Idea

```text
Process A
    ↓
Queue
    ↓
Process B
```

---

# 41. `multiprocessing.Pipe`

A `Pipe` provides communication between processes.

```python
multiprocessing.Pipe()
```

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

A `Pool` is useful when we have many similar tasks.

It creates a group of worker processes and distributes tasks among them.

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

Use:

```python
pool.map(function, iterable)
```

to apply the same function to every item.

Example:

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

The results are returned as a list.

---

# 44. Why Use a Pool?

Without a pool, we may need to manually create many processes:

```python
p1 = Process(...)
p2 = Process(...)
p3 = Process(...)
p4 = Process(...)
```

A `Pool` makes this easier.

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

# 45. Advantages of Multiprocessing

### 1. Good for CPU-heavy Work

It can run CPU-intensive tasks using multiple processes.

### 2. Multiple CPU Cores

Different processes can run on different CPU cores.

### 3. Process Isolation

Each process normally has separate memory.

### 4. Fault Isolation

If a child process crashes, the parent process does not automatically have to crash.

### 5. Parallel Execution

Independent tasks can run at the same time.

---

# 46. Disadvantages of Multiprocessing

### 1. Higher Memory Usage

Each process normally has its own memory space.

### 2. More Process Creation Overhead

Creating a process is usually more expensive than creating a thread.

### 3. Communication is More Complex

Processes need IPC mechanisms such as:

```text
Queue
Pipe
Manager
Shared Memory
```

### 4. Serialization Overhead

Data sent between processes may need to be serialized/pickled.

This can take extra time.

### 5. Debugging is More Difficult

Multiple processes make debugging more complex.

---

# 47. When Should You Use Multiprocessing?

Consider multiprocessing when:

```text
✓ The task is CPU-intensive
✓ Tasks are mostly independent
✓ Multiple CPU cores are available
✓ Parallel execution can help
✓ The calculation is large enough to justify the overhead
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

# 48. When Should You Avoid Multiprocessing?

Multiprocessing is not always faster.

If the task is very small, process creation and communication overhead may be larger than the actual work.

Examples:

```text
Very Small Calculations
Simple Print Operations
Tiny Tasks
Tasks with frequent shared-state communication
```

For such tasks, multiprocessing may make the program slower.

---

# 49. Important Process Methods

| Method              | Purpose                                               |
| ------------------- | ----------------------------------------------------- |
| `start()`           | Starts the process                                    |
| `join()`            | Waits for the process to finish                       |
| `is_alive()`        | Checks whether the process is running                 |
| `terminate()`       | Terminates the process                                |
| `kill()`            | Forcefully terminates the process                     |
| `close()`           | Releases resources associated with the Process object |
| `run()`             | Runs the target callable                              |
| `current_process()` | Returns the current process object                    |

---

# 50. Important Process Attributes

| Attribute  | Purpose                                       |
| ---------- | --------------------------------------------- |
| `name`     | Process name                                  |
| `pid`      | OS process ID                                 |
| `ident`    | Process identifier                            |
| `exitcode` | Process exit status                           |
| `daemon`   | Shows whether the process is a daemon process |

To get the PID:

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

The exact order is **not guaranteed**.

---

# 52. Multiprocessing Mental Model

The easiest way to understand multiprocessing:

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

Each process normally has:

```text
Its own execution
       +
Its own memory space
       +
Its own process ID
```

---

# 53. Short Revision

### What is a Process?

A process is a running instance of a program.

### What is Multiprocessing?

Multiprocessing means using multiple processes to perform tasks.

### What is `Process()`?

It creates a new process.

### What is `start()`?

It starts the process.

### What is `join()`?

It waits for the process to finish.

### What is `target`?

The function/callable that the child process executes.

### What is `args`?

It passes positional arguments.

### What is `kwargs`?

It passes keyword arguments.

### What is `terminate()`?

It terminates a process.

### What is `kill()`?

It forcefully terminates a process.

### What is `is_alive()`?

It checks whether a process is currently running.

### What is `exitcode`?

It tells how the process ended.

### What is `pid`?

The OS-level Process ID.

### What is `current_process()`?

It returns the current process object.

### What is `Queue`?

It allows processes to exchange data/messages.

### What is `Pipe`?

It provides communication between processes.

### What is `Pool`?

It distributes many tasks among worker processes.

---

# 54. Most Important Exam & Interview Topics

Focus on these topics:

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

### Multiprocessing

```text
Multiprocessing
       ↓
Multiple Processes
       ↓
Separate Memory
       ↓
Can use Multiple CPU Cores
       ↓
Good for CPU-bound Tasks
```

### Process Lifecycle

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

### CPU vs I/O

```text
CPU-bound
    ↓
Multiprocessing
```

```text
I/O-bound
    ↓
Threading / Asyncio
```

## One-Line Memory Rule

> **Multiprocessing = multiple processes working independently, usually with separate memory, and it is especially useful for CPU-bound tasks.**

"""