#!/usr/bin/env python

import sys

buffer = {}

for line in sys.stdin:
    node, page_rank = line.split("\t")
    page_rank = float(page_rank)

    if len(buffer) < 20:
        buffer[node] = page_rank
        threshold = min(buffer.values())

    if page_rank > threshold:
        for n, p in buffer.items():
            if p == threshold:
                buffer.pop(n)
                break

        buffer[node] = page_rank
        threshold = min(buffer.values())


for node, page_rank in buffer.items():
    print("%s\t%f" % (node, page_rank))

