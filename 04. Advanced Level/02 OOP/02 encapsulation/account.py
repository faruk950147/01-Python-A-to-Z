class Account:
    def __init__(self, owner, balance=0, password="default123"):
        self.owner = owner
        self.__balance = balance
        self.__password = password
        print(f"Account created for {self.owner} with initial balance {self.__balance}")

    # Private method (only internal use)
    def __create_password(self, new_password):
        if isinstance(new_password, str) and len(new_password) >= 6:
            self.__password = new_password
            print("Password reset successfully")
        else:
            print("Password must be a string with at least 6 characters")

    # Public method to reset password securely
    def reset_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__create_password(new_password)
        else:
            print("Incorrect old password. Cannot reset.")

    # Check password before sensitive actions
    def verify_password(self, password):
        return password == self.__password

    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to balance")
        else:
            print("Deposit amount must be positive")

    def debit(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from balance")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self, password):
        if self.verify_password(password):
            return self.__balance
        else:
            print("Wrong password! Cannot access balance.")
            return None

    def set_balance(self, balance, password):
        if not self.verify_password(password):
            print("Access denied. Wrong password.")
            return False
        if isinstance(balance, (int, float)):
            if balance >= 0:
                self.__balance = balance
                print("Balance updated successfully")
                return True
            else:
                print("Balance cannot be negative")
                return False
        else:
            print("Balance must be a number")
            return False

    def __str__(self):
        return f"Account owner: {self.owner}\nBalance: {self.__balance}"


if __name__ == "__main__":
    account = Account("John", 100, "john123")
    print(account)

    account.debit(50)
    account.credit(20)
    print(account)

    print("Balance:", account.get_balance("john123"))

    account.set_balance(300, "john123")
    print(account)

    account.reset_password("wrongpass", "newpass123")  # invalid
    account.reset_password("john123", "newpass123")    # valid

    print("Balance with old password:", account.get_balance("john123"))
    print("Balance with new password:", account.get_balance("newpass123"))
