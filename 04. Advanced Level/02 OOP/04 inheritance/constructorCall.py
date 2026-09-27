# ==========================================================
# =============== Constructor Call in Python ===============
# ==========================================================

# Constructor Call is a mechanism in which a constructor of 
# one class is called from another constructor of the same 
# or derived class.
#
# It can be done in two ways:
#    Manual Constructor Call (using __init__ directly)
#    Automatic Constructor Call (using super())
# ==========================================================


# =====================  __init__ Call =====================
# __init__ constructor call chain (Manual)
# Here, each parent class constructor is called manually.
# Order: Child → Parent1.__init__() → Parent2.__init__()

class Parent1:
    def __init__(self):
        print("__init__ Parent1 constructor")

class Parent2:
    def __init__(self):
        print("__init__ Parent2 constructor")

class Child(Parent1, Parent2):
    def __init__(self):
        # Manually calling both parent constructors
        Parent1.__init__(self)   # Call Parent1 constructor
        Parent2.__init__(self)   # Call Parent2 constructor
        print("__init__ Child constructor")

# ===================== Object Creation =====================
print("===== Manual Constructor Call Chain =====")
child1 = Child()

# ===================== Output =====================
# __init__ Parent1 constructor
# __init__ Parent2 constructor
# __init__ Child constructor
# ==========================================================



# ===================== super() Call =====================
# super() constructor call chain (Automatic)
# Using super(), constructors are called automatically based 
# on the MRO (Method Resolution Order).
# Order: Child → Parent1 → Parent2 → object
# Each class must use super() to maintain the chain.

class Parent1:
    def __init__(self):
        super().__init__()   # Calls next class (Parent2)
        print("__super__ Parent1 constructor")

class Parent2:
    def __init__(self):
        super().__init__()   # Calls next class (object)
        print("__super__ Parent2 constructor")

class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()   # Calls next class (Parent1)
        print("__super__ Child constructor")

# ===================== Object Creation =====================
print("\n===== super() Constructor Call Chain =====")
child2 = Child()

# ===================== Output =====================
# __super__ Parent2 constructor
# __super__ Parent1 constructor
# __super__ Child constructor
# ==========================================================


# Explanation:
# In the manual method (Parent1.__init__, Parent2.__init__), 
#     you explicitly call each parent constructor yourself.
#
# In the super() method, Python automatically follows 
#     the MRO (Method Resolution Order) chain and executes 
#     all constructors in order.
#
# MRO (Method Resolution Order):
#     Child → Parent1 → Parent2 → object
#
# super() automatically manages this sequence —
# that’s why it’s called the “Magic Chain System” 🔗✨
# ==========================================================
