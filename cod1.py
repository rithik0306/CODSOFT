def add_task(tasks, description):
    """Add a task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✘"
            print(f"{idx}. [{status}] {task['description']}")

def update_task(tasks, task_number, new_description):
    """Update the description of a task."""
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['description'] = new_description
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_number):
    """Delete a task from the list."""
    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted.")
    else:
        print("Invalid task number.")

def toggle_completion(tasks, task_number):
    """Toggle the completion status of a task."""
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = not tasks[task_number - 1]['completed']
        print("Task completion toggled.")
    else:
        print("Invalid task number.")

def main():
    # Initialize an empty list of tasks
    tasks = []

    # Main loop
    while True:
        # Display the menu
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Task Completion")
        print("6. Exit")

        # Get user's choice
        choice = input("Enter your choice: ")

        # Execute the corresponding action
        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            new_description = input("Enter new description: ")
            update_task(tasks, task_number, new_description)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == '5':
            task_number = int(input("Enter task number to toggle completion: "))
            toggle_completion(tasks, task_number)
        elif choice == '6':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()
