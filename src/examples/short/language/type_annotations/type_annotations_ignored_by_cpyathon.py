"""
This is an example that shows that type annotations are basically ignored by the python
runtime.

So what are type annotations for?
- for development environments to offer better auto completion and early error detectioon (red squigly-wigglie).
- for linter tools like pylint and mypy.
"""

x: int = "hello"  # type: ignore
print(x)
