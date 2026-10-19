from enum import StrEnum, auto
from datetime import date
from dataclasses import dataclass

@dataclass
class Project:
    name: str
    slug: str
    archived: bool = False

    def archive(self):
        self.archived = True

def is_overdue(due_date, _status):
    if due_date is None:
        return False
    if _status == "done":
        return False
    return due_date < date.today()

class TaskStatus(StrEnum):
    planned = auto()
    in_progress = "in progress"
    blocked = "blocked"
    done = "done"

for status in TaskStatus:
    print(f"Status: {status}")

print(TaskStatus.blocked)

def slugify(name: str, sep: str="-") -> str:
    cleaned = name.strip().lower()
    return cleaned.replace(" ", sep)

print(slugify("Payment APi"))

def add_tag(name, tags=None):
    if tags is None:
        tags = []
    tags.append(name)
    return tags

def build_project(name, **kwargs):
    project = { "name": name, "slug": slugify(name) }
    project.update(kwargs)
    return project

def archive_project(name, *, notify=False, force=False):
    if force:
        print(f"Force archive {name}")
    if notify:
        print(f"sent notification for {name}")

