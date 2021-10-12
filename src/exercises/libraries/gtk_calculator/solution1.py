import gi
gi.require_version('Gtk', '3.0')
# pylint: disable=wrong-import-position
from gi.repository import Gtk  # noqa: E402

w = Gtk.Window()
w.connect('delete_event', lambda *ignored: Gtk.main_quit())

horizontal_box = Gtk.HBox()
w.add(horizontal_box)

entry1 = Gtk.Entry()
entry2 = Gtk.Entry()
result = Gtk.Label()
# for widget in [entry1, Gtk.Label(label='+'), entry2, Gtk.Label(label='='), result]:
#   horizontal_box.pack_start(widget)


def compute(*_ignored):
    """Recompute result."""
    try:
        arg1 = float(entry1.get_text())
        arg2 = float(entry2.get_text())
        result.set_text(str(arg1 + arg2))
    except ValueError:
        result.set_text('<ERROR>')


entry1.connect('changed', compute)
entry2.connect('changed', compute)

# Initialize so it's immediately useful
entry1.set_text('3')
entry2.set_text('2')

w.show_all()
Gtk.main()
