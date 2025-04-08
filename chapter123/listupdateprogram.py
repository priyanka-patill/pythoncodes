# Task Manager using Lists and Tuples
class TaskManager:
    def __init__(self):
        # Initialize an empty list to store tasks, where each task is represented as a tuple
        self.tasks = []

    def add_task(self, task_name, priority):
        # Add a task with the name and priority to the task list
        self.tasks.append((task_name, priority))
        print(f"Task '{task_name}' with priority '{priority}' added.")

    def remove_task(self, task_name):
        # Remove task from the task list by task name
        task_found = False
        for task in self.tasks:
            if task[0] == task_name:
                self.tasks.remove(task)
                task_found = True
                print(f"Task '{task_name}' removed.")
                break
        if not task_found:
            print(f"Task '{task_name}' not found.")

    def update_task(self, old_task_name, new_task_name, new_priority):
        # Update an existing task
        task_found = False
        for i, task in enumerate(self.tasks):
            if task[0] == old_task_name:
                self.tasks[i] = (new_task_name, new_priority)
                task_found = True
                print(f"Task '{old_task_name}' updated to '{new_task_name}' with priority '{new_priority}'.")
                break
        if not task_found:
            print(f"Task '{old_task_name}' not found.")

    def sort_tasks(self):
        # Sort tasks based on priority (lowest priority first)
        self.tasks.sort(key=lambda x: x[1])
        print("Tasks sorted by priority.")

    def show_tasks(self):
        # Display all tasks
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Task List:")
            for task in self.tasks:
                print(f"Task: {task[0]}, Priority: {task[1]}")

# Main Program to use TaskManager
def main():
    task_manager = []

    while True:
        print("\nTask Manager Options:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Sort Tasks by Priority")
        print("5. Show Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = int(input("Enter task priority (1 is highest priority): "))
            task_manager.add_task(task_name, priority)

        elif choice == "2":
            task_name = input("Enter task name to remove: ")
            task_manager.remove_task(task_name)

        elif choice == "3":
            old_task_name = input("Enter task name to update: ")
            new_task_name = input("Enter new task name: ")
            new_priority = int(input("Enter new priority: "))
            task_manager.update_task(old_task_name, new_task_name, new_priority)

        elif choice == "4":
            task_manager.sort_tasks()

        elif choice == "5":
            task_manager.show_tasks()

        elif choice == "6":
            print("Exiting Task Manager...")
            break

        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
