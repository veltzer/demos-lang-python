"""
AsyncNotifier example from tutorial

See: http://github.com/seb-m/pyinotify/wiki/Tutorial
"""

# pylint: disable=deprecated-module
import asyncore

import pyinotify

folder = "/tmp"


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print(f"IN_CREATE: {event.pathname} {self}")

    def process_IN_DELETE(self, event):
        print(f"IN_DELETE: {event.pathname} {self}")


wm = pyinotify.WatchManager()  # Watch Manager
notifier = pyinotify.AsyncNotifier(wm, EventHandler())
# pylint: disable=no-member
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events
wdd = wm.add_watch(folder, mask, rec=True)
print(f"watching [{folder}] for changes...")

print("going into mainloop")
asyncore.loop()
