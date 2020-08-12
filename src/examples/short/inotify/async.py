"""
AsyncNotifier example from tutorial

See: http://github.com/seb-m/pyinotify/wiki/Tutorial
"""

import asyncore

import pyinotify

folder = '/tmp'


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print('IN_CREATE: {}', event.pathname, self)

    def process_IN_DELETE(self, event):
        print('IN_DELETE: {}', event.pathname, self)


wm = pyinotify.WatchManager()  # Watch Manager
notifier = pyinotify.AsyncNotifier(wm, EventHandler())
# noinspection PyUnresolvedReferences
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events
wdd = wm.add_watch(folder, mask, rec=True)
print('watching [{0}] for changes...'.format(folder))

print('going into mainloop')
asyncore.loop()
