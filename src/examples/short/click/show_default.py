"""
This example demonstrates how to show the default value for a paramter
in click.
"""

import click


@click.command()  # type: ignore
@click.option(
    "--count",
    default=1,
    type=int,
    help="Number of greetings.",
    show_default=True,
)
def main(count: int) -> None:
    """ simple demo that shows default values """
    print(count)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()  # type: ignore
