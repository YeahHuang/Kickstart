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
for it in range(T):
    l, r = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    print("Case #%d: %d"%(it+1, ans))


out = open('hyh.txt','w') 
print("", file=out)
sys.stdout.flush()
out.close()
#!/usr/bin/python3 main文件需要

from string import ascii_lowercase
from bisect import bisect_left, bisect_right, insort_left
from collections import defaultdict, Counter, deque, nemedtuple, OrderedDict
from operator import add
from heapq import heapify, heappop
from re import split, sub

def insertR(nums, target):
    l,r = 0, len(nums)-1
    while l<=r:  
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

def insertL(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
    return r

class DSU: #Disjoint Set Union 就是常见的染色问题
    def __init__(self,n):
        self.p = {}
        self.sz = {}
        for i in range(1,n+1):
            self.p[i] = i
            self.sz[i] = 1

    def find(self, x):
        stack = []
        while self.p[x] != x:
            stack.append(x)
            x = self.p[x]
        for xx in stack:
            self.p[xx] = x
        '''
        if self.p[x] != x: 会MLE
            self.p[x] = self.find(self.p[x])
        '''
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.sz[px] < self.sz[py]:
            self.sz[py] += self.sz[px]
            self.p[px] = self.p[py]
        else:
            self.sz[px] += self.sz[py]
            self.p[py] = self.p[px]
        return px!=py

#sol1.1 188ms -> 172ms 而且内存基本没变 
class DSU: #Disjoint Set Union 就是常见的染色问题
    def __init__(self):
        self.p = {}
        self.sz = {}

    def find(self, x):

        stack = []
        while self.p[x] != x:
            stack.append(x)
            x = self.p[x]
        for xx in stack:
            self.p[xx] = x
        '''
        if self.p[x] != x: 会MLE
            self.p[x] = self.find(self.p[x])
        '''
        return x

    def union(self, x, y):
        self.p.setdefault(x,x)
        self.sz.setdefault(x,1)
        self.p.setdefault(y,y)
        self.sz.setdefault(y,1)
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            self.sz[py] += self.sz[px]
            self.p[px] = self.p[py]
        else:
            self.sz[px] += self.sz[py]
            self.p[py] = self.p[px]
        return True

tarjan
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dfn, low, father = [-1]*n, [-1]*n, [-1]*n
        t = collections.defaultdict(list)
        self.time_stamp = 0
        for c in connections:
            t[c[0]].append(c[1])
            t[c[1]].append(c[0])
        ret = []

        def dfs(idx):
            self.time_stamp += 1 #WA一次 一开始以为可以自动默认global了 结果还是需要加self. 的
            low[idx] = dfn[idx] = self.time_stamp 
            for child in t[idx]:
                if dfn[child]==-1:
                    father[child] = idx
                    dfs(child)
                if child != father[idx]:
                    low[idx] = min(low[idx], low[child])
        '''
        我尝试把father[] 用单一的father代替，结果时间2524 -> 2412  81.9 -> 81.6 
        def dfs(idx, father):
            self.time_stamp += 1
            low[idx] = dfn[idx] = self.time_stamp
            for child in t[idx]:
                if dfn[child]==-1:
                    dfs(child, idx)
                if child != father:
                    low[idx] = min(low[idx], low[child])
        '''

        dfs(0)
        #print(dfn, low, father)
        for c in connections:
            #if (dfn[c[0]] - dfn[c[1]]) * (low[c[0]] - low[c[1]]) > 0: #WA 一次 一开始弄错了
            if low[c[0]] > dfn[c[1]] or low[c[1]]>dfn[c[0]]:
                ret.append(c)
        return ret

#https://www.geeksforgeeks.org/maximum-bipartite-matching/
# Python program to find maximal Bipartite matching. 

class GFG: 
    def __init__(self,graph): 
        
        # residual graph 
        self.graph = graph 
        self.ppl = len(graph) 
        self.jobs = len(graph[0]) 

    # A DFS based recursive function 
    # that returns true if a matching 
    # for vertex u is possible 
    def bpm(self, u, matchR, seen): 

        # Try every job one by one 
        for v in range(self.jobs): 

            # If applicant u is interested 
            # in job v and v is not seen 
            if self.graph[u][v] and seen[v] == False: 
                
                # Mark v as visited 
                seen[v] = True

                '''If job 'v' is not assigned to 
                an applicant OR previously assigned 
                applicant for job v (which is matchR[v]) 
                has an alternate job available. 
                Since v is marked as visited in the 
                above line, matchR[v] in the following 
                recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v], 
                                            matchR, seen): 
                    matchR[v] = u 
                    return True
        return False

    # Returns maximum number of matching 
    def maxBPM(self): 
        '''An array to keep track of the 
        applicants assigned to jobs. 
        The value of matchR[i] is the 
        applicant number assigned to job i, 
        the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs 
        
        # Count of jobs assigned to applicants 
        result = 0
        for i in range(self.ppl): 
            
            # Mark all jobs as not seen for next applicant. 
            seen = [False] * self.jobs 
            
            # Find if the applicant 'u' can get a job 
            if self.bpm(i, matchR, seen): 
                result += 1
        return result 


bpGraph =[[0, 1, 1, 0, 0, 0], 
        [1, 0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1]] 

g = GFG(bpGraph) 

print ("Maximum number of applicants that can get job is %d " % g.maxBPM()) 

# This code is contributed by Neelam Yadav 


快排的partition

def partition(l, r):
    if l>=r:
        return
    pivot = a[l]
    i, j = l+1, r
    while True:
        while i<j and a[i]<pivot:
            i+=1
        while i<=j and a[j]>=pivot:
            j-=1
        if i>=j:
            break
        a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


nums = [1,3,5,7,9]
print("ori:",nums)
print("insertL, 0,1,2,3,4,5,6,7,8,9,10:", [insertL(nums,i) for i in range(11)])
print("insertR, 0,1,2,3,4,5,6,7,8,9,10:", [insertR(nums,i) for i in range(11)])


bisect.insort_left(self.records, (timestamp, id))
l = bisect.bisect_left(self.records, (s, 0))
r = bisect.bisect_right(self.records, (e, float('inf')))
return [id for (_, id) in self.records[l:r]]

n =  sum(map(lambda x: int(x)**2, list(str(n)))) 

map(''.join, itertools.product(list1, list2))代替自己写的zip会快 
>>> l1 = ['a','b','c']
>>> l2 = ['ee','ff']
>>> list(map(''.join, itertools.product(l1,l2)))
['aee', 'aff', 'bee', 'bff', 'cee', 'cff']

tuple(map(operator.add,a, b))
dict的参数转换很酷： idx = {‘Year’:5, ‘’Month’:8…}[gra]

collections.defaultdict(set)
Stone = collections.namedtuple('Stone',['s','e','l','maxs'])

chr(i) ord('A')

filter(lambda log: log[log.find(" ") + 1].isalpha(), logs)

de = collections.deque([1,2,3])
de.append(4) #默认右边，appendleft
de.pop() #默认右边，popleft
de.count(x) #输出和x相等的数量
de.remove(x) #remove第一个
de.extend([4,5,6]) #extendleft,  加iteratable
de.ratate(n=1)  n可以为- 就是反方向left转了 
clear


maxlen属性 deque([iterable[,maxlen]])


Binary Index Tree:
1. x & (-x) 就是last set bit in a number x
    e.g. 当x=10(decimal) = 1010(b)  x&-x = (10)1(0)&(01)1(0) = 2(decimal)
2. BIT[i] = sum(num[i-(1<<r)+1]..num[i]) r就是上面说的last set bit 
    所以如果i是奇数 就只有它本身; 如果i是2的poweder 那就直接是sum(num[0]..num[i])
3. 需满足可逆性 比如 * / + - 但是gcd这样不可逆的就么的办法了

class BIT:
    def __init__(self, n, nums):
        self.BIT = [0]*n+1
        for i,num in enumerate(nums):
            self.update(i+1, num)

    def update(idx, val):
        while idx <= n: 
            self.BIT[idx] += val
            idx += idx & -idx

    def query(idx):
        sum = 0
        while idx>0:
            sum += self.BIT[idx]
            idx -= idx & -idx
        return sum

segmentation tree 发现python TLE c++就能过
参考自己的diverseSubarray_large
或者https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/python-well-commented-solution-using-segment-trees

带lazy propagation https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
其实还是用下载的c++的吧

d = {"banana":3, 'apple':4, 'pear':1, 'orange':2};

>>> # dictionary sorted by length of the key string
>>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

paragraph = re.sub("[!?',;.]"," ", paragraph.lower())
re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
#'Baked Beans & Spam'
re.split('\w+', 'Words, words, words.')
['Words', 'words', 'words', '']

words = re.findall(r'\w+',p.lower())

result = string.ascii_lowercase 
    
# Printing the value  
print(result)

1. 注意题目是否读错 一定要静下心来 无论题目多么复杂
2. n =  sum(map(lambda x: int(x)**2, list(str(n))))  用lambda 而不是trans呀 
3.map(''.join, itertools.product(list1, list2))
4. TreeNode之类的指针没有办法一次TreeNode(10) 多次赋值.left .right的
5. str不支持直接替换的 如果要修改部分的s 可以写成 s = s[:17]+’00’;  
dict的参数转换很酷： idx = {‘Year’:5, ‘’Month’:8…}[gra]
6. unichr(258)
7. WA1 set1=set1.union(set2) 才会真的改变set1；
8. math.factorial 

手写快排 + insort_left, right 
bisect.insort_left(list, int)
bisect_insort_right()


heapq.heapify(sticks)
heapq.heappop(sticks)
heapq.heappush(sticks, p1+p2)

2020/05/01
1. 变量名要清晰
2. 大数据集要大胆猜测 / 小数据集模拟找规律 
3. 我发现对我来说 先把small过了 还挺有用的 心态大法好（官方说 写一个暴力的小的 然后观察结果 经常对大的很有帮助哦）
4. 因为debug信息没删除WA一次
5. 有读题30min的题 一定不要光想 先写起来呀
6. 随机化大法好 贪心顺序etc random.randlist(l, r) [l,r]均包含 random.shuffle(list) ;   
    有时候可以枚举random次数  16cjIO shuffle 1000次->3000次就过了
7. 一开始就很懵 不想去下手 后来发现其实是有规律的（不变 / reverse / 01互换 / reverse+01互换） 耐心！耐心！再耐心！
8. WA: while (N[i] >= S[idx] && idx < S.size())  显然应该先判断大小呀； 反过来后又写错了 >= 写成了 > 要谨慎呀～～ 
9. 交互题 str(int(round(x[5])))(一开始没加这个 心态崩了 其实是可以做出来的 只要跟踪一下输出结果就OK了)
    细心读题啊！读题～～ 大的数据集关键是要发现输出是mod 2^64 这个特殊点 所以剩下的那就是依次输出即可
10. 花了6min查sublime变光标 是 command + option +o
11. chr ord 之类的用dict来表示 可能更清晰
12. hit[c] = hit.get(c,0) + 1 defaultdict的默认初始值✌️
trie如果不行的话 可以参照 bundling_trie_large.cpp


sum(a==b for a,b in zip(secret, guess))
