#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    # choose not to win contests, if have to win, choose smallest contest
    # sort important contests to know which one to lose based on k
    k_count = 0
    important = []
    luck = 0
    for i in contests:
        if contests[i][1] == 1:
            bisect.insort(important, contests[i][0])
        else:
            luck += contests[i][0]
    if k - len(contests) >= 0:
        luck += sum(important)
    else:
        maximize = sum(important[0:len(contests) - k])
        luck += sum(important[len(contests-k)-1 : ])
        luck -= maximize
    return luck


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(str(result) + '\n')

    #fptr.write(str(result) + '\n')

    #fptr.close()
