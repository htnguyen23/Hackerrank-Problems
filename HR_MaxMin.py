#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    # (1) find two numbers in arr that have minimum difference (the value of k doesn't matter?) -> doesn't work b/c the numbers w/ the minimum differenece have to contain k-2 elements between them
    # (2) sort the arr, then find the minimum difference w k-2 elems b/t?
    arr.sort()
    minUnfair = float('inf')
    for i in range(len(arr)-(k-1)):
        minUnfair = min(minUnfair, (arr[i+(k-1)] - arr[i]))
        print(str(arr[i+k-1]) + " - " + str(arr[i]) + " = " + str(arr[i+k-1] - arr[i]))
        print(str(i+k) + " - " + str(i))
        print("minUnfair = " + str(minUnfair) + "\n")

    print(arr)
    return minUnfair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
