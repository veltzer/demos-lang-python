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
    'dbus-python',
    'python-jenkins',
    'SortedContainers',
    'PyRSS2Gen',
    'fire',
    'PyGithub',
    'prompt-toolkit',
    'PyQt5',
    'PyQt5-stubs',
    'azure-cognitiveservices-search-websearch',
    'pygraph',
    'flask',
    'tsv',
    'psycopg2',
    'pygments',
    'simpleparse',
    'progressbar',
    'numpy',
    'inject',
    'scrapy',
    'ConfigParser',
    'unidecode',
    'bitmath',
    'paramiko',
    'systemd-python',
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
    'PyGObject',
    'PyGObject-stubs',
]

test_requires = [
]

dev_requires = [
    'pydmt',  # for building
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.5"
