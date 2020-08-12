import ftplib
import os.path
import sys

p_debug = False


def ftp_rmdir(ftp, folder, remove_toplevel, dontremove):
    for filename, attr in ftp.mlsd(folder):
        if attr['type'] == 'file' and filename not in dontremove:
            if p_debug:
                print(
                    'removing file [{0}] from folder [{1}]'.format(filename, folder))
            ftp.delete(os.path.join(folder, filename))
        if attr['type'] == 'dir':
            ftp_rmdir(ftp, filename, True, dontremove)
    if remove_toplevel:
        if p_debug:
            print('removing folder [{0}]'.format(folder))
        ftp.rmd(folder)


def main():
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
    # ftp_rmdir(ftp, p_dir, False, set(['.ftpquota']))
    ftp_rmdir(ftp, p_dir, False, set())
    ftp.quit()

if __name__ == '__main__':
    main()
