"""
An example of how to build a quit command in cmd2.
The idea is just to "return True" from the command.

Note that the 'do_quit' function still needs to get
the argument 'arg' as it is called with two arguments
(self and arg).

References:
- https://stackoverflow.com/questions/15537427/how-to-exit-the-cmd-loop-of-cmd-module-cleanly
"""

from cmd2 import Cmd


class CmdLineApp(Cmd):
    def __init__(self):
        Cmd.__init__(self, use_ipython=False)

    def do_quit(self, arg):
        """ quit the app """
        return True


if __name__ == '__main__':
    c = CmdLineApp()
    c.cmdloop()
