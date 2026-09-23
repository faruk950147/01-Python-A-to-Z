class AuthSystem:

    def __init__(self):
        self.users = {
            "admin": "1234",
            "faruk": "abcd"
        }
        self.current_user = None

    def login(self):
        if self.current_user is not None:
            print("Already logged in")
            return

        username = input("Username: ")
        password = input("Password: ")

        if username in self.users and self.users[username] == password:
            self.current_user = username
            print(f"Login successful! Welcome {username}")
        else:
            print("Invalid username or password")

    def logout(self):
        if self.current_user is None:
            print("No user logged in")
        else:
            print(f"{self.current_user} logged out")
            self.current_user = None

    def dashboard(self):
        if self.current_user is None:
            print("Please login first")
        else:
            print(f"Dashboard | Logged in as: {self.current_user}")


# Program Start
auth = AuthSystem()

while True:
    print("\n--- MENU ---")
    print("1. Login")
    print("2. Dashboard")
    print("3. Logout")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        auth.login()
    elif choice == "2":
        auth.dashboard()
    elif choice == "3":
        auth.logout()
    elif choice == "4":
        print("Program closed")
        break
    else:
        print("Invalid choice")
