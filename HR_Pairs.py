
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    # AtTTEMPT 2: iterate through arr and add k to curr elem to find matching difference
    arr_set = set(arr)
    count = 0
    for num in arr:
        if (num + k) in arr_set:
            count += 1
    return count

    # ATTEMPT 1: iterate through arr and find difference between every pair - too long
    # n = len(arr)
    # count = 0
    
    # for i in range(n):
    #     for j in range(i, n):
    #         if abs(arr[i] - arr[j]) == k:
    #             count += 1
    
    # return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
