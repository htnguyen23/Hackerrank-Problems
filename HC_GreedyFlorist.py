#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # buy the more expensive flowers first, buy least expensive flower last
    # every friend buy same amount of flowers before leftovers, to maximize new customers
    each = len(c) / k 
    remain = len(c) % k 
    cost = 0
    inc = 0
    each_curr = 0
    c = sorted(c)
    # split flower purchases by (current purchase +- previous purchase) - ie. what ith number is this for that friend (so we know what factor is apply it by)
    # (inc + 1) * original price

    # every friend buys at least this amount
    for i in reversed(range(remain, len(c))):
        cost += (inc + 1) * c[i]
        each_curr += 1
        if each_curr == k:
            inc += 1
            each_curr = 0
    for i in range(remain):
        cost += (inc + 1) * c[i]

    return cost

# return sum((i // k + 1) * x for i, x in enumerate(sorted(c, reverse=True)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
