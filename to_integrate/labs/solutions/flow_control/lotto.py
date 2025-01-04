#! /usr/bin/python
import random

# Generate seven lottery numbers
lotto = []
while len(lotto) < 7:
    if len(lotto) <= 4: num = random.randint(1, 50)
    if len(lotto) > 4:  num = random.randint(1, 12)

    # Check for duplicates.
    if num not in lotto:
        lotto.append(num)
    else:
        print('Duplicate number: ', num)

print('Lottery:', lotto[0:-2], 'Bonus numbers:', lotto[-2:])
