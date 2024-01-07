#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def childHelper(s1, s2):
    # This method doesn't work b/c it disregards a part of the string once a match has been made
    i1, j2, imatch = 0, 0, 0
    char1, char2 = '', ''
    child_len = 0
    match = False
    child = ""
    
    while (i1 < len(s1)):
        char1 = s1[i1]
        while (j2 < len(s2)):
            char2 = s2[j2]
            if char1 == char2:
                match = True
                imatch = j2
                child += char1
                child_len += 1
                break
            else:
                j2 += 1
        i1 += 1
        if match:
            j2 += 1
            match = False
        else:
            j2 = imatch + 1
            
    #print("i1 = " + str(i1) + ", j2 = " + str(j2) + " " + child)
    return child
    
def commonChild(s1, s2):
    # Write your code here
    # (1) have two ptrs iterating through the strs, incrementing when there is a matching char
    no_visit = s1
    substrings = {}
    max_len = 0
    set1 = set()
    set2 = set(s2)
    child = ""

    for i1 in range(len(s1)):
        if s1[i1] in set2:
            child = childHelper(s1[i1:], s2)
            substrings[child] = len(child)
            max_len = max(max_len, substrings[child])
        
    print(substrings)
    
    return max_len
    
    # n = len(s1)
    # char1, char2 = 0, 0
    # i1, i2 = 0, 0
    # while (i1 < n):
    #     char1 = s1[i1]
    #     while (i2 < n):
    #         char2 = s2[i2]
    #         if char1 == char2:
               
           
    
    # (1.5) naive way - O(n2)
    
    # children = {}
    # for char1 in s1:
    #     for char2 in s2:
    #         if char1 == char2:
                
    # (2) have dict of chars and indeces, count the matching chars with inc index to keep order

    # s1_dic, s2_dic = {}, {}
    # s1_len = len(s1)
    # s2_len = len(s2)
    
    # for i in range(max(s1_len, s2_len)):
    #     if (i < s1_len):
    #         if not s1[i] in s1_dic:
    #             s1_dic[s1[i]] = []
    #         s1_dic[s1[i]].append(i)
    #     if (i < s2_len):
    #         if not s2[i] in s2_dic:
    #             s2_dic[s2[i]] = []
    #         s2_dic[s2[i]].append(i)
    
    # (3) DP solution
    # dynamic programming (bottom-up approach), longest common subsequence
    n = len(s1) + 1

    lcs_mat = [[0 for j in range(len(s1)+1)] for j in range(len(s2)+1)]
    
    for i in range(len(s1)-1, -1, -1):
        for j in range(len(s2)-1, -1, -1):
            if s1[i] == s2[j]:
                lcs_mat[i][j] = 1 + lcs_mat[i+1][j+1]
            else:
                lcs_mat[i][j] = max(lcs_mat[i][j+1], lcs_mat[i+1][j])
                        
    print(lcs_mat)
    return lcs_mat[0][0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
