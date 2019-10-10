from bisect import bisect_left
from collections import defaultdict
from functools import reduce
from copy import deepcopy

T = int(input())
debug = False

for it in range(T):  
    n, s = map(int, input().split())
    skills = [set([]) for _ in range(s+1)]
    A,ans = [],0
    for i in range(n):
        A.append([list(map(int, input().split()))])
        for skill in A[i][1:]:
            skills[skill].add(i)
    if debug:
        print("A:",A)
        print("Skills:",skills)
    for r in A:
        if r[0] == 1:
            ans += n - len(skills[r[1]])
        elif r[0] == 2:
            if memo[r[1]][r[2]]==-1:
                memo[r[1]][r[2]] = len(skills[r[1]] & skills[r[2]])
            ans += n - len(memo[r[1]][r[2]])
        elif r[0] == 3:
            if memo[r[1]][r[2]]==-1:
                memo[r[1]][r[2]] = len(skills[r[1]] & skills[r[2]])
            ans += n - len(skills[r[1]] & skills[r[2]] & skills[r[3]])
        elif r[0] == 4:
            ans += n - len(skills[r[1]] & skills[r[2]] & skills[r[3]] & skills[r[4]])
        else:
            ans += n - len(skills[r[1]] & skills[r[2]] & skills[r[3]] & skills[r[4]] & skills[r[5]])

        #ans += n - len(inter)
        
    print("Case #%d: %d"%(it+1, ans))

