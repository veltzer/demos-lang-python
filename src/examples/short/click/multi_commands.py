"""
A demo of how to do multi commands in click

The idea is to group commands into groups (see below).
You can also override the name of a command.

TODO:
- add how to pass options to the subcommands and global options.
"""

import click


@click.group()
def cli():
    pass


@cli.command()
def say_hello():
    print('hello')


@cli.command()
def say_goodbye():
    print('goodbye')


@cli.command(name="foo")
def bar():
    print('foo')


if __name__ == '__main__':
    cli()
