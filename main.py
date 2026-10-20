task = {
    "age": 37,
    "first_name": "Dirk",
    "last_name": "de Klerk"
}

tasks = [
    {"title": "Learn Python", "status": "DONE"},
    {"title": "Review exercises", "status": "TODO"},
    {"title": "Practice", "status": "DONE"},
]

for index, task in enumerate(tasks, start=1):
    if task["status"] == "TODO":
        print(index, task["title"])