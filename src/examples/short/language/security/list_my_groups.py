"""
This example is very similar to the command line groups(1) or id(1) utilities.

References:
http://stackoverflow.com/questions/9323834/python-how-to-get-group-ids-of-one-username-like-id-gn
"""

import getpass
import grp
import pwd

username = getpass.getuser()
userid = pwd.getpwnam(username).pw_uid
print(f"current username is [{username}] and uid is [{userid}]")
groups = [(g.gr_name, g.gr_gid)
          for g in grp.getgrall() if username in g.gr_mem]
primary_gid = pwd.getpwnam(username).pw_gid
details = (grp.getgrgid(primary_gid).gr_name, primary_gid)
groups.append(details)
print(groups)
