#!/usr/bin/python

import argparse
import time
import sys
import hashlib

#todo Be more descriptive
argparsev = argparse.ArgumentParser("Generates passwords")
argparsev.add_argument("--master-pass", '-m', default=('%f' % time.time()), help='The master password for use in this program. Can be any string. Defaults to current time.time() when not specified.')
argparsev.add_argument('--iterations', '-i', default=0, type=int, help='The number of additional iterations to perform. Defaults to 0 if not provided.')

args = argparsev.parse_args(sys.argv[1:])

print(args)

#todo Choose hash type
hash = hashlib.shs256()

hash.update(args.master_pass)

for i in range(args.iterations):
    hash.update(hash.digest())

print(hash.hexdigest())
