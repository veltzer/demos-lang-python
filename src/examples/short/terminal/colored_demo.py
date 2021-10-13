"""
This example shows how to do colors at the terminal in python.

References:
- http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
"""

import colored


print(colored.stylize('hello', colored.fg('red')), colored.stylize('world', colored.fg('green')))
print(colored.stylize("warning", colored.fg('red') + colored.attr('bold')))
