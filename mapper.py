#!/usr/bin/env python

import sys

N = 7967  # number of pages
# N = 4  # number of pages (test with adj)
s = 0.15  # probability of going to a random page
x_0 = [1.0 / N for i in range(N)]


for line in sys.stdin:
    i, pages = line.split(": ")
    pages = list(map(float, pages.split(" ")[:-1]))

    x_0_i = x_0[int(i)]

    for j in range(N):
        t_ij = float((j in pages)) / len(pages) if len(pages) > 0 else 0
        p_ij = (1 - s) * t_ij + s / N

        x_1_ij = x_0_i * p_ij
        print("%s\t%f" % (i, x_1_ij))

