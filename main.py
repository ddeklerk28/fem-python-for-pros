from enum import StrEnum, auto

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
