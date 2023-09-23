"""
This example shows how with works for file streams
"""


def count_lines_in_file(filename):
    with open(filename, "rt") as stream:
        counter = 0
        for _ in stream:
            counter += 1
    return counter


def count_lines_in_file_2(filename):
    # pylint: disable=consider-using-with
    stream = open(filename, "rt")
    try:
        counter = 0
        for _ in stream:
            counter += 1
        return counter
    except Exception as e:
        raise e
    finally:
        stream.close()


print(count_lines_in_file("/etc/passwd"))
print(count_lines_in_file_2("/etc/passwd"))
