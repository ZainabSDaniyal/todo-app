tasks = []

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Added: {task}")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"Deleted: {removed}")
    except (IndexError, ValueError):
        print("Invalid number!")
    
while True:
    show_menu()
    choice = input("Choose (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
