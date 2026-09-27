# ==========================
# Python __name__ == '__main__' – Full Guide
# ==========================

# 1 What is __name__?
# Every Python file is a module.
# Python automatically assigns a special variable called __name__ to every module.
# Its value depends on how the module is used:

# | Usage | Value of __name__ |
# |-------|-----------------|
# | Run directly (python file.py) | '__main__' |
# | Imported into another module | Module’s name (file name without .py) |

# 2 Why use if __name__ == "__main__"?
# - Run certain code only when executed directly.
# - Prevent that code from running when imported as a module.
# This makes scripts reusable and modular.

# 3 How it works
# Step 1: Python sets __name__ depending on execution.
# Step 2: Python checks if __name__ == "__main__".
# Step 3: If true → executes the block; if false → skips it.

# 4 Example 1: Run directly
# file: greet.py
def hello():
    print("Hello from function!")

if __name__ == "__main__":
    print("This code runs directly!")
    hello()

# Running: python greet.py
# Output:
# This code runs directly!
# Hello from function!

# 5 Example 2: Imported as a module
# file: main.py
# import greet

# Running: python main.py
# Output: nothing printed
# Explanation: greet.py is imported, __name__ = "greet", so if block is skipped

# 6 Example 3: Call functions after import
# file: main.py
# import greet
# greet.hello()

# Output:
# Hello from function!
# Explanation: Only the function is executed, if block skipped.

# 7 Diagram
# greet.py
#  ├─ Run directly (python greet.py)
#  │    └─ __name__ = "__main__" → if block executes
#  └─ Imported in main.py
#       └─ __name__ = "greet" → if block skipped

# 8 When to use it
# - Writing test code inside a module
# - Making a file executable & importable
# - Keeping reusable functions/classes separate from script logic
# - Preventing unwanted side effects when importing

# 9 Real-world example
# file: calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Testing calculator functions")
    print(add(5, 3))
    print(subtract(5, 3))

# Run directly → prints test outputs
# Import in another module → use add() or subtract() without printing test outputs

# Key Takeaways
# 1. __name__ tells how a module is used
# 2. '__main__' means the script is executed directly
# 3. if __name__ == "__main__" protects code from running on import
# 4. Essential for modular and reusable Python code
