"""
This example shows how to do colors at the terminal in python.

References:
- http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
"""

from termcolor import colored

print(colored('hello', 'red'), colored('world', 'green'))
