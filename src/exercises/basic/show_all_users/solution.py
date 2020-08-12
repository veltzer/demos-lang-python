"""
This script shows all users on a UNIX system
"""

file_name = '/etc/passwd'
all_users = []
for line in open(file_name):
    all_users.append(line.split(':')[0])

# now we are out of the loop, lets output all users...
print(all_users)
