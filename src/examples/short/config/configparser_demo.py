"""
This is an example of how to use pythons built-in configparser.
"""

import configparser
import os.path

inifile = '/tmp/demo.ini'
if os.path.isfile(inifile):
    print('inifile exists, reading it')
    config = configparser.ConfigParser()
    config.read(inifile)
    myint = config.getint('section1', 'myint')
    mybool = config.getboolean('section1', 'mybool')
    myfloat = config.getfloat('section2', 'myfloat')
    print('\tmyint is {myint}'.format(**vars()))
    print('\tmybool is {mybool}'.format(**vars()))
    print('\tmyfloat is {myfloat}'.format(**vars()))

    # iterating over all sections and all values in all sections
    for section in config.sections():
        # iterating all key/value pairs in a section
        print('section [{0}]'.format(section))
        for k, v in config.items(section):
            print('\tkey [{0}], value [{1}]'.format(k, v))
else:
    print(
        'inifile did not exist, writing it for the first time. find it in {inifile}'.format(**vars()))
    config = configparser.ConfigParser()
    config.add_section('section1')
    config.set('section1', 'myint', str(15))
    config.set('section1', 'mybool', str(True))
    config.add_section('section2')
    config.set('section2', 'myfloat', str(3.14))
    with open(inifile, 'w') as configfile:
        config.write(configfile)
