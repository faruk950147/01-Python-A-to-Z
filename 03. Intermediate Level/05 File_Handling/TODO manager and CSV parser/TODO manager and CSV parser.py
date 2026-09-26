# ======================== TODO manager ========================
# TODO manager is a program that allows you to manage your TODO list


import csv
import os

TODO_FILE = "todos.csv"

# -----------------------------
# TODO MANAGER FUNCTIONS
# -----------------------------
def load_tasks():
    """Load all tasks from CSV"""
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            tasks = list(reader)
    return tasks


def save_tasks(tasks):
    """Save tasks to CSV"""
    with open(TODO_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(tasks)


def add_task(task):
    """Add a new task"""
    tasks = load_tasks()
    tasks.append([task])
    save_tasks(tasks)
    print(f"Task added: {task}")


def view_tasks():
    """View all tasks"""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour TODO list:")
    for i, (task,) in enumerate(tasks, 1):
        print(f"{i}. {task}")


def delete_task(index):
    """Delete a task"""
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed[0]}")
    else:
        print("Invalid index!")


# -----------------------------
# CSV PARSER FUNCTIONS
# -----------------------------
def parse_csv(filename):
    """Parse a CSV file and print each row"""
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print(f"\nReading: {filename}\n")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"Error: {e}")


# -----------------------------
# MAIN MENU
# -----------------------------
def todo_menu():
    while True:
        print("\n--- TODO Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(input("Enter task: "))
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Invalid input! Enter a number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice! Try again.")


def csv_parser_menu():
    while True:
        print("\n--- CSV Parser ---")
        print("1. Parse CSV File")
        print("2. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            filename = input("Enter CSV file name: ")
            parse_csv(filename)
        elif choice == "2":
            break
        else:
            print("Invalid choice! Try again.")


def main():
    while True:
        print("\n===========================")
        print("TODO & CSV Manager   ")
        print("===========================")
        print("1. TODO Manager")
        print("2. CSV Parser")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            todo_menu()
        elif choice == "2":
            csv_parser_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
