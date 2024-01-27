from typing import List


config_requires: List[str] = []
dev_requires: List[str] = [
    "black",
]
install_requires: List[str] = [
    # command line parsing
    "click",
    "cmd2",
    # web
    "furl",
    "requests",
    "beautifulsoup4",
    "types-beautifulsoup4",
    "html5lib",
    "lxml",
    # progress and tui
    "tqdm",
    "types-tqdm",
    "pythondialog",
    # systems programming
    "psutil",
    "types-psutil",
    # problems intalling the next module on github systems
    # "systemd-python",
    "PyGObject",
    "PyGObject-stubs",
    "dbus-python",
    # cache and database
    "lmdb",
    "cachetools",
    # databases
    "pymysql",
    "mysql.connector",
    "sqlalchemy",
    "psycopg2",
    "types-psycopg2",
    # data languages
    "jsonschema",
    "types-jsonschema",
    "jsonpickle",
    # GUI
    "PyQt5",
    "PyQt5-stubs",
    # selenium stuff
    "webdriver-manager",
    "selenium",
    "selenium-wire",
    # music
    "music",
    "mingus",
    # GUI
    "PyQt5",
    "PyQt5-stubs",
    # selenium stuff
    "webdriver-manager",
    "selenium",
    "selenium-wire",
    # music
    "music",
    "mingus",
    # machine learning
    "pandas",
    "pandas-stubs",
    "numpy",
    "matplotlib",
    "colorspacious",
    # terminal color stuff
    "termcolor",
    "colored",
    "colorama",
    "types-colorama",
    # yaml
    "oyaml",
    "ruamel.yaml",
    # google cloud
    "google-api-python-client",
    "google-auth-httplib2",
    "google-auth-oauthlib",
    "google-cloud-datastore",
    # dependency injection
    "dependency-injector",
    # misc
    "texttable",
    "dispy",
    "mako",
    "luigi",
    "pyinotify",
    "twisted",
    "yapsy",
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
    "azure-cognitiveservices-search-websearch",
    "pygraph",
    "flask",
    "tsv",
    "pygments",
    "types-pygments",
    "simpleparse",
    "progressbar",
    "inject",
    "scrapy",
    "ConfigParser",
    "unidecode",
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
    "elasticsearch",
    "statistics",
    "opencv-python",
    "python-magic",
    "imageio",
    # my stuff
    "pyapikey",
    "pyvardump",
    # EXIF and image related libraries
    "Pillow",
    "types-Pillow",
    "ExifRead",
    "exif",
    "piexif",
    "PyExifTool",
    # k8s
    "kubernetes",
    "kubernetes-stubs",
    "openshift-client",
    # math
    "bitmath",
    "mpmath",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pytest-flake8",
    "flake8",
    "pylogconf",
    "mypy",
    "types-PyYAML",
    "types-setuptools",
    "types-boto",
    "types-PyMySQL",
    "types-requests",
    "types-paramiko",
    "types-termcolor",
]
requires = config_requires + install_requires + build_requires + test_requires
