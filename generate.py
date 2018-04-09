#!/usr/bin/python

import argparse
import time
import sys

#todo Be more descriptive
argparsev = argparse.ArgumentParser("Generates passwords")
argparsev.add_argument("--master-pass", '-m', default=('%f' % time.time()), help='The master password for use in this program. Can be any string. Defaults to current time.time() when not specified.')
argparsev.add_argument('--iterations', '-i', default=0, type=int, help='The number of additional iterations to perform. Defaults to 0 if not provided.')

#todo Choose hash type

args = argparsev.parse_args(sys.argv[1:])

print(args)
