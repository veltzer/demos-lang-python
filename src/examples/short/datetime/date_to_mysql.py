"""
example of how to convert the output of date(1) on the command line
to mysql type dates.
"""

import datetime
import subprocess


def date_to_mysql(output: str):
    format_str = '%a %b %d %H:%M:%S %Z %Y'
    mysql_str = datetime.datetime.strptime(output, format_str)
    # print('mysql_str is [{0}]'.format(mysql_str))
    return mysql_str


def main():
    output = subprocess.check_output('date').decode().strip()
    print('output is [{0}]'.format(output))
    d = date_to_mysql(output)
    print('d is [{0}]'.format(d))


if __name__ == '__main__':
    main()
