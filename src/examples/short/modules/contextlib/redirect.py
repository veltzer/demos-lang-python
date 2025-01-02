from contextlib import redirect_stdout, redirect_stderr
import sys
from io import StringIO


def function_with_outputs():
    # Regular print goes to stdout
    print("This is printed to stdout")

    # Write to stderr
    print("This is an error message", file=sys.stderr)


# Create string buffers to capture output
stdout_buffer = StringIO()
stderr_buffer = StringIO()

# Demonstrate capturing both outputs
with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
    function_with_outputs()

print("Captured stdout:")
print(stdout_buffer.getvalue())
print("Captured stderr:")
print(stderr_buffer.getvalue())

# You can also capture them separately
print("Capturing only stdout:")
stdout_buffer = StringIO()
with redirect_stdout(stdout_buffer):
    function_with_outputs()  # stderr will still go to terminal
print("Captured stdout only:")
print(stdout_buffer.getvalue())
