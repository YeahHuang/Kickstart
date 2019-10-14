
'''
N energy stones  1次吃1个 Si seconds

Ei 初始能量
Li 每秒lose的能量
开始即获得所有
'''
from collections import namedtuple
from functools import cmp_to_key
T = int(input())
Stone = namedtuple('Stone',['s','e','l','maxs']) #https://docs.python.org/3.7/library/collections.html#collections.namedtuple
debug = False
for it in range(T):
    n, ans = int(input()), 0 
    stones = []
    for i in range(n):
        s,e,l = map(int, input().split())
        if l == 0:
            ans += e
        else:
            stones.append(Stone(s,e,l,e//l+s))
    n = len(stones)
    if n == 0:
        print("Case #%d: %d"%(it+1, ans))
        continue
    #base_ans = ans
    #ans = 0
    #stones.sort(key = lambda x: x.l, reverse = True)    
    stones.sort(key = cmp_to_key(lambda x,y: 1 if x.l*y.s<x.s*y.l else -1)) #确认一下对不对
    max_time = min(sum([stone.s for stone in stones]),max([stone.maxs for stone in stones]))
    #print(stones)
    #print("ans, max_time, max_eat_cnt: ",ans, max_time, max_eat_cnt)
    f = [[0]*(max_time+1) for _ in range(n)]
    for i in range(n):
        curs = stones[i].s
        if i:
            f[i][:curs] = f[i-1][:curs]
        for j in range(curs, min(max_time,stones[i].maxs)+1):
            f[i][j] = max((f[i-1][j-curs] if i else 0) + max(0, stones[i].e - (stones[i].l * (j-curs))), f[i-1][j] if i else 0, f[i-1][j])
        #ans = max(ans, max(f[i]))
        #print(f[i],ans)
    #ans += base_ans
    print("Case #%d: %d"%(it+1, ans+f[-1][-1]))

