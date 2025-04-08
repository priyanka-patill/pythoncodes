# List of tasks with priority
tasks = [
    ("Task 1", 3),
    ("Task 2", 1),
    ("Task 3", 4),
    ("Task 4", 2),
    ("Task 5", 5)
]

# Sort the tasks by priority (second element of the tuple)
sorted_tasks = sorted(tasks, key=lambda x: x[1])

# Print sorted tasks
print("Sorted tasks by priority:")
for task in sorted_tasks:
    print(f"Task: {task[0]}, Priority: {task[1]}") 
