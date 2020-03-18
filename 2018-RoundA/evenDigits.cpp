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
+ +1
- -1
N  no leading zeros 

小数据集合： 枚举哪个方向 
+ distance 依次类推
11:26开始
50 attempt1 
56 AC
6min 查光标
*/



const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0


int main(){
    int q,p1,p2,T;
    long long n, tmp_n, tmp_ten, ten, plus_dist, minus_dist, ans;
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(it,0,T){
        cin>>n;
        tmp_n = n;
        ten = 1;
        while (n>0){
            n /= 10;
            ten *= 10;
        }
        ten /= 10;
        plus_dist = 0;
        minus_dist = 0;
        //debug(ten);
        //calculate plus
        tmp_ten = ten;
        n = tmp_n;
        while (ten > 0){
            if ((n / ten) & 1){
                plus_dist = ten - n % ten;
                if (n/ten == 9) //
                    plus_dist += ten * 10;
                break;
            }
            n %= ten;
            ten /= 10;
        };

        //debug(plus_dist);
        ten = tmp_ten;
        n = tmp_n;
        while (ten > 0){
            if ((n/ten)&1){
                minus_dist += n%ten + 1;
                n -= (n%ten + 1);
            }
            n %= ten;
            ten /= 10;
        }
        //debug(minus_dist);
        ans = min(plus_dist, minus_dist);
        cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
}