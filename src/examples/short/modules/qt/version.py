"""
An example of how to know which PyQt version you are using
"""

# pylint: disable=c-extension-no-member
import PyQt5.QtCore


print(f"version is {PyQt5.QtCore.QT_VERSION_STR}")
