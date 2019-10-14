from bisect import bisect_left


T = int(input())

for it in range(T):
    l, r = map(int, input().split())
    ans = 0
    print("Case #%d: %d"%(it+1, ans))