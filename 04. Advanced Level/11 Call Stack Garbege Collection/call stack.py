# ======================== WHAT IS CALL STACK ========================

# The call stack is a data structure that stores information
# about the active (currently executing) functions in a program.
#
# It helps the program keep track of which function is currently running
# and where to return after a function call finishes.
#
# The call stack works on the principle of LIFO (Last In, First Out).

# ====================================================================


# ======================== WORKING FLOW OF CALL STACK ========================

# 1. When a function is called, it is pushed onto the call stack.
# 2. When the function finishes executing, it is popped off the stack.
# 3. The call stack helps manage the order of function execution
#    and ensures the correct return after each call.

# ============================================================================


# ======================== EXAMPLE OF CALL STACK ==============================

def func_a():
    print("Inside func_a")
    func_b()
    print("Exiting func_a")

def func_b():
    print("Inside func_b")
    func_c()
    print("Exiting func_b")

def func_c():
    print("Inside func_c")

print("Program started")
func_a()
print("Program ended")

# ============================================================================
# Output Explanation:
#
# Step-by-step call stack behavior:
#
# 1. main() calls func_a()
#     [Call Stack: func_a()]
#
# 2. func_a() calls func_b()
#     [Call Stack: func_b(), func_a()]
#
# 3. func_b() calls func_c()
#     [Call Stack: func_c(), func_b(), func_a()]
#
# 4. func_c() finishes -> popped
#     [Call Stack: func_b(), func_a()]
#
# 5. func_b() finishes -> popped
#     [Call Stack: func_a()]
#
# 6. func_a() finishes -> popped
#     [Call Stack: empty]
#
# Program ends.
## ======================== WHAT IS CALL STACK ========================

CALL STACK – FULL NOTES
🔹 Definition

Call Stack হলো একটি data structure (Stack), যা program execution এর সময়
active (চলমান) function গুলোর information store করে।

🔹 Purpose (কাজ কী?)
কোন function এখন চলছে → track করে
function call হলে কোথায় return করবে → manage করে
program execution flow control করে
🔹 Basic Principle
 LIFO (Last In First Out)

শেষ যে function call হয় → আগে শেষ হয়
🔹 How Call Stack Works
Function call হলে → Push হয়
Function execute হয়
কাজ শেষ হলে → Pop হয়
Previous function এ control ফিরে যায়
🔹 Example
def a():
    print("A start")
    b()
    print("A end")

def b():
    print("B start")
    c()
    print("B end")

def c():
    print("C running")

a()
🔹 Execution Flow
Start → a() → b() → c()
              ↓
        c() finished
              ↓
        b() finished
              ↓
        a() finished
🔹 Stack Visualization
[ a() ]
[ b() ]
[ c() ]   ← Top (last called)

Then:

[ a() ]
[ b() ]

Then:

[ a() ]

Then:

[ empty ]
🔹 Key Terms
Push → Stack এ ঢোকানো
Pop → Stack থেকে বের করা
Top → Stack এর উপরের element
🔹 Advantages
Function call manage করে
Nested function call সহজ করে
Recursion support করে
🔹 Disadvantages
বেশি recursive call হলে → memory overflow হতে পারে
Stack overflow error হতে পারে
🔹 Stack Overflow

যখন call stack limit exceed করে

Example:
def loop():
    loop()

loop()

➡ Infinite recursion → stack full → crash ❌

🔹 Real Life Example

 Plate stack:

Last plate → first remove
➡ Same as call stack
🔹 Important Points (Exam Tips)
Call Stack = execution context storage
Works on LIFO
Every function call → new stack frame
Return হলে → frame remove হয়
Recursion heavily uses call stack
One Line Summary

Call Stack হলো program এর function execution track করার system (LIFO based)

# ====================================================================


# ======================== WORKING FLOW OF CALL STACK ========================

# 1. যখন একটি ফাংশন কল করা হয়, সেটি call stack-এর উপর (top) এ push করা হয়।
# 2. যখন ঐ ফাংশনের execution শেষ হয়, সেটি call stack থেকে pop করা হয়।
# 3. এইভাবে stack সর্বদা “Last In, First Out” (LIFO) পদ্ধতিতে কাজ করে।
# 4. call stack ব্যবহারের মাধ্যমে Python জানে বর্তমানে কোন ফাংশন চলছে
#    এবং কোনটিতে ফিরে যেতে হবে যখন একটি ফাংশন শেষ হবে।

# ============================================================================


# ======================== EXAMPLE OF CALL STACK ==============================

def func_a():
    print("Inside func_a")
    func_b()
    print("Exiting func_a")

def func_b():
    print("Inside func_b")
    func_c()
    print("Exiting func_b")

def func_c():
    print("Inside func_c")

print("Program started")
func_a()
print("Program ended")

# ============================================================================
# Output Explanation:
#
# Step-by-step call stack behavior:
#
# 1. main() -> calls func_a()
#     [Call Stack: func_a()]
#
# 2. func_a() -> calls func_b()
#     [Call Stack: func_b(), func_a()]
#
# 3. func_b() -> calls func_c()
#     [Call Stack: func_c(), func_b(), func_a()]
#
# 4. func_c() finishes -> removed (popped)
#     [Call Stack: func_b(), func_a()]
#
# 5. func_b() finishes -> removed (popped)
#     [Call Stack: func_a()]
#
# 6. func_a() finishes -> removed (popped)
#     [Call Stack: empty]
#
# Program ends.
# ============================================================================


