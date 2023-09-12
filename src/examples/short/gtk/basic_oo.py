"""
A pygtk hello world application
"""

import signal

import gi
from gi.repository import Gtk
gi.require_version("Gtk", "4.0")


class HelloWorld:
    # noinspection PyMethodMayBeStatic
    def hello(self, _widget, _data=None):
        """
        This is a callback function. The data arguments are ignored
        in this example. More on callbacks below.
        """
        print("Hello World")

    # noinspection PyMethodMayBeStatic
    # def delete_event(self, _widget, _event, _data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you dont want the window to be destroyed.
        # This is useful for popping up "are you sure you want to quit?"
        # type dialogs.
        print("delete event occurred")

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
    #     return False

    # noinspection PyMethodMayBeStatic
    def destroy(self, _widget, _data=None):
        print("destroy signal occurred")
        Gtk.main_quit()

    def __init__(self):
        """ create a new window """
        self.window = Gtk.Window()

        # When the window is given the "delete_event" signal (this is given
        # by the window manager,usually by the "close" option,or on the
        # title bar),we ask it to call the delete_event () function
        # as defined above. The data passed to the callback
        # function is NULL and is ignored in the callback function.
        # self.window.connect("delete_event", self.delete_event)

        # Here we connect the "destroy" event to a signal handler.
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)

        # Sets the border width of the window.
        # self.window.set_border_width(10)

        # Creates a new button with the label "Hello World".
        self.button = Gtk.Button()

        # When the button receives the "clicked" signal,it will call the
        # function hello() passing it None as its argument. The hello()
        # function is defined above.
        self.button.connect("clicked", self.hello, None)

        # This will cause the window to be destroyed by calling
        # gtk_widget_destroy(window) when "clicked". Again,the destroy
        # signal could come from here,or the window manager.
        # self.button.connect_object("clicked",gtk.Widget.destroy,self.window)

        # This packs the button into the window (a GTK container).
        # self.window.add(self.button)
        # self.window.add_controller(self.button)
        self.window.set_child(self.button)

        # The final step is to display this newly created widget.
        self.button.show()

        # and the window
        self.window.show()

    # noinspection PyMethodMayBeStatic
    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        Gtk.main()


# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
signal.signal(signal.SIGINT, signal.SIG_DFL)
hello = HelloWorld()
hello.main()
hello.main()
