"""
This is an example of how to create a job for jenkins by remote using python.
This uses the "python-jenkins" module.

References:
- http://python-jenkins.readthedocs.io/en/latest/
"""

import jenkins
import os
import configparser

def get_data():
    inifile = os.path.expanduser("~/.jenkins.cnf")
    config = configparser.ConfigParser()
    config.read(inifile)
    d_user = config.get("jenkins", "user")
    d_password = config.get("jenkins", "password")
    d_url = config.get("jenkins", "url")
    return d_user, d_password, d_url

d_user, d_password, d_url = get_data()
server = jenkins.Jenkins(
    url=d_url,
    username=d_user,
    password=d_password
)
version = server.get_version()
print("server version is [{}]".format(version))
