"""
solution
"""

my_hash = {
    "Israel": "Jerusalem",
    "France": "Paris",
    "Italy": "Rome",
    "Egypt": "Cairo",
}

# recall that zip(my_hash.keys(), my_hash.values())==my_hash.items()
rev_d = dict(zip(my_hash.values(), my_hash.keys()))
print(rev_d)
