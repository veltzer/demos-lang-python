"""
This is an example that shows that type annotations are basically ignored by the python
runtime.

So what are type annotations for?
- for development environments to offer better auto completion and early error detectioon (red squigly-wigglie).
- for linter tools like pylint and mypy.
"""

x: int = "hello"  # pyrefly: ignore[bad-assignment]  teaching: the wrong annotation is ignored at runtime
print(x)
