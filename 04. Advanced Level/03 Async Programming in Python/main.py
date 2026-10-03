'''
# Async and Await in Python

## 1. Introduction

In Python, **Asynchronous Programming** is used to handle tasks where a program can make 
progress on other tasks while waiting for an asynchronous operation to complete.

The main concepts are:

```text
async
await
asyncio
```

The easiest way to remember them:

```text
async   → Defines an asynchronous function
await   → Waits for an asynchronous operation
asyncio → Provides tools for asynchronous programming
```

---

# Part 1: async

## 2. What is `async`?

`async` is a Python **keyword** used to define an **asynchronous function**, also called a **coroutine function**.

### Simple Definition

> **`async` is a keyword used to define an asynchronous function (coroutine function).**

Example:

```python
async def main():
    print("Hello World")
```

Here:

```python
async def
```

defines `main()` as an asynchronous function.

---

## 3. Simple Example of `async`

```python
import asyncio


async def main(name):
    print(f"Hello World {name}")


asyncio.run(main("Faruk"))
```

### Output

```text
Hello World Faruk
```

Here:

```python
async def main(name):
```

defines the asynchronous function.

And:

```python
asyncio.run(main("Faruk"))
```

runs the coroutine.

---

## 4. What Happens Here?

Conceptually:

```text
async def
    ↓
Coroutine Function
    ↓
main("Faruk")
    ↓
Coroutine Object
    ↓
asyncio.run()
    ↓
Execution
```

Calling:

```python
main("Faruk")
```

creates a coroutine object.

It does not execute the coroutine body in the same way as calling a normal synchronous function.

---

# Part 2: await

## 5. What is `await`?

`await` is a Python **keyword** used inside an asynchronous function to wait for an **awaitable operation** to complete.

### Simple Definition

> **`await` is used inside an async function to wait for an asynchronous operation to complete.**

Example:

```python
import asyncio


async def main():
    print("Start")

    await asyncio.sleep(1)

    print("End")


asyncio.run(main())
```

### Output

```text
Start
End
```

Here:

```python
await asyncio.sleep(1)
```

waits for the asynchronous sleep operation.

---

# Part 3: asyncio

## 6. What is `asyncio`?

`asyncio` is a Python **standard library module** used for writing and running asynchronous programs.

### Simple Definition

> **`asyncio` is a Python standard library module that provides tools for asynchronous programming.**

Import:

```python
import asyncio
```

---

# 7. `asyncio.run()`

`asyncio.run()` is used to run a top-level coroutine.

Example:

```python
import asyncio


async def main(name):
    print(f"Hello World {name}")


asyncio.run(main("Faruk"))
```

Here:

```python
asyncio.run(main("Faruk"))
```

runs the `main()` coroutine.

Conceptually:

```text
Coroutine
    ↓
asyncio.run()
    ↓
Event Loop
    ↓
Coroutine Execution
```

---

# Part 4: async + await

## 8. Simple Example

```python
import asyncio


async def main(name):
    print(f"Hello World {name}")

    await asyncio.sleep(1)

    print(f"Hello World {name}")


asyncio.run(main("Faruk"))
```

### Output

```text
Hello World Faruk
Hello World Faruk
```

---

## 9. Step-by-Step Explanation

First:

```python
async def main(name):
```

defines an asynchronous function.

Then:

```python
asyncio.run(main("Faruk"))
```

runs the coroutine.

First:

```python
print(f"Hello World {name}")
```

is executed.

Then:

```python
await asyncio.sleep(1)
```

waits for one second.

After the wait:

```python
print(f"Hello World {name}")
```

is executed again.

Conceptually:

```text
async def main()
        ↓
      Start
        ↓
Print Hello World
        ↓
await asyncio.sleep(1)
        ↓
      Wait
        ↓
Print Hello World
        ↓
       End
```

---

# Part 5: Why Use Async?

## 10. Why Asynchronous Programming?

Asynchronous programming is especially useful for **I/O-bound operations**, such as:

```text
Network Requests
Database Operations
API Requests
File I/O
Timers
```

For example, suppose a program is waiting for a network response.

In synchronous programming:

```text
Task A
  ↓
Wait
  ↓
Task A Complete
  ↓
Task B
```

In asynchronous programming:

```text
Task A
  ↓
Waiting ─────────┐
                 ↓
               Task B
                 ↓
Task A Complete
```

While one asynchronous operation is waiting, other asynchronous work can make progress.

---

# Part 6: asyncio.sleep()

## 11. `asyncio.sleep()`

`asyncio.sleep()` provides an asynchronous sleep operation.

Example:

```python
import asyncio


async def main():
    print("Start")

    await asyncio.sleep(2)

    print("End")


asyncio.run(main())
```

Conceptually:

```text
Start
  ↓
Wait 2 seconds
  ↓
End
```

Important:

```python
await asyncio.sleep(2)
```

uses `await` because `asyncio.sleep()` returns an awaitable.

---

# Part 7: Multiple Async Tasks

## 12. Running Multiple Coroutines

One of the important benefits of asynchronous programming is that multiple coroutines can make progress while other operations are waiting.

Example:

```python
import asyncio


async def task1():
    print("Task 1 started")

    await asyncio.sleep(2)

    print("Task 1 completed")


async def task2():
    print("Task 2 started")

    await asyncio.sleep(1)

    print("Task 2 completed")


async def main():
    await asyncio.gather(
        task1(),
        task2()
    )


asyncio.run(main())
```

Conceptually:

```text
Task 1 ── Start ── Wait 2s ── Complete
Task 2 ── Start ── Wait 1s ── Complete
```

While `task1()` is waiting, `task2()` can make progress.

---

# Part 8: asyncio.gather()

## 13. What is `asyncio.gather()`?

`asyncio.gather()` is used to schedule multiple awaitables and wait for their results.

Example:

```python
import asyncio


async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"


async def task2():
    await asyncio.sleep(1)
    return "Task 2 completed"


async def main():
    results = await asyncio.gather(
        task1(),
        task2()
    )

    print(results)


asyncio.run(main())
```

### Output

```text
['Task 1 completed', 'Task 2 completed']
```

Conceptually:

```text
             main()
               │
       ┌───────┴───────┐
       ↓               ↓
    task1()          task2()
       ↓               ↓
    sleep 2s         sleep 1s
       ↓               ↓
   completed        completed
       └───────┬───────┘
               ↓
          gather()
               ↓
            results
```

---

# Part 9: async vs await

## 14. Difference Between `async` and `await`

### `async`

Used to define an asynchronous function.

```python
async def main():
    pass
```

### `await`

Used to wait for an awaitable operation.

```python
await asyncio.sleep(1)
```

Therefore:

```text
async  → Defines a coroutine function
await  → Waits for an awaitable
```

---

# Part 10: async vs asyncio

## 15. Difference Between `async` and `asyncio`

`async` is a Python keyword:

```python
async def main():
    pass
```

`asyncio` is a Python standard library module:

```python
import asyncio
```

Therefore:

```text
async
→ Keyword

asyncio
→ Standard Library Module
```

---

# Part 11: Complete Example

## 16. Full Example

```python
import asyncio


async def main(name):
    print(f"Hello World {name}")

    await asyncio.sleep(1)

    print(f"Hello Again {name}")


asyncio.run(main("Faruk"))
```

### Output

```text
Hello World Faruk
Hello Again Faruk
```

### Explanation

```text
async def
    ↓
Defines coroutine function

main("Faruk")
    ↓
Creates coroutine

asyncio.run()
    ↓
Runs coroutine

await asyncio.sleep(1)
    ↓
Waits asynchronously

Next statement
    ↓
Executes
```

---

# Part 12: Important Rules

## 17. Rule 1 — `await` is used inside an async function

Correct:

```python
async def main():
    await asyncio.sleep(1)
```

Incorrect:

```python
def main():
    await asyncio.sleep(1)
```

In normal Python code, `await` must be used in an appropriate asynchronous context, typically inside an `async def` coroutine.

---

## 18. Rule 2 — `async def` defines a coroutine function

Example:

```python
async def main():
    print("Hello")
```

This is a coroutine function.

Calling:

```python
main()
```

creates a coroutine object.

It can then be executed using:

```python
asyncio.run(main())
```

---

# Part 13: Synchronous vs Asynchronous

## 19. Synchronous Example

```python
import time


def task1():
    print("Task 1 started")

    time.sleep(2)

    print("Task 1 completed")


def task2():
    print("Task 2 started")

    time.sleep(1)

    print("Task 2 completed")


task1()
task2()
```

Conceptually:

```text
Task 1
  ↓
Wait 2s
  ↓
Task 1 Complete
  ↓
Task 2
  ↓
Wait 1s
  ↓
Task 2 Complete
```

---

## 20. Asynchronous Example

```python
import asyncio


async def task1():
    print("Task 1 started")

    await asyncio.sleep(2)

    print("Task 1 completed")


async def task2():
    print("Task 2 started")

    await asyncio.sleep(1)

    print("Task 2 completed")


async def main():
    await asyncio.gather(
        task1(),
        task2()
    )


asyncio.run(main())
```

Conceptually:

```text
Task 1 ──────── Wait ───────── Complete
     \
      \
Task 2 ── Wait ── Complete
```

Here, while `task1()` is waiting, `task2()` can make progress.

---

# Part 14: Async Programming Mental Model

## 21. Easy Mental Model

Imagine you are a restaurant waiter.

### Synchronous

```text
Take Customer A's order
        ↓
Give it to the kitchen
        ↓
Wait for the order
        ↓
Order completed
        ↓
Serve Customer B
```

### Asynchronous

```text
Take Customer A's order
        ↓
Give it to the kitchen
        ↓
Do not wait there
        ↓
Take Customer B's order
        ↓
Take Customer C's order
        ↓
A's order becomes ready
        ↓
Serve Customer A
```

This is the basic idea of asynchronous programming.

---

# Part 15: Common Mistakes

## Mistake 1

Wrong:

```text
await = async function
```

Correct:

```text
async  → Defines a coroutine function
await  → Waits for an awaitable
```

---

## Mistake 2

Thinking:

```python
async def
```

automatically means the function runs in parallel.

This is not correct.

**Asynchronous programming and parallelism are different concepts.**

---

## Mistake 3

Using `await` inside a normal function:

```python
def main():
    await asyncio.sleep(1)
```

Usually, it should be:

```python
async def main():
    await asyncio.sleep(1)
```

---

## Mistake 4

Thinking `asyncio` is a keyword.

Correct:

```text
asyncio = Python standard library module
```

---

# Part 16: Interview Questions

## Q1. What is `async`?

### Answer

> **`async` is a Python keyword used to define an asynchronous function, also called a coroutine function.**

Example:

```python
async def main():
    pass
```

---

## Q2. What is `await`?

### Answer

> **`await` is a Python keyword used inside an async function to wait for an awaitable operation to complete.**

Example:

```python
await asyncio.sleep(1)
```

---

## Q3. What is `asyncio`?

### Answer

> **`asyncio` is Python's standard library module for writing and running asynchronous programs.**

Example:

```python
import asyncio
```

---

## Q4. What is a coroutine?

### Answer

A coroutine is an asynchronous computation defined using `async def`.

Example:

```python
async def main():
    print("Hello")
```

Calling:

```python
main()
```

creates a coroutine object.

---

## Q5. What does `asyncio.run()` do?

### Answer

`asyncio.run()` runs a top-level coroutine and manages the event loop used to execute it.

Example:

```python
asyncio.run(main())
```

---

## Q6. Can we use `await` outside an async function?

### Answer

In normal Python code, `await` must be used in an appropriate asynchronous context, typically inside an `async def` coroutine.

Example:

```python
async def main():
    await asyncio.sleep(1)
```

---

## Q7. What is the difference between synchronous and asynchronous programming?

### Answer

```text
Synchronous
→ Tasks generally execute sequentially
→ A waiting operation can block subsequent work

Asynchronous
→ Other asynchronous work can make progress while an operation is waiting
→ Especially useful for I/O-bound workloads
```

---

# Part 17: Main Comparison Table

| Concept            | What it is              | Main Purpose                     | Example                     |
| ------------------ | ----------------------- | -------------------------------- | --------------------------- |
| `async`            | Keyword                 | Define coroutine function        | `async def main()`          |
| `await`            | Keyword                 | Wait for an awaitable            | `await asyncio.sleep(1)`    |
| `asyncio`          | Standard library module | Async programming tools          | `import asyncio`            |
| Coroutine          | Async computation       | Represents async work            | `main()`                    |
| `asyncio.run()`    | Function                | Run a top-level coroutine        | `asyncio.run(main())`       |
| `asyncio.gather()` | Function                | Run/wait for multiple awaitables | `await asyncio.gather(...)` |

---

# Part 18: Final Cheat Sheet

```text
┌────────────────────────────────────────────┐
│          ASYNCHRONOUS PROGRAMMING          │
├────────────────────────────────────────────┤
│                                            │
│ async                                      │
│ → Python keyword                           │
│ → Defines coroutine function               │
│                                            │
│ await                                      │
│ → Python keyword                           │
│ → Waits for an awaitable                   │
│                                            │
│ asyncio                                    │
│ → Standard library module                  │
│ → Provides async programming tools         │
│                                            │
│ asyncio.run()                              │
│ → Runs a top-level coroutine               │
│                                            │
│ asyncio.gather()                           │
│ → Runs/waits for multiple awaitables       │
│                                            │
└────────────────────────────────────────────┘
```

---

# 19. One-Line Summary

```text
async   → Define an asynchronous function
await   → Wait for an asynchronous operation
asyncio → Tools for asynchronous programming
```

### The easiest way to remember:

> **async = "Define an async function."**

> **await = "Wait for this async operation."**

> **asyncio = "Tools for asynchronous programming."**

> **asyncio.run() = "Run this coroutine."**
'''
