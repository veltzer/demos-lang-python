"""
os level dependencies for this project
"""

import platform


desktop = platform.freedesktop_os_release()
VERSION_ID = desktop["VERSION_ID"]
ver_python = None
if VERSION_ID == "22.04":
    ver_python = "3.10"
if VERSION_ID == "22.10":
    ver_python = "3.10"
if VERSION_ID == "23.04":
    ver_python = "3.11"
if VERSION_ID == "23.10":
    ver_python = "3.11"
if VERSION_ID == "24.04":
    ver_python = "3.12"
if VERSION_ID == "24.10":
    ver_python = "3.12"
if VERSION_ID == "25.10":
    ver_python = "3.13"
assert ver_python is not None

packages = [
    # dbus
    "libdbus-glib-1-dev",
    "libdbus-1-dev",
    # glib
    "libglib2.0-dev",
    # gtk
    "libgirepository1.0-dev",
    "gcc",
    "libcairo2-dev",
    "libasound2-dev",
    "pkg-config",
    "python3-dev",
    "gir1.2-gtk-3.0",
    # for pyscopg2 (postgres interface)
    "postgresql-common",
    "libpq-dev",
    "python3-gi",
    "libcairo2-dev",
    # python
    "python3-distutils-extra",
    "python3-pip",
    # swig
    "swig",
    "swig-doc",
    "fluidsynth",
    # systemd
    "libsystemd0",
    # TODO: cannot install this at this moment because of a problem in ubuntu repos
    # "libsystemd-dev",
    # c libs for python
    f"libpython{ver_python}-dev",
]

dev_packages = [
	"libpq-dev",
	"libcairo2-dev",
]
