#!/usr/bin/env python3
"""
Sam McNurlen
This script uses argparse to set up an argument.
"""

import argparse
import sys

parser = argparse.ArgumentParser(description="This is Sam's script.")

parser.add_argument('-m',
                    dest='basic',
                    help='Enter some text')

parser.add_argument('-i', '--integer',
                    dest='varInteger',
                    metavar='[an integer]',
                    default=10,
                    type=int,
                    required=True,
                    help='<required> Enter a simple Integer')

parser.add_argument('-d', '--float',
                    dest='varFloat',
                    metavar='[a float]',
                    type=float,
                    help='Enter a simple float')

parser.add_argument('-s', '--string',
                    dest='varString',
                    metavar='[a string]',
                    type=str,
                    help='Enter a simple string')

parser.add_argument('-l',
                    dest='varList',
                    metavar='[strings]',
                    nargs='+',
                    help='Enter a list of strings (space delimited)')

parser.add_argument('-t', '--set-true',
                    dest='varBoolFalse',
                    default=True,
                    action='store_false',
                    help='Toggle from default False to True')

parser.add_argument('-f', '--set-false',
                    dest='varBoolTrue',
                    default=False,
                    action='store_true',
                    help='Toggle from default True to False')

parser.add_argument('-v', '--version',
                    dest='varVersion',
                    action='version',
                    version='%(prog)s 2.0',
                    help='show program'+'s version number and exit')

if len(sys.argv) == 1:
    print(parser.print_help())

args = parser.parse_args()
print(type(args.varInteger),args.varInteger)
print(type(args.varString),args.varString)
print(type(args.varFloat),args.varFloat)
print(type(args.varList),args.varList)