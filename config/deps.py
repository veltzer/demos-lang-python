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
]

dev_packages = [
	"libpq-dev",
	"libcairo2-dev",
]
