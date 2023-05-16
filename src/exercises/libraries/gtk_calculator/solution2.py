# type: ignore
"""
This extended version allow selection of the arithmetic operator by
radio boxes. Constructing them and tracking which is active is
somewhat messy, so we want to isolate it from the rest of the
application.

This is a nice example how a class can encapsulate a non-trivial
group of widgets, together with some functionality.
"""

import operator

import gi
gi.require_version("Gtk", "3.0")
# pylint: disable=wrong-import-position,no-member
from gi.repository import Gtk  # noqa: E402


class OperatorChoice(Gtk.VBox):
    """An operator selection box."""

    def __init__(self):
        Gtk.VBox.__init__(self)
        self.radio_funcs = {}

        radio = None  # helps RadioButton grouping below
        for op, func in zip("+-*/", [operator.add, operator.sub, operator.mul, operator.truediv]):
            radio = Gtk.RadioButton(radio, op)
            self.pack_start(radio)
            if op == "+":
                radio.set_active(True)
            self.radio_funcs[radio] = func

    def compute(self, arg1, arg2):
        for radio, func in self.radio_funcs.items():
            if radio.get_active():
                return func(arg1, arg2)
        raise ValueError("No operator chosen")

    # The app should react to change or operator, but shouldn"t know
    # the implementation details of this widget. The "elegant" way
    # would be to define and emit our own "changed" signal.
    # Quick-and-dirty way:
    def connect_changed(self, callback, *args, **kw):
        for radio in self.radio_funcs:
            radio.connect("toggled", callback, *args, **kw)


# Notice how the rest of the app is almost unchanged. Success!

w = Gtk.Window()
w.connect("delete_event", lambda *ignored: Gtk.main_quit())

horizontal_box = Gtk.HBox()
w.add(horizontal_box)

entry1 = Gtk.Entry()
operator_choice = OperatorChoice()
entry2 = Gtk.Entry()
result = Gtk.Label()
for widget in [entry1, operator_choice, entry2, Gtk.Label("="), result]:
    print(type(widget))
    horizontal_box.pack_start(widget)


def compute(*_ignored):
    """Recompute result."""
    try:
        arg1 = float(entry1.get_text())
        arg2 = float(entry2.get_text())
        result.set_text(str(arg1 + arg2))
    except ValueError:
        result.set_text("<ERROR>")


entry1.connect("changed", compute)
entry2.connect("changed", compute)
operator_choice.connect_changed(compute)

# Initialize so its immediately useful
entry1.set_text("3")
entry2.set_text("2")

w.show_all()
Gtk.main()
