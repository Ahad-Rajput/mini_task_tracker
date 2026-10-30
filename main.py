

def add_task():
    pass


def view_tasks():
    pass

def complete_task():
    pass

def delete_task():
    pass




while True:
    print("\n--- TASK TRACKER ---")
    print("1. Add")
    print("2. View")
    print("3. Complete")
    print("4. Delete")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid menu choice. Select 1-5.")

