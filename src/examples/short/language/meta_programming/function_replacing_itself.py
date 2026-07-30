"""
This example shows a function that replaces itself at runtime: after a few
calls, `log` swaps itself in globals() for a cheaper no-op implementation,
so the check inside it no longer runs on subsequent calls.
"""

counter = 0

def log_empty(m):
    # pylint: disable=unused-argument
    print("going through the cheap function")

def log(m):
    # pylint: disable=global-statement
    global counter
    counter = counter + 1
    if counter < 4:
        print(m)
    else:
        globals()["log"] = log_empty

for x in range(10):
    log(x)
