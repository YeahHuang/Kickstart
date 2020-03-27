from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = 0
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode() 
        self.sum = 0

    def cal(self, k):
        self.calChild(self.root, 0, k)
        return self.sum

    def calChild(self, cur, depth, k):
        summ = cur.end
        for c in cur.children:
            #print("Is going to calChild: ", c)
            summ += self.calChild(cur.children[c], depth+1, k)

        self.sum += summ //k * depth 
        #print("Returning: ", summ, summ/k)
        return summ % k 

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.end += 1

    def search(self, word):
        cur = self.root
        is_exist = True
        for c in word:
            cur = cur.children.get(c) #这里为了判定是否为空 由直接新建 -> .get 函数 注意一下
            if cur is None:
                is_exist = False
                break
        return is_exist and cur.end

    def startsWith(self, prefix):
        cur = self.root
        is_prefix = True
        for c in prefix:
            cur = cur.children.get(c) #这里为了判定是否为空 由直接新建 -> .get 函数 注意一下
            if cur is None:
                is_prefix = False
                break
        return is_prefix



T = int(input())

for it in range(T):
    n, k = map(int, input().split())
    trie = Trie()
    for i in range(n):
        s = input()
        trie.insert(s)

    
    ans = trie.cal(k)
    print("Case #%d: %d"%(it+1, ans))
