"""
This script shows all users on a UNIX system
"""


def main() -> None:
    """ the main function """
    with open("/etc/passwd") as f:
        all_users = [line.split(":")[0] for line in f]

    # now we are out of the loop, lets output all users...
    print(all_users)


main()
