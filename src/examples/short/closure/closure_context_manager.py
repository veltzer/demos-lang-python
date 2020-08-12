"""
This is a basic closure example.
"""


def iterate_it(filename):
    with open(filename) as f:
        yield from f


def iter_through_files(filenames: List[str]):
    l = []
    for filename in filenames:
        l.append(iterate_it(filename))
    return l


def main():
    iters = iter_through_files(['/etc/passwd', '/etc/group'])
    for i in iters:
        for j in i:
            print(j, end='')


if __name__ == '__main__':
    main()
