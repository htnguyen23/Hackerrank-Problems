#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    # ticket position compared to/subtracted from array len = bribe
    totalBribe, bribe, curr = 0, 0, 0
    n = len(q)
    #debug = 0
    #tc_flag = False
    for i in range(n):
        #print(q[:i+1])
        bribe = 0
        curr = q[i]
        if (curr > (i+1)):
            bribe = abs(curr - (i+1))
        totalBribe += bribe
        #debug += curr - (i+1)
        #print("i: " + str(i+1) + "  curr: " + str(curr) + "  pos: " + str(curr - (i+1)) + "  bribe: " + str(bribe) + "  totalBribe: " + str(totalBribe))
        if bribe > 2:
            totalBribe = "Too chaotic"
            break
        #print("")
    #print(debug)
    print(totalBribe)
    #print("")

'''
    bribes = flag = 0
    while (q != sorted(q)):
        for i in range(len(q)-1):
            if abs(q[i]-1-i) > 2:
                flag = 1
                break
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                bribes += 1
        if flag == 1:
            print("Too chaotic")
            break
    if flag == 0:
        print(bribes)
'''
         

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
