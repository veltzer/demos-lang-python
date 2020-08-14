#!/usr/bin/python3


"""
- We may add "-a" or "-a -a" to the autopep8 to make it fix more.
- Use 'autopep8 --list-fixes' to see the list of things autopep8 does
- You can select exactly which fixes to apply and which to ignore.
- Currently we apply all fixes quite aggressively.
"""

import subprocess

subprocess.check_call([
    'autopep8',
    # '--aggressive',
    # '--aggressive',
    # '--aggressive',
    '--recursive',
    '--in-place',
    'src',
])
