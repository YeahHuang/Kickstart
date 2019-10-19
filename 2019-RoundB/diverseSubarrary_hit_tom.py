'''
N trinkets 1..N   type Ai(positive)

consecutive interval of trinkets [l, r]
某一类的数量>S 都throw away
'''
import collections

global ma, lazy,b

def pushdown(i):
    global ma, lazy
    if lazy[i]:
        ma[i<<1] += lazy[i]
        ma[i<<1 | 1] += lazy[i]
        lazy[i<<1] += lazy[i]
        lazy[i<<1 | 1] += lazy[i]
        lazy[i] = 0

def pushup(i):
    global ma
    ma[i] = max(ma[i<<1] , ma[i<<1|1])

def build(i, l, r):
    global lazy, ma, b
    lazy[i] = 0
    if l == r:
        ma[i] = b[l]
    else:
        mid = l+r >> 1
        build(i<<1, l, mid)
        build(i<<1|1, mid+1, r)
        pushup(i)

def update(i, l, r, x, y, value):
    global ma, lazy
    if x<=l<=r<=y:
        ma[i] += value
        lazy[i] += value
    else:
        pushdown(i)
        mid = l+r >> 1
        if x<=mid: 
            update(i<<1, l, mid, x, y, value)
        if mid<y:
            update(i<<1|1, mid+1, r, x, y, value)
        pushup(i)

def query(i, l, r, x, y):
    if x<=l<=r<=y:
        res = ma[i]
    else:
        res = 0
        pushdown(i)
        mid = l+r>>1
        if x<=mid:
            res = query(i<<1, l, mid, x, y)
        if mid < y:
            res = max(res, query(i<<1|1, mid+1, r,x, y))
    return res

T = int(input())
#Seg = collections.namedtuple('Seg',['value','mark'])

for it in range(T):
    n, s = map(int, input().split())
    types = list(map(int, input().split())) #一开始忘记加list 会报错TypeError: 'map' object is not subscriptable
    b,rec = [0]*(n+1), [0]*(n+1)
    ma, lazy = [0]*(n*4+4),[0]*(n*4+4)
    m = collections.defaultdict(list)
    for i in range(1,n+1):
        a = types[i-1]
        m[a].append(i) 
        rec[i] = len(m[a])        #每一个最后都pushback(n+1)
        if len(m[a]) == s+1:
            b[i] = b[i-1] - s
        elif len(m[a]) <= s:
            b[i] = b[i-1] + 1
        else:
            b[i] = b[i-1]
    '''
    for k in m.keys():
        m[k].append(n+1)
    '''
    build(1,1,n)  
    ans = 0
    #ans = query(1,1,n,1,n)
    for l in range(1, n+1):
        '''
        ans = max(ans, query(1, 1, n, l, n))
        a = types[l-1]
        if rec[l] + s < len(m[a]):
            x = rec[l] + s - 1
            update(1,1,n, l,m[a][x]-1, -1)
            update(1,1,n, m[a][x], m[a][x+1]-1,s)
        else:
            update(1,1,n,l,n,-1)
        '''
        q = query(1, 1, n, l, n)
        #print(ma)
        #print(lazy)
        ans = max(ans, query(1, 1, n, l, n))
        a = types[l-1]
        if len(m[a])>s:
            update(1,1,n, l, m[a][s]-1, -1)
            update(1,1,n, m[a][s], (m[a][s+1]-1) if len(m[a])>s+1 else n,s)
        else:
            update(1,1,n,l,n, -1)
        m[a].pop(0)
        
        #ans = max(ans, query(1, 1, n, l, n))
        #ans = max(ans, seg[1].value + seg[1].mark)
    print("Case #%d: %d"%(it+1, ans))