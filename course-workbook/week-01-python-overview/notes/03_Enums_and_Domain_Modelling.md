# Enums and Domain Modelling

## Learning Outcomes

Represent a fixed set of meaningful states without relying on arbitrary strings scattered throughout a program.

## Learn - 30 minutes

- Watch the Enums lesson (00:46:37–00:53:50).
- Investigate `Enum`, `StrEnum` where appropriate, and `IntEnum`.
- Consider why a status enum can be safer and clearer than raw strings.

## Practice - 30 minutes

Introduce task statuses such as `TODO`, `IN_PROGRESS`, and `DONE`. Update the summary to display the status meaningfully and distinguish completed tasks from incomplete ones.

## Acceptance Criteria

- Status is represented by an enum.
- Invalid status strings aren't silently treated as valid states.
- You can explain why a string enum differs from an ordinary string and when an enum is unnecessary.

## Scope Notes

Focus on defining and using enums. Avoid adding validation frameworks or complex status-transition rules unless those concepts have already been introduced.
