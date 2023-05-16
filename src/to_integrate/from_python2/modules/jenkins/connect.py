"""
This is an example of how to create a job for jenkins by remote using python.
This uses the "python-jenkins" module.

References:
- http://python-jenkins.readthedocs.io/en/latest/
"""

import os
import configparser
import jenkins


def get_data():
    inifile = os.path.expanduser("~/.jenkins.cnf")
    config = configparser.ConfigParser()
    config.read(inifile)
    f_user = config.get("jenkins", "user")
    f_password = config.get("jenkins", "password")
    f_url = config.get("jenkins", "url")
    return f_user, f_password, f_url


d_user, d_password, d_url = get_data()
server = jenkins.Jenkins(
    url=d_url,
    username=d_user,
    password=d_password
)
version = server.get_version()
print(f"server version is [{version}]")
