"""
A minimal gtk application demo.
"""

import sys
import signal
import gi
gi.require_version("Gtk", "4.0")
# pylint: disable=wrong-import-position
from gi.repository import Gtk


def on_activate(app):
    """ activate code """
    win = Gtk.ApplicationWindow(application=app)
    win.present()
    button = Gtk.Button()
    button.num = 0
    clicked_callback(button)
    win.set_child(button)
    button.connect("clicked", clicked_callback)
    signal.signal(signal.SIGINT, signal.SIG_DFL)


def clicked_callback(button):
    """ function to be called when the button is clicked """
    button.set_label("Hello World! " + str(button.num))
    button.num += 1


def quit_callback(_window, _event):
    """ function to be called when the application is quitted """
    Gtk.main_quit()


def main():
    """ main app code """
    app = Gtk.Application()
    app.connect('activate', on_activate)
    app.run(sys.argv)


if __name__ == "__main__":
    main()
