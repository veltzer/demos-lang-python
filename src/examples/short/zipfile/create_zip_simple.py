#!/usr/bin/env python

"""
This example shows how to create a zip file in python using
the built in python module 'zipfile'
"""

import zipfile

zipfile_handle = zipfile.ZipFile('/tmp/demo.zip', 'w', zipfile.ZIP_DEFLATED)
# add a file to the archive, name in the archive will be the full
# name of the file
zipfile_handle.write("/etc/passwd")
# add a file with a different name
zipfile_handle.write(
        filename="/etc/group",
        arcname="this_is_groups",
)
# add a string as content
# TBD
zipfile_handle.close()
