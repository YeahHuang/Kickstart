
T = int(input())
debug = False

global hash_map, mentor_cnt

def dfs(step, n, cur, skills):
    global hash_map, mentor_cnt
    if step == n:
        mentor_cnt += hash_map.get(tuple(cur), 0)
    else:
        dfs(step+1, n,  cur, skills)
        cur.append(skills[step])
        dfs(step+1, n, cur, skills)
        cur.pop()

for it in range(T):  
    n, s = map(int, input().split())
    skills = [set([]) for _ in range(s+1)]
    A, ans= [], 0
    hash_map = {}
    for i in range(n):
        row = list(map(int, input().split()))
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
