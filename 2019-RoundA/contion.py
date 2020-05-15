from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random
import sys
"""
1'47 火速提交 但是好像不行 

"""
global debug, test

def solve():
    global debug, test

T = int(input())
debug = True
test = True
for it in range(T):
    n, q = map(int, input().split())
    li = [tuple(map(int, input().split())) for _ in range(q)]
    li.sort(key=lambda x: x[1]-x[0])
    f = [True] * (n+1)
    ans = n
    for l, r in li:
        cur = 0 
        for i in range(l, r+1):
            cur += int(f[i])
            f[i] = False
        ans = min(ans, cur)
    print("Case #%d: %d"%(it+1, ans))
