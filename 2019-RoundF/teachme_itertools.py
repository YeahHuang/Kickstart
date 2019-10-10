from itertools import chain, combinations

def powerset(l):
    return chain.from_iterable(combinations(l, r) for r in range(len(l)+1))


def solve(N, S, skills):
    d = {}
    dd = {}
    for r in skills:
        print("skill: ", r)
        for x in powerset(r):  #dd[x]记录会这个skill的有几人？
            print("x: ",x) #跟踪得知这个其实会返回它全部的子集
            if x in dd:
                dd[x] += 1
            else: dd[x] = 1

        if r in d: #d[r]记录了同等skill(r)的有几人 
            d[r] += 1
        else: d[r] = 1

    g = 0
    for k,v in d.items():
        g += v * (N - dd[k]) # dd[k]表示k不可以教多少人(即k是多少个人的子集)  v是k这样状态的有多少种。 所以v*(n-dd[k])就是我们要的
    return g


#T = int(raw_input().strip())
T = int(input())
for i in range(T):
    #N, S = map(int, raw_input().strip().split())
    N, S = map(int, input().split())
    skills = []
    for j in range(N):
        #l = map(int, raw_input().strip().split())
        l = list(map(int, input().split()))
        skills.append(tuple(sorted(l[1:])))
    res = solve(N, S, skills)
    print('Case #' + str(i + 1) + ': ' + str(res))

'''
https://docs.python.org/2/library/itertools.html
chain('ABC', 'DEF') --> A B C D E F
product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2) --> AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2) --> AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2) --> AA AB AC AD BB BC BD CC CD DD  
'''