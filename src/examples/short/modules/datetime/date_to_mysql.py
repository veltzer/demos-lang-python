"""
example of how to convert the output of date(1) on the command line
to mysql type dates.
"""

import datetime as dt
import subprocess
from datetime import datetime


def date_to_mysql(output: str) -> datetime:
    format_str = "%a %b %d %H:%M:%S %Z %Y"
    return dt.datetime.strptime(output, format_str).astimezone()
    # print("mysql_str is [{0}]".format(mysql_str))  # noqa: ERA001  teaching: kept in the comment for the reader


def main() -> None:
    output = subprocess.check_output("date").decode().strip()
    print(f"output is [{output}]")
    d = date_to_mysql(output)
    print(f"d is [{d}]")


if __name__ == "__main__":
    main()
