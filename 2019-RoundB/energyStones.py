
'''
N energy stones  1次吃1个 Si seconds

Ei 初始能量
Li 每秒lose的能量
开始即获得所有
'''
from collections import namedtuple

T = int(input())
Stone = namedtuple('Stone',['s','e','l']) #https://docs.python.org/3.7/library/collections.html#collections.namedtuple
debug = False
for it in range(T):
    n, ans = int(input()), 0 
    stones = []
    for i in range(n):
        s,e,l = map(int, input().split())
        if l == 0:
            ans += e
        else:
            stones.append(Stone(s,e,l))
    n = len(stones)
    if n == 0:
        print("Case #%d: %d"%(it+1, ans))
        continue
    stones.sort(key = lambda x: x.l, reverse = True)    
    sec = stones[0].s
    max_time = max(map(lambda x: x.e // x.l, stones)) + 1
    max_eat_cnt = max_time//sec + 1
    #print(stones)
    #print("ans, max_time, max_eat_cnt: ",ans, max_time, max_eat_cnt)
    f = [[0]*(max_eat_cnt+1) for _ in range(n)]
    for i in range(n):
        for j in range(1, max_eat_cnt+1):
            f[i][j] = max((f[i-1][j-1] if i else 0) + max(0, stones[i].e - (stones[i].l * sec * (j-1))), f[i-1][j] if i else 0, f[i][j-1])
        #print(f[i])
    print("Case #%d: %d"%(it+1, ans + f[-1][-1]))

