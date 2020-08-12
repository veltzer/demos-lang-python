"""
A basic glade based python project.
"""

import gtk


class HelloWorldGTK:
    """This is a Hello World GTK/Glade application"""

    def __init__(self):
        self.glade_file = 'project.glade'
        self.glade = gtk.Builder()
        self.glade.add_from_file(self.glade_file)
        self.glade.connect_signals(self)
        '''
        the name 'MainWindow' matches the name of the main window widget
        in the glade XML file
        '''
        self.glade.get_object('MainWindow').show_all()

    ''' the name of this method matches the event handler in the glade xml file '''

    # noinspection PyMethodMayBeStatic
    def delete_event(self, *args):
        gtk.main_quit(*args)


"""
The try/except is needed so that if you CTRL+C the application you will not get an exception
with stack trace
"""
try:
    app = HelloWorldGTK()
    gtk.main()
except KeyboardInterrupt:
    pass
