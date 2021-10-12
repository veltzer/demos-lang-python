"""
A sample application for cmd2
"""

from cmd2 import Cmd2ArgumentParser, Cmd, with_argparser

argparser = Cmd2ArgumentParser()
argparser.add_argument('-p', '--piglatin', action='store_true', help='atinLay')
argparser.add_argument('-s', '--shout', action='store_true', help='N00B EMULATION MODE')
argparser.add_argument('-r', '--repeat', type=int, help='output [n] times')
argparser.add_argument('word', nargs='?', help='word to say')


class CmdLineApp(Cmd):
    def __init__(self):
        self.multilineCommands = ['orate']
        self.maxrepeats = 3

        # Add stuff to settable and shortcutgs before calling base class initializer
        # self.settable['maxrepeats'] = 'max repetitions for speak command'
        # self.shortcuts.update({'&': 'speak'})

        # Set use_ipython to True to enable the "ipy" command which embeds and interactive IPython shell
        Cmd.__init__(self)

        # For option commands, pass a single argument string instead of a list of argument strings to the do_* methods
        # set_use_arg_list(False)

    @with_argparser(argparser)
    def do_speak(self, arg, opts=None):
        """Repeats what you tell me to."""
        arg = ''.join(arg)
        if opts.piglatin:
            arg = f"{arg[1:]}{arg[0]}ay"
        if opts.shout:
            arg = arg.upper()
        repetitions = opts.repeat or 1
        for _ in range(min(repetitions, self.maxrepeats)):
            self.stdout.write(arg)
            self.stdout.write('\n')
            # self.stdout.write is better than "print", because Cmd can be
            # initialized with a non-standard output destination

    do_say = do_speak  # now "say" is a synonym for "speak"
    do_orate = do_speak  # another synonym, but this one takes multi-line input


if __name__ == '__main__':
    c = CmdLineApp()
    c.cmdloop()
