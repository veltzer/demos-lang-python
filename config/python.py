make_requires = [
    "pymakehelper",
]
dev_requires = [
    "black",
]
install_requires = [
    "click",
    "requests",
    "tqdm",
    "cmd2",
    "pythondialog",
    "lmdb",
    "cachetools",

    "dispy",
    "mako",
    "luigi",
    "pyinotify",
    "twisted",
    "yapsy",
    "pymysql",
    "mysql.connector",
    "sqlalchemy",
    "plotly",
    "gcloud",
    "networkx",
    "keyring",
    "python-jenkins",
    "SortedContainers",
    "PyRSS2Gen",
    "fire",
    "PyGithub",
    "gitpython",
    "prompt-toolkit",
    "PyQt5",
    "PyQt5-stubs",
    "azure-cognitiveservices-search-websearch",
    "pygraph",
    "flask",
    "tsv",
    "pygments",
    # "simpleparse", causing problems
    "progressbar",
    "inject",
    "scrapy",
    "ConfigParser",
    "unidecode",
    "bitmath",
    "paramiko",
    "boto",
    "boto3",
    "boto3-stubs",
    "attr",
    "pyparsing",
    "fastparquet",
    "logging_tree",
    "pluginbase",
    "reportlab",
    "imdbpy",
    "python-pptx",
    "selenium",
    # music
    "music",
    "mingus",
    # my stuff
    "pyapikey",
    "pyfakeuse",
    "pyvardump",
    # gtk stuff
    "vext",
    "vext.gi",
    # machine learning
    "pandas",
    "numpy",

    # There packages require special attention (they do not install without issues)
    "psycopg2",
    "systemd-python",
    "PyGObject",
    "PyGObject-stubs",
    "dbus-python",
    # terminal color stuff
    "termcolor",
    "colored",
    # yaml
    "oyaml",
    "ruamel.yaml",
    # google cloud
    "google-api-python-client",
    "google-auth-httplib2",
    "google-auth-oauthlib",
    "google-cloud-datastore",
]
test_requires = [
    "pymakehelper",
    "pylint",
    "pytest",
    "pytest-cov",
    "pytest-flake8",
    "flake8",
    "pylogconf",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python=["3.10"]
