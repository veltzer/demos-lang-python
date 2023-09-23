"""
This example shows how to split a list into evenly sized chunks.

References:
- http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
"""


def chunks(a_list, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(a_list), n):
        yield a_list[i:i + n]


def main():
    for sublist in chunks(range(5, 28), 7):
        print(sublist)


main()
