from bisect import bisect_left
from collections import Counter, defaultdict
from time import time
start = time()
T = 100
debug = False
for it in range(T):
    #n, k = map(int, input().split())
    n, k = 100, 9
    A = [i for i in range(n)]
    #A = list(map(int, input().split()))
    same_cnt = [[0]*n for _ in range(n)]
    for i in range(n): #Edited: 
        c = defaultdict()
        maxn = 0
        for j in range(i, n):
            c[A[j]] = c.get(A[j], 0) + 1
            maxn = max(maxn, c[A[j]])
            same_cnt[i][j] = j-i+1 - maxn
            
    f = [[0]*(k+1) for _ in range(n)]
    for i in range(n):
        f[i][0] = same_cnt[0][i]
    for j in range(1, k+1):
        for i in range(j+1, n):
            f[i][j] = min([f[ii][j-1] + same_cnt[ii+1][i] for ii in range(i)]+[f[i][j-1]])
    if debug:
        print(f)
    print("Case #%d: %d"%(it+1, f[n-1][k]))


print("Time used: ",time()-start)
