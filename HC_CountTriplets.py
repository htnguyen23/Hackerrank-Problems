#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # use dictionary to keep track of 1) index of num OR 2) num of occurences of num
    # count num of occurences of each num to find total combinations of sequences for triplets?
    num_count_dic = {}
    curr = 0
    curr_trip = []
    for i in range(len(arr)):
        # only count the numbers that satisfy common ratio r?
        curr = arr[i]
        if (curr % r) == 0:
            num_count_dic.setdefault(arr[i], 0)
            num_count_dic[arr[i]] += 1
        
    # how to find geometric triples in a sequence of unique ints
    for i in range(len(arr)):
        curr = arr[i]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
