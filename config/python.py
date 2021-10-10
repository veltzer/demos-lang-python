import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

run_requires = [
    'click',
    'requests',
    'tqdm',
    'cmd2',
    'pythondialog',
    'lmdb',
    'cachetools',
    'pandas',
    'dispy',
    'mako',
    'luigi',
    'pyinotify',
    'twisted',
    'yapsy',
    'pymysql',
    'mysql.connector',
    'sqlalchemy',
    'plotly',
    'gcloud',
    'networkx',
    'keyring',
    'python-jenkins',
    'SortedContainers',
    'PyRSS2Gen',
    'fire',
    'PyGithub',
    'gitpython',
    'prompt-toolkit',
    'PyQt5',
    'PyQt5-stubs',
    'azure-cognitiveservices-search-websearch',
    'pygraph',
    'flask',
    'tsv',
    'pygments',
    # 'simpleparse', causing problems
    'progressbar',
    'numpy',
    'inject',
    'scrapy',
    'ConfigParser',
    'unidecode',
    'bitmath',
    'paramiko',
    'boto',
    'boto3',
    'boto3-stubs',
    'attr',
    'pyparsing',
    'fastparquet',
    'logging_tree',
    'pluginbase',
    'reportlab',
    'imdbpy',
    'python-pptx',
    'selenium',
    # music
    'music',
    'mingus',
    # my stuff
    'pyapikey',
    'pyfakeuse',
    'pyvardump',
    # gtk stuff
    'vext',
    'vext.gi',

    # There packages require special attention (they do not install without issues)
    'psycopg2',
    'systemd-python',
    'PyGObject',
    'PyGObject-stubs',
    'dbus-python',

    # terminal color stuff
    'termcolor',
    'colored',

    # yaml
    'oyaml',
    'ruamel.yaml',
]

test_requires = [
]

dev_requires = [
    'pydmt',  # for building
    'pymakehelper',  # the the makefile
    'pylint',
    'flake8==3.7.9',
    'black',
    'pydmt',
]

test_container="[ 'ubuntu:21.04' ]"
test_python="[3.9]"

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.9"
