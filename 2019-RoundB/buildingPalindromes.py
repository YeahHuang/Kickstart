from bisect import bisect_left


T = int(input())

mydict = {}
for i in range(ord('A'),ord('Z')+1):
    mydict[chr(i)] = 1<<(i-ord('A'))
valid = set([0] + [v  for _, v in mydict.items()])
for it in range(T):
    n, q = map(int, input().split())
    ans = 0
    blocks = input()
    f = [0] * n
    for i, c in enumerate(blocks):
        f[i] = (f[i-1] if i else 0) ^ mydict[c]
    #print(f)
    for i in range(q):
        l, r = map(int, input().split())
        l, r = l-1, r-1
        delta_sum = f[r] ^ (f[l-1] if l else 0)
        if delta_sum in valid:
            ans += 1
            #print("valid", l+1, r+1)
    print("Case #%d: %d"%(it+1, ans))
