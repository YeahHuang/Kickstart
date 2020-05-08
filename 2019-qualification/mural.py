from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random
import sys

global debug, test

def solve():
    global debug, test
"""
at least b beauty
n sections long
n digits of beauty score 
小： n [2,100]
大的 有一个是5*1e6

7:13 - 7:35 
两头加起来  要 >= 中间length - 1 
"""

T = int(input())
debug = True
test = True
for it in range(T):
    n = int(input())
    s = input()
    summ = [0] * (n+1) #sum[i+1] == sum(0..i)
    for i in range(n):
        summ[i+1] = summ[i] + int(s[i])
    length = (n+1)//2
    ans = max([summ[i+length] - summ[i] for i in range(n-length+1)])
    print("Case #%d: %d"%(it+1, ans))


