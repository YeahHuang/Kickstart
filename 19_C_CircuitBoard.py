# -*- coding:utf-8 -*-
import copy 
import pprint as pp
from functools import reduce
import math


T = int(input())

debug = True

for it in range(T):
    qpp = input().split(" ")
    R, C, K = int(qpp[0]), int(qpp[1]), int(qpp[2])
    max_len = [[1] * C for _ in range(R)]
    dp = [[[0]] * C for _ in range(R)]
    ans = 0 
    for i in range(R):
        qpp = input().split(" ")
        for j in range(1, C):
            if qpp[j]==qpp[j-1]:
                max_len[i][j] = max_len[i][j-1] + 1
    for j in range(C):
        print(max_len[0][j], dp[0][j])
        for k in range(max_len[0][j]):
            dp[0][j].append(1)
    ans = max(max_len[0])
    if debug:
        print(max_len)
        print(dp[0])
    for i in range(1,R):
        dp[i][0].append(1)
        for j in range(1,C):
            if max_len[i-1][j] >= max_len[i][j]:
                dp[i][j] = map(lambda x: x+1, dp[i-1][j][:max_len[i][j]+1])
            else:
                dp[i][j] = list(map(lambda x: x+1, dp[i-1][j][:max_len[i-1][j]+1])) + ([1]*(max_len[i][j] - max_len[i-1][j]))
            ans = max(ans,  max(k*num  for k,num in enumerate(dp[i][j])))
            if debug:
                print(i,j,ans)
                print(dp[i][j])
    print("Case #%d: %d"%(it+1, ans))