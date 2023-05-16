"""
A basic glade based python project.
"""


import gi
gi.require_version("Gtk", "3.0")
# pylint: disable=wrong-import-position
from gi.repository import Gtk  # noqa: E402


class HelloWorldGTK:
    """This is a Hello World GTK/Glade application"""

    def __init__(self):
        self.glade_file = "project.glade"
        self.glade = Gtk.Builder()
        self.glade.add_from_file(self.glade_file)
        self.glade.connect_signals(self)
        # the name "MainWindow" matches the name of the main window widget
        # in the glade XML file
        self.glade.get_object("MainWindow").show_all()

    # the name of this method matches the event handler in the glade xml file

    # noinspection PyMethodMayBeStatic
    def delete_event(self, *args):
        Gtk.main_quit(*args)


# The try/except is needed so that if you CTRL+C the application you will not get an exception
# with stack trace
try:
    app = HelloWorldGTK()
    Gtk.main()  # type: ignore
except KeyboardInterrupt:
    pass
