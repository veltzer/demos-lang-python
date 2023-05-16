"""
How to remove files from git using git api

References:
- https://stackoverflow.com/questions/47041004/how-do-you-delete-a-file-with-gitpython
"""

import git

repo = git.Repo(".")
repo.index.remove(["folder"], True, r=True)
