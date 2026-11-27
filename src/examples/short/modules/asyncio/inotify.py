"""
This is an example of integrating pyinotify with asyncio

Notes:
- this is a python3 example since python2 does not have "asyncio".

References:
http://stackoverflow.com/questions/26414052/watch-for-a-file-with-asyncio
"""

import asyncio
from typing import Any

import pyinotify


class AsyncioNotifier(pyinotify.Notifier):
    """
    Notifier subclass that plugs into the asyncio event loop.
    """

    def __init__(self, watch_manager: Any, loop: Any, callback: Any = None,
                 default_proc_fun: Any = None, read_freq: int = 0, threshold: int = 0, timeout: Any = None) -> None:
        self.loop = loop
        self.handle_read_callback = callback
        pyinotify.Notifier.__init__(
            self, watch_manager, default_proc_fun, read_freq, threshold, timeout)
        loop.add_reader(self._fd, self.handle_read)

    def handle_read(self) -> None:
        self.read_events()
        self.process_events()
        if self.handle_read_callback is not None:
            self.handle_read_callback(self)


class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, loop: Any = None) -> None:
        super().__init__()
        self.loop = loop

    def process_IN_CREATE(self, event: Any) -> None:
        print("Creating:", event.pathname)


main_loop = asyncio.get_event_loop()

# set up pyinotify stuff
wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE

folder = "/tmp"
wm.add_watch(folder, mask)
handler = EventHandler(loop=main_loop)
notifier = pyinotify.AsyncioNotifier(wm, main_loop, default_proc_fun=handler)

main_loop.run_forever()
