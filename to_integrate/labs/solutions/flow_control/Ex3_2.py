#! /usr/local/bin/python

import sys

PIN = '0138'
LIMIT = 4

for tries in range(1, LIMIT):
    supplied_pin = input('Enter your PIN: ')
    if supplied_pin == PIN:
        print('Well done, you remembered it!')
        print('... and after only', tries, 'attempts')
        break

# Note the else: is on the for, not the if!
else:
    print('You had', tries, 'tries and failed!')


