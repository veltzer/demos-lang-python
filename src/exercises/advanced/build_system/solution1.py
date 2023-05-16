"""
Parse a simple Makefile (without commands) and output a build plan.
Doen"t support comments, variables, patterns or anything complex...
Doesn"t check file system, all targets are always built.
"""


import doctest


def parse_makefile(filename):
    """Parses a file of lines of the form::

            target: dependency1 dependency2...

    Returns a dict {"target": ["dependency1", ...], ...}
    """
    rules = {}
    with open(filename) as f:
        for line in f:
            target, rest = line.split(":")
            target = target.strip()
            rules[target] = rest.split()
    return rules


def build_plan(target, rules):
    """Compute order in which things should be built for target.

    >>> build_plan("a", {"a": ["b", "c"], "b": ["d"]})
    ["b", "a"]
    """
    if target not in rules:
        # Nothing needs to be done.
        # (A real make tool would verify that the file exists.)
        return []

    plan = []
    # Build all dependencies.
    for dep in rules[target]:
        plan += build_plan(dep, rules)

    # And then build the target.
    # (A real make tool would compare file dates to see if its needed.)
    plan.append(target)

    return plan


def main():
    doctest.testmod()
    rules = parse_makefile("make.txt")
    print(build_plan("all", rules))


main()
