#!/usr/bin/env python

"""
This is an example of how to create a job for jenkins by remote using python.
This uses the 'python-jenkins' module.

References:
- http://python-jenkins.readthedocs.io/en/latest/
"""

import jenkins

# connect with user and password
server = jenkins.Jenkins(
    url='https://localhost:8080',
    username='myuser',
    password='mypassword'
)
version = server.get_version()
print('server version is [{}]'.format(version))
