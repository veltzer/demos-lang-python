"""
This example shows that you can put characters in different languages directly in your code.
What you need to do is:
- use a unicode enabled editor that can save in an encoding different than ascii (vi can do that).
    encodings such as UTF-8 etc...
- write "u" strings when you want then unicode. This is needed in python2 but not in python3
where all strings are unicode by default.
- tell python about the encoding of your file (see the right after the shbang line).
"""

print("הי")
