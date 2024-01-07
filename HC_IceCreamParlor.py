#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    # x + y = money
    # enumerate array to get indices and their complements?
    pair = [0, 0]
    # cost_dic = {value: i for i, value in enumerate(cost)}
    # for x in cost:
    #     if (money - x) in cost_dic and (cost_dic[x] != cost_dic[money - x]):
    #         pair = [cost_dic[x] + 1, cost_dic[money - x] + 1]
    #         break
    comp_dic = {}
    complement = 0
    for i, value in enumerate(cost):
        complement = money - value
        if complement in comp_dic:
            pair = [comp_dic[complement] + 1, i + 1]
        comp_dic[value] = i

    print(str(pair[0]) + " " + str(pair[1]))


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
