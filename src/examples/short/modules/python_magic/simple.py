"""
A simple exapmle of how to use python-magic to identify file types by content
"""

import glob
import magic

magic_obj = magic.Magic(mime=True)
for filename in glob.glob("data/python-magic/**"):
    file_type = magic_obj.from_file(filename)
    print(f"filename is [{filename}], file_type [{file_type}]")
    with open(filename, "rb") as stream:
        file_type2 = magic.from_buffer(stream.read(2048))
        print(f"filename is [{filename}], file_type [{file_type}]")
