# =============== LEGB Rule =================
# L - Local is the first priority
# E - Enclosing is the second priority
# G - Global is the third priority
# B - Built-in is the last priority

# =============== local scope =================
# contains local names defined inside the current function

def local_scope():
    num = 10 
    # local variable because it is defined inside the function
    # access available only inside the function
    print(f"It's a local variable: {num}")

local_scope()


# =============== enclosing scope =================
# contains names defined inside any and all enclosing functions

global_num = 10   # Global variable

def enclosing_scope():
    num = 20
    print(f"It's a enclosing local variable for outer function: {num}")

    def nested_function():
        num2 = 30
        global global_num
        global_num += 30     # Modify global variable
        nonlocal num
        num += 30            # Modify enclosing variable
        print(f"It's a enclosing local variable for inner function: {num2}")
        print(f"It's a enclosing global variable for outer function: {num}")
        print(f"It's a global variable: {global_num}")

    nested_function()
    print(f"It's a enclosing global variable for outer function: {num}")
    print(f"It's a global variable: {global_num}")

enclosing_scope()



# =============== global scope =================
# contains names defined at the top level of the module
# =============== global scope =================
# contains names defined at the top level of the module

global_num = 10   # Global variable

def global_scope():
    local_num = 20
    print(f"It's a local variable: {local_num}")
    print(f"It's a global variable: {global_num}")

global_scope()


def change_global():
    global global_num     # Declare that we’ll modify the global variable
    global_num += 30
    local_num = 990
    print(f"It's a local variable: {local_num}")
    print(f"It's a global variable: {global_num}")

change_global()

print(f"It's a global variable: {global_num}")

# =============== built-in scope =================
# contains names preassigned by the interpreter
def built_in_scope():
    print(f"It's a built-in variable: {dir()}")

built_in_scope()



