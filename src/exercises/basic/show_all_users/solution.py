"""
This script shows all users on a UNIX system
"""


def main():
    """ the main function """
    all_users = []
    with open("/etc/passwd") as f:
        for line in f:
            all_users.append(line.split(':')[0])

    # now we are out of the loop, lets output all users...
    print(all_users)


main()
