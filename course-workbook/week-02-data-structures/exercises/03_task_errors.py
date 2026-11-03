"""Practice handling expected errors while working with task data."""

task = {"title": "Practice exceptions", "estimated_hours": "2"}

class NegativeValueError(Exception):
    pass

def calculate_total_time(extra_hours: int, estimated_hours: int):
    if extra_hours < 0:
        raise NegativeValueError("cannot provide negative extra hours")

    return extra_hours + estimated_hours

# TODO: Read the title and estimated_hours.
try:
    title = task["title"]
    # TODO: Convert estimated_hours to an integer.
    hours = int(task["estimated_hours"])
    total_time = calculate_total_time(2, hours)

    print(f"Title: {title}")
    print(f"Estimated Hours: {hours}")
    print(f"Total Time: {total_time}")


# TODO: Handle the specific error that occurs for the current value.
except ValueError:
    print("estimated_hours needs to be a numeral representation")

except NegativeValueError as neg_value_error:
    print(neg_value_error)

except KeyError as keyError:
    print(f"{keyError} is not a valid dictionary key")

# TODO: Change the value to a valid one and verify the success path.
# TODO: Explain why the exception occurs and where it is handled.
# ANSWER: When estimated hours is the word two instead of of a numerical string,
# the cast cannot be performed and the int function raises the ValueError.
# the except ValueError clause catches this error and and provides the user with a
# description as to why something went wrong

# if an invalid key was provided, it would be raised during the dictionary reads, and it again would be caught by the
# KeyError clause
