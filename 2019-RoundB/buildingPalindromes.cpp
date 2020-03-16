//#include <bits/stdc++.h>

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <vector>
#include <cmath>
#include <cstring>
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



const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,ans,T, t, n,cnt,  l,r,f[N][26];
bool flag;
string s;
vector<int> m[100015];

int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    for (int it=0; it<T; it++){

        cin>>n>>q;
        cin>>s;
        clr(f[0],0);
        ans = 0;
        fto(i,0,n){
            fto(j,0,26)
                f[i+1][j] = f[i][j] ^ (s[i] == j+'A');
            //f[i][s[i]-'A'] = (f[i-1][s[i]-'A']+1)%2;
        }
        fto(i,0,q){
            cin>>l;cin>>r;
            l--;
            cnt = 0;
            fto(j,0,26){
                cnt += f[r][j] ^ f[l][j];
                //if ((l==0 && f[r][j]==1)|| f[r][j]!=f[l-1][j])
                //    cnt++;
            }
            if (cnt<=1){
                //cout<<l<<r<<endl;
                ans ++; 
            }
        }

        
        cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
}