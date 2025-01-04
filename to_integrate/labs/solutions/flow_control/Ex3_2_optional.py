#! /usr/local/bin/python
# Note: You will have to execute this program in a windows console to test the
# getpass functionality.

import sys
import getpass

PIN = '0138'
LIMIT = 4

for tries in range(1, LIMIT):
    supplied_pin = getpass.getpass('Enter your PIN: ')
    if supplied_pin == PIN:
        print('Well done, you remembered it!')
        print('... and after only', tries, 'attempts')
        break

# Note the else: is on the for, not the if!
else:
    print('You had', tries, 'tries and failed!')


