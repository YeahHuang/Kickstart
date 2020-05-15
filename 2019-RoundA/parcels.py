"""
r, c 
r lines
1 有delivery office

2:15 - 2:07
y is the minimum overall delivery time you can obtain after adding at most one additional delivery office.

小的：枚举加在哪儿 然后重新计算
它只会影响自己目前manhatten距离 <= p 的点

r * c * r * c

然后加一个 就是 r*c 

小的： 先

自己暴力弄出了o((rc)*(rc))
其实想到了bfs会更快(推算能力很重要呀) 只是自己bfs速度可能不行 就没写emmm
但关于 manhattan distance 的公式也必须知道 dist((x1, y1), (x2, y2)) = max(abs(x1 + y1 - (x2 + y2)), abs(x1 - y1 - (x2 - y2))) 
所以就可以转化成 求 maximize/minimize x1+y1 x1-y1 就行
最后可以做到O(rc * log(rc))
"""

from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random
import sys

global debug, test

def solve():
    global debug, test

T = int(input())
debug = True
test = True
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for it in range(T):
    m, n = map(int, input().split())
    t = [input() for _ in range(m)]
    dist = [[float('inf')]*n for _ in range(m)]
    list0 = []
    list1 = []

    for i in range(m):
        for j in range(n):
            if t[i][j] == '0':
                list0.append((i,j))
            else:
                flag_all1 = True
                for k in range(4):
                    tx, ty = i+dx[k], j+dy[k]
                    if 0<=tx<m and 0<=ty<n:
                        if t[tx][ty]=='0':
                            flag_all1 = False
                            dist[tx][ty] = 1
                if flag_all1 == False:
                    list1.append((i,j))
    if debug:
        print("list0: ",list0)
        print("list1: ",list1)
    max_d = 0
    max_pos = []
    #could change to bfs 
    for x, y in list0:
        if dist[x][y]!=1:
            dist[x][y] = min(dist[x][y-1] if y else float('inf'), dist[x-1][y] if x else float('inf')) + 1
            while list1 and (list1[0][0] < x or (list1[0][0] == x and list1[0][1] < y)):
                list1.pop(0)
            for x1, y1 in list1:
                dist[x][y] = min(dist[x][y], abs(x1-x)+abs(y1-y))
            if dist[x][y] == max_d:
                max_pos.append((x,y))
            elif dist[x][y] > max_d:
                max_d = dist[x][y]
                max_pos = [(x,y)]

    if debug:
        print("dist:", dist)
        print("max_d = %d"%(max_d))
    if max_d == 0:
        if len(list0)>1:
            ans = 1
        else:
            ans = 0
    else:
        if len(max_pos) == 1:
            target_office = max_pos.copy()
        else:
            sumx, sumy = 0, 0
            for x,y in max_pos:
                sumx += x
                sumy += y
            x1, y1 = (sumx // len(max_pos), sumy // len(max_pos))
            target_office = [(x1,y1), (x1+1, y1), (x1, y1+1), (x1+1, y1+1)]
        if debug:
            print("max_pos:",max_pos)
            print("target_office:", target_office)
        for x1, y1 in target_office:
            tmp_max_d = 0
            for x, y in list0:
                tmp_max_d = max(tmp_max_d, min(dist[x][y], abs(x1-x)+abs(y1-y)))
            max_d = min(max_d, tmp_max_d)
        ans = max_d
    print("Case #%d: %d"%(it+1, ans))