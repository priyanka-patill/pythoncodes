# Define the task list
tasks = []

# Function to add a task
def add_task(description, priority):
    tasks.append((description, priority))
    print(f'Task "{description}" with priority {priority} added.')

# Function to remove a task
def remove_task(description):
    global tasks
    tasks = [task for task in tasks if task[0] != description]
    print(f'Task "{description}" removed.')

# Function to update a task
def update_task(description, new_description, new_priority):
    for i, task in enumerate(tasks):
        if task[0] == description:
            tasks[i] = (new_description, new_priority)
            print(f'Task "{description}" updated to "{new_description}" with priority {new_priority}.')
            break
    else:
        print(f'Task "{description}" not found.')

# Function to sort tasks based on priority
def sort_tasks():
    global tasks
    tasks.sort(key=lambda task: task[1])
    print('Tasks sorted by priority.')
    print (tasks)

# Function to display all tasks
def display_tasks():
    if not tasks:
        print('No tasks to display.')
    else:
        for task in tasks:
            print(f'Task: {task[0]}, Priority: {task[1]}')

def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Sort Tasks by Priority")
        print("5. Display Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = int(input("Enter task priority: "))
            add_task(description, priority)
        elif choice == '2':
            description = input("Enter task description to remove: ")
            remove_task(description)
        elif choice == '3':
            description = input("Enter task description to update: ")
            new_description = input("Enter new task description: ")
            new_priority = int(input("Enter new task priority: "))
            update_task(description, new_description, new_priority)
        elif choice == '4':
            sort_tasks()
        elif choice == '5':
            display_tasks()
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
