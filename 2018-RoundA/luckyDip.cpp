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
Vi value 1..N

放回 maximum K times 

12:02 - 12:13 答题 猜不出为什么12.3584

12:21 吃了很多当安慰剂
12:32 还是想不通 

12:40 WA小的
12:58 枚举还是WA
*/


const int N = 2e4 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,T, t, k, n;
long long v[N];
long double sum, avg, ans,sum1, sum2;
bool flag;
string s;
vector<int> m[100015];

int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(it,0,T){
        cin>>n>>k;
        sum = 0.0;
        fto(i,0,n){
            cin >> v[i];
            sum += v[i];
        }  
        avg = sum / n;   
        //avg = sum /= n; 一开始这里错误的写成了/=
        ans = avg; 
        if (k == 0)
            ans = avg;
        else{
            p1 = 0;
            sum1 = 0.0;
            sum2 = sum;
            sort(v, v+n);
            //debuga1(v, 0,n);
            fto(i,0,n){
                p1 = i+1;
                sum2 -= v[i];
                //debug(p1);
                //debug(sum2);
                ans = max(ans, p1*1.0/n * avg + (1-p1*1.0/n) * sum2/(n-p1));

                //ans = max(ans, pow(p1*1.0/n, 2) * sum1 / p1 + (1 - pow(p1*1.0/n, 2)) * sum2/p2);
            }

               /* 
                if (v[i] - avg < EPS){
                    p1 += 1;
                    sum1 += v[i];
                }else{
                    p2 += 1;
                    sum2 += v[i];
                }*/       
        }
        cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
}