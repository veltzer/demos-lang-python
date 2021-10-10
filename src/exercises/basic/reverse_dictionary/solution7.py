"""
solution
"""

d1 = {
    'Israel': 'Jerusalem',
    'France': 'Paris',
    'Italy': 'Rome',
    'Egypt': 'Cairo',
}
d2 = {}
# pylint: disable=consider-using-dict-items,consider-iterating-dictionary
for key in d1.keys():
    d2[d1[key]] = key
print(d2)
