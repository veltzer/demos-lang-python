"""
References:
The basic code I stole from and modified:
    https://gist.github.com/evoL/1650115
How to write a custom pygtk widget:
    http://www.pygtk.org/articles/writing-a-custom-widget-using-pygtk/writing-a-custom-widget-using-pygtk.htm
"""

import signal

import gi

from gi.repository import Gtk

gi.require_version("Gtk", "4.0")


class EntryMultiCompletion(Gtk.Entry):
    def __init__(self):
        Gtk.Entry.__init__(self)
        self.completion = Gtk.EntryCompletion()
        # customize the matching function to match multiple space
        # separated words
        self.completion.set_match_func(self.match_func, None)
        # handle the match-selected signal, raised when a completion
        # is selected from the popup
        self.completion.connect("match-selected", self.on_completion_match)
        self.set_completion(self.completion)

    def match_func(self, _completion, key_string, iterator, _data):
        model = self.completion.get_model()
        # get the completion strings
        model_str = model[iterator][0]
        # check if the user has typed in a space char,
        # get the last word and check if it matches something
        if " " in key_string:
            last_word = key_string.split()[-1]
            return model_str.startswith(last_word)
        # we have only one word typed
        return model_str.startswith(key_string)

    def on_completion_match(self, _completion, model, iterator):
        current_text = self.get_text()
        # if more than a word has been typed, we throw away the
        # last one because we want to replace it with the matching word
        # note: the user may have typed only a part of the entire word
        # and so this step is necessary
        if " " in current_text:
            current_text = " ".join(current_text.split()[:-1])
            # current_text="%s %s"%(current_text, model[iter][0])
        else:
            current_text = model[iterator][0]
        # add the matching word
        # current_text="%s %s"%(current_text, model[iter][0])
        # set back the whole text
        self.set_text(current_text)
        # move the cursor at the end
        self.set_position(-1)
        # stop the event propagation
        return True


# pylint: disable=no-member
signal.signal(signal.SIGINT, signal.SIG_DFL)
win = Gtk.Window()
# win.connect("delete-event", Gtk.main_quit)  # type: ignore[attr-defined]
entry_completion = EntryMultiCompletion()
list_store = Gtk.ListStore()
entry_completion.completion.set_model(list_store)
entry_completion.completion.set_text_column(0)
for word in ["python", "perl", "scala", "c++", "ruby", "c#", "java", "assembly", "PHP"]:
    list_store.append([word])
win.add(entry_completion)  # type: ignore[attr-defined]
win.show_all()  # type: ignore[attr-defined]

Gtk.main()  # type: ignore[attr-defined]
