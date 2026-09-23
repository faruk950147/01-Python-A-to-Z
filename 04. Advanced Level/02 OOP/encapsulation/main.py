"""
# ====================== What is Encapsulation ======================

Encapsulation is the process of wrapping:

1. Data (variables)
2. Methods (functions)

into a single unit, usually a class.

It also helps control access to the internal data
of an object and prevents unwanted direct modification.

In Python, encapsulation is commonly implemented using:

Public members
Protected members (_variable)
Private members (__variable)


# ============================================================
# Example: Bank Account
# ============================================================

class Account:

    def __init__(self, owner, account_number, balance=0):

        # Public attributes
        self.owner = owner
        self.account_number = account_number

        # Private attribute
        self.__balance = balance

    # ========================================================
    # Deposit
    # ========================================================

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

            return (
                f"Deposit of {amount} successful. "
                f"New balance: {self.__balance}"
            )

        return "Deposit amount must be greater than 0."

    # ========================================================
    # Withdraw
    # ========================================================

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount

            return (
                f"Withdrawal of {amount} successful. "
                f"New balance: {self.__balance}"
            )

        return "Invalid withdrawal amount."

    # ========================================================
    # Getter
    # ========================================================

    def get_balance(self):
        return f"Balance: {self.__balance}"

    # ========================================================
    # Setter
    # ========================================================

    def set_balance(self, balance):

        # Check type first
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance

            return (
                f"Balance updated to {self.__balance}."
            )

        return (
            "Invalid balance. "
            "Only non-negative int or float values are allowed."
        )

    # ========================================================
    # String Representation
    # ========================================================

    def __str__(self):

        return (
            f"Account owner: {self.owner}\n"
            f"Account number: {self.account_number}\n"
            f"Balance: {self.__balance}"
        )


# ============================================================
# Object Creation
# ============================================================

if __name__ == "__main__":

    account = Account(
        "John",
        "123456789",
        1000
    )

    print(account)

    print("--------------------")

    print(account.get_balance())

    print("--------------------")

    print(account.deposit(500))

    print("--------------------")

    print(account.withdraw(300))

    print("--------------------")

    print(account.set_balance(2000))

    print("--------------------")

    print(account.get_balance())


# ====================== How Encapsulation Works ======================

The most important line is:

self.__balance = balance

Here, __balance is a private-style attribute.

Instead of directly modifying the balance from outside the class,
we use controlled methods:

account.get_balance()

account.set_balance(2000)

account.deposit(500)

account.withdraw(300)

So the class controls how the balance can be accessed or modified.


                    Account
                       |
             +---------+---------+
             |                   |
            Data              Methods
             |                   |
        __balance          deposit()
                           withdraw()
                           get_balance()
                           set_balance()


# ====================== Public, Protected and Private ======================

class Account:

    def __init__(self):

        self.owner = "John"
        self._account_type = "Savings"
        self.__balance = 1000


# ====================== 1. Public Member ======================

self.owner

Public members can be accessed directly:

account.owner

There is no special access restriction.


# ====================== 2. Protected Member ======================

self._account_type

A single underscore indicates a protected/internal-use convention.

Example:

account._account_type

Python does not actually prevent access.

It is mainly a signal to programmers:

"This member is intended for internal use."


# ====================== 3. Private Member ======================

self.__balance

A double underscore triggers name mangling.

Direct access like this:

account.__balance

will normally raise:

AttributeError

Python internally changes the name approximately to:

_Account__balance

Therefore, technically this can still access it:

account._Account__balance

So Python's __variable is not absolute security.

It is better described as a name-mangled private attribute.


# ====================== Getter and Setter ======================

A getter is a method used to read a value:

def get_balance(self):
    return self.__balance


A setter is a method used to modify a value:

def set_balance(self, balance):

    if isinstance(balance, (int, float)) and balance >= 0:
        self.__balance = balance


This allows us to validate data before changing it.

For example:

account.set_balance(2000)

is allowed.

But:

account.set_balance(-500)

is rejected.


# ====================== Why Encapsulation is Useful ======================

Encapsulation helps to:

1. Group data and methods together
2. Control access to internal data
3. Validate data before modification
4. Reduce accidental data modification
5. Hide implementation details
6. Improve code organization
7. Make classes easier to maintain


# ====================== Encapsulation Flow ======================

Outside Code

     |
     v

deposit() / withdraw() / set_balance()

     |
     v

Validation

     |
     v

__balance

     |
     v

Data Updated


Instead of:

Outside Code

     |
     v

Directly modify balance

     |
     v

Possible invalid data


# ====================== Simple Definition ======================

Encapsulation = Bundling Data + Methods
                + Controlling Access

Or simply:

Encapsulation means keeping data and the methods
that operate on that data together inside a class
while controlling how the data is accessed or modified.


# ====================== Final Example ======================

account = Account("John", "123456789", 1000)

print(account.get_balance())

# Balance: 1000

account.deposit(500)

print(account.get_balance())

# Balance: 1500

account.withdraw(300)

print(account.get_balance())

# Balance: 1200

account.set_balance(2000)

print(account.get_balance())

# Balance: 2000


# ====================== Key Point ======================

Public    → Directly accessible

Protected → _variable
            Intended for internal/subclass use
            (convention only)

Private   → __variable
            Name mangling is applied


Easy way to remember:

Encapsulation

     =

Protect and control access to data
through the class's methods.
"""