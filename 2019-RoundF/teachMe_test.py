from bisect import bisect_left
from collections import defaultdict
from functools import reduce
from copy import deepcopy
from time import time
from random import randint 
#T = int(input())
T = 10
debug = False
start = time()
'''
#47s
for it in range(T):  
    #n, s = map(int, input().split())
    n, s = 5*int(1e4), 1000
    skills = [set([]) for _ in range(s+1)]
    A, ans= [], 0
    hash_map = {}
    for i in range(n):
        #row = list(map(int, input().split()))
        row = [5] + [randint(1,1000) for _ in range(5)]
        tmp = sorted(row[1:])
        hash_map[tuple(tmp)] = hash_map.get(tuple(tmp),0) + 1
        A.append([row[0]]+tmp)
    for row in A:
        mentor_cnt = 0 
        for i in range((1<<row[0])):
            cur = []
            for j in range(row[0]):
                if i&(1<<j):
                    cur.append(row[j+1])
            mentor_cnt += hash_map.get(tuple(cur), 0)
        #dfs(0, row[0], [], row[1:])
        ans += n - mentor_cnt
        #print(mentor_cnt, row, ans)
    print("Case #%d: %d"%(it+1, ans))

#15s
for it in range(T):  
    #n, s = map(int, input().split())
    n, s = 5*int(1e4), 1000
    skills = [set([]) for _ in range(s+1)]
    A, ans, memo = [], 0, [[{-1}]*(s+1) for _ in range(s+1)]
    for i in range(n):
        #A.append(list(map(int, input().split()))) Edit
        #row = list(map(int, input().split()))
        row = [5] + [randint(1,1000) for _ in range(5)]
        tmp = sorted(row[1:])
        A.append([row[0]]+tmp)
        #A.append([randint(1,1000) for _ in range(6)])
        for skill in A[i][1:]:
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
    print("Case #%d: %d"%(it+1, ans))
'''

CONST = 1007
for it in range(T):  
    #n, s = map(int, input().split())
    n, s = 5*int(1e4), 1000
    skills = [set([]) for _ in range(s+1)]
    A, ans= [], 0
    hash_map = {}
    for i in range(n):
        #row = list(map(int, input().split()))
        row = [5] + [randint(1,1000) for _ in range(5)]
        tmp = sorted(row[1:])
        key = reduce(lambda x,y: x*CONST+y, tmp, 0)
        hash_map[key] = hash_map.get(key,0)+1
        #hash_map[tuple(tmp)] = hash_map.get(tuple(tmp),0) + 1
        A.append([row[0]]+tmp)
    for row in A:
        mentor_cnt = 0 
        for i in range((1<<row[0])):
            cur = 0
            for j in range(row[0]):
                if i&(1<<j):
                    cur = cur*CONST + row[j+1]
            mentor_cnt += hash_map.get(cur, 0)
        #dfs(0, row[0], [], row[1:])
        ans += n - mentor_cnt
        #print(mentor_cnt, row, ans)
    print("Case #%d: %d"%(it+1, ans))
print("Time used: ",time()-start)