
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
1m 网格

n cafes (Vi, Hi)

pick 3 cafes

正方形环 

 N, V1, H1, A, B, C, D, E, F and M.
 Vi = (A × Vi-1 + B × Hi-1 + C) modulo M
 Hi = (D × Vi-1 + E × Hi-1 + F) modulo M

1:30 两头线段推移法 每一个set去排序 或者标注目前start end 依次更新 
或者直接暴力相加 
*/
class Point{
    int x,y;
    Point(int x,int y){
        x = x;
        y = y;
    }
};

const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,ans,T, t, n,cnt,  v,h,preV, preH, a,b,c,d,e,f,m,l,r;
bool flag;
set<int> vs;
string s;


int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(it,0,T){

        cin>>n>>v>>h>>a>>b>>c>>d>>e>>f>>m;
        cin>>s;
        vs.clear();
        fto(i,0,n){
            preV = v; preH = h;
            v = (a*preV + b * preH + c)%m;
            h = (d*preV + e * preH + f )%m;

            
            vs.insert(v);
        }
        ans = 0;
    
        cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
}