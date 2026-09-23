import sqlite3
import hashlib


class AuthSystem:

    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.current_user = None
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        self.conn.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self):
        username = input("New Username: ")
        password = input("New Password: ")

        hashed_password = self.hash_password(password)

        try:
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            self.conn.commit()
            print("Registration successful")
        except sqlite3.IntegrityError:
            print("Username already exists")

    def login(self):
        if self.current_user is not None:
            print("Already logged in")
            return

        username = input("Username: ")
        password = input("Password ")

        hashed_password = self.hash_password(password)

        self.cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, hashed_password)
        )

        user = self.cursor.fetchone()

        if user:
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
    print("1. Register")
    print("2. Login")
    print("3. Dashboard")
    print("4. Logout")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        auth.register()
    elif choice == "2":
        auth.login()
    elif choice == "3":
        auth.dashboard()
    elif choice == "4":
        auth.logout()
    elif choice == "5":
        print("Program closed")
        break
    else:
        print("Invalid choice")
