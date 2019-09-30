
from collections import defaultdict

T = int(input())
debug = False
for it in range(T):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    if k>=n-1:
        print("Case #%d: 0"%(it+1))
        continue
    same_cnt = [[0]*n for _ in range(n)]
    for i in range(n): 
        c = defaultdict()
        maxn = 0
        for j in range(i, n):
            c[A[j]] = c.get(A[j], 0) + 1 #这里一开始用自带的most_common 改成自己的后 19s->16s
            maxn = max(maxn, c[A[j]])
            same_cnt[i][j] = j-i+1 - maxn
            
    f = [[0]*(k+1) for _ in range(n)]
    for i in range(n):
        f[i][0] = same_cnt[0][i]
    for j in range(1, k+1):
        for i in range(j+1, n): #这里从i in range(n) 到 j+1..n 16s->9s
            f[i][j] = min([f[ii][j-1] + same_cnt[ii+1][i] for ii in range(i)]+[f[i][j-1]])
    if debug:
        print(f)
    print("Case #%d: %d"%(it+1, f[n-1][k]))


