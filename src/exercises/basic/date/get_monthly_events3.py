import sys
from time import localtime

from date3 import Calendar, Date  # type: ignore

filename = sys.argv[0]
c = Calendar()
with open(filename) as f:
    events = f.readlines()
    for event in events:
        events_ev = event.rstrip().split(" ")
        name = events_ev[0]
        date_values = events_ev[1].split(".")
        if date_values[0].isdigit() and date_values[1].isdigit() and date_values[2].isdigit():
            date = Date(int(date_values[0]), int(
                date_values[1]), int(date_values[2]))
            c.add_event(name, date)

current_month = localtime()[1]
monthly_events = c.get_all_events_in_month(current_month)
print("Events of the month:")
for name, e in monthly_events.items():
    print(f"{name} happened at: {e}")
