"""
This context manager suppresses all exceptions
"""

class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Return True to suppress any exception
        return True

# Usage
with SuppressAll():
    print("This will run")
    raise ValueError("This error will be suppressed")
    # pylint: disable=unreachable
    print("This won't run because of the exception above")

print("This will run - exception was suppressed")
