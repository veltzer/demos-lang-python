import sys
from time import localtime

from date5 import Calendar, Date, DateException  # type: ignore

c = Calendar()
with open("calendar.txt") as f:
    events = f.readlines()
    for event in events:
        events_sp = event.split(" ")
        name = events_sp[0]
        date_values = events_sp[1].rstrip().split(".")
        if date_values[0].isdigit() and date_values[1].isdigit() and date_values[2].isdigit():
            try:
                date = Date(int(date_values[0]), int(
                    date_values[1]), int(date_values[2]))
                c.add_event(name, date)
            except DateException as e:
                sys.stderr.write(str(e))
                print(e)
        else:
            print("date must be initialized with numbers")

current_month = localtime()[1]
monthly_events = c.get_all_events_in_month(current_month)
print("Events of the month:")
for name, ev in monthly_events.items():
    print(f"{name} happened at {ev}")
