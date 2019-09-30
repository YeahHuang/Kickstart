class DSU: #Disjoint Set Union 就是常见的染色问题
    def __init__(self,n):
        self.p = {}
        for i in range(1,n+1):
            self.p[i] = i

    def find(self, x):
        stack = []
        while self.p[x] != x:
            stack.append(x)
            x = self.p[x]
        for xx in stack:
            self.p[xx] = x
        '''
        if self.p[x] != x:  #RE because of too much depth
            self.p[x] = self.find(self.p[x])
        '''
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if y == py:
            self.p[px] = self.p[py]
        else:
            self.p[py] = self.p[px]
        return px!=py

import copy 
import pprint as pp
from functools import reduce
import math

T = int(input())

debug = False

for it in range(T): 
    n, m = map(int, input().split())
    #n, m = 100000, 99998
    dsu = DSU(n)
    ans = 0
    for t in range(m):
        c, d = map(int, input().split())
        #c, d = 1, t+2
        ans += dsu.union(c,d)
    if debug:
        print(dsu.p)
    ans += 2*(len(set([dsu.find(k) for k, v in dsu.p.items()]))-1)
    print("Case #%d: %d"%(it+1, ans))
