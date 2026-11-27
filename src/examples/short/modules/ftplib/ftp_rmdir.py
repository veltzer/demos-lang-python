""" ftp_rmdir.py """

import ftplib
import os.path
import sys
from ftplib import FTP

p_debug = False


def ftp_rmdir(ftp: FTP, folder: str, *, remove_toplevel: bool, dont_remove: set[str]) -> None:
    for filename, attr in ftp.mlsd(folder):
        if attr["type"] == "file" and filename not in dont_remove:
            if p_debug:
                print(f"removing file [{filename}] from folder [{folder}]")
            ftp.delete(os.path.join(folder, filename))
        if attr["type"] == "dir":
            ftp_rmdir(ftp, filename, remove_toplevel=True, dont_remove=dont_remove)
    if remove_toplevel:
        if p_debug:
            print(f"removing folder [{folder}]")
        ftp.rmd(folder)


def main() -> None:
    p_host = sys.argv[1]
    p_user = sys.argv[2]
    p_pass = sys.argv[3]
    p_dir = sys.argv[4]
    if p_debug:
        print(p_host)
        print(p_user)
        print(p_pass)
        print(p_dir)

    ftp = ftplib.FTP(p_host)
    ftp.login(user=p_user, passwd=p_pass)
    # ftp_rmdir(ftp, p_dir, False, set([".ftpquota"]))  # noqa: ERA001  teaching: kept in the comment for the reader
    ftp_rmdir(ftp, p_dir, remove_toplevel=False, dont_remove=set())
    ftp.quit()


if __name__ == "__main__":
    main()
