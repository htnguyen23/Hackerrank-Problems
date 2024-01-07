#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

'''ATTEMPT 1
def sherlockAndAnagrams(s):
    # Write your code here
    # use four ptrs to iterate through string to find potential substring
    # incr R ptr to find next matching char 
    # incr matchR & matchL ptr to get substring, sort substring, if substrings don't match, then is not ana pair
    # incr R until EOS, then incr L 
    # store pairs in dict
    ana_pairs = {}
    count = 0
    L = R = matchL = matchR = 0
    subL = subR = ""
    len_s = len(s)
    match_flag = True
    for L in range(len_s-1):
        for R in range(L+1, len_s):
            matchL, matchR = L, R
            if s[L] == s[R]:
                match_flag = True
                if (R == len_s - 1):
                    count += 1
                    print(str(count) + ": \"" + s[L] + "\" \"" + s[R] + "\"")
                    ana_pairs[s[L]] = [[L], [R]]
                    break
                while match_flag and (matchR <= len_s):
                    matchL += 1
                    matchR += 1
                    subL = "".join(sorted(s[L:matchL]))
                    subR = "".join(sorted(s[R:matchR]))
                    print(s[L:matchL] + "\t" + s[R:matchR])
                    if subL == subR:
                        count += 1
                        print(str(count) + " \n\t" + 
                              str(L) + ":" + str(matchL) + " \"" + s[L: matchL] + "\" \n\t" + 
                              str(R) + ":" + str(matchR) + " \"" + s[R: matchR] + "\"")
                        #ana_pairs[count] = [[L, matchL], [R, matchR]]
                        ana_pairs[subL] = [[L, matchL], [R, matchR]]
                    else:
                        match_flag = False

    return len(ana_pairs.keys())
'''

'''ATTEMPT 2'''

def sherlockAndAnagrams(s):
    # Write your code here
    # find all substring of s
    # store sorted substring in dict
    # find number of pairs in substring by triangular numbers 
    # -> formula: n=#occurrences (aka nth triangular number), ( (n-1)n ) / 2

    ana_pairs = {}
    sub = ""
    len_s = len(s)
    for L in range(len_s):
        for R in range(L, len_s):
            sub = s[L:R+1]
            #print(sub)
            sub = "".join(sorted(sub))
            ana_pairs.setdefault(sub, 0)
            ana_pairs[sub] += 1
        
    count = pairs = 0
    for occur in ana_pairs.values():
        pairs = sum(x for x in range(occur))    # or use formula: ((occur-1) * occur) / 2    
        count += int(pairs)

    print(ana_pairs)
    return count

                

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

q = int(input().strip())

for q_itr in range(q):
    s = input()

    result = sherlockAndAnagrams(s)

    print(str(result) + '\n')
