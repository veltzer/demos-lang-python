"""
A notebook pygtk application
"""

import signal

import gi
from gi.repository import Gtk

gi.require_version('Gtk', '3.0')


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

    def __init__(self):
        window = Gtk.Window()
        window.connect('delete_event', self.delete)
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

        # Let's append a bunch of pages to the notebook
        for i in range(5):
            buffer_frame = 'Append Frame {0}'.format(i + 1)
            buffer_label = 'Page {0}'.format(i + 1)

            frame = Gtk.Frame()
            frame.set_border_width(10)
            frame.set_size_request(100, 75)
            frame.show()

            label = Gtk.Label(buffer_frame)
            frame.add(label)
            label.show()

            label = Gtk.Label(buffer_label)
            notebook.append_page(frame, label)

        # Now let's add a page to a specific spot
        checkbutton = Gtk.CheckButton('Check me please!')
        checkbutton.set_size_request(100, 75)
        checkbutton.show()

        label = Gtk.Label('Add page')
        notebook.insert_page(checkbutton, label, 2)

        # Now finally let's prepend pages to the notebook
        for i in range(5):
            buffer_frame = 'Prepend Frame {0}'.format(i + 1)
            buffer_label = 'PPage {0}'.format(i + 1)

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
        button = Gtk.Button('close')
        button.connect('clicked', self.delete)
        table.attach(button, 0, 1, 1, 2)
        button.show()

        button = Gtk.Button('next page')
        button.connect('clicked', lambda w: notebook.next_page())
        table.attach(button, 1, 2, 1, 2)
        button.show()

        button = Gtk.Button('prev page')
        button.connect('clicked', lambda w: notebook.prev_page())
        table.attach(button, 2, 3, 1, 2)
        button.show()

        button = Gtk.Button('tab position')
        button.connect('clicked', self.rotate_book, notebook)
        table.attach(button, 3, 4, 1, 2)
        button.show()

        button = Gtk.Button('tabs/border on/off')
        button.connect('clicked', self.tabs_border_book, notebook)
        table.attach(button, 4, 5, 1, 2)
        button.show()

        button = Gtk.Button('remove page')
        button.connect('clicked', self.remove_book, notebook)
        table.attach(button, 5, 6, 1, 2)
        button.show()

        table.show()
        window.show()


signal.signal(signal.SIGINT, signal.SIG_DFL)
NotebookExample()
Gtk.main()
