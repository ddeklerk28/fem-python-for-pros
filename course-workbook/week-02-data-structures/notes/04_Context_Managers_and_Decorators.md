# Context Managers and Decorators

## Learning Outcomes

Explain the purpose of a context manager and the `with` statement, and describe at a high level how a decorator wraps or changes a function's behavior.

## Learn - 30 minutes

- Watch the Context Managers and Decorators lesson.
- Investigate how a `with` block manages a resource and why cleanup should still happen when an error occurs.
- Read a simple decorator example and trace which function is called.
- Identify decorator syntax such as `@some_decorator` without feeling obliged to write a general-purpose decorator.

## Practice - 30 minutes

Use a context manager in a small file or resource-handling example. Separately, trace a simple decorator example and explain the relationship between the decorated name and the wrapped function.

## Acceptance Criteria

- You can explain what the context manager manages and when its block exits.
- You can describe the basic purpose of a decorator.
- You can explain the observed behavior rather than only recognizing the syntax.

## Scope Notes

The goal is understanding and a small experiment, not designing a reusable decorator framework. Keep file operations small and use a clear, temporary output path if needed.