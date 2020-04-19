from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
"""
wth col   E: w++   W: w--
hth row   S: h++   N: h--

输出 final的w, h

x(y)  y non-empty subprogram
2<=x<=9

7:48 - 8:20 大的会RE


结果 8:20 - 9:47 写了那个大的还是RE
才写了下面的if test 的大数据集 然后发现 RE的原因是OverflowError: int too large to convert to float
每次加之后 % 1e9 就可以了
"""

global tr, debug
tr = {'E':0, 'W':1, 'S':2, 'N':3}
debug = True
test = True

def solve(s):
    global tr, debug
    ret = [0] * 4
    i = 0
    while i<len(s):
        if s[i].isdigit():
            idx = int(s[i])
            cnt = 1
            for j in range(i+2, len(s)):
                if s[j] == ')':
                    if cnt == 1:
                        break
                    else:
                        cnt -= 1
                elif s[j] == '(':
                    cnt += 1
            #if debug:
            #    print("is going to solve ", s[i+2:j])
            subRet = solve(s[i+2: j]) #j==')' 
            # if debug:
            #     print(idx, subRet)
            for k in range(4):
                ret[k] = (ret[k] + idx * subRet[k]) % 1e9 #list(map(add, test_list1, test_list2)) 
            i = j + 1
        else:
            # if debug:
            #     print(i, s[i])
            ret[tr[s[i]]] += 1
            i += 1
    return ret  #[E, W, S, N]


def solve_noRE(s:str) -> int:
    global debug, tr
    if True:
        if True:
            
            operator_list, retList = ['+'],  [[0,0,0,0]]
            if s[0].isalpha():
                operator_list.append('+')
            n, ans, i = len(s), 0, 0
            while i<n:
                if s[i].isalpha():
                    start_idx = i
                    ret = [0] * 4
                    while i<n and s[i].isalpha():
                        ret[tr[s[i]]] += 1
                        i += 1
                    retList.append(ret)
                    #i-=1
                elif s[i].isdigit():
                    operator_list.append('+')
                    operator_list.append(s[i])
                    if i+2 < n and s[i+2].isalpha():
                        operator_list.append('+')
                    #operator_list.append('+')
                    #idxList.append(int(s[i]))
                    i += 2
                    #operator_list = operator_list + ['(','+']
                elif s[i] == ')':
                    tmp = [0] * 4
                    if debug:
                        print("Going to pop", operator_list, retList)
                    while True:
                        op = operator_list.pop()
                        if op == '+':
                            ret = retList.pop()
                            for k in range(4):
                                #retList[-1][k] += ret[k]
                                tmp[k] += ret[k]
                        else: #op.isdigit()
                            idx = int(op)
                            for k in range(4):
                                tmp[k] *= idx
                            break
                    retList.append(tmp)
                    #if len(retList)==0:
                    #    retList.append([0,0,0,0])
                    if (i+1<n and s[i+1].isalpha()):
                        operator_list.append('+')
                    if debug: 
                        print(idx, ret, tmp, retList)
                    i += 1
                else:
                    print("ERROR! i=%d s[i]=%s"%(i,s[i]))
                #i+=1
        
        hyh = [0,0,0,0]
        for ret in retList:
            for i in range(4):
                hyh[i] += ret[i]
        return hyh


T = int(input())

for it in range(T):
    if test:
        s = ""
        for i in range(900):
            s += '9('
        s += 'E)WW))EW)'
        for i in range(896):
            s += ')'

    else:
        s = input()
    #s = '1(' + s + ')'


    ret = solve(s)
    #ret = solve_noRE(s) 
    if debug:
        ret0 = solve(s)
        print("ans:", ret0, ret)
    w = int(0 + ret[0] - ret[1]) % 1e9 + 1
    h = int(0 + ret[2] - ret[3]) % 1e9 + 1
    print("Case #%d: %d %d"%(it+1, w, h))
