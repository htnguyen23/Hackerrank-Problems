#!/bin/python3

import math
import os
import random
import re
import sys
import statistics 

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

'''
from bisect import bisect_left

def activityNotifications(expenditure, d):
    k = 0
    res = [0] * (max(expenditure) + 1)
    sorted_trail = []
     
    for i in expenditure[:d]:
        res[i] += 1
    for i in range(len(res)):
        sorted_trail += [i] * res[i]
    
    for i in range(len(expenditure) - d):
        median = sorted_trail[d // 2] if d % 2 == 1 else (sorted_trail[d // 2 - 1] + sorted_trail[d // 2]) / 2
        if expenditure[i+d] >= 2 * median:
            k += 1
        index = bisect_left(sorted_trail, expenditure[i])
        sorted_trail.pop(index)
        index = bisect_left(sorted_trail, expenditure[i+d])
        sorted_trail.insert(index, expenditure[i+d])
    
    return k
'''

def activityNotifications(expenditure, d):
    # Write your code here
    exp_len = len(expenditure)
    if d >= exp_len:
        return 0
    notices = med = 0
    idel = daydel = dayadd = 0
    exp_sorted = sorted(expenditure[:d])
    med = statistics.median(exp_sorted)
    if expenditure[d] >= (2 * med):
            notices += 1
    #print(exp_sorted)
    #print("med = " + str(med) + "  med*2 = " + str(2*med) + " =< day[" + str(d) + "] = " + str(expenditure[d]))
    #print("\t" + str(notices))
    for day in range(d, exp_len-1):
        # remove [day-1] sort new [day] into prexisting sorted exp (optimize)
        dayadd = expenditure[day]
        daydel = expenditure[day-d]
        idel = exp_sorted.index(daydel)
        exp_sorted[idel] = dayadd           #d el exp_sorted[idel]
        #print(exp_sorted)
        exp_sorted = sorted(exp_sorted)     # insort(exp_sorted, dayadd)  
        med = statistics.median(exp_sorted)
        #print(exp_sorted)
        #print("med = " + str(med) + "  med*2 = " + str(2*med) + " =< day[" + str(day) + "] = " + str(expenditure[day]))
        if expenditure[day+1] >= (2 * med):
            notices += 1
        #print("\t" + str(notices))
    return notices

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
