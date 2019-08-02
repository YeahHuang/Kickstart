# -*- coding:utf-8 -*-
import copy 
import pprint as pp
from functools import reduce
import math
#突破点在于 偶xor偶=偶 参考了https://blog.csdn.net/liufengwei1/article/details/97616117 c++ 
#第一次RE了 因为自己定义的odd_idx 在新添加一个元素后 后面的元素没办法实时update
#接下来TLE了 因为list.remove(value) 实际的复杂度是O(n)
#接下来又RE了 因为list.pop(idx) 没改过来 写成了list.pop(value)
#然后才AC。以后注意的debug print东西写全一点 耐心一点呐

def judgeEven(num: int) -> bool:
    #print("start to judge ", num)
    s = bin(num)[2:]
    cnt_1 = 0 
    for c in s:
        if c == '1':
            cnt_1 += 1
    return not(cnt_1 & 1)


T = int(input()) #细致的分析一下 我觉得可能 除去一个再配上一个 这中间是有bitwise的优化的 嗯

debug = False
is_even = []
for i in range(1024):
    is_even.append(judgeEven(i))
for it in range(T):
    qpp = input().split(" ")
    N, Q = int(qpp[0]), int(qpp[1])
    qpp = input().split(" ")
    a = [int(s) for s in qpp]
    odd_list = []
    for i in range(N):
        if is_even[a[i]]==False:
            odd_list.append(i)
    if debug:
        print(odd_list)
    ans = [0] * Q
    for i in range(Q):
        qpp = input().split(" ")
        idx, num = int(qpp[0]), int(qpp[1])
        if debug and i > 1:
            print("ans[%d]=%d"%(i-1, ans[i-1]))
        if is_even[a[idx]]+is_even[num] == 1: 
            l, r = 0, len(odd_list)-1
            while l<=r:  
                mid = (l+r)//2
                if odd_list[mid] < idx:
                    l = mid + 1
                else:
                    r = mid - 1
            if is_even[a[idx]]==False and is_even[num]==True:
                odd_list.pop(l)
            if is_even[a[idx]]==True and is_even[num]==False:
                odd_list.insert(l, idx)
            if debug:
                print("After odd_list:",odd_list)
        a[idx] = num
        if len(odd_list) & 1 == 0:
            ans[i] = N
        else:
            ans[i] = max(odd_list[-1], N-1-odd_list[0]) #odd_list[-1]-1-0+1 = odd_list[-1]  N-1 - (odd_list[0]+1) +1 = N-1-odd_list[0]
    print("Case #%d:"%(it+1),end="")
    for num in ans:
        print(" %d"%num, end="")
    print()

'''
debug = True
is_even = []
for i in range(1024):
    is_even.append(judgeEven(i))
print(is_even[:100])
for it in range(T): #是空的case
    qpp = input().split(" ")
    N, Q = int(qpp[0]), int(qpp[1])
    qpp = input().split(" ")
    a = [int(s) for s in qpp]
    odd_list = []
    odd_idx = [-1] * N
    for i in range(N):
        if is_even[a[i]]==False:
            odd_list.append(i)
            odd_idx[i] = len(odd_list) - 1
    if debug:
        print(odd_list)
        print(odd_idx)
    ans = [0] * Q
    for i in range(Q):
        qpp = input().split(" ")
        idx, num = int(qpp[0]), int(qpp[1])
        if debug and i > 1:
            print("ans[%d]=%d"%(i-1, ans[i-1]))
        if odd_idx[idx]!=-1:
            odd_list.pop(odd_idx[idx])
            if debug:
                print("odd_list pop %d"%idx)
                print(odd_list)
        a[idx] = num
        if debug:
            print("new num=%d byte is %s is_even = %d"%(num, bin(num), is_even[num]))
        if is_even[num]==False:
            l, r = 0, len(odd_list)-1
            while l<=r:  
                mid = (l+r)//2
                if odd_list[mid] < idx:
                    l = mid + 1
                else:
                    r = mid - 1
            if debug:
                print("is going to insert %d at %d"%(idx, l))
            odd_list.insert(l, idx)
            odd_idx[idx] = l
            if debug:
                print("After odd_list:",odd_list)
                print("After odd_idx:",odd_idx)
        else:
            odd_idx[idx] = -1
        if len(odd_list) & 1 == 0:
            ans[i] = N
        else:
            ans[i] = max(odd_list[-1], N-1-odd_list[0]) #odd_list[-1]-1-0+1 = odd_list[-1]  N-1 - (odd_list[0]+1) +1 = N-1-odd_list[0]
    print("Case #%d:"%(it+1),end="")
    for num in ans:
        print(" %d"%num, end="")
    print()
'''