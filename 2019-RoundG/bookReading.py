from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

T = int(input())

for it in range(T):
    n,m,q = map(int, input().split())
    p = list(map(int, input().split()))
    r = list(map(int, input().split()))
    ans = 0
    flag = [1] * (n+1)
    for i in range(m):
        flag[p[i]] = 0
    for i in range(q):
        for j in range(r[i], n+1, r[i]):
            ans += flag[j]
    print("Case #%d: %d"%(it+1, ans))