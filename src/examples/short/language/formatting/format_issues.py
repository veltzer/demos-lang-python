"""
This example explores issues that one may have with formatting.

Notes:
- if you want to write any string you like you need to use double
curly braces.

References:
http://stackoverflow.com/questions/5466451/how-can-i-print-a-literal-characters-in-python-string-and-also-use-format
"""



try:
    # noinspection PyStringFormat
    # s = """{this will not work} {0}""".format("mark")
    s = """{this will not work} {0}""".format("mark")  # noqa: F524  teaching: shows a format call with a missing argument
    print(s)
except KeyError as e:
    print(f"yes got an exception {e}")

s = """{{this will work}} {0}""".format("mark")  # noqa: UP030  teaching: demonstrating explicit positional format fields
print(s)
