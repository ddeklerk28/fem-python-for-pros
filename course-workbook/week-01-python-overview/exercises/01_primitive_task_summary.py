# Build a task summary from primitive values.
# Represent a task's title, estimated hours, completion state, and optional description.
# Derive a readable summary from those values.

title = "Learn Python"
duration = 1
total_units = 100
completed_units = 10
completion_state = False
description = "Gain a thorough understanding of the python language and ecosystem"

print(f"Task: {title}")
print(f"Duration: {duration} hour(s)")
print(f"Description: {description}")
print(f"Task Completed: {completion_state}")
print(f"Progress: {(completed_units / total_units) * 100}%")