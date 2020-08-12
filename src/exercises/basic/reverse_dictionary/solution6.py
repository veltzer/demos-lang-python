d = {
    'Israel': 'Jerusalem',
    'France': 'Paris',
    'Italy': 'Rome',
    'Egypt': 'Cairo',
}

# Build from reverse items:
# =========================

# recall that zip(d.keys(), d.values())==d.items()
rev_d = dict(zip(d.values(), d.keys()))
print(rev_d)
