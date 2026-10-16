# Extract the task's overdue calculation and status description into functions.
# Add rules for completed tasks, tasks with no deadline, and tasks whose deadline has passed.
from datetime import date
from enum import Enum

class TaskStatus(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

title = "Learn Python"
duration = 1
total_units = 100
completed_units = 10
status = TaskStatus.IN_PROGRESS
description = "Gain a thorough understanding of the python language and ecosystem"
due_date = date(2026, 10, 16)

def is_overdue(_due_date: date | None) -> bool:
    if _due_date is None:
        return False
    return date.today() > _due_date

def is_done(_status: TaskStatus) -> bool:
    return _status == TaskStatus.DONE

def calculate_progress(_completed_units: int, _total_units: int) -> float:
    return (_completed_units / _total_units) * 100

def get_status_description(_status: TaskStatus) -> str:
    if _status == TaskStatus.TODO:
        return "not started"
    elif _status == TaskStatus.IN_PROGRESS:
        return "in progress"
    else:
        return "completed"

print(f"Task: {title}")
print(f"Duration: {duration} hour(s)")
print(f"Description: {description}")
print(f"Progress: {calculate_progress(completed_units, total_units)}%")
print(f"Task Status: {get_status_description(status)}")
if status == TaskStatus.DONE:
    print("Task is completed")
elif due_date is None:
    print("Task has no deadline")
else:
    print(f"Task is overdue: {is_overdue(due_date)}")
