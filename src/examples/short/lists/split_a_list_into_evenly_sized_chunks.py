"""
This example shows how to split a list into evenly sized chunks.

References:
- http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
"""


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def main():
    for l in chunks(range(5, 28), 7):
        print(l)


main()
