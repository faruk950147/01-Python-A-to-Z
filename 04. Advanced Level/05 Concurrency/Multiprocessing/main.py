"""
# Python Processing & Multiprocessing — Full Notes

## 1. What is Processing?

**Processing** is the process of applying different operations to input/data in order to transform, analyze, or convert it into useful output.

In Python, there are several ways to perform processing:

* Single Processing
* Multithreading
* Multiprocessing
* Asynchronous Programming

---

# 2. What is Multiprocessing?

**Multiprocessing** is a technique where the tasks of a Python program are executed using multiple **independent processes**.

Each process generally has its **own memory space**, and multiprocessing can allow tasks to run in parallel on multiple CPU cores.

Multiprocessing is especially useful for **CPU-bound tasks**.

### Examples

* Image Processing
* Video Processing
* Large Mathematical Calculations
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

A **Process** is a currently running instance of a program.

When we run a Python program, the operating system runs it as a process.

Multiple processes can be created from a single program.

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

The process from which the execution of a Python program starts is generally called the **Main Process**.

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

To get the `Process` object representing the process that is currently executing the code:

```python
multiprocessing.current_process()
```

is used.

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

is used.

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

The default name of child processes may look like:

```text
Process-1
Process-2
Process-3
```

---

# 7. Process ID — PID

Every running process has a **Process ID (PID)**.

In Python, the PID can be obtained using:

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

The `ident` attribute of a `multiprocessing.Process` object provides the process identifier.

```python
import multiprocessing


process = multiprocessing.current_process()

print(process.ident)
```

### Important

`ident` and the OS-level PID are not exactly the same concept.

To get the OS-level process ID:

```python
os.getpid()
```

can be used.

---

# 9. `is_alive()`

To check whether a process is currently running:

```python
process.is_alive()
```

is used.

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

A process created by a main/parent process is called a **Child Process**.

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

To create a new process:

```python
multiprocessing.Process()
```

is used.

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

The most commonly used parameters are:

```text
target
args
kwargs
name
daemon
```

---

# 12. `target`

`target` is the **callable/function** that will be executed in the child process.

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

means that the child process will execute the `task` function.

---

# 13. `target=task` vs `target=task()`

This is very important.

### Correct

```python
process = multiprocessing.Process(target=task)
```

Here, a reference to the `task` function is passed.

### Incorrect

```python
process = multiprocessing.Process(target=task())
```

Here, `task()` is executed immediately, and its return value is passed as the `target`.

Therefore, normally use:

```python
target=task
```

---

# 14. `start()`

To start a process:

```python
process.start()
```

is used.

### Example

```python
import multiprocessing


def task():
    print("Child process is running")


if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
```

After calling `start()`, a new process is created and begins execution of the target callable.

---

# 15. `join()`

To make the calling process wait until a child process finishes:

```python
process.join()
```

is used.

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

causes the main process to wait until the child process finishes.

---

# 16. `start()` vs `join()`

### `start()`

```python
process.start()
```

Purpose:

```text
Starts the new process
```

### `join()`

```python
process.join()
```

Purpose:

```text
Waits for the process to finish
```

Simply:

```text
start() = Start the process

join() = Wait for the process to finish
```

---

# 17. Windows and `if __name__ == "__main__":`

When using multiprocessing, especially on Windows, using the **main guard** is extremely important.

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

# 18. Why is the Main Guard Necessary?

Especially with the Windows `spawn` start method, a child process starts with a fresh Python interpreter.

If process-creation code exists at the top level of the module, the child process may try to execute that code again.

This can cause unwanted recursive process creation.

Therefore, it is recommended to use:

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

Here:

```python
os.getpid()
```

returns the PID of the current process.

And:

```python
os.getppid()
```

returns the PID of the parent process.

---

# 21. Child Process Name

The default name of a child process may look like:

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

You can give a process a custom name.

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

Multiple child processes can be created.

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

The output order is not fixed:

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

because process scheduling depends on the operating system and runtime conditions.

---

# 24. `args`

To pass positional arguments to the target function of a child process:

```python
args=
```

is used.

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

Even when passing one argument, a comma is required to create a tuple:

```python
args=("Faruk",)
```

Because:

```python
("Faruk")
```

is a string, not a tuple.

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

To pass keyword arguments:

```python
kwargs=
```

can be used.

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

To manually terminate a running process:

```python
process.terminate()
```

can be used.

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

`terminate()` may not give the process an opportunity to perform graceful cleanup.

Therefore, be careful when the process is using files, locks, resources, etc.

---

# 28. `kill()`

To forcefully terminate a process:

```python
process.kill()
```

can be used.

### Example

```python
process.kill()
```

### `terminate()` vs `kill()`

```text
terminate() → Terminates the process

kill() → Forcefully terminates the process
```

---

# 29. `exitcode`

After a process finishes, its exit code can be obtained using:

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

When the process finishes successfully, the exit code is typically:

```text
0
```

If the process terminates because of an error, a non-zero exit code may be returned.

---

# 30. Process Lifecycle

The general lifecycle of a process is:

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

Simply:

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

# 31. `start()` Can Normally Be Used Only Once

The `start()` method can normally be called only once on a particular `Process` object.

### Incorrect

```python
process.start()
process.start()
```

The same process object cannot be started again.

To run another process, create a new `Process` object.

---

# 32. `join()` Does Not Stop a Process

This is very important.

```python
process.join()
```

does not terminate the process.

`join()` only makes the calling process wait until the target process finishes.

```text
start() → Starts the process

join() → Waits until the process finishes
```

---

# 33. CPU-Bound Task

A task whose execution time mainly depends on CPU computation is called a **CPU-bound task**.

### Examples

```text
Large Mathematical Calculations
Image Processing
Video Encoding
Scientific Calculations
Complex Algorithms
CPU-heavy Data Processing
```

Multiprocessing can be a good option for CPU-bound work.

---

# 34. I/O-Bound Task

A task where a large portion of execution time is spent waiting for input/output operations is called an **I/O-bound task**.

### Examples

```text
File Read/Write
Network Request
Database Query
API Request
Waiting for External Services
```

For I/O-bound tasks, in many cases:

```text
Threading
Asyncio
```

may be more suitable.

However, I/O-bound tasks can also be implemented using multiprocessing.

---

# 35. Why Use Multiprocessing?

Multiprocessing is especially useful for **CPU-bound workloads**.

### Examples

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

In **CPython**, the **GIL (Global Interpreter Lock)** limits multiple threads within the same process from executing Python bytecode simultaneously.

With multiprocessing, each process has its own Python interpreter and generally its own memory space.

Therefore, for CPU-bound workloads, multiple processes can use multiple CPU cores.

Simply:

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

| Feature           | Multiprocessing    | Multithreading            |
| ----------------- | ------------------ | ------------------------- |
| Unit              | Process            | Thread                    |
| Memory            | Separate           | Shared                    |
| CPU-bound         | Good choice        | GIL limitation in CPython |
| I/O-bound         | Possible           | Often suitable            |
| Communication     | Relatively complex | Relatively easy           |
| Memory usage      | Higher             | Lower                     |
| Isolation         | Higher             | Lower                     |
| Creation overhead | Higher             | Lower                     |

### General Rule

```text
CPU-bound
    ↓
Multiprocessing

I/O-bound
    ↓
Threading / Asyncio
```

This is a general guideline, not an absolute rule.

---

# 38. Separate Memory in Processes

An important feature of multiprocessing is that processes generally have separate memory spaces.

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

The child process may have its own process-specific copy of the variable.

A change to an ordinary Python variable in the child process does not directly change the corresponding variable in the parent process.

---

# 39. Sharing Data Between Processes

Because processes have separate memory spaces, ordinary Python variables cannot be directly shared between processes.

Python's `multiprocessing` module provides several IPC/data-sharing mechanisms:

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

To send data/messages from one process to another:

```python
multiprocessing.Queue()
```

can be used.

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

For communication between two processes:

```python
multiprocessing.Pipe()
```

can be used.

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

To distribute many similar tasks among worker processes:

```python
multiprocessing.Pool
```

can be used.

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

To execute the same function on every item of an iterable:

```python
pool.map(function, iterable)
```

is used.

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

A list of results is returned.

---

# 44. Why Use a Pool?

If there are many similar independent tasks, instead of manually writing:

```python
p1 = Process(...)
p2 = Process(...)
p3 = Process(...)
p4 = Process(...)
```

you can use a `Pool`.

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

### 1. CPU-Bound Performance

It helps parallelize CPU-intensive workloads.

### 2. Multiple CPU Cores

Multiple processes can use multiple CPU cores.

### 3. Process Isolation

A process generally has a separate memory space from other processes.

### 4. Fault Isolation

If a child process crashes, the parent process does not necessarily crash.

### 5. Parallel Execution

Independent tasks can execute concurrently.

---

# 46. Disadvantages of Multiprocessing

### 1. Higher Memory Usage

Each process generally has its own memory space.

### 2. Process Creation Overhead

Creating processes is generally more expensive than creating threads.

### 3. Communication Complexity

IPC mechanisms may be required to exchange data between processes.

### 4. Serialization Overhead

When data is sent between processes, object serialization/pickling may introduce overhead.

### 5. Debugging Complexity

Debugging can be more difficult because multiple processes may execute simultaneously.

---

# 47. When Should You Use Multiprocessing?

Consider using multiprocessing when:

```text
✓ The task is CPU-intensive
✓ Tasks are independent
✓ Multiple CPU cores are available
✓ Parallel execution is beneficial
✓ Large computations need to be performed
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

If the task is very small and the overhead of creating processes is greater than the computation itself, multiprocessing may make the program slower instead of faster.

Examples:

```text
Very Small Calculations
Simple Print Operations
Tiny Tasks
Tasks Requiring Frequent Shared-State Access
```

---

# 49. Important Process Methods

| Method              | Purpose                                               |
| ------------------- | ----------------------------------------------------- |
| `start()`           | Starts the process                                    |
| `join()`            | Waits for the process to finish                       |
| `is_alive()`        | Checks whether the process is alive                   |
| `terminate()`       | Terminates the process                                |
| `kill()`            | Forcefully terminates the process                     |
| `close()`           | Releases resources associated with the process object |
| `run()`             | Runs the target callable                              |
| `current_process()` | Returns the current process object                    |

---

# 50. Important Process Attributes

| Attribute    | Purpose                                  |
| ------------ | ---------------------------------------- |
| `name`       | Process name                             |
| `pid`        | OS Process ID                            |
| `ident`      | Process identifier                       |
| `exitcode`   | Process exit status                      |
| `daemon`     | Indicates whether it is a daemon process |
| `is_alive()` | Checks whether the process is running    |

### PID

The PID can also be obtained from a `Process` object:

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

The exact output order is not guaranteed.

---

# 52. Multiprocessing Mental Model

The simplest mental model is:

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

Each process has:

```text
Its own execution
       +
Its own memory space
       +
Its own process ID
```

---

# 53. Multiprocessing Short Revision

### What is a Process?

A running instance of a program.

### What is Multiprocessing?

A technique of executing tasks using multiple processes.

### What is `Process()`?

It creates a new process.

### What is `start()`?

It starts the process.

### What is `join()`?

It waits for the process to finish.

### What is `target`?

The callable executed by the child process.

### What is `args`?

It passes positional arguments.

### What is `kwargs`?

It passes keyword arguments.

### What is `terminate()`?

It terminates a process.

### What is `kill()`?

It forcefully terminates a process.

### What is `is_alive()`?

It checks whether a process is currently alive.

### What is `exitcode`?

The process's exit status code.

### What is `pid`?

The OS-level Process ID.

### What is `current_process()`?

It returns the current process object.

### What is `Queue`?

It helps exchange data/messages between processes.

### What is `Pipe`?

It provides communication between processes.

### What is `Pool`?

It distributes multiple tasks among worker processes.

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
Best suited for CPU-bound Tasks
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