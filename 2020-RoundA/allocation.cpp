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
hashmap num[i] = (ai == i 的有几个)
*/

const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,ans,T,  n,cnt, num[N], a,b, res, l,r;
bool flag;
string s;
vector<int> m[100015];
bool debugg = true;
bool test = true;

int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(it,0,T){

        cin>>n>>b;
        clr(num, 0);
        fto(i,0,n){
            cin >> a;
            num[a] ++;
        }

        ans = 0;
        res = b;
        fto(i,1,1001){
            if (num[i]>0)
                if (num[i] * i <=res) {
                        ans += num[i];
                        res -= num[i] * i;
                        }

                        else{
                            ans += res / i;
                            break;
                        }
        }

        cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
}