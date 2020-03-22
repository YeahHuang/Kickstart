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
N 堆盘子 每堆K个
每个盘子  positive beauty value 


take P plates 没拿一个它上面的也要拿
    take plates[i] must take [0..i]

f[i][j] 到第几个为止 拿了几个盘子 
        50 * 1500 能过

f[i][p] = 

第一次的肯定好说 直接每一个就是sum
第二次的 k..2k 部分 
*/

const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,ans,T,  n,cnt, f[100][2000], pre,val,sum, pick, k, p; //会不会需要弄到long long
bool flag;
string s;
vector<int> m[100015];
bool debugg = false;
bool test = true;



int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(it,0,T){
        fto(i,0,100)
            fto(j,0,2000)
                f[i][j] = 0;
        cin>>n>>k>>p;
        pre = 0;
        fto(i,1,n+1){
            sum = 0;
            fto(pick, 1, pre+1)
                f[i][pick] = f[i-1][pick];
            fto(j,1,k+1){
                cin>>val;
                sum += val;
                if (debugg) printf("pick from %d to %d\n", j,min(p, pre+j) );
                fto(pick, j, min(p, pre+j)+1){
                    if (debugg)  {
                        cout<<f[i][pick]<<" "<<f[i-1][pick-j]<<" "<< sum<<endl;
                    }
                    f[i][pick] = max(f[i][pick], f[i-1][pick-j] + sum);
                }
            }
            //debuga1(f[i], 0, k+1);
            if (debugg)
                fto(j,0,k+1)
                    cout<<f[i][j]<<" ";
            pre += k;
        }
            
        
        
        ans = f[n][p];
    
        cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
}