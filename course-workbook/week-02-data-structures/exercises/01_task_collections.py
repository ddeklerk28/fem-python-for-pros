"""Explore tuples, sets, and dictionaries with task-related data."""

# TODO: Represent a task's fixed fields using a tuple.
tuple_task = ("Learn Python", 2, "IN_PROGRESS")
print(tuple_task[0], tuple_task[1], tuple_task[2])

# TODO: Represent a collection of unique task statuses using a set.
set_task = {"TODO", "IN_PROGRESS", "DONE"}
print(set_task)

# TODO: Represent one task using a dictionary with named keys.
dict_task = {
    "title": "Learn Python",
    "estimated_hours": 2,
    "status": "IN_PROGRESS"
}
print(dict_task["title"])

# TODO: Try repeated values and a missing dictionary key.
# Missing Dictionary key:
print(dict_task["dob"]) # raises KeyError: 'dob'
print(dict_task.get("dob")) # returns None

# Repeated Values in a set:
repeated_set_task = {"Learn Python", 2, "IN_PROGRESS", "IN_PROGRESS"}
print(repeated_set_task) # {"Learn Python", 2, "IN_PROGRESS"}

# TODO: Explain which structure is appropriate for each purpose.
'''
list: would be appropriate if we need to store collections of objects/primitives of the same type, and we need it to be mutable.
tuple: appropriate for immutable collections that have different typed elements, and your require indexed access. Perhaps for example 
       a coordinate, vector etc.
set: if we need a collection of unique elements, let's say for example cast votes, we don't want votes to be counted twice.
dictionary: the best choice to model most data types, since it's keyed and mutable
'''
