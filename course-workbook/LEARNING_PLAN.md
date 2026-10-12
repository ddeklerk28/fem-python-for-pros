# Python Learning Curriculum

## 1. Purpose

Develop a deep, practical understanding of Python by focusing on demonstrable engineering outcomes rather than memorizing syntax or rushing through course material.

The goal is to become proficient at reasoning about Python, solving problems independently, and making informed implementation decisions.

**Primary course:** [Master.dev — Pro Python](https://master.dev/courses/pro-python/)

**Curriculum:** [Python Fundamentals 1](https://python-pros.netlify.app/chapters/01-python-fundamentals-1/)

## 2. Learning Principles

1. **Outcome-based learning:** Every week has a tangible deliverable and measurable learning outcomes.
2. **Progressive complexity:** Each exercise builds on previously learned concepts.
3. **Depth over speed:** Progress depends on demonstrated understanding, not video completion.
4. **Independent practice:** Attempt exercises before consulting solutions.
5. **Conceptual understanding:** Explain why code behaves as it does, not merely how to write it.
6. **Scope discipline:** Exercises must use concepts introduced so far. Future concepts may be identified but should not be implemented prematurely.
7. **Practical evidence:** Every exercise produces working code that can be run, inspected, modified, and committed.
8. **Deliberate reflection:** Misconceptions, questions, and discoveries are recorded for future reference.

## 3. Weekly Schedule

**Monday–Friday: 1 hour per day**

- 30 minutes: Learn and investigate.
- 30 minutes: Implement and experiment.

The learning block includes watching relevant videos, investigating examples, predicting behavior, and recording questions.

The practice block focuses on independently implementing the day's outcome.

**Sunday: Weekly review and planning**

- Assess the week's learning outcomes.
- Identify misconceptions and remaining uncertainties.
- Test whether concepts can be applied to unfamiliar examples.
- Decide whether additional practice is necessary.
- Define the next week's objective and daily exercises.

Do not advance simply because a week has ended. Adjust the plan according to demonstrated understanding.

## 4. Standard Practice Cycle

Every exercise follows this cycle:

1. **Predict:** Explain what the code should do before running it.
2. **Implement:** Write the simplest solution using the concepts currently available.
3. **Run:** Execute the program and compare actual behavior with the prediction.
4. **Break:** Change inputs, explore edge cases, or investigate unexpected behavior.
5. **Explain:** Articulate the underlying mechanics and justify implementation decisions.
6. **Commit:** Save the completed outcome using an outcome-focused commit message.

## 5. Repository Conventions

Each week follows the same structure:

```text
python-learning/
├── LEARNING_PLAN.md
└── week-NN-topic/
    ├── README.md
    ├── exercises/
    │   ├── 01_first_outcome.py
    │   └── 02_second_outcome.py
    └── notes/
        ├── concepts.md
        ├── questions.md
        └── weekly-review.md
```

### Responsibilities

- `LEARNING_PLAN.md`: Overall learning principles, curriculum progression, and current checkpoint.
- `README.md`: Weekly objective, outcomes, exercise sequence, acceptance criteria, and definition of done.
- `exercises/`: Numbered implementations demonstrating individual outcomes.
- `concepts.md`: Explanations of concepts and important discoveries.
- `questions.md`: Unresolved questions and topics to investigate.
- `weekly-review.md`: Assessment, reflections, and decisions for the following week.

### Commit convention

Use descriptive, outcome-focused commit messages.

Example:

`week-01: add primitive task summary`

Exercise numbering represents the learning sequence, not difficulty.

## 6. Review Standards

Feedback should distinguish between three categories:

- **Required:** Necessary to meet the current exercise's stated outcome.
- **Observation:** A useful behavior, limitation, or edge case worth understanding.
- **Out of scope:** A concept or improvement that should wait until the relevant material has been introduced.

Do not introduce unnecessary abstractions, dependencies, or advanced techniques merely to polish an exercise.

Correctness matters, but so does the ability to explain the implementation independently.

## 7. Current Curriculum — Week 01

**Topic:** Python Overview / Python Fundamentals 1

**Weekly outcome:** Build a runnable task status and deadline evaluator by progressively applying Python's fundamental language constructs.

| Day | Topic | Exercise |
|---|---|---|
| Monday | Variables, primitive values, expressions, f-strings | `01_primitive_task_summary.py` |
| Tuesday | Types, conversions, and imports | `02_task_deadline.py` |
| Wednesday | Enums and task status | `03_task_status.py` |
| Thursday | Functions, type hints, and conditionals | `04_task_evaluation.py` |
| Friday | Classes, dataclasses, and integration | `05_task_evaluator.py` |

These are planned learning stages, not mandatory deadlines. The sequence can be adjusted based on the week's progress.

## 8. Progress Tracking

Maintain an explicit distinction between:

- **Planned:** The outcome has been defined.
- **In progress:** Learning or implementation is underway.
- **Completed:** A working implementation exists.
- **Demonstrated:** The outcome can be explained and applied independently.

Completion of an exercise does not automatically establish mastery.

## 9. Current Checkpoint

**Week 01 — Day 01: Completed**

Exercise: `01_primitive_task_summary.py`

Implemented concepts:

- Assigning primitive values to names.
- Using names in expressions and f-strings.
- Calculating a derived percentage.
- Representing task properties using strings, numbers, and a boolean.

Demonstrated understanding:

- Names bind to objects.
- Reassignment changes a name's binding.
- Multiple names can refer to the same mutable object.
- Mutation and reassignment are different operations.
- Integers are immutable; lists are mutable.
- List `.copy()` creates a shallow copy, not a deep copy.

Important learning decision:

Keep each exercise within the concepts introduced so far. For example, do not introduce branching merely to improve singular/plural formatting during the primitive-values exercise.

**Next session:** Week 01, Day 02 — Types and imports.

## 10. Sunday Review Template

At the end of each week, answer:

1. What can I now implement independently?
2. Which concepts can I explain confidently?
3. Which misconceptions did I discover?
4. Where did my predictions differ from actual behavior?
5. What remains unclear?
6. Can I apply the concepts to an unfamiliar problem?
7. Should I advance, consolidate, or repeat an exercise?
8. What is the primary outcome for next week?
