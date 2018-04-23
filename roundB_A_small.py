
# -*- coding: UTF-8 -*-

import os
import numpy as np

def judge(n):
    temp = n
    flag = 1
    while temp>0:
        if (temp%10==9):
            flag = 0
            break
        temp /= 10
    if (n%9==0):
        flag = 0
    return flag

in_file = open('A-small-attempt0.in.txt','r+')
#in_file = open('A.in','r+')
lines = in_file.readlines()
out_file = open('A-small-attempt0.out.txt','w+')

num_case = int(lines[0])
debug = 0
for i in range(1, num_case+1):
    line = lines[i]
    f,l = line.split(" ")
    f = int(f)
    l = int(l)
    ans = 0
    for j in range(f, l+1):
        if judge(j):
            ans += 1
        else:
            if debug>0:
                print(j)
    print ("Case #%d: %d\n"%(i, ans))
    out_file.write("Case #%d: %d\n"%(i, ans))
out_file.close()
        

