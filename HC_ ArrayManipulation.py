#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    
    # (1) naive method
    # arr = [0 for x in range(n)]
    # start, stop, summand, max_val = 0, 0, 0, 0
    # for q in queries:
    #     start = q[0] - 1
    #     stop = q[1]
    #     summand = q[2]
    #     for i in range(start, stop):
    #         arr[i] += summand
    #         max_val = max(arr[i], max_val)
    #     #print(arr)
             
    # return max_val
    
    # (2) array slicing -> array addition (list comprehension) is linear runtime
    # arr = [0 for x in range(n)]
    # temp = []
    # start, stop, summand, max_val = 0, 0, 0, 0
    # for q in queries:
    #     start = q[0] -1
    #     stop = q[1]
    #     summand = q[2]
    #     # left arr, target arr, right arr
    #     temp = [x + summand for x in arr[start:stop]]
    #     arr = arr[:start] + temp + arr[stop:]
    
    # (3) using a dict
    # arr_dict = {} # {f'{i}': 0 for i in range(n)}
    # for i in range(n):
    #     arr_dict[i] = 0
    # start, stop, summand, max_val = 0, 0, 0, 0
    # for q in queries:
    #     start = q[0] -1
    #     stop = q[1]
    #     summand = q[2]
    
    # (4) keep a max and i and check each iter if a summand has been added in the past
    start, stop, summand = 0, 0, 0
    max_val = queries[0][2]
    max_i = [queries[0][0], queries[0][1]]
    for i in range(1, len(queries)):
        start = queries[i][0] -1
        stop = queries[i][1]
        summand = queries[i][2]
        
        if (start >= max_i[0]) and (stop <= max_i[1]):
            max_val += summand
            max_i = [start, stop]
            
        # what if the curr summand is greater than the prev summands?
        max_val = max(summand, max_val)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
