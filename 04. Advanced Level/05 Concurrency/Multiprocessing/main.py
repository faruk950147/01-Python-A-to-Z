"""
# Python Processing & Multiprocessing — Complete Notes (Easy English)

## 1. What Is Processing?

**Processing** means performing operations on data to produce a result.

In Python, tasks can be performed using different execution models:

- **Sequential Processing:** Tasks execute one after another.
- **Multithreading:** Multiple threads make progress concurrently within a process.
- **Multiprocessing:** Multiple processes perform tasks independently.
- **Asynchronous Programming:** Tasks can suspend while waiting for operations and allow other tasks to progress.

The best approach depends on the type of task and the application's requirements.

---

## 2. What Is Multiprocessing?

**Multiprocessing** means using multiple processes to perform tasks.

A process is an independent running instance of a program. Each process normally has its own memory space and Python interpreter.

Multiprocessing is particularly useful for **CPU-bound tasks** because multiple processes can execute on different CPU cores simultaneously, when the system and workload permit it.

### Examples

- Image processing
- Video processing
- Large mathematical calculations
- Scientific computations
- Data processing
- Machine learning computations
- CPU-intensive algorithms

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

### Explanation

1. `multiprocessing.Process()` creates a process object.
2. `target=task` specifies the function to execute.
3. `start()` starts the child process.
4. `join()` waits for the child process to finish.
5. The main process continues after `join()` returns.

The `if __name__ == "__main__":` guard is important for portable multiprocessing code, especially on systems using the `spawn` start method.

---

## 3. What Is a Process?

A **process** is a running instance of a program.

When we run a Python program, the operating system creates a process to execute it.

A process can create additional processes called child processes.

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

Each process normally has its own memory space, process ID, and execution state.

Processes can communicate through mechanisms such as queues, pipes, shared memory, and other inter-process communication tools.

---

## 4. Main Process

The **main process** is the process in which the program initially starts.

We can inspect the current process using `multiprocessing.current_process()`.

```python
import multiprocessing

process = multiprocessing.current_process()

print(process)
```

Possible output:

```text
<_MainProcess name='MainProcess' parent=None started>
```

The exact representation may differ between Python versions and environments.

---

## 5. `multiprocessing.current_process()`

The `current_process()` function returns the process object representing the process that is currently executing the code.

### Example

```python
import multiprocessing


def task():
    process = multiprocessing.current_process()
    print("Current Process:", process.name)


if __name__ == "__main__":
    print("Main Process:", multiprocessing.current_process().name)

    process = multiprocessing.Process(target=task)
    process.start()
    process.join()
```

Possible output:

```text
Main Process: MainProcess
Current Process: Process-1
```

The child process name is automatically assigned unless you specify a custom name.

---

## 6. Process Name

Every `multiprocessing.Process` object has a `name` attribute.

### Example

```python
import multiprocessing


if __name__ == "__main__":
    process = multiprocessing.current_process()

    print("Process Name:", process.name)
```

Output:

```text
Process Name: MainProcess
```

Child processes commonly receive names such as:

```text
Process-1
Process-2
Process-3
```

You can also assign your own process name.

---

## 7. Process ID (PID)

Every running operating-system process has a **Process ID**, or PID.

Python provides `os.getpid()` to get the PID of the current process.

### Example

```python
import multiprocessing
import os


def task():
    print("Child PID:", os.getpid())


if __name__ == "__main__":
    print("Main PID:", os.getpid())

    process = multiprocessing.Process(target=task)
    process.start()
    process.join()
```

You can also obtain a started process's PID using:

```python
process.pid
```

A process's PID identifies it at the operating-system level while that process exists. PIDs may be reused after processes exit.

---

## 8. Process `ident` vs. PID

A common mistake is assuming that every `multiprocessing.Process` object has an `ident` attribute.

The standard `multiprocessing.Process` API provides `pid`, not the `ident` attribute used by `threading.Thread`.

To get the current process's operating-system ID, use:

```python
import os

print(os.getpid())
```

To get a child process's PID, use:

```python
process.pid
```

**Remember:**

- `os.getpid()` returns the current process's OS PID.
- `process.pid` returns the PID associated with a process object, once assigned.
- `threading.Thread.ident` is a thread identifier, not a multiprocessing process identifier.

---

## 9. `is_alive()`

The `is_alive()` method checks whether a process has started and has not yet finished.

### Example

```python
import multiprocessing
import time


def task():
    time.sleep(3)


if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()

    print("Before join:", process.is_alive())

    process.join()

    print("After join:", process.is_alive())
```

Typical output:

```text
Before join: True
After join: False
```

The first result is expected because the task sleeps for three seconds, although exact timing can vary.

`is_alive()` returns `False` before a process starts and after it finishes.

---

## 10. Child Process

A **child process** is a process created by another process.

The process that creates it is called the parent process.

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

The parent can manage the child using the process object.

---

## 11. `multiprocessing.Process()`

Use `multiprocessing.Process()` to create a process object.

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
    kwargs=None,
    daemon=None
)
```

Important parameters:

- `target`: The callable to execute.
- `args`: Positional arguments for the target.
- `kwargs`: Keyword arguments for the target.
- `name`: A custom process name.
- `daemon`: Specifies whether the process is a daemon process.

`group` is reserved for future use and should normally remain `None`.

The process is not started until you call `start()`.

---

## 12. `target`

The `target` parameter specifies the function or callable that the child process should execute.

### Example

```python
import multiprocessing


def task():
    print("Hello from child process")


if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()
```

Here:

```python
target=task
```

passes the function itself as the target.

---

## 13. `target=task` vs. `target=task()`

This is an important concept.

### Correct

```python
process = multiprocessing.Process(target=task)
```

The function is passed as the target to execute later.

### Incorrect for this purpose

```python
process = multiprocessing.Process(target=task())
```

Here, `task()` executes immediately in the current process while the `Process` object is being created.

Its return value is passed to `target`, which is usually not what we want.

Remember:

```text
target=task
      |
      v
Pass the function itself
      |
      v
Execute it in the child process
```

---

## 14. `start()`

The `start()` method starts a new process.

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

Calling `start()` launches the process according to the selected multiprocessing start method.

The child process executes the target callable through its `run()` method.

A `Process` object can normally be started only once.

---

## 15. `join()`

The `join()` method makes the calling process wait for another process to finish.

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

Output:

```text
Child finished
Main finished
```

Here, the main process waits for the child process.

**Important:** `join()` does not stop the child process. It waits for the process to finish.

You can also use a timeout:

```python
process.join(timeout=2)
```

This waits for at most two seconds. The child may still be running after the timeout.

---

## 16. `start()` vs. `join()`

### `start()`

```python
process.start()
```

Purpose: Starts the process.

### `join()`

```python
process.join()
```

Purpose: Waits for the process to finish.

Easy way to remember:

```text
start() = Start the process

join() = Wait for the process
```

The methods perform different operations and are commonly used together.

---

## 17. Windows and the Main Guard

When writing multiprocessing programs, use:

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

This structure is particularly important on Windows, where `spawn` is the default start method.

It is also good practice for portable multiprocessing programs on other platforms.

---

## 18. Why Is the Main Guard Important?

With the `spawn` start method, a child process starts a fresh Python interpreter and imports the main module.

Without the main guard, top-level process-creation code may execute again when the module is imported by the child.

This can cause recursive process creation or a multiprocessing bootstrap error.

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

For reusable multiprocessing code, keep worker functions at module scope when possible. This helps the `spawn` method locate and import them.

---

## 19. Complete Basic Multiprocessing Program

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

### Program Flow

```text
Program Starts
      |
      v
Main Process
      |
      v
Create Process Object
      |
      v
start()
      |
      v
Child Executes task()
      |
      v
Child Finishes
      |
      v
join() Returns
      |
      v
Main Process Continues
```

---

## 20. Parent and Child Process IDs

Use `os.getpid()` to obtain the current process's PID and `os.getppid()` to obtain its parent process's PID.

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

On typical systems, the child's reported parent PID matches the main process's PID.

Operating-system behavior may differ if the parent exits or the child becomes reparented.

---

## 21. Child Process Name

A child process usually receives an automatically generated name.

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

Possible output:

```text
Child Name: Process-1
```

The automatically assigned name may differ depending on how many processes have been created.

---

## 22. Custom Process Name

You can assign a meaningful name to a process.

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

Custom names are useful for debugging and identifying workers in logs.

---

## 23. Multiple Child Processes

You can create several child processes to perform independent tasks.

### Example

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

The output order is not guaranteed.

For example:

```text
Task: 2
Task: 1
Task: 3
```

Or:

```text
Task: 1
Task: 3
Task: 2
```

The operating system and process scheduling determine when each process runs.

---

## 24. `args`

Use `args` to pass positional arguments to the target function.

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

For one positional argument, use a one-element tuple:

```python
args=("Faruk",)
```

Compare:

```python
("Faruk")   # A string
("Faruk",)  # A tuple
```

---

## 25. Passing Multiple Arguments

You can pass multiple positional arguments using a tuple.

### Example

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

Output:

```text
Name: Faruk
Age: 25
```

---

## 26. `kwargs`

Use `kwargs` to pass keyword arguments.

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

Output:

```text
Name: Faruk
Age: 25
```

With the `spawn` start method, the target and its arguments generally need to be picklable. Top-level functions and simple data types are usually good choices.

---

## 27. `terminate()`

The `terminate()` method requests immediate termination of a child process using the operating system's termination mechanism.

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

    if process.is_alive():
        process.terminate()

    process.join()

    print("Process terminated")
```

### Important

`terminate()` does not provide a normal cleanup opportunity to the child process.

If the child is using files, locks, queues, database connections, or other resources, forced termination may leave resources or shared state in an inconsistent condition.

When possible, use a cooperative shutdown mechanism, such as an event or a message sent through a queue.

---

## 28. `kill()`

The `kill()` method forcefully terminates a process using a stronger operating-system mechanism where available.

### Example

```python
if process.is_alive():
    process.kill()

process.join()
```

Use `kill()` only when necessary.

### `terminate()` vs. `kill()`

- `terminate()`: Requests termination using the platform's termination mechanism.
- `kill()`: Uses a forceful kill mechanism where supported.

The exact behavior depends on the operating system. Neither method should be treated as a safe cleanup mechanism.

---

## 29. `exitcode`

The `exitcode` attribute reports the process's exit status after it terminates.

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

Typical output:

```text
Child process
Exit Code: 0
```

Common interpretations:

- `0`: The process finished successfully.
- A positive nonzero value: Often indicates an error or explicit nonzero exit status.
- A negative value on POSIX systems: Commonly indicates termination by a signal.
- `None`: The process has not started or has not yet terminated.

An exit code of `0` does not necessarily prove that every intended business operation succeeded. Applications may need additional result verification.

---

## 30. Process Lifecycle

A simplified process lifecycle looks like this:

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
   Process Terminates
          |
          v
       join() Returns
```

Important distinction:

- Creating a `Process` object does not start a new process.
- `start()` starts it.
- `join()` waits for its termination.
- `exitcode` can be inspected after it terminates.

---

## 31. A Process Object Can Normally Be Started Only Once

You cannot restart the same `Process` object after it has been started.

### Incorrect

```python
process.start()
process.start()
```

This raises an error.

### Correct

Create a new process object when you need another execution.

```python
import multiprocessing


def task(number):
    print("Task:", number)


if __name__ == "__main__":
    for i in range(2):
        process = multiprocessing.Process(
            target=task,
            args=(i,)
        )

        process.start()
        process.join()
```

For many repeated tasks, a process pool is usually more convenient.

---

## 32. `join()` Does Not Stop a Process

This is a common interview question.

```python
process.join()
```

does not stop or terminate the process.

It waits for the process to finish naturally or otherwise terminate.

Remember:

```text
start()     → Starts the process
join()      → Waits for the process
terminate() → Requests process termination
kill()      → Forcefully terminates the process
```

---

## 33. CPU-Bound Tasks

A **CPU-bound task** spends most of its time performing calculations.

Examples:

- Large mathematical calculations
- Image processing
- Video encoding
- Scientific computations
- Complex algorithms
- CPU-intensive data processing

Multiprocessing can improve performance when tasks can be divided into independent computations and the overhead is justified.

---

## 34. I/O-Bound Tasks

An **I/O-bound task** spends much of its time waiting for input/output operations.

Examples:

- Reading and writing files
- Network requests
- Database queries
- API requests
- Waiting for external services

For many I/O-bound workloads, threading or asynchronous programming may be more efficient than creating multiple processes.

Multiprocessing can still be appropriate for some I/O-bound workloads, depending on isolation, libraries, and application design.

---

## 35. Why Use Multiprocessing?

Multiprocessing is especially useful when:

- Tasks are CPU-intensive.
- Tasks can run independently.
- Multiple CPU cores are available.
- The workload benefits from parallel execution.
- The computation is large enough to justify process overhead.

Examples:

```text
Image Processing
Video Processing
Scientific Computation
Large Mathematical Operations
CPU-Intensive Data Processing
```

Multiprocessing is a tool, not a guarantee of faster execution. Measure performance with representative workloads.

---

## 36. Multiprocessing and the GIL

GIL stands for **Global Interpreter Lock**.

In traditional GIL-enabled CPython builds, the GIL generally prevents multiple threads in the same interpreter from executing Python bytecode simultaneously.

Multiprocessing uses separate processes. Each process normally has its own Python interpreter and its own GIL in traditional builds.

Therefore, CPU-bound Python programs can use multiple CPU cores through multiple processes.

### Multithreading

```text
One Process
     |
     +--- Thread 1
     |
     +--- Thread 2
     |
     +--- Thread 3

Traditional CPython:
The GIL can limit parallel execution of Python bytecode.
```

### Multiprocessing

```text
Main Process
     |
     +--- Process 1
     |
     +--- Process 2
     |
     +--- Process 3

Traditional CPython:
Separate processes can execute Python code in parallel.
```

Modern Python also offers free-threaded CPython builds that can run without the GIL. Performance and behavior depend on the Python build, libraries, and workload.

---

## 37. Multiprocessing vs. Multithreading

| Feature | Multiprocessing | Multithreading |
|---|---|---|
| Basic unit | Process | Thread |
| Memory | Separate process memory by default | Shared memory within the process |
| CPU-bound pure Python | Often useful in traditional CPython | Usually limited by the GIL in traditional CPython |
| I/O-bound tasks | Can be useful | Often suitable |
| Communication | Often requires IPC | Shared data is readily accessible |
| Memory overhead | Usually higher | Usually lower |
| Isolation | Stronger process isolation | Threads share process resources |
| Creation overhead | Usually higher | Usually lower |
| Failure isolation | A child crash need not crash the parent | An unhandled thread exception does not automatically terminate the whole process |

### General Rule

```text
CPU-bound pure-Python tasks
             |
             v
Consider Multiprocessing
```

```text
I/O-bound tasks
       |
       v
Consider Threading or Asyncio
```

These are guidelines, not absolute rules. Benchmark your application and consider its architecture.

---

## 38. Separate Memory in Processes

Processes normally have separate memory spaces.

### Example

```python
import multiprocessing


number = 10


def task():
    global number

    number = 20
    print("Child:", number)


if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    process.start()
    process.join()

    print("Parent:", number)
```

Typical output:

```text
Child: 20
Parent: 10
```

The child modifies its own process-local variable. The parent's ordinary Python variable remains unchanged.

The exact process-start mechanism affects how initial state is obtained, but changing a normal Python variable in the child does not directly update the parent's variable.

---

## 39. Sharing Data Between Processes

Because processes normally have separate memory spaces, ordinary Python variables are not automatically shared.

Python provides several communication and sharing mechanisms:

```text
Queue
Pipe
Value
Array
Manager
Shared Memory
```

Choose the mechanism based on the data size, communication pattern, and synchronization requirements.

---

## 40. `multiprocessing.Queue`

A multiprocessing queue allows processes to exchange messages and data safely.

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

    message = queue.get()
    print(message)

    process.join()
    queue.close()
    queue.join_thread()
```

Output:

```text
Hello from child
```

### How It Works

```text
Process A
    |
    v
  Queue
    |
    v
Process B
```

Important methods:

- `put()`: Adds an item.
- `get()`: Retrieves an item.
- `empty()`: Provides an unreliable snapshot for coordination; do not use it to decide whether a queue will remain empty.
- `close()`: Closes the queue's local resources.
- `join_thread()`: Waits for the queue's feeder thread to finish flushing buffered data.

For more complex programs, coordinate queue shutdown carefully to avoid blocking or waiting indefinitely.

---

## 41. `multiprocessing.Pipe`

A pipe provides a communication channel between processes.

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
    child_conn.close()

    print(parent_conn.recv())

    process.join()
    parent_conn.close()
```

Output:

```text
Hello from child
```

### Important Methods

- `send()`: Sends an object through the connection.
- `recv()`: Receives an object.
- `close()`: Closes the connection.

Objects sent through a pipe are generally serialized. A pipe created without `duplex=False` is bidirectional.

Use queues for convenient multi-producer or multi-consumer communication. Pipes can be useful for direct communication between processes.

---

## 42. `multiprocessing.Pool`

A process pool manages a group of worker processes.

It is useful when you have many similar tasks to distribute among workers.

### Example

```python
import multiprocessing


def square(number):
    return number * number


if __name__ == "__main__":
    with multiprocessing.Pool(processes=3) as pool:
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

Here, `processes=3` requests a pool of three worker processes.

The number of workers should be chosen based on available resources and the workload.

---

## 43. `Pool.map()`

Use:

```python
pool.map(function, iterable)
```

to apply a function to each item in an iterable.

### Example

```python
results = pool.map(square, [1, 2, 3, 4, 5])
```

Conceptually:

```text
1 → square(1)
2 → square(2)
3 → square(3)
4 → square(4)
5 → square(5)
```

The returned list preserves the input order, even if tasks complete in a different order.

`map()` waits for the results and returns them together.

---

## 44. Why Use a Process Pool?

Without a pool, you may need to manage many processes manually.

```python
p1 = multiprocessing.Process(...)
p2 = multiprocessing.Process(...)
p3 = multiprocessing.Process(...)
```

A process pool simplifies task distribution and worker management.

```text
Many Tasks
    |
    v
Process Pool
    |
    +--- Worker 1
    |
    +--- Worker 2
    |
    +--- Worker 3
    |
    v
Results
```

A pool can also reduce the repeated cost of creating a new process for every task.

**Important:** The `Pool` context manager terminates the pool when its context exits. Ensure required work has completed and results have been collected before leaving the context.

---

## 45. Advantages of Multiprocessing

### 1. CPU-Heavy Work

Multiple processes can improve performance for CPU-intensive tasks.

### 2. Multi-Core Execution

Independent processes can run on separate CPU cores simultaneously.

### 3. Process Isolation

Each process normally has its own memory space.

### 4. Failure Isolation

A child process can fail without automatically terminating the parent process.

### 5. Parallel Execution

Independent tasks can execute in parallel when sufficient resources are available.

---

## 46. Disadvantages of Multiprocessing

### 1. Higher Memory Usage

Each process usually requires its own interpreter and process memory.

### 2. Process Creation Overhead

Creating processes is generally more expensive than creating threads.

### 3. More Complex Communication

Processes often need IPC mechanisms such as:

```text
Queue
Pipe
Manager
Shared Memory
```

### 4. Serialization Overhead

Objects passed between processes often need to be serialized and deserialized.

This adds processing time and may increase memory usage.

### 5. More Complex Debugging

Debugging, logging, exception handling, and lifecycle management can be more complicated with multiple processes.

### 6. Synchronization Challenges

Shared memory and coordinated access may require locks or other synchronization mechanisms.

---

## 47. When Should You Use Multiprocessing?

Consider multiprocessing when:

```text
✓ The task is CPU-intensive.
✓ Tasks are mostly independent.
✓ Multiple CPU cores are available.
✓ Parallel execution can improve performance.
✓ The workload justifies process overhead.
```

Examples:

```text
Image Processing
Video Processing
Scientific Computation
Large Mathematical Operations
CPU-Intensive Data Processing
```

---

## 48. When Should You Avoid Multiprocessing?

Multiprocessing is not always faster.

The overhead of creating processes, transferring data, and collecting results may outweigh the benefits.

Examples:

```text
Very Small Calculations
Simple Print Operations
Tiny Tasks
Tasks with Frequent Data Transfer
Tasks with Heavy Synchronization
```

For small tasks, sequential execution or threading may be simpler and faster.

Measure performance instead of assuming that more processes always mean better performance.

---

## 49. Important Process Methods

| Method | Purpose |
|---|---|
| `start()` | Starts the process |
| `join()` | Waits for the process to terminate |
| `is_alive()` | Checks whether the process is running |
| `terminate()` | Requests termination using the platform's termination mechanism |
| `kill()` | Forcefully terminates the process using the platform's kill mechanism |
| `close()` | Releases resources associated with a finished process object |
| `run()` | Executes the target callable when called directly or by the process startup mechanism |
| `multiprocessing.current_process()` | Returns the current process object |

### Important Notes

- Calling `run()` directly does not create a new process.
- `close()` should generally be called only after the process has stopped. Calling it while the process is still running raises an error.
- A process object cannot normally be restarted after `start()` has been called.

---

## 50. Important Process Attributes

| Attribute | Purpose |
|---|---|
| `name` | Process name |
| `pid` | Operating-system process ID |
| `exitcode` | Exit status after termination |
| `daemon` | Indicates whether the process is a daemon process |
| `sentinel` | An OS handle or file descriptor that becomes ready when the process exits |

The standard `multiprocessing.Process` API does not provide the `ident` attribute used by `threading.Thread`.

### Examples

```python
process.name
process.pid
process.exitcode
process.daemon
```

To get the current process ID:

```python
import os

print(os.getpid())
```

To get the parent process ID:

```python
print(os.getppid())
```

---

## 51. Complete Multiprocessing Example

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
Task 1 finished
Task 0 finished
Task 2 finished
All processes finished
```

The PIDs and output order are illustrative. Actual values and ordering vary between runs.

The final message appears after all three child processes have terminated because the parent joins every process.

---

## 52. Multiprocessing Mental Model

The easiest way to understand multiprocessing is to think of independent processes working on separate tasks.

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
          +------------+------------+
                       |
                       v
              Operating System
             Schedules CPU Time
```

Each process normally has:

```text
Its own execution
       +
Its own memory space
       +
Its own process ID
       +
Its own Python interpreter
```

Processes can execute simultaneously on different CPU cores, but actual parallelism depends on the operating system, hardware, and workload.

---

## 53. Short Revision

### What is a process?

A process is a running instance of a program.

### What is multiprocessing?

Multiprocessing means using multiple processes to perform tasks.

### What is `Process()`?

It creates a process object.

### What is `start()`?

It starts a new process.

### What is `join()`?

It waits for a process to terminate.

### What is `target`?

The callable that the child process executes.

### What is `args`?

It passes positional arguments.

### What is `kwargs`?

It passes keyword arguments.

### What is `terminate()`?

It requests termination of a process.

### What is `kill()`?

It forcefully terminates a process.

### What is `is_alive()`?

It checks whether a process is currently running.

### What is `exitcode`?

It reports the process's exit status after termination.

### What is `pid`?

The operating-system Process ID.

### What is `current_process()`?

It returns the current process object.

### What is a Queue?

It allows processes to exchange data and messages.

### What is a Pipe?

It provides a communication channel between processes.

### What is a Pool?

It manages worker processes and distributes tasks among them.

### What is the main guard?

`if __name__ == "__main__":` prevents top-level process-creation code from being executed again when the main module is imported by a spawned child process.

---

## 54. Most Important Exam and Interview Topics

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
16. Multiprocessing vs. Multithreading
17. CPU-bound vs. I/O-bound
18. GIL
19. Queue
20. Pipe
21. Pool
22. Separate Process Memory
23. if __name__ == "__main__"
24. Process Exit Codes
25. Process Start Methods
26. Inter-Process Communication
27. Serialization and Pickling
28. Process Synchronization
```

---

## 55. Bonus: Process Start Methods

Python multiprocessing supports different ways of starting child processes.

The main start methods are:

- **`spawn`:** Starts a fresh Python interpreter.
- **`fork`:** Creates a child by forking the parent process. Available on supported POSIX systems.
- **`forkserver`:** Uses a separate server process to create child processes. Available on supported POSIX systems.

Availability and defaults depend on the operating system and Python version.

You can inspect the available methods:

```python
import multiprocessing

print(multiprocessing.get_all_start_methods())
print(multiprocessing.get_start_method())
```

You can choose a start method explicitly when appropriate:

```python
import multiprocessing


def task():
    print("Child process is running")


if __name__ == "__main__":
    ctx = multiprocessing.get_context("spawn")

    process = ctx.Process(target=task)

    process.start()
    process.join()
```

Using a context is useful when you want predictable behavior across environments.

With `spawn`, the target function and its arguments generally need to be picklable, and the main module must be safely importable.

---

## 56. Bonus: Process Synchronization

Processes sometimes need to coordinate their work or access shared resources safely.

Python provides synchronization tools such as:

```text
Lock
RLock
Semaphore
Event
Condition
Barrier
```

These tools are available through `multiprocessing` and are designed for synchronization between processes.

### Example: Process Lock

```python
import multiprocessing


def worker(lock, number):
    with lock:
        print(f"Worker {number} entered")


if __name__ == "__main__":
    lock = multiprocessing.Lock()

    processes = []

    for i in range(3):
        process = multiprocessing.Process(
            target=worker,
            args=(lock, i)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()
```

The lock ensures that only one process at a time holds the lock while executing the protected section.

However, the order in which workers acquire the lock is not guaranteed.

---

## 57. Final Quick Revision

### Multiprocessing

```text
Multiprocessing
       |
       v
Multiple Processes
       |
       v
Separate Process Memory
       |
       v
Possible Multi-Core Execution
       |
       v
Useful for CPU-Bound Tasks
```

### Process Lifecycle

```text
Process()
    |
    v
start()
    |
    v
Task Execution
    |
    v
Process Terminates
    |
    v
join() Returns
```

### CPU-Bound vs. I/O-Bound

```text
CPU-Bound
    |
    v
Consider Multiprocessing
```

```text
I/O-Bound
    |
    v
Consider Threading or Asyncio
```

## One-Line Memory Rule

> **Multiprocessing uses multiple independent processes, normally with separate memory spaces, and is especially useful for CPU-bound tasks when the benefits of parallel execution outweigh the overhead.**

## Recommended Practice Order

1. Create a process using `multiprocessing.Process()`.
2. Understand `target`, `args`, and `kwargs`.
3. Practice `start()` and `join()`.
4. Learn process names, PIDs, and `is_alive()`.
5. Understand the main guard and the `spawn` start method.
6. Practice creating multiple processes.
7. Learn `terminate()`, `kill()`, and `exitcode`.
8. Exchange data using `Queue` and `Pipe`.
9. Process multiple tasks using `Pool`.
10. Understand the GIL and compare multiprocessing with multithreading.
11. Practice process synchronization.
12. Measure performance using CPU-bound examples.

**Final advice:** Start with simple child-process programs, then practice `Queue`, `Pool`, and process synchronization. Once you understand process creation and communication, multiprocessing becomes much easier to use in real Python applications.
"""