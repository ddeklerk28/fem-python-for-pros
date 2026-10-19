# Refactor the task data into a Task dataclass.
# Integrate its enum status, deadline, and evaluation functions.
# Run the program with several different task scenarios.
from datetime import date
from enum import Enum
from dataclasses import dataclass

class TaskStatus(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

@dataclass
class Task:
    title: str
    description: str
    duration: int = 1
    due_date: date | None = None
    status: TaskStatus = TaskStatus.TODO

    def is_overdue(self) -> bool:
        if self.due_date is None:
            return False
        return date.today() > self.due_date

    def is_done(self) -> bool:
        return self.status == TaskStatus.DONE

    def set_status(self, new_status: TaskStatus):
        if type(new_status) is TaskStatus:
            self.status = new_status

    def get_status_description(self) -> str:
        if self.status == TaskStatus.TODO:
            return "not started"
        elif self.status == TaskStatus.IN_PROGRESS:
            return "in progress"
        else:
            return "completed"

task_a = Task(title="Task A", description="This is task A")
print(task_a.get_status_description())
task_a.set_status(TaskStatus.IN_PROGRESS)
print(task_a.get_status_description())
print(task_a.is_overdue())

task_b = Task(title="Task B", description="This is task B", due_date=date(2026, 10, 23))
print(task_b.get_status_description())
task_b.set_status(TaskStatus.IN_PROGRESS)
print(task_b.get_status_description())
task_b.set_status(TaskStatus.DONE)
print(task_b.get_status_description())
print(task_b.is_overdue())

task_c= Task(title="Task C", description="This is task C", due_date=date(2026, 10, 16))
print(task_c.get_status_description())
task_c.set_status(TaskStatus.DONE)
print(task_c.is_overdue())
