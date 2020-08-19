"""
Parse a simple Makefile and execute it.
Doesn't support comments, variables, patterns or anything complex...
Doesn't check file system. all targets are always built.
"""

import os


def parse_makefile(filename):
    """Parses a makefile.

    Input consists of only 2 kinds of lines::

            target: dependency1 dependency2...
                    command1
                    command2
                    ...
            target2: dependency3...
                    command3

    (any leading whitespace means command.)

    Returns tuple (rules, commands) where:
    - rules is a dict {'target': ['dependency1', ...], ...}
    - commands is a dict {'target': ['command1', ...], ...}
    """
    rules = {}
    commands = {}
    target = None
    for line in open(filename):
        if not line[0].isspace():
            # dep line (parse, set `target`)
            target, rest = line.split(':')
            target = target.strip()
            rules[target] = rest.split()
            commands[target] = []
        else:
            # command line (`target` was set by last dep line)
            commands[target].append(line.strip())

    return rules, commands


def build(target, rules, commands):
    """Compute order in which things should be built for target.

    >>> build('a', {'a': ['b', 'c'], 'b': ['d']}, {'a': [], 'b': []})
    == Building d -> b ==
    == Building b, c -> a ==
    """
    if target not in rules:
        # Nothing needs to be done.
        # (A real make tool would verify that the file exists.)
        return

    # Build all dependencies.
    for dep in rules[target]:
        build(dep, rules, commands)
    # And then build the target.
    # (A real make tool would compare file dates to see if it's needed.)
    build_one(target, rules, commands)


def build_one(target, rules, commands):
    """Execute commands for one target."""
    print('== Building {0} -> {1} =='.format(', '.join(rules[target]), target))
    for command in commands[target]:
        print(command)
        os.system(command)


def main():
    import doctest
    doctest.testmod()

    rules, commands = parse_makefile('make_bonus.txt')
    build('all', rules, commands)


main()
