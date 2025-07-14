# Simple To-Do List App using File Handling

def show_menu():
    print("\n---- To-Do List Menu ----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nNo tasks found.")
    except FileNotFoundError:
        print("\nTask file not found. Starting fresh!")

def add_task():
    task = input("Enter the task to add: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Removed: {removed.strip()}")
        else:
            print("Invalid task number.")
    except (ValueError, FileNotFoundError):
        print("Error removing task.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
