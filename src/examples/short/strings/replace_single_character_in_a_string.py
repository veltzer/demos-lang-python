"""
These are examples of replacing a character or characters in strings.
"""

from string import maketrans

s = 'a.b.c'
result = "a-b-c"

s1 = '-'.join(s.split('.'))
assert s1 == result

s2 = s.replace('.', '-')
assert s2 == result

s3 = s.translate(maketrans(".", "-"))
assert s3 == result
