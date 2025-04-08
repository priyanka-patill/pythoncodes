# List of tasks with priority
tasks = [
    ("Task 1", 3),
    ("Task 2", 6),
    ("Task 3", 4),
    ("Task 4", 2),
    ("Task 5", 5)
]
new_task = ("Task 6", 1)

# Append the new task to the list
tasks.append(new_task)

# Remove the task
tasks.remove( ("Task 3", 4))

# Print the updated list
print("Updated list of tasks:")
for task in tasks:
        print(f"Task: {task[0]}, Priority: {task[1]}")

# Sort the tasks by priority (second element of the tuple)
sorted_tasks = sorted(tasks, key=lambda x: x[1])


#print(sorted_tasks)
for task in sorted_tasks:
        print(f"Task: {task[0]}, Priority: {task[1]}")


