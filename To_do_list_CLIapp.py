# A simple To-Do List app using Python (CLI based)
# This program allows users to add, view, and remove tasks from a list

# Let's start by defining an empty list to hold our tasks
todo_list = []

def show_menu():
    print("\n====== To-Do List Menu ======")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    # If the list is empty, let the user know
    if not todo_list:
        print("\n✅ Your to-do list is empty!")
    else:
        print("\n📋 Here are your tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("📝 Enter the task you want to add: ")
    todo_list.append(task)
    print(f"✅ Task '{task}' added successfully!")

def remove_task():
    view_tasks()  # Show current tasks so user can choose
    try:
        task_number = int(input("❌ Enter the task number to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed = todo_list.pop(task_number - 1)
            print(f"🗑️ Task '{removed}' removed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Main loop that keeps the app running until the user chooses to exit
while True:
    show_menu()
    choice = input("👉 Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("👋 Exiting the To-Do List app. Have a great day!")
        break
    else:
        print("⚠️ Invalid option. Please choose between 1 and 4.")
