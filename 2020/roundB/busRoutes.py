from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
n bus routes
ith bus route 每xi天跑一次  Xi, 2Xi, 3Xi

每一天可以take多辆bus

finish by day D 求最晚的乘第一班车的时间

贪心 直接算最后一次出现的时间？

n,d
1 line with n integers xi

"""

T = int(input())

for it in range(T):
    n, d = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n-1, -1, -1):
        x = p[i]
        p[i] = d // x * x 
        d = p[i]
    #print(p)
    ans = p[0]
    print("Case #%d: %d"%(it+1, ans))