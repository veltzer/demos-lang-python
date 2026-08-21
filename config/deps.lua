-- os level dependencies for this project

PACKAGES = {
    -- dbus
    "libdbus-glib-1-dev",
    "libdbus-1-dev",
    -- glib
    "libglib2.0-dev",
    -- gtk
    "libgirepository1.0-dev",
    "gcc",
    "libcairo2-dev",
    "libasound2-dev",
    "pkg-config",
    "python3-dev",
    "gir1.2-gtk-3.0",
    -- for pyscopg2 (postgres interface)
    "postgresql-common",
    "libpq-dev",
    "python3-gi",
    "libcairo2-dev",
    -- python
    "python3-distutils-extra",
    "python3-pip",
    -- swig
    "swig",
    "swig-doc",
    "fluidsynth",
    -- systemd
    "libsystemd0",
    -- TODO: cannot install this at this moment because of a problem in ubuntu repos
    -- "libsystemd-dev",
    -- c libs for python
    -- python version matches the CI runner (ubuntu-24.04); the old
    -- deps.py derived it from /etc/os-release
    "libpython3.12-dev",
}

DEV_PACKAGES = {
    "libpq-dev",
    "libcairo2-dev",
}
