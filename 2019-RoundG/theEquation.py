from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

T = int(input())

for it in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = -1
    for i in range(128, -1, -1):
        if sum([num^i for num in a])<=m:
            ans = i
            break
    print("Case #%d: %d"%(it+1, ans))