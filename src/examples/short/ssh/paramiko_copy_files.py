"""
This is an example of how to copy files via paramiko.
"""

import os

import paramiko

hostname = "HOSTNAME"
username = "USERNAME"
key_filename = os.path.expanduser("~/.aws/keys/ec2_instances.pem")
local_path = "/etc/passwd"
remote_path = "passwd"

ssh_connection = paramiko.SSHClient()
# no known_hosts error
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect(
    hostname=hostname,
    username=username,
    key_filename=key_filename,
)

# this is ssh
stdin, stdout, stderr = ssh_connection.exec_command("ls -la")
for x in stdout.readlines():
    print(x, end="")
for x in stderr.readlines():
    print(x, end="")
print(stdout.channel.recv_exit_status())

_stdin, stdout, stderr = ssh_connection.exec_command("ls -la /non")
for x in stdout.readlines():
    print(x, end="")
for x in stderr.readlines():
    print(x, end="")
print(stdout.channel.recv_exit_status())

ssh_connection.close()

do_ftp = False
if do_ftp:
    sftp = ssh_connection.open_sftp()
    sftp.put(local_path, remote_path)
    sftp.close()
