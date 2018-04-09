#!/usr/bin/python

import argparse
import time
import sys
import hashlib


#todo Be more descriptive
argparsev = argparse.ArgumentParser("Generates passwords")
argparsev.add_argument("--master-pass", '-m', default=('%f' % time.time()), help='The master password for use in this program. Can be any string. (Default time.time())')
argparsev.add_argument('--iterations', '-i', default=0, type=int, help='The number of additional iterations to perform. (Default %(default)s)')
argparsev.add_argument('--hash-type','-a',choices=hashlib.algorithms_available, help="All hash functions available are those available via the hashlib library. The list can be found by running the python command 'hashlib.algorithms_available'. (Default %(default)s)", default="sha256")
args = argparsev.parse_args(sys.argv[1:])

#todo Choose hash type
hash = hashlib.new(args.hash_type)

hash.update(args.master_pass.encode())

for i in range(args.iterations):
    hash.update(hash.digest())

print(hash.hexdigest())


