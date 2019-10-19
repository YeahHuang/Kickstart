//#include <bits/stdc++.h>

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <cmath>
//#include <tgmath.h>
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
#define fdto(i, r, l) for(int i = (r); i >= (l); --i)
#define fto(i, l, r) for(int i = (l); i <= (r); ++i)

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

struct Stone {
    int s, e, l;
};


bool cmp(const Stone &a, const Stone &b) {
    return b.s * a.l > a.s * b.l;
}

sort(a, a+n, cmp);

const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,ans,T, n, s, a[100015], b[100015], rec[100015],ma[400015], lazy[400015];
vector<int> m[100015];

int main(){
    scanf("%d",&T);
    for (int it=0;it<T; it++){
        scanf("%d%d",&n,&s);
        clr(b,0); for(int i=1; i<=100000;i++) m[i].clear();
        for (int i=1;i<=n;i++){
            scanf("%d",&a[i]);

        }