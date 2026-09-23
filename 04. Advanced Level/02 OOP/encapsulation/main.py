# ====================== What is Encapsulation ======================

# Encapsulation is the process of wrapping data (variables) and methods (functions) that operate on that data into a single unit — typically a class.
# It also helps to hide the internal details of an object and protect data from being modified directly from outside the class.

class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit of {amount} successful. New balance: {self.__balance}"
        return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawal of {amount} successful. New balance: {self.__balance}"
        return "Invalid withdrawal amount."

    def get_balance(self):
        if self.__balance >= 0:
            return f"Balance: {self.__balance}"
        return "No balance found."
    
    def set_balance(self, balance):
        if balance >= 0 and isinstance(balance, (int, float)):
            self.__balance = balance
            return f"Balance updated to {self.__balance}."
        return "Balance amount is not valid allowed only int and float."
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount number: {self.account_number}\nBalance: {self.__balance}"
if __name__ == "__main__":
    account = Account("John", "123456789", 1000)
    print(account)
    print(account.get_balance())
    print(account.set_balance(2000))
    print(account.get_balance())