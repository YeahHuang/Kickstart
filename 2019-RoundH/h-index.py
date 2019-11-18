from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product


T = int(input())

for it in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [1] * n
    qpp = []
    cnt = n
    for i in range(n):
      insort_left(qpp,a[i]) #qpp: [0..i] 共 i+1个 
      #target: ans[i-1] + 1 
      #i-target+1 = i-ans[i-1]
      if i and qpp[i - ans[i-1]] >= ans[i-1] + 1:
        ans[i] = ans[i-1] + 1
      else:
        ans[i] = ans[i-1]
        cnt -= 1

    print("Case #%d:"%it, end="")
    for num in ans:
      print(" %d"%num, end="")
    print()
