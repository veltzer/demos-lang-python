import gi

gi.require_version('Gtk', '3.0')
# noinspection PyPep8
import gi.repository.Gtk

win = gi.repository.Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show()
Gtk.main()
