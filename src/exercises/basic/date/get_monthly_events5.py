import sys
from time import localtime

from date import *

filename = 'c:/tmp.txt'
f = open(filename)
c = Calendar()
events = f.readlines()
for event in events:
    event = event.split(' ')
    name = event[0]
    date_values = event[1].rstrip().split('.')
    if date_values[0].isdigit() and date_values[1].isdigit() and date_values[2].isdigit():
        try:
            date = Date(int(date_values[0]), int(
                date_values[1]), int(date_values[2]))
            c.add_event(name, date)
        except DateException as e:
            sys.stderr.write(e)
            print(e)
    else:
        print('date must be initialized with numbers')

current_month = localtime()[1]
monthly_events = c.get_all_events_in_month(current_month)
print('Events of the month:')
for name in monthly_events.keys():
    print(name, ' happened at: ', monthly_events[name])
