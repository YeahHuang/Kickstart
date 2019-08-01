#m = m % n
#全模拟
#N*N

T = int(input()) #细致的分析一下 我觉得可能 除去一个再配上一个 这中间是有bitwise的优化的 嗯

debug = False

for it in range(T): #是空的case #转一圈 和 刚好转一圈 和 M=0 的case 一定要自己先测试一下 
    qpp = input().split(" ")
    N, G, M = int(qpp[0]), int(qpp[1]), int(qpp[2])
    if M > 2*N:
        M = M%N + N
    H = [0] * G
    dx = [1] * G
    ans = [0] * G
    last_visit = [[] for i in range(N)]
    for i in range(G):
        qpp = input().split(" ")
        H[i] = int(qpp[0]) - 1
        if qpp[1]=='A':
            dx[i] = -1 #是C的话 do nothing
    if debug:
        print(H)
        print(dx)
        print(last_visit)
    for i, Hi in enumerate(H):
        last_visit[Hi].append(i)
    if debug:
        print("When time = 0", last_visit)
    for time in range(1, M+1):
        visited = [False] * N #visited表示本轮是否被访问
        H = [(H[i] + dx[i])%N for i in range(G)]
        for i, Hi in enumerate(H):
            if visited[Hi]:
                last_visit[Hi].append(i)
            else:
                last_visit[Hi] = [i]
                visited[Hi] = True
        if debug:
            print("when time = %d"%time)
            print(visited)
            print(last_visit)
    for guests in last_visit:
        for g in guests:
            ans[g] += 1
    print("Case #%d:"%(it+1),end="")
    for num in ans:
        print(" %d"%num, end="")
    print()