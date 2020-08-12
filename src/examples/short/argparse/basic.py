"""
A demo for the argparse module which is arguably the best python
command line parsing module.

try this command to check it out:
./demo_argparse.py process --input in --output out

References:
https://docs.python.org/3/howto/argparse.html
https://docs.python.org/3/library/argparse.html#module-argparse
"""

import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='sub commands', dest='sub_command')
sub_parser_process = subparsers.add_parser('process')
sub_parser_process.add_argument('--input', help='input file')
sub_parser_process.add_argument('--output', help='output file')
sub_parser_process.add_argument(
    '--chmod', help='chmod the output?', default=True, action='store_false')
sub_parser_print = subparsers.add_parser('print')
parser.add_argument(
    '-d', '--debug', help='debug the script', default=False, action='store_true')
parser.add_argument(
    '-i', '--integer', help='integer', type=int, default=5, choices=[5, 7, 9])
args = parser.parse_args()

print(args)
