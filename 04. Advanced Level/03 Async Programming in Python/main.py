"""
# Python Async and Await

## 1. What is Asynchronous Programming?

**Asynchronous Programming** means a program can work on other tasks while one task is waiting.

It is very useful when the program spends time waiting for:

* Network requests
* API responses
* Database operations
* File I/O
* Timers

The three main concepts are:

```text
async   → Defines an asynchronous function
await   → Waits for an awaitable operation
asyncio → Provides tools for asynchronous programming
```

### Easy way to remember

> **async = Define an async function**
> **await = Wait for an async operation**
> **asyncio = Tools for async programming**

---

# Part 1: `async`

## 2. What is `async`?

`async` is a Python **keyword** used to define an asynchronous function.

An asynchronous function is also called a **coroutine function**.

### Example

```python
async def main():
    print("Hello World")
```

Here:

```python
async def
```

means `main()` is an asynchronous function.

### Easy Definition

> **`async` is used to define a coroutine function.**

---

## 3. Simple Example

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

### What happens?

```text
async def main()
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

Important:

When we call:

```python
main("Faruk")
```

it creates a **coroutine object**.

It does not immediately execute the coroutine body like a normal function call.

---

# Part 2: `await`

## 4. What is `await`?

`await` is a Python keyword used inside an asynchronous function to wait for an **awaitable** operation.

### Example

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

### Easy Definition

> **`await` is used to wait for an awaitable operation inside an async function.**

---

# Part 3: `asyncio`

## 5. What is `asyncio`?

`asyncio` is a Python **standard library module** used for asynchronous programming.

It provides tools for:

* Running coroutines
* Creating tasks
* Waiting for async operations
* Managing the event loop
* Running multiple async operations

Import it using:

```python
import asyncio
```

### Easy Definition

> **`asyncio` is Python's standard library for asynchronous programming.**

---

# Part 4: `asyncio.run()`

## 6. What is `asyncio.run()`?

`asyncio.run()` is commonly used to run a **top-level coroutine**.

Example:

```python
import asyncio


async def main():
    print("Hello")


asyncio.run(main())
```

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

### Easy Definition

> **`asyncio.run()` starts and runs a coroutine from normal synchronous code.**

---

# Part 5: `async` + `await`

## 7. Simple Example

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

### Step-by-step

First:

```python
async def main(name):
```

defines the coroutine function.

Then:

```python
asyncio.run(main("Faruk"))
```

runs the coroutine.

Next:

```python
print(f"Hello World {name}")
```

prints the first message.

Then:

```python
await asyncio.sleep(1)
```

waits asynchronously for one second.

Finally:

```python
print(f"Hello Again {name}")
```

prints the second message.

### Flow

```text
Start
  ↓
Print "Hello World Faruk"
  ↓
await asyncio.sleep(1)
  ↓
Wait for 1 second
  ↓
Print "Hello Again Faruk"
  ↓
End
```

---

# Part 6: Why Use Async Programming?

## 8. Why Do We Need Asynchronous Programming?

Async programming is especially useful for **I/O-bound tasks**.

Examples:

```text
Network Requests
API Requests
Database Operations
File I/O
Timers
```

Suppose a program sends a network request.

The program may have to wait for the server response.

### Synchronous

```text
Task A
  ↓
Wait
  ↓
Task A Complete
  ↓
Task B
```

The program waits for Task A before moving to Task B.

### Asynchronous

```text
Task A
  ↓
Waiting
  ↓
Task B starts
  ↓
Task B works
  ↓
Task A completes
```

While Task A is waiting, other asynchronous tasks can make progress.

### Important

Async programming does **not automatically mean parallel execution**.

Asynchronous programming and parallelism are different concepts.

---

# Part 7: `asyncio.sleep()`

## 9. What is `asyncio.sleep()`?

`asyncio.sleep()` creates an asynchronous delay.

Example:

```python
import asyncio


async def main():
    print("Start")

    await asyncio.sleep(2)

    print("End")


asyncio.run(main())
```

### Flow

```text
Start
  ↓
Wait 2 seconds
  ↓
End
```

The important part is:

```python
await asyncio.sleep(2)
```

`asyncio.sleep()` returns an awaitable, so we normally use `await` with it.

---

# Part 8: Multiple Async Tasks

## 10. Running Multiple Coroutines

One important advantage of async programming is that multiple coroutines can make progress while other coroutines are waiting.

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
Task 1 → Start → Wait 2s → Complete
Task 2 → Start → Wait 1s → Complete
```

While Task 1 is waiting, Task 2 can continue.

### Typical Output

```text
Task 1 started
Task 2 started
Task 2 completed
Task 1 completed
```

---

# Part 9: `asyncio.gather()`

## 11. What is `asyncio.gather()`?

`asyncio.gather()` is used to run multiple awaitables and wait until they finish.

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

Notice something important:

Although `task2()` finishes first, the result list keeps the **same order as the awaitables passed to `gather()`**.

We passed:

```python
task1(),
task2()
```

So the result is:

```python
[
    "Task 1 completed",
    "Task 2 completed"
]
```

### Visual Flow

```text
              main()
                │
        ┌───────┴───────┐
        ↓               ↓
     task1()          task2()
        ↓               ↓
    sleep 2s          sleep 1s
        ↓               ↓
    completed        completed
        └───────┬───────┘
                ↓
           gather()
                ↓
             results
```

---

# Part 10: `async` vs `await`

## 12. Difference Between `async` and `await`

### `async`

Used to **define** an asynchronous function.

```python
async def main():
    pass
```

### `await`

Used to **wait for** an awaitable.

```python
await asyncio.sleep(1)
```

### Easy Table

| `async`                      | `await`                  |
| ---------------------------- | ------------------------ |
| Defines a coroutine function | Waits for an awaitable   |
| Used before `def`            | Used before an awaitable |
| `async def main()`           | `await asyncio.sleep(1)` |

Remember:

```text
async  → Define
await  → Wait
```

---

# Part 11: `async` vs `asyncio`

## 13. Difference Between `async` and `asyncio`

### `async`

`async` is a Python **keyword**.

```python
async def main():
    pass
```

### `asyncio`

`asyncio` is a Python **standard library module**.

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

# Part 12: Coroutine

## 14. What is a Coroutine?

A **coroutine** is an asynchronous computation created from an `async def` function.

Example:

```python
async def main():
    print("Hello")
```

This defines a coroutine function.

When we call:

```python
main()
```

we get a **coroutine object**.

It can be run using:

```python
asyncio.run(main())
```

### Simple Flow

```text
async def main()
       ↓
Coroutine Function
       ↓
main()
       ↓
Coroutine Object
       ↓
asyncio.run()
       ↓
Execution
```

---

# Part 13: Synchronous vs Asynchronous

## 15. Synchronous Programming

Example:

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

Flow:

```text
Task 1 starts
    ↓
Wait 2 seconds
    ↓
Task 1 completes
    ↓
Task 2 starts
    ↓
Wait 1 second
    ↓
Task 2 completes
```

The total waiting time is approximately:

```text
2 + 1 = 3 seconds
```

---

# Part 14: Asynchronous Programming

## 16. Asynchronous Example

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
Task 1 → Start → Wait ─────────→ Complete
              ↘
Task 2 → Start → Wait → Complete
```

The two waits can overlap, so the total waiting time is approximately **2 seconds**, not 3 seconds.

### Important

This happens because both tasks are doing asynchronous waiting.

---

# Part 15: Easy Mental Model

## 17. Restaurant Waiter Example

Imagine you are a restaurant waiter.

### Synchronous

```text
Take Customer A's order
        ↓
Give order to kitchen
        ↓
Wait for A's food
        ↓
Food ready
        ↓
Serve A
        ↓
Take Customer B's order
```

The waiter stays focused on Customer A.

### Asynchronous

```text
Take Customer A's order
        ↓
Give order to kitchen
        ↓
Do not wait there
        ↓
Take Customer B's order
        ↓
Take Customer C's order
        ↓
A's food becomes ready
        ↓
Serve Customer A
```

### Main Idea

> **When one task is waiting, the program can work on other available asynchronous tasks.**

---

# Part 16: Important Rules

## 18. Rule 1 — `await` is normally used inside `async def`

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

In normal Python code, `await` must be used in an appropriate asynchronous context.

---

## 19. Rule 2 — `async def` creates a Coroutine Function

Example:

```python
async def main():
    print("Hello")
```

This defines a coroutine function.

Calling:

```python
main()
```

creates a coroutine object.

To run it from normal top-level code:

```python
asyncio.run(main())
```

---

# Part 17: Common Mistakes

## Mistake 1: Confusing `async` and `await`

Wrong idea:

```text
await = async function
```

Correct:

```text
async → Defines a coroutine function
await → Waits for an awaitable
```

---

## Mistake 2: Thinking `async` Means Parallel

This is incorrect:

```text
async = parallel
```

Async programming is about **cooperative concurrency**.

Parallelism means multiple computations can execute at the same time, typically using multiple CPU cores or workers.

So:

```text
Concurrency ≠ Parallelism
```

Asyncio is mainly useful for handling many **I/O-bound** operations efficiently.

---

## Mistake 3: Using `await` in a Normal Function

Wrong:

```python
def main():
    await asyncio.sleep(1)
```

Correct:

```python
async def main():
    await asyncio.sleep(1)
```

---

## Mistake 4: Thinking `asyncio` is a Keyword

Incorrect:

```text
asyncio = keyword
```

Correct:

```text
asyncio = standard library module
```

---

# Part 18: Complete Example

## 20. Full Example

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
Creates coroutine object

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

# Part 19: Real-Life Example

Suppose you need to call three APIs:

```text
API 1 → 2 seconds
API 2 → 1 second
API 3 → 3 seconds
```

### Synchronous approach

```text
API 1 → Wait 2s
API 2 → Wait 1s
API 3 → Wait 3s

Total ≈ 6s
```

### Asynchronous approach

```text
API 1 ─────── Wait 2s ─── Complete
API 2 ── Wait 1s ── Complete
API 3 ───────────── Wait 3s ───────── Complete
```

The waits can overlap.

So the total time can be close to:

```text
3 seconds
```

rather than:

```text
6 seconds
```

This is why async programming is useful for many I/O-bound tasks.

---

# Part 20: Important Terms

## 21. Awaitable

An **awaitable** is an object that can be used with `await`.

Common examples include:

* Coroutine objects
* `asyncio.Task`
* `asyncio.Future`

Example:

```python
await asyncio.sleep(1)
```

Here, the result of `asyncio.sleep(1)` is awaitable.

---

## 22. Event Loop

The **event loop** is the mechanism that manages and runs asynchronous tasks.

Simple mental model:

```text
Event Loop
    ↓
Check tasks
    ↓
Run task
    ↓
Task waits
    ↓
Run another ready task
    ↓
Task becomes ready
    ↓
Continue task
```

You can think of it as the **manager of async tasks**.

---

# Part 21: Interview Questions

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

> **`await` is a Python keyword used to wait for an awaitable operation inside an asynchronous context.**

Example:

```python
await asyncio.sleep(1)
```

---

## Q3. What is `asyncio`?

### Answer

> **`asyncio` is Python's standard library module for writing asynchronous programs.**

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

`asyncio.run()` runs a top-level coroutine and manages the event loop needed to execute it.

Example:

```python
asyncio.run(main())
```

---

## Q6. Can we use `await` outside an async function?

### Answer

In normal Python code, `await` must be used in an appropriate asynchronous context, typically inside an `async def` function.

Example:

```python
async def main():
    await asyncio.sleep(1)
```

---

## Q7. What is the difference between synchronous and asynchronous programming?

### Answer

### Synchronous

```text
Task A
  ↓
Wait
  ↓
Task A Complete
  ↓
Task B
```

### Asynchronous

```text
Task A
  ↓
Wait
  ↓
Task B can make progress
  ↓
Task A completes
```

Async programming is especially useful for I/O-bound work.

---

## Q8. Does async mean parallelism?

### Answer

**No.**

Asynchronous programming and parallelism are different.

```text
Async
→ Multiple tasks can make progress without blocking on I/O

Parallelism
→ Multiple computations execute at the same time
```

---

## Q9. What is `asyncio.gather()`?

### Answer

`asyncio.gather()` is used to run multiple awaitables and wait for all of them to finish.

Example:

```python
results = await asyncio.gather(
    task1(),
    task2()
)
```

---

## Q10. What is an event loop?

### Answer

> **An event loop manages and executes asynchronous tasks and decides which ready task should run next.**

---

# Part 22: Main Comparison Table

| Concept            | Type              | Main Purpose                     | Example                     |
| ------------------ | ----------------- | -------------------------------- | --------------------------- |
| `async`            | Keyword           | Define coroutine function        | `async def main()`          |
| `await`            | Keyword           | Wait for an awaitable            | `await asyncio.sleep(1)`    |
| `asyncio`          | Module            | Async programming tools          | `import asyncio`            |
| Coroutine          | Async computation | Represents async work            | `main()`                    |
| Awaitable          | Object/protocol   | Can be used with `await`         | `asyncio.sleep(1)`          |
| Event Loop         | Async mechanism   | Manages async execution          | `asyncio.run()`             |
| `asyncio.run()`    | Function          | Run top-level coroutine          | `asyncio.run(main())`       |
| `asyncio.gather()` | Function          | Run/wait for multiple awaitables | `await asyncio.gather(...)` |

---

# Part 23: Quick Revision

```text
async
↓
Defines an asynchronous/coroutine function
```

```text
await
↓
Waits for an awaitable
```

```text
asyncio
↓
Python standard library for async programming
```

```text
asyncio.run()
↓
Runs a top-level coroutine
```

```text
asyncio.gather()
↓
Runs multiple awaitables and waits for them
```

```text
Coroutine
↓
Asynchronous computation
```

```text
Event Loop
↓
Manages asynchronous execution
```

---

# Part 24: Final Cheat Sheet

```text
┌──────────────────────────────────────────────┐
│       PYTHON ASYNCHRONOUS PROGRAMMING        │
├──────────────────────────────────────────────┤
│                                              │
│ async                                        │
│ → Defines a coroutine function              │
│                                              │
│ await                                        │
│ → Waits for an awaitable                     │
│                                              │
│ asyncio                                      │
│ → Standard library module                    │
│ → Provides async programming tools           │
│                                              │
│ Coroutine                                    │
│ → Asynchronous computation                   │
│                                              │
│ asyncio.run()                                │
│ → Runs a top-level coroutine                 │
│                                              │
│ asyncio.gather()                             │
│ → Runs/waits for multiple awaitables         │
│                                              │
│ Event Loop                                   │
│ → Manages asynchronous execution             │
│                                              │
└──────────────────────────────────────────────┘
```

# One-Line Summary

```text
async   → Define an asynchronous function
await   → Wait for an awaitable
asyncio → Tools for asynchronous programming
```

### Easiest Way to Remember

> **async = Define**

> **await = Wait**

> **asyncio = Async tools**

> **asyncio.run() = Run a coroutine**

> **asyncio.gather() = Run/wait for multiple async operations**

### Most Important Point

```text
Async programming is mainly useful when tasks spend time
waiting for I/O, such as network requests, APIs, databases,
files, and timers.
```

"""