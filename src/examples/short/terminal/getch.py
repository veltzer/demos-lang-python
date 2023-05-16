"""
This example shows how to read just one character from the keyboard in python

References:
- http://stackoverflow.com/questions/27750536/python-input-single-character-without-enter
"""

import sys
import termios
import tty


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


print("press 6 to end")
while True:
    c = getch()
    print(c, end="")
    sys.stdout.flush()
    if c == "6":
        break
