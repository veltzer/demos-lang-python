"""
This checks whether the order of options and arguments in click matters
"""

import click


@click.command()
@click.argument("arg")
@click.option("--count", default=1, help="Number of greetings.", show_default=True)
@click.option("--output", required=False, help="output file", type=click.File("w", lazy=False))
@click.option("--hash-type", required=False, type=click.Choice(["md5", "sha1"]))
def main(arg, count, output, hash_type):
    """Simple program that greets NAME for a total of COUNT times."""
    print(arg)
    print(count)
    print(output)
    print(hash_type)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
