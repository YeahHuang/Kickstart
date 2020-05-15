# -*- coding:utf-8 -*-
import copy 
import pprint as pp
from functools import reduce
import math
from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random
import sys

def hash(x, y):
    return (x << 20) + y

def solve_small(x, y, s):
    visited = set()
    visited.add(hash(x,y))
    for c in s:
        while hash(x,y) in visited:
            x += dx[c]
            y += dy[c]
        visited.add(hash(x,y))
        if debug:
            print(x, y)
    return x, y



debug = False
test = True
if test:
    T = 10
else:
    T = int(input())
dx = {'N':-1, 'S':1, 'E':0, 'W': 0 }
dy = {'N':0,  'S':0, 'E':1, 'W': -1}
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
update = {'E':LEFT, 'W':RIGHT, 'S':UP, 'N':DOWN}
nex = {'E':RIGHT, 'W':LEFT, 'S':DOWN, 'N':UP} #next
for it in range(T):
    if test:
        x, y = 1,1000
        s = "EW"*int(1e4) + "NS" + "EW"*int(1e4)
    else:
        n, r, c, x, y = map(int, input().split())
        s = input()
    #x, y = solve_small(x, y, s)
    visited = defaultdict(list)
    visited[hash(x,y)] = [y-1, y+1, x-1, x+1] #left, right, up, down
    for c in s:
        prex, prey = x, y
        if c in "EW": 
            y = visited[hash(prex, prey)][nex[c]]
        else:
            x = visited[hash(prex, prey)][nex[c]]
        qpp = visited[hash(prex, prey)][update[c]]
        while hash(x, y) in visited:
            visited[hash(x,y)][update[c]] = qpp
            if c in "EW": 
                y = visited[hash(x, y)][nex[c]]
            else:
                x = visited[hash(x, y)][nex[c]]

        visited[hash(x,y)] = [y-1, y+1, x-1, x+1]
        if hash(x,y-1) in visited:
            visited[hash(x,y)][0] = visited[hash(x,y-1)][0]
        if hash(x,y+1) in visited:
            visited[hash(x,y)][1] = visited[hash(x,y+1)][1]
        if hash(x-1,y) in visited:
            visited[hash(x,y)][2] = visited[hash(x-1,y)][2]
        if hash(x+1,y) in visited:
            visited[hash(x,y)][3] = visited[hash(x+1,y)][3]
        visited[hash(x,y)][update[c]] = qpp
        visited[hash(prex, prey)][nex[c]] = visited[hash(x,y)][nex[c]]
        if debug:
            print(x,y)
            print(visited[hash(x,y)])
    print("Case #%d: %d %d"%(it+1, x, y))
