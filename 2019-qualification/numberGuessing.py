from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random
import sys

global debug, test
"""
迟到3min
p (a, b]
t

a=0, b
n
CORRECT TOO_SMALL TOO_BIG

WRONG_ANSWER
"""

def solve():
    global debug, test

T = int(input())
debug = True
test = True
out = open('hyh.txt','w') 
for it in range(T):
    _, b = map(int, input().split())
    n = int(input())
    l, r = 1, b
    while l <= r:
        mid = (l+r)//2
        print(mid)
        sys.stdout.flush()
        feedback = input()
        if feedback == "CORRECT":
            break
        elif feedback == "TOO_SMALL":
            l = mid + 1
        elif feedback == "TOO_BIG":
            r = mid - 1
        else:
            if debug:
                print("WRONG ANSWER WHEN OUTPUT=%d l = %d r = %d"%(mid, l, r), file=out)

out.close()