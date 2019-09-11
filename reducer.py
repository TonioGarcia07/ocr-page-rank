#! /usr/bin/env python3

import sys

total = 0
last_index = None

for line in sys.stdin:
    line = line.strip()

    index, product = line.split("\t")
    index = int(index)
    product = float(product)

    if last_index is None:
        last_index = index
    if index == last_index:
        total += product
    else:
        print("%s\t%f" % (last_index, total))
        total = product
        last_index = index

if last_index is not None:
    print("%s\t%f" % (last_index, total))
