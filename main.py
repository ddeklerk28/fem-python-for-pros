from enum import StrEnum, auto

class TaskStatus(StrEnum):
    planned = auto()
    in_progress = "in progress"
    blocked = "blocked"
    done = "done"

for status in TaskStatus:
    print(f"Status: {status}")