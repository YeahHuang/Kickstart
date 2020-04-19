from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

T = int(input())

for it in range(T):
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1,n-1):
        if p[i+1]<p[i] and p[i]>p[i-1]:
            ans+=1
    print("Case #%d: %d"%(it+1, ans))