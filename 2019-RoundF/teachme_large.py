from bisect import bisect_left
from collections import defaultdict
from functools import reduce
from copy import deepcopy

T = int(input())
debug = False

for it in range(T):  
    n, s = map(int, input().split())
    skills = [set([]) for _ in range(s+1)]
    A, ans, memo = [], 0, [[set([-1])]*(s+1) for _ in range(s+1)]
    for i in range(n):
        row = list(map(int, input().split()))
        tmp = sorted(row[1:])
        A.append([row[0]]+tmp)
        for skill in tmp:
            skills[skill].add(i)
    if debug:
        print("A:",A)
        print("Skills:",skills)
    for r in A:
        if r[0] == 1:
            ans += n - len(skills[r[1]])
        elif r[0] == 2:
            if -1 in memo[r[1]][r[2]]:
                memo[r[1]][r[2]] = skills[r[1]] & skills[r[2]]
            ans += n - len(memo[r[1]][r[2]])
        elif r[0] == 3:
            if -1 in memo[r[1]][r[2]]:
                memo[r[1]][r[2]] = skills[r[1]] & skills[r[2]]
            ans += n - len(memo[r[1]][r[2]] & skills[r[3]])
        elif r[0] == 4:
            if -1 in memo[r[1]][r[2]]:
                memo[r[1]][r[2]] = skills[r[1]] & skills[r[2]]
            if -1 in memo[r[3]][r[4]]:
                memo[r[3]][r[4]] = skills[r[3]] & skills[r[4]]
            ans += n - len(memo[r[1]][r[2]]&memo[r[3]][r[4]])
        else:
            if -1 in memo[r[1]][r[2]]:
                memo[r[1]][r[2]] = skills[r[1]] & skills[r[2]]
            if -1 in memo[r[3]][r[4]]:
                memo[r[3]][r[4]] = skills[r[3]] & skills[r[4]]
            ans += n - len(memo[r[1]][r[2]]&memo[r[3]][r[4]]&skills[r[5]])
        if debug:
            print("For row = ",r, "ans=",ans)

        #ans += n - len(inter)
        
    print("Case #%d: %d"%(it+1, ans))

