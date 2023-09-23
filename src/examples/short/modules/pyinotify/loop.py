"""
This is a simple example of using pyinotify.

References:
https://github.com/seb-m/pyinotify/blob/master/python2/examples/loop.py
https://github.com/seb-m/pyinotify/wiki/List-of-Examples
"""

import pyinotify

# Instanciate a new WatchManager (will be used to store watches).
wm = pyinotify.WatchManager()
# Associate this WatchManager with a Notifier (will be used to report and
# process events).
notifier = pyinotify.Notifier(wm)
# Add a new watch on /tmp for ALL_EVENTS.
wm.add_watch("/tmp", pyinotify.ALL_EVENTS)
# Print a message to the user
print("do stuff in [{0}] and see the events here...")
# Loop forever and handle events.
notifier.loop()
