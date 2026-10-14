# Introduce task statuses such as TODO, IN_PROGRESS, and DONE.
#  Update the summary to display the status meaningfully and distinguish completed tasks from incomplete ones.
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
due_date = date(2026, 10, 23)

print(f"Task: {title}")
print(f"Duration: {duration} hour(s)")
print(f"Description: {description}")
print(f"The task is: {status.value}")
print(f"Task Completed: {status == TaskStatus.DONE}")
print(f"Progress: {(completed_units / total_units) * 100}%")
print(f"Task is overdue: {date.today() >= due_date}")
