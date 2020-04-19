from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
"""

H - m
W - n

(l,u) - (r,d) removed

小的暴力 大的 1e5 找规律 看一下分布？ 

我的第一遍想法不ok 可以先暴力

7:32 -  7:47 WA 想法不对 先看另一题
 W, H, L, U, R and D.
"""
T = int(input())
debug = True
for it in range(T):
    w, h, l, u, r, d = map(int, input().split())
    l, u, r, d = l-1, u-1, r-1, d-1
    f = [[0.0]*h for _ in range(w)]

    f[0][0] = 1.0

    for i in range(w-1):
        for j in range(h-1):
            if (l<=i<=r and u<=j<=d)==False:
                f[i+1][j] += 0.5 * f[i][j]
                f[i][j+1] += 0.5 * f[i][j]

    j = h-1
    for i in range(w-1):
        if (l<=i<=r and u<=j<=d)==False:
            f[i+1][j] += f[i][j]

    i = w - 1

    for j in range(h-1):
        if (l<=i<=r and u<=j<=d)==False:
            f[i][j+1] += f[i][j]

    # for i in range(1, w):
    #     for j in range(1, h):
    #         if l<=i<=r and u<=j<=d:
    #             f[i][j] = 0
    #         else:
    #             f[i][j] = (f[i][j-1] + f[i-1][j]) * 0.5
    if debug:
        print(f)
    ans = f[w-1][h-1]
    print("Case #%d: %.6f"%(it+1, ans))


"""
4
3 3 2 2 2 2
5 3 1 2 4 2
1 10 1 3 1 5
6 4 1 3 3 4
t = [[[0, 0] for _ in range(h)] for _ in range(w)] #0 good 1 bad
    t[0][0][0] = 1
    for i in range(1, w):
        if l<=i<=r and u==0:
            t[i][0][1] = t[i-1][0][0] + t[i-1][0][1]
        else:
            t[i][0][0] = t[i-1][0][0] + t[i-1][0][1]
    
    for j in range(1,h):
        if u<=j<=d and l == 0:
            t[0][j][1] = t[0][j-1][0] + t[0][j-1][1]
        else:
            t[0][j][0] = t[0][j-1][0] + t[0][j-1][1]
    if debug:
        print(t[0])
    for i in range(1, w):
        for j in range(1, h):
            if l<=i<=r and u<=j<=d:
                t[i][j][1] = t[i-1][j][0] + t[i-1][j][1] + t[i][j-1][0] + t[i][j-1][1] 
            else:
                t[i][j][0] = t[i-1][j][0] + t[i][j-1][0]
                t[i][j][1] = t[i-1][j][1] + t[i][j-1][1]  
        if debug:
            print(t[i])     

    ans = t[w-1][h-1][0] / (t[w-1][h-1][0] + t[w-1][h-1][1])
"""