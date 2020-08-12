"""
This example shows how to remove the last character from a string

Here are the WRONG answers:
- s.strip() - removes whitespace from the beginning of the string too
- s.rstrip() - removes tabs and whitespace from the end of the string, not just newline
- s.rstrip("\n") - removes multiple newlines from the end of the string and does not handle windows
    style newlines.
- s.rstrip("\r\n") - removes multiple newlines and carriage returns from the end of the string

The right solution? write your own function as below...

References:
- http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python
"""


def chomp(x):
    if x.endswith("\r\n"):
        return x[:-2]
    if x.endswith("\n"):
        return x[:-1]
    return x


s = "hello\n\n\t\n"

print("s.strip() is [{}]".format(s.rstrip()))
print("s.strip('\\n') is [{}]".format(s.rstrip("\n")))
print("chomp(s) is [{}]".format(chomp(s)))
