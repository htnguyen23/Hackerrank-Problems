#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # swap based on indices
    # dict of elem-index key-value pair for fast index lookup
    arr_dic = {value: i for i, value in enumerate(arr)}
    swap = 0
    iswap = 0
    elemswap = 0
    for i in range(len(arr)):
        iswap = arr_dic[i+1]
        if (i != iswap):
            elemswap = arr[i]
            arr[i] = arr[iswap]
            arr[iswap] = elemswap   # can this swap be done with: arr[i], arr[iswap] = arr[iswap]. arr[i]?
            swap += 1
            # update dict w/ swapped indices
            arr_dic[i+1] = i
            arr_dic[elemswap] = iswap
    return swap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
