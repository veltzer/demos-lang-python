"""
solution
"""

# The simplest solution, iterates the keys...
d1 = {
    "Israel": "Jerusalem",
    "France": "Paris",
    "Italy": "Rome",
    "Egypt": "Cairo",
}
d2 = {}
# the next line is equivalent to: for key in d1.keys():
for key in d1:  # noqa: PLC0206  teaching: demonstrating iteration over the keys and indexing for the value
    d2[d1[key]] = key
print(d2)
