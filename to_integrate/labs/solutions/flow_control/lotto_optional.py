#! /usr/bin/python
import random

lines = int(input('Enter number of lines: '))

for line in range(0, lines):
    # Generate seven new lottery numbers.
    lotto = []
    while len(lotto) < 7:
        if len(lotto) <= 4: num = random.randint(1, 50)
        if len(lotto) > 4:  num = random.randint(1, 12)

        # Check for duplicates.
        if num not in lotto: lotto.append(num)

    print('Lottery:', lotto[0:-2], 'Bonus numbers:', lotto[-2:])
else:
    print('Good luck and remember your instructor if you win!')

