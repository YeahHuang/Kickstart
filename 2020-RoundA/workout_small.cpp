//#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <bitset>
#include <vector>
#include <complex>
#include <algorithm>
#include <unordered_map>
#include <memory.h>
#include <set>
#include <functional>
using namespace std;



#define ll long long
#define pii pair<int, int>
#define pb push_back
#define pli pair<ll, int>
#define pil pair<int, ll>
#define clr(a, x) memset(a, x, sizeof(a))
#define sz(a) (int)a.size()
#define debug(a) cout << #a << ": " << a << endl
#define debuga1(a, l, r) fto(i, l, r) cout << a[i] << " "; cout << endl
#define fdto(i, r, l) for(int i = (r); i > (l); --i)
#define fto(i, l, r) for(int i = (l); i < (r); ++i)

const double pi = acos(-1.0);
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const double EPS = 1e-9;

double fRand(double fMin, double fMax)
{
    double f = (double)rand() / RAND_MAX;
    return fMin + f * (fMax - fMin);
}

template <class T>
T min(T a, T b, T c) {
    return min(a, min(b, c));
}

template <class T>
T max(T a, T b, T c) {
    return max(a, max(b, c));
}

/*
n sessions   每个Mi minutes
Mi严格上升
难度：max( Mi+1 - Mi )

add K sessions

small: 直接找到max gap 偶数输出/2 奇数输出/2+1
WA 了一次 因为还需要和second_largest 比较哦


large: 
1. 把gap排序
2. 肯定可以的是：
    f[i][j] 到第几个 我砍了几刀 能拿到的最好值 

    我把所有>1 的gap加起来 ➗ k 的值得 如果余数>0 则+1 那就是我最多可能拿到的了 


3. 二分我们砍到哪儿 
    砍到中间 看一下和是不是小于k
    gap种类 lg(1e9) * n 
*/

const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,ans,T, second_max_gap, n,cnt, max_gap, pre, cur,k, l,r;
bool flag;
string s;
vector<int> m[100015];
bool debugg = true;
bool test = true;

int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(it,0,T){

        cin>>n>>k;
        cin>>pre;
        max_gap = 0;
        second_max_gap = 0;
        fto(i,1,n){
            cin >> cur;
            if (cur - pre > max_gap){
                second_max_gap = max_gap;
                max_gap = cur - pre ;
            } else if (cur - pre > second_max_gap)
                second_max_gap = cur - pre;
            max_gap = max(max_gap, cur - pre);
            pre = cur;
        }
        max_gap = (max_gap & 1) ? max_gap/2+1:max_gap/2;
        ans = max(max_gap, second_max_gap);
        cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
}