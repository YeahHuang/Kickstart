from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

T = int(input())

for it in range(T):
    a = list(map(int, input().split()))
    global flag
    flag = False
    summ = sum(a)
    def dfs(step, cur, a, left_pos, couldBeOne):
      global flag
      #print(step+1, cur, left_pos)
      if step==9:
        if cur%11 == 0 and (left_pos==0 or (left_pos==1 and couldBeOne)):
          flag = True
        return
      if flag:
        return
      if a[step]==0:
        dfs(step+1, cur,a, left_pos, couldBeOne)
      else:
        for pos in range(min(left_pos, a[step])+1):
          dfs(step+1, cur + (step+1)*pos - (step+1)*(a[step]-pos),a, left_pos-pos, couldBeOne)

    dfs(0, 0, a, (summ+1)//2, summ&1)
    ans = "YES" if flag else "NO"
    print("Case #%d: %s"%(it+1, ans))