# Extend the task summary with a due date.
# Parse or construct a date, calculate whether the deadline has passed, and format a useful output.

from datetime import date

title = "Learn Python"
duration = 1
total_units = 100
completed_units = 10
completion_state = False
description = "Gain a thorough understanding of the python language and ecosystem"
due_date = date(2026, 10, 23)

print(f"Task: {title}")
print(f"Duration: {duration} hour(s)")
print(f"Description: {description}")
print(f"Task Completed: {completion_state}")
print(f"Progress: {(completed_units / total_units) * 100}%")
print(f"Task is passed due: {date.today() >= due_date}")