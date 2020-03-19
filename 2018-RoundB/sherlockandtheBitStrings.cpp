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
12:45读题
12:55开始
N charactors    S1..Sn
K constraints 
    Ai Bi Ci 
    sum Sai ~ Sbi == Ci
Pth counting from 1 字母序列第P个

n, k, p

小数据集： 直接把剩下的n一下？ 

*/

const int N = 105; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2, T, n,k,cnt,idx,s[N], l,r, a[N],b[N],c[N];
bool flag;
ll p;
string ans;
vector<int> m[100015];

int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(it,0,T){
        cin>>n>>k>>p;
        fto(i, 0, n){
            s[i] = -1; //unknown
        }

        fto(i,0,k){
            cin >> a[i] >> b[i] >> c[i];
            s[a[i]-1] = c[i];
        }
        //debuga1(s, 0,n);
        p --;
        idx = n-1;
        while (p>0){
            while (s[idx]!=-1){
                idx --;
            }
            s[idx] = p%2;
            p/=2;
        };

        ans = "";
        //debuga1(s, 0,n);
        fto(i,0,n){
            ans += (s[i]!=-1) ? char(s[i]+48) : '0';
        }
        cout << "Case #" << it + 1 << ": "<<ans<<endl;
        
    }
}