"""
This demo shows how to create a click program that accepts many free
parameters on the command line.

Notes:
- The parameters: show_default, help, type, as NOT allowed for the
free arguments section (click.argument).
- The parameter 'required' is allowed.

References:
- http://click.pocoo.org/5/arguments/#variadic-arguments
"""

import click


@click.command()
@click.argument(
    'args',
    nargs=-1,
    required=True,
)
def main(args):
    """Simple program that greets NAME for a total of COUNT times."""
    print(args)


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()
