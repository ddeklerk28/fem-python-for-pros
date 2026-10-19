# Week 01 — Python Overview

## Objective

Develop a foundational mental model of Python by applying its core language constructs to a small, practical problem.

The focus is on understanding Python's execution model, working with its standard library, expressing business rules, and modelling domain concepts — not memorising syntax.

## Weekly Outcome

Build a task status evaluator that represents a task, evaluates its deadline and completion status, and produces a readable summary.

By the end of this week, I should be able to implement and explain the solution independently, using the concepts covered in the Python Overview section of the Pro Python course.

## Learning Resources

- [Pro Python — Course](https://master.dev/courses/pro-python/)
- [Python Fundamentals 1 — Curriculum](https://python-pros.netlify.app/chapters/01-python-fundamentals-1/)

## Daily Schedule

| Day | Focus | Exercise |
|---|---|---|
| Monday | Variables and expressions | `01_primitive_task_summary.py` |
| Tuesday | Types and imports | `02_task_deadline.py` |
| Wednesday | Enums | `03_task_status.py` |
| Thursday | Functions and conditionals | `04_task_evaluation.py` |
| Friday | Classes and dataclasses | `05_task_evaluator.py` |

Daily time allocation: 30 minutes learning and 30 minutes deliberate practice.

## Learning Outcomes

By the end of the week, I should be able to:

- [X] Explain how Python names, objects, assignments, and expressions behave.
- [X] Work with primitive values and understand runtime types.
- [X] Import and use relevant standard-library functionality.
- [X] Represent a fixed set of states using an enum.
- [X] Write functions with explicit inputs, outputs, and type hints.
- [X] Express business rules using conditionals and boolean logic.
- [X] Model related data using a dataclass and justify the design choice.
- [X] Run Python scripts, investigate tracebacks, and debug basic errors.
- [ ] Integrate the concepts into a working task evaluator.

## Exercise Requirements

Each exercise should:

1. Address a specific learning outcome.
2. Be implemented independently before consulting a solution.
3. Include experiments with alternative inputs or edge cases.
4. Produce observable behaviour that can be verified.
5. Be explainable without relying on memorised syntax.

## Constraints

- Use only concepts introduced so far, unless an experiment explicitly calls for further investigation.
- Prefer the simplest implementation that satisfies the exercise.
- Avoid unnecessary dependencies and application scaffolding.
- Separate business logic from output where appropriate.
- Do not advance solely to complete the curriculum; prioritise understanding.

## Definition of Done

This week is complete when:

- [ ] All five exercises have working implementations.
- [ ] The weekly learning outcomes have been assessed honestly.
- [ ] Edge cases have been explored and the observed behaviour is understood.
- [ ] The final evaluator handles completed, overdue, upcoming, and deadline-free tasks.
- [ ] The implementation can be explained and modified independently.
- [ ] The weekly review has been completed.

## Weekly Reflection

Complete this section on Sunday.

### What I learned

- Monday (12/10/2026): Python names point to objects, assignments bind names to objects, and expressions dereferences addresses of names to produce values.
- Tuesday (13/10/2026): How dynamic types work in python and how to convert to different types. How to import modules and classes from modules.
- Wednesday (14/10/2026): The enum class exposes various types of enums. The difference between the type of the enum and the name, value of it\'s members. The difference between Enum and StrEnum
- Thursday (15/10/2026): How to define functions, how to use type hints, how to use conditionals and boolean logic to express business rules.
- Friday (16/10/2026): How to define classes and dataclasses, how to use them to model related data, and how to integrate the week's concepts into a working program.

### What I can now do independently

- Monday (12/10/2026): I can reason about python names, and how their assignments and expressions behave. I can distinguish this from other languages.
- Tuesday (13/10/2026): I am able to predict the values of casting operations and work with imported date class to create due dates etc.
- Wednesday (14/10/2026): I can declare enums and use them to represent a domain's state. 
- Thursday (15/10/2026): I can write functions with explicit inputs, outputs, and type hints. I can express business rules using conditionals and boolean logic.
- Friday (16/10/2026): I can create classes, and utilise dataclasses to deligate some of the boilerplate code.

### What I still find difficult

- Wednesday (14/10/2026): When to use Enum vs StrEnum
- Thursday (15/10/2026): usage of kwargs and the ** syntax

### Questions to investigate

- Tuesday (13/10/2026): When should I use `import datetime` versus `from datetime import date`, and how does each choice affect the names available in my code?
- Thursday (15/10/2026): Look into args and ** syntax and any other variants that might exist; Also look into the "*" parameter, to make sure you understand it fully

### Changes for next week

-

### Next week's objective

- 
