"""
This is an example of how to copy files via paramiko.
"""

import os
import sys

import paramiko

# server = "MarksHome"
server = "172.34.5.111"
username = "ubuntu"
key_filename = os.path.expanduser("~/.aws/keys/ec2_instances.pem")

sshcon = paramiko.SSHClient()
# no known_hosts error
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcon.connect(
    server,
    username=username,
    key_filename=key_filename,
)

# this is ssh
stdin, stdout, stderr = sshcon.exec_command('ls -la')
for x in stdout.readlines():
    print(x, end="")
for x in stderr.readlines():
    print(x, end="")
print(stdout.channel.recv_exit_status())

_stdin, stdout, stderr = sshcon.exec_command('ls -la /non')
for x in stdout.readlines():
    print(x, end="")
for x in stderr.readlines():
    print(x, end="")
print(stdout.channel.recv_exit_status())

sshcon.close()

sys.exit(1)
print("here")

# this is sftp
# sftp = ssh.open_sftp()
# sftp.put(localpath, remotepath)
# sftp.close()
