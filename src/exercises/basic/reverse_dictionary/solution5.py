"""
Solution for the reversed dict exercise using dictionary comprehensions...
"""

orig = {'Israel': 'Jerusalem', 'France':
    'Paris', 'Italy': 'Rome', 'Egypt': 'Cairo'}
rev = {v: k for k, v in orig.items()}
print(rev)
