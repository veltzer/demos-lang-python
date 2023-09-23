"""
This is an example of how to convert numbers with commans to ints or floats using
the "locale" module.


References:
- http://stackoverflow.com/questions/6633523/how-can-i-convert-a-string-with-dot-and-comma-into-a-float-number-in-python
- http://stackoverflow.com/questions/1779288/
    how-do-i-use-python-to-convert-a-string-to-a-number-if-it-has-commas-in-it-as-th
"""

import locale

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
print(locale.atoi("1,000,000"))
print(locale.atof("1,000,000.53"))
