import gi
# pylint: disable=wrong-import-position
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # noqa: E402

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)  # type: ignore[attr-defined]
win.show()
Gtk.main()  # type: ignore[attr-defined]
