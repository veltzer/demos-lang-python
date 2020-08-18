"""
This is an example of how to use pythons built-in configparser.
"""

import configparser
import os.path

ini_file = '/tmp/demo.ini'
if os.path.isfile(ini_file):
    print('ini_file exists, reading it')
    config = configparser.ConfigParser()
    config.read(ini_file)
    my_int = config.getint('section1', 'my_int')
    my_bool = config.getboolean('section1', 'my_bool')
    my_float = config.getfloat('section2', 'my_float')
    print('\tmy_int is {my_int}'.format(**vars()))
    print('\tmy_bool is {my_bool}'.format(**vars()))
    print('\tmy_float is {my_float}'.format(**vars()))

    # iterating over all sections and all values in all sections
    for section in config.sections():
        # iterating all key/value pairs in a section
        print('section [{0}]'.format(section))
        for k, v in config.items(section):
            print('\tkey [{0}], value [{1}]'.format(k, v))
else:
    print(f'{ini_file} did not exist, writing it for the first time.')
    config = configparser.ConfigParser()
    config.add_section('section1')
    config.set('section1', 'my_int', str(15))
    config.set('section1', 'my_bool', str(True))
    config.add_section('section2')
    config.set('section2', 'my_float', str(3.14))
    with open(ini_file, 'w') as configfile:
        config.write(configfile)
