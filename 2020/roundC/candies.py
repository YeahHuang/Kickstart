"""
n q
second line: a[1..n]
following q lines:
U/Q    
U xj, vj    a[xj] -> v[j]
Q lj, rj    sweetness from lj to rj 
update/query



ai <= 100
n <= 2e5
q <= 1e5

其他的n q 都是300

线段树？ 

隔项和？ 好像OK！！！！ 
隔项的RMQ！！！

1:58 TLE
"""
class SEG_TREE:

    def __init__(self, nums):
        self.n = len(nums)
        self.seg_tree = [0]*self.n + nums
        for i in range(self.n-1, 0, -1):
            self.seg_tree[i] = self.seg_tree[i*2] + self.seg_tree[i*2+1]
        #print(self.seg_tree)
        
    def update(self, i: int, val: int) -> None:
        i += self.n
        self.seg_tree[i] = val
        while i>0:
            if i%2==1: #一开始这里写反了 WA
                self.seg_tree[i//2] = self.seg_tree[i] + self.seg_tree[i-1]
            else:
                self.seg_tree[i//2] = self.seg_tree[i] + self.seg_tree[i+1]
            i=i//2
        
        
    def sumRange(self, i: int, j: int):
        sum = 0
        i, j = i+self.n, j+self.n #一开始忘记加 WA
        while i<=j:
            if i%2==1:
                sum += self.seg_tree[i]
                i+=1
            if j%2==0:
                sum +=  self.seg_tree[j]
                j-=1
            i,j = i//2,  j//2
        return sum
#PS 这里尝试了把i//2 换做 i>>1  i%2换做i&1 但最后无差 我想可能是python编译器已经对类似的东西做了该骚操作了
#未完成： 1. lazy dfs segmentation propagetion: https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
#2. Binary Index Tree 写法：https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j) [i..j]
from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random
import sys

global debug, test

def solve_small(n, Q, a):
    
    ans = 0
    for i in range(Q):
        q, p1, p2 =  input().split()
        if q == 'U':
            a[int(p1)] = int(p2)
        else:
            tmp = 0 
            l, r = int(p1), int(p2)
            for j in range(l, r+1):
                tmp += (-1)**(j-l)*(j-l+1)*a[j]
            if debug:
                print("tmp sum = %d"%tmp)
            ans += tmp
    return ans


debug = False
test = True
if test:
    T = 1
else:
    T = int(input())
xi = [(-1)**(i+1) * i for i in range(int(2*1e5 + 10))]
for it in range(T):
    if test:
        n, Q = 200000, 100000
        a = [0]
        a.extend([1]*n)
        
        qs = [('Q',1,1),('U',1,2),('Q',1,1)]
    else:
        n, Q = map(int, input().split())
        a = [0]
        a.extend(list(map(int, input().split())))
        qs = [input().split() for _ in range(Q)]
    ji = []
    ou = []
    aa = []
    ans = 0 
    for i in range(1, n+1):
        aa.append(xi[i] * a[i])
        if i%2 == 1:
            ji.append(a[i])
        else:
            ou.append(a[i])
    if debug:
        print("ji: ", ji)
        print("ou: ", ou)
        print("aa: ", aa)
    #aa ji ou 0..n 
    seg_aa = SEG_TREE(aa)                          
    seg_ji = SEG_TREE(ji)
    seg_ou = SEG_TREE(ou)

    for i in range(Q):
        q, p1, p2 =  qs[i]
        if q == 'U':
            #a[int(p1)] = int(p2)  obj.update(i,val)
            x, y = int(p1)-1, int(p2)
            seg_aa.update(x, xi[x+1] * y)
            if (x+1)%2==1:
                seg_ji.update(x//2, y)
            else:
                if len(ou):
                    seg_ou.update(x//2, y)
        else:
            #param_2 = obj.sumRange(i,j) [i..j] 从0开始标号
            l, r = int(p1)-1, int(p2)-1
            tmp = seg_aa.sumRange(l, r)
            if (l+1)%2 == 1: #start is ji
                ji_l = l // 2
                ou_l = (l+1)//2
                xi_ji = 1-xi[l+1] #xi[l+1] ->  1 
                xi_ou = -2 - xi[l+2] #xi[l+2] -> -2
            else:
                tmp *= -1 
                ou_l = l // 2
                ji_l = (l+1)//2
                xi_ou = 1 - (-1)*xi[l+1] #xi[l+1] ->  1 
                xi_ji = -2 - (-1)*xi[l+2] #xi[l+2] -> -2
            if (r+1)%2 == 1: #end is ji
                ji_r = r //2
                ou_r = (r-1)//2
            else:
                ou_r = r // 2
                ji_r = (r-1)//2
            
            delta_ji = seg_ji.sumRange(ji_l, ji_r)
            if len(ou):
                delta_ou = seg_ou.sumRange(ou_l, ou_r)
            else:
                delta_ou = 0 
            if (debug):
                print("ji: %d to %d    ou: %d to %d"%(ji_l, ji_r, ou_l, ou_r))
                print("tmp = %d xi_ji=%d delta_ji=%d; xi_ou=%d delta_ou=%d "%(tmp, xi_ji, delta_ji, xi_ou, delta_ou))
            tmp = tmp + xi_ji*delta_ji + xi_ou * delta_ou
            if (debug):
                print("tmp=%d"%tmp)
            ans += tmp
    print("Case #%d: %d"%(it+1, ans))
