# 📝 Simple To-Do List Application
# Author: Zainab
# Description: Add, view, and delete tasks using a terminal-based menu.

tasks = []

def view_tasks():
    """Display all tasks in the list."""
    print("\n📋 Your Tasks:")
    if not tasks:
        print("❌ No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    """Add a new task to the list."""
    task = input("➕ Enter your task: ")
    tasks.append(task)
    print("✅ Task added!")

def delete_task():
    """Delete a task based on its number."""
    view_tasks()
    try:
        num = int(input("🗑️ Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"❎ Removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def menu():
    """Main menu loop for user interaction."""
    while True:
        print("\n=== 🗂️ TO-DO LIST MENU ===")
        print("1️⃣  View Tasks")
        print("2️⃣  Add Task")
        print("3️⃣  Delete Task")
        print("4️⃣  Exit")
        choice = input("👉 Choose (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 4.")

# Run the app
if __name__ == "__main__":
    menu()
