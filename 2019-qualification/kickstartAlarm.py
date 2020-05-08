"""
 
 7:35 - 
 7:54 洗脸去 

 N, K, x1, y1, C, D, E1, E2 and F
 
 n length of A  k(number of wakeup calls)
 
 
xi = ( C × xi-1 + D × yi-1 + E1 ) modulo F.
yi = ( D × xi-1 + C × yi-1 + E2 ) modulo F.

We define Ai = ( xi + yi ) modulo F, for all i = 1 to N.

ai = ((c+d) * (ai-1) + (e1+e2))  % f

output power (the summation of POWERi[1..k] mod (1e9+7)


x, y, c, d, e, f [1,1e5]
小：  n 1..100 k 1..20
大： n 1..1e6 k 1..1e4

同18 C 最后一题 

关键是按照啥来合并同类项

subarray length [1..n]       idx : idx + subarray length [idx , idx + subarray length-1]
cnt[i][j] 位置i 在第j个出现了几次
  sum[j] =  j = 2  2**1.. 2**2 ...2**k  s = j * ( 1- j**(k)) / ( 1 - j)  [1..n]
   cnt[i][j] * num[i] * sum[j]

8:29 1st submit
"""

from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random
import sys

global debug, test, MOD

def solve():
    global debug, test

def power(j, k):
    global MOD
    if k == 0:
        return 1
    res = j
    curk = 1
    while curk*2 <= k:
        res = res * res
        curk *= 2
    return res * power(j, k-curk) 

def multi(a, b, mod):
    ans = 0
    a %= mod
    while b:
        if (b%2==1):
            ans = (ans + a )% mod
            b -= 1
        b = b // 2
        a = (a + a) % mod
    return ans


def quick_mod(a, b, mod):
    res = 1
    while (b):
        if (b%2==1):
            res = multi(res, a, mod)
        b =b // 2
        a = multi(a, a, mod)
    return res

T = int(input())
debug = True
test = True

MOD = int(1e9 + 7)
#summ = [(power(j, k+1) - j) // (j-1) % MOD if j!=1 else k for j in range(n+1)]
for it in range(T):
    n, k, x1, y1, c, d, e1, e2, f = map(int, input().split())
    a = [(x1+y1)%f]
    for i in range(n-1):
        a.append((a[-1]*(c+d)+(e1+e2))%f)
    #意外的TLE了 其实这里不是o(n) 是o（nk）了
    #summ = [j * (1 - j**k) // (1-j) % MOD if j!=1 else k for j in range(n+1)]
    #summ = [(power(j, k+1) - j) // (j-1) % MOD if j!=1 else k for j in range(n+1)]
    summ = [0, k]
    # // 首项为 1 ， 公比为 a，长度 为 b 的等比数例求和
    # printf("%I64d\n",((quick_mod(a,b,mod*(a-1)) - 1) / (a-1)));

    for j in range(2, n+1):
        summ.append((quick_mod(j, k+1, MOD*(j-1))-1)//(j-1)-1)

    # cnt = [[0]*(n+1) for _ in range(n+1)]

    # for subLength in range(1, n+1): #n*n*n
    #     for start in range(0, n - subLength+1):
    #         for i in range(subLength):
    #             cnt[start+i][i+1] += 1

    ans = 0

    cur_summ = 0 
    for i in range(n):
        #cnt[i][j] == n - i 
        cur_summ = (cur_summ + summ[i+1])%MOD
        ans = (ans + cur_summ * (n-i) * a[i]) % MOD
        # for j in range(1, i+2):  #n*n 
        #     ans = (ans + cnt[i][j] * a[i] * summ[j] ) % MOD
        # if debug:
        #     print("cnt[",i,"]: ", cnt[i])
    print("Case #%d: %d"%(it+1, ans))








