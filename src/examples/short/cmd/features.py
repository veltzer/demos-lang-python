"""
This is an example of how to use the cmd python module adjusted for python3

Notes:
- all commands are in the 'do_XXX' methods.
- these methods *must* received both self and args.
You may choose to not use the args but they must be received.
- an empty line method must really be called 'emptyline'
- return True when you want to quit. Returning nothing is OK and so is returning
False or None. Returning -1 is exiting.
- so: returning anything which evaluates to True is exiting.

References:
http://code.activestate.com/recipes/280500-console-built-with-cmd-object/
"""

import cmd
import os


class Console(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "=>> "
        self.intro = "Welcome to console!"  # defaults to None
        self._hist = None
        self._locals = None
        self._globals = None

    # Command definitions
    # noinspection PyUnusedLocal
    def do_hist(self, args):
        """Print a list of commands that have been entered"""
        print(self._hist)

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def do_exit(self, args):
        """Exits from the console"""
        return -1

    # Command definitions to support Cmd object functionality
    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_exit(args)

    # noinspection PyMethodMayBeStatic
    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        os.system(args)

    # noinspection PyMethodMayBeStatic
    def do_a_plus_b(self, args):
        """ add two numbers """
        args = args.split(" ")
        print(int(args[0])+int(args[1]))
        return True

    def do_return_true(self, args):
        """ return True """
        return True

    def do_return_false(self, args):
        """ return False """
        return False

    def do_return(self, args):
        """ return """
        return

    def do_return_m1(self, args):
        """ return -1 """
        return -1
 
    def do_return_none(self, args):
        """ return None """
        return None

    def do_help(self, args):
        """Get help on commands
           'help' or '?' with no arguments prints a list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """
        # The only reason to define this method is for the help text in the doc string
        cmd.Cmd.do_help(self, args)

    # Override methods in Cmd object
    def preloop(self):
        """Initialization before prompting user for commands.
           Despite the claims in the Cmd documentation, Cmd.preloop() is not a stub.
        """
        cmd.Cmd.preloop(self)  # sets up command completion
        self._hist = []  # No history yet
        self._locals = {}  # Initialize execution namespace for user
        self._globals = {}

    def postloop(self):
        """Take care of any unfinished business.
           Despite the claims in the Cmd documentation, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)  # Clean up command completion
        print("Exiting...")

    def precmd(self, line):
        """ This method is called after the line has been input but before
            it has been interpreted. If you want to modify the input line
            before execution (for example, variable substitution) do it here.
        """
        self._hist += [line.strip()]
        return line

    def postcmd(self, stop, line):
        """If you want to stop the console, return something that evaluates to true.
           If you want to do some post command processing, do it here.
        """
        return stop

    def emptyline(self):
        """Do nothing on empty input line"""
        print("this is an empty line")

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        try:
            exec(line) in self._locals, self._globals
        except Exception as e:
            print(e.__class__, ":", e)


if __name__ == '__main__':
    console = Console()
    console.cmdloop()
