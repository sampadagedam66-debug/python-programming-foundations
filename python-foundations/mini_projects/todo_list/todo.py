"""
todo.py

Mini Project: To-Do List Manager
Covers: lists of dictionaries | loops | menu-driven program
Note: in-memory only — tasks reset each time the program is run.
"""

tasks = []  # each task: {"description": str, "done": bool}


def add_task(description):
    tasks.append({"description": description, "done": False})
    print(f"Task added: '{description}'")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet. Add one to get started!")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['description']}")


def mark_task_complete(task_number):
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return
    tasks[task_number - 1]["done"] = True
    print(f"Task {task_number} marked as complete.")


def delete_task(task_number):
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return
    removed_task = tasks.pop(task_number - 1)
    print(f"Deleted task: '{removed_task['description']}'")


def display_menu():
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            task_number = int(input("Enter task number to mark complete: "))
            mark_task_complete(task_number)

        elif choice == "4":
            view_tasks()
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)

        elif choice == "5":
            print("Goodbye! (Note: tasks are not saved after exit)")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
