
import json

FILE_NAME = "tasks.json"


def load_tasks():
    """Load saved tasks from the JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            print("Invalid task file. Starting with an empty list.")
            return []

        return tasks

    except FileNotFoundError:
        return []

    except (json.JSONDecodeError, UnicodeDecodeError):
        print("Task file is invalid. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save all tasks to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Add a new pending task."""
    title = input("Task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- YOUR TASKS ---")

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def complete_task(tasks):
    """Mark a selected task as complete."""
    if not tasks:
        print("No tasks available to complete.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Task number: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        if tasks[number - 1]["done"]:
            print("This task is already completed.")
            return

        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task completed.")

    except ValueError:
        print("Please enter a valid whole number.")


def delete_task(tasks):
    """Delete a selected task."""
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed_task['title']}")

    except ValueError:
        print("Please enter a valid whole number.")


# Run the menu-based task tracker.
tasks = load_tasks()

while True:
    print("\n--- TASK TRACKER ---")
    print("1. Add")
    print("2. View")
    print("3. Complete")
    print("4. Delete")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        complete_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
            print("Invalid menu choice. Select 1-5.")

