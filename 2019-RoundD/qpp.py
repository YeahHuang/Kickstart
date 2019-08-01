# -*- coding:utf-8 -*-
import copy 
import pprint as pp
from functools import reduce
import math


def judgeEven(num: int) -> bool:
    #print("start to judge ", num)
    s = bin(num)[2:]
    cnt_1 = 0 
    for c in s:
        if c == '1':
            cnt_1 += 1
    return not(cnt_1 & 1)

T = int(input()) #细致的分析一下 我觉得可能 除去一个再配上一个 这中间是有bitwise的优化的 嗯

debug = False

for it in range(T): #是空的case
    qpp = input().split(" ")
    N, Q = int(qpp[0]), int(qpp[1])
    qpp = input().split(" ")
    a = [int(s) for s in qpp]
    ans = [0] * Q
    for i in range(Q):
        qpp = input().split(" ")
        if debug and i > 1:
            print("ans[%d]=%d"%(i-1, ans[i-1]))
        a[int(qpp[0])] = int(qpp[1])
        for j in range(N, 0, -1): #长度
            cur_sum = 0
            for tmp in range(0, j):
                cur_sum ^= a[tmp]
            if judgeEven(cur_sum):
                ans[i] = j
                break
            for k in range(1, N-j+1):
                cur_sum = cur_sum ^ a[k-1] ^ a[k+j-1]
                if judgeEven(cur_sum):
                    ans[i] = j
                    break
            if ans[i]:
                break
    print("Case #%d:"%(it+1),end="")
    for num in ans:
        print(" %d"%num, end="")
    print()