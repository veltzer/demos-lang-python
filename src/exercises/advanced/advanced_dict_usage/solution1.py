places = {
    'Shire': {'leave': 'Bree', 'stay': 'DEATH'},
    'DEATH': {},
    'Bree': {'with Strider': 'Rivendell', 'alone': 'DEATH'},
    'Rivendell': {'over mountains': 'DEATH', 'through Moria': 'Lorien'},
    'Lorien': {'down Anduin': 'Falls of Rauros'},
    'Falls of Rauros': {'down Anduin': 'Minas Tirith',
                        'east': 'Ithilien'},
    'Ithilien': {'south': 'Black Gate'},
    'Black Gate': {'in': 'DEATH', 'follow Gollum': 'Minas Morgul'},
    'Minas Morgul': {'road': 'DEATH', 'tunnel': 'Mordor'},
    'Mordor': {'eagles': 'Minas Tirith'},
    'Minas Tirith': {'return home': 'Shire (tired)'},
    'Shire (tired)': {'stay': 'Shire (tired)', 'retire': 'the West'},
    'the West': {}
}

place = 'Shire'
while True:
    print(f"You are in: {place}. Possible actions:")
    # Print actions with numbers, so user only has to type a number
    actions = sorted(places[place].keys()) + ['EXIT GAME']
    for i, action in enumerate(actions):
        print(f" ({i}) {action}")
    choice = input('Your action? ')
    if choice.isdigit() and 0 <= int(choice) < len(actions):
        action = actions[int(choice)]
        if action == 'EXIT GAME':
            break
        place = places[place][action]
