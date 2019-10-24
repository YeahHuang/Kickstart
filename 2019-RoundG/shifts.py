from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

global ans
global a,b,suma, sumb, n, h
def dfs(i, cur_a, cur_b):
    global ans,a,b,suma, sumb, n, h
    #print(i, cur_a, cur_b)
    if cur_a>=h and cur_b>=h:
        ans += 3**(n-i)
        return 
    if (i<n) and (suma[-1]-suma[i]+cur_a>=h) and (sumb[-1]-sumb[i]+cur_b>=h):
        dfs(i+1, cur_a+a[i], cur_b)
        dfs(i+1, cur_a, cur_b+b[i])
        dfs(i+1, cur_a+a[i], cur_b+b[i])

T = int(input())

for it in range(T):
    n, h = map(int, input().split())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    tmp = []
    for i in range(n):
        tmp.append((aa[i],bb[i]))
    tmp.sort(reverse=True)
    a,b = [],[]
    for i in range(n):
        a.append(tmp[i][0])
        b.append(tmp[i][1])
    suma, sumb = [0] * (n+1), [0]*(n+1)
    for i in range(n):
        suma[i+1] = suma[i] + a[i]
        sumb[i+1] = sumb[i] + b[i]
    ans = 0
    dfs(0, 0, 0)
    print("Case #%d: %d"%(it+1, ans))
