def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks(tasks)  # Display tasks to the user
    task_index = int(input("Enter the number of the task to mark as done: ")) - 1

    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task marked as done successfully!")
    else:
        print("Invalid task number. Please try again.")


tasks = []

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_task_done(tasks)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")