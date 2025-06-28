""" python deps for this project """

install_requires: list[str] = [
    "pydantic",
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
    "dbus-python",
    # problems intalling the next module on github systems
    # "systemd-python",
    # gtk stuff
    # "PyGObject",
    # "PyGObject-stubs",
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
    "pyFluidSynth",
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
    "simpleaudio",
    "pygame",
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
    # "dependency-injector",
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
    "tsv",
    "pygments",
    "types-pygments",
    # "simpleparse",
    "progressbar",
    "inject",
    "scrapy",
    "browser_cookie3",
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
    "openshift",
    # math and machine learning
    "bitmath",
    "mpmath",
    "sympy",
    "scipy",
    "pandas",
    "pandas-stubs",
    "numpy",
    "matplotlib",
    "colorspacious",
    "scikit-learn",
    # flask-web
    "flask",
    "Flask-RESTful",
    # fastapi-web
    "fastapi",
    "uvicorn",
    "tornado",
    "django",
    "djangorestframework",
    "cryptography",
    "svgwrite",
    "jq",
    "docker",
    "humanize",
    # my own stuff
    "pygooglehelper",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pylogconf",
    "mypy",
    # types
    "types-PyYAML",
    "types-setuptools",
    "types-boto",
    "types-PyMySQL",
    "types-requests",
    "types-paramiko",
    "types-termcolor",
]
requires = install_requires + build_requires + test_requires
