"""
A minimal gtk application demo.
"""

import signal

import gi

from gi.repository import Gtk
gi.require_version("Gtk", "3.0")


def clicked_callback(button):
    button.set_label("Hello World! " + str(button.num))
    button.num += 1


def quit_callback(_window, _event):
    Gtk.main_quit()


# pylint: disable=no-member
b = Gtk.Button("Click me")  # type: ignore[arg-type]
b.num = 0  # type: ignore
b.connect("clicked", clicked_callback)  # attach it to the callback

w = Gtk.Window()  # create a new window
# put it inside the window
w.add(b)  # type: ignore[attr-defined]
w.connect("delete-event", quit_callback)
# must do this in GTK
w.show_all()  # type: ignore[attr-defined]

signal.signal(signal.SIGINT, signal.SIG_DFL)
# main loop. Will only quit if you call "gtk.main_quit()"
Gtk.main()  # type: ignore[attr-defined]
