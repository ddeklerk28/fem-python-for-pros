"""
Practice iterating through a collection of tasks.
Given a collection of tasks,
print a useful summary and find tasks matching a simple condition.
Try iterating over a dictionary in more than one way.
"""

tasks = [
    {"title": "Review Python notes", "status": "DONE"},
    {"title": "Practice dictionaries", "status": "IN_PROGRESS"},
    {"title": "Write a collection report", "status": "TODO"},
]

def create_task_report(task):
    return f"{task["title"]!r} is in status: {task["status"]!r}"

# TODO: Print a readable summary of every task.
for task in tasks:
    print(create_task_report(task))

# TODO: Find and report tasks with a selected status.
def find_task_by(tasks, status: str):
    print(f"finding task in status type {status!r}")
    for task in tasks:
        if task["status"] == status:
            print(create_task_report(task))

find_task_by(tasks, 'IN_PROGRESS')
find_task_by(tasks, 'DONE')
find_task_by(tasks, 'TODO')

# TODO: Try iterating through a dictionary's keys, values, and items.
first_task = tasks[0]

for key in first_task:
    print(key)

for value in first_task.values():
    print(value)

for key, value in first_task.items():
    print(f"({key!r}: {value!r})")
# TODO: Predict the output before running the script.
