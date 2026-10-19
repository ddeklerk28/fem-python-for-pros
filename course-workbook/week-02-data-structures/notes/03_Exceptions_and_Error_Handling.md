# Exceptions and Error Handling

## Learning Outcomes

Explain how exceptions affect program execution and handle a known, expected failure using a specific exception type.

## Learn - 30 minutes

- Watch the Error Handling lesson.
- Investigate the difference between an exception being raised and being caught.
- Compare a narrow `try` block with one that catches too much.
- Explore the difference between common input errors, such as `ValueError` and `KeyError`.

## Practice - 30 minutes

Write a small task-data operation that can encounter an expected invalid value or missing key. Handle that specific failure and provide a useful result or message.

## Acceptance Criteria

- The script runs for valid input.
- An expected invalid input is handled deliberately.
- You can explain which statement may raise the exception and which handler catches it.
- Unrelated programming errors are not silently swallowed.

## Scope Notes

Do not use a broad `except Exception` as a shortcut. Custom exception classes are out of scope unless the lesson explicitly requires them.