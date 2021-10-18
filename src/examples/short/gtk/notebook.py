"""
A notebook pygtk application
"""

import signal

import gi
gi.require_version("Gtk", "3.0")
# pylint: disable=wrong-import-position
from gi.repository import Gtk  # noqa: E402


class NotebookExample:
    """
    This method rotates the position of the tabs
    """

    # noinspection PyMethodMayBeStatic
    def rotate_book(self, _button, notebook):
        notebook.set_tab_pos((notebook.get_tab_pos() + 1) % 4)

    # Add/Remove the page tabs and the borders
    def tabs_border_book(self, _button, notebook):
        tab_val = False
        button_val = False
        if not self.show_tabs:
            tab_val = True
        if not self.show_border:
            button_val = True

        notebook.set_show_tabs(tab_val)
        self.show_tabs = tab_val
        notebook.set_show_border(button_val)
        self.show_border = button_val

    # noinspection PyMethodMayBeStatic
    def remove_book(self, _button, notebook):
        """
        Remove a page from the notebook
        """
        page = notebook.get_current_page()
        notebook.remove_page(page)
        # Need to refresh the widget --
        # This forces the widget to redraw itself.
        notebook.queue_draw_area(0, 0, -1, -1)

    # noinspection PyMethodMayBeStatic
    def delete(self, _widget, _event=None):
        Gtk.main_quit()
        return False

    def add_button(self, table, name, event, p1, p2, p3, p4):
        button = Gtk.Button(name)
        button.connect("clicked", event)
        table.attach(button, p1, p2, p3, p4)
        button.show()

    def __init__(self):
        window = Gtk.Window()
        window.connect("delete_event", self.delete)
        window.set_border_width(10)

        table = Gtk.Table(3, 6, False)
        window.add(table)

        # Create a new notebook,place the position of the tabs
        notebook = Gtk.Notebook()
        # notebook.set_tab_pos(gtk.POS_TOP)
        table.attach(notebook, 0, 6, 0, 1)
        notebook.show()
        self.show_tabs = True
        self.show_border = True

        # Lets append a bunch of pages to the notebook
        for i in range(5):
            buffer_frame = f"Append Frame {i+1}"
            buffer_label = f"Page {i+1}"

            frame = Gtk.Frame()
            frame.set_border_width(10)
            frame.set_size_request(100, 75)
            frame.show()

            label = Gtk.Label(buffer_frame)
            frame.add(label)
            label.show()

            label = Gtk.Label(buffer_label)
            notebook.append_page(frame, label)

        # Now lets add a page to a specific spot
        checkbutton = Gtk.CheckButton("Check me please!")
        checkbutton.set_size_request(100, 75)
        checkbutton.show()

        label = Gtk.Label("Add page")
        notebook.insert_page(checkbutton, label, 2)

        # Now finally lets prepend pages to the notebook
        for i in range(5):
            buffer_frame = f"Prepend Frame {i+1}"
            buffer_label = f"PPage {i+1}"

            frame = Gtk.Frame()
            frame.set_border_width(10)
            frame.set_size_request(100, 75)
            frame.show()

            label = Gtk.Label(buffer_frame)
            frame.add(label)
            label.show()

            label = Gtk.Label(buffer_label)
            notebook.prepend_page(frame, label)

        # Set what page to start at (page 4)
        notebook.set_current_page(3)

        # Create a bunch of buttons
        self.add_button("close", table, self.delete, 0, 1, 1, 2)
        self.add_button("next page", table, lambda w: notebook.next_page(), 1, 2, 1, 2)
        self.add_button("prev page", table, lambda w: notebook.prev_page(), 2, 3, 1, 2)
        self.add_button("tab position", table, self.rotate_book, 3, 4, 1, 2)
        self.add_button("tabs/border on/off", table, self.tabs_border_book, 4, 5, 1, 2)
        self.add_button("remove page", table, self.remove_book, 5, 6, 1, 2)

        table.show()
        window.show()


signal.signal(signal.SIGINT, signal.SIG_DFL)
NotebookExample()
Gtk.main()
