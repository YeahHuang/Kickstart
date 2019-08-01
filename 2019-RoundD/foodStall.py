# -*- coding:utf-8 -*-
import copy 
import pprint as pp
from functools import reduce
import math

T = int(input())

debug = True

for it in range(T): #是空的case
    qpp = input().split(" ")
    K, N = int(qpp[0]), int(qpp[1])
    qpp = input().split(" ")
    x = [int(s) for s in qpp] #length = N
    qpp = input().split(" ")
    cost = [int(s) for s in qpp] #length = N
    #ware_idx = 0
    tmp_cost = [cost[i] + abs(x[i] - x[0]) for i in range(1, N)]
    tmp_cost.sort()
    ans = sum(tmp_cost[:K]) + cost[0]
    #ans = 4294967295 #INT_MAX 一开始因为自定义的INT_MAX其实并不是max 所以
    for ware_idx in range(1,N):
        tmp_cost = [cost[i] + abs(x[i] - x[ware_idx]) for i in range(N)]
        tmp_cost.pop(ware_idx)
        tmp_cost.sort()
        ans = min(ans, sum(tmp_cost[:K]) + cost[ware_idx])

    print("Case #%d: %s"%(it+1, ans))
