from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random
import sys

global debug, test
"""
n(students number) p(pick number)

s1..sn skills[i]

= 区间和 - max() * p 

7min
大的主要是max问题 

28min 提交第一次 WA了 不是很知道为什么 
45min solve_small 也WA 不知道为什么 不管了先坐后头的

1‘22的时候 后来忽然发现读题错误 很快就pass了 1e5 nlgn直接过的

一开始题目理解错 并没有说要取连续的p个呀～
所以我错误的开始觉得是一个RMQ问题 ans = min( max(s[i:i+p]) * p - sum(s[i:i+p])  ) 
不会RMQ（有机会可以补一下） 我还机智的想出了heappop出的max直接check是不是最大的就行了的方法
可惜 哎 方向比速度更重要啊
其实直接sort一下 算一算 10min 就over了emmmm
"""
def solve():
    global debug, test

T = int(input())
debug = False
test = True

def solve_small(n, p, s):
    ans = float('inf')
    s.sort()
    summ = sum(s[:p])
    ans = s[p-1]*p - summ
    for i in range(1, n-p+1):
        summ = summ - s[i-1] + s[i+p-1]
        ans = min(ans, s[i+p-1]*p - summ)
    return ans
    # for i in range(n-p+1):
    #     summ = sum(s[i:i+p])
    #     maxm = max(s[i:i+p])
    #     ans = min(ans, maxm*p - summ)
    return ans

def solve_wrong_RMQ(n, p, s):
for it in range(T):
    n, p = map(int, input().split())
    s = list(map(int, input().split()))
    ans = solve_small(n, p,s)
    

    
    print("Case #%d: %d"%(it+1, ans))
    continue
    summ = sum(s[:p])
    maxm = [(-si, i) for i, si in enumerate(s[:p])]
    heapify(maxm)
    ans =  maxm[0][0]*(-1)*p - summ
    
    for i in range(1, n-p+1):
        
        summ = summ - s[i-1] + s[i+p-1]
        heappush(maxm,(-s[i+p-1], i+p-1))
        if debug:
            print("from %d to %d summ=%d"%(i,i+p-1, summ))
            print("maxm:", maxm)
        while maxm[0][1] < i:
            heappop(maxm)
        ans = min(ans, -maxm[0][0]*p - summ)
        # while True: 一开始直接把最大的pop出来了 是不对的 后头还是要用的呀 只能取最前头的
        #     num, idx = heappop(maxm)
        #     if idx >= i:    #in range:
        #         ans = min(ans,  (-num)*p - summ)
        #         if debug:
        #             print("current max num=%d idx=%d ans=%d"%(-num, idx, ans))
        #         break