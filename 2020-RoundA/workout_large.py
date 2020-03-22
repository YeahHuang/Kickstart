from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

T = int(input())


debug = False
for it in range(T):
    n,k = map(int, input().split())
    val = list(map(int, input().split()))
    gap = [0] * (n-1)
    for i in range(n-1):
        gap[i] = val[i+1] - val[i]
    if debug:
        print(gap)
    l, r = 1, max(gap)
    while (l<r):

        m = (l+r)//2
        if (debug):
            print(l,r,m)
        qpp = 0
        for i in range(n-1):
            if gap[i] > m:
                qpp += gap[i]//m - 1
                if gap[i]%m!=0:
                    qpp +=1
        if qpp <= k:
            r = m
        else:
            l = m + 1

    ans = l
    print("Case #%d: %d"%(it+1, ans))

