"""
a more efficient solution to the exercise since we are iterating items
and getting BOTH the key AND the value immediately without the need to preform
a second lookup...
"""

orig = {
    "Israel": "Jerusalem",
    "France": "Paris",
    "Italy": "Rome",
    "Egypt": "Cairo",
}

rev = {}
for k, v in orig.items():
    rev[v] = k
print(rev)
