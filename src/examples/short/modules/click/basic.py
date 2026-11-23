"""
A Demo for click

Notes:
- when you give a flag the "--XXX" could be written as "--XXX/--YYY" and then
    --XXX will turn on the flag and --YYY will turn it off.
    In this case *YOU MUST NOT* pass the "type=bool" parameters (bug in click)
- add "show_default=True" to every option to show the default value for that option.

References:
- http://click.pocoo.org/5
"""

import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.", show_default=True)
@click.option("--name", prompt="Your name", help="The person to greet.")
@click.option("--required", required=True, help="this is a required parameter")
@click.option("--output", required=True, help="output file", type=click.File("w", lazy=False))
@click.option("--hash-type", required=True, type=click.Choice(["md5", "sha1"]))
@click.option("--foo/--bar", required=False, help="this is foo")
def main(count, name, required, output, hash_type):
    """Simple program that greets NAME for a total of COUNT times."""
    print(required)
    print(output)
    print(hash_type)
    for _ in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
