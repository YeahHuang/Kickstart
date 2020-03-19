//passed both small & large

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



const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,T, t, n,cnt,r;

bool flag;
bool debugg= false;
ll f,l,ans, dp[20][9];
string s;
vector<int> m[100015];

bool judge(ll num){
    if (num%9==0) return false;
    while (num > 0){
        if (num%10 == 9)
            return false;
        num /=10;
    }
    return true;
}

int tr(int j, int k){
    return (j+9-k)%9;
}

ll solve_small(ll f, ll l){
        ll ans = 0;
        for(ll i=f; i<l+1; i++)
            if (judge(i))
                ans ++;
        return ans;
}



ll cal1(int qpp[], int idx, int len, ll num){ //requires unit test
    if (debugg){
        cout<<"cal1 ";
        debug(idx);
        debuga1(qpp, 0, len);
    }
    if (idx == 0)
        return solve_small(num/10*10, num);
    ll ret = 0;
    ll cur[9], pre[9];
    clr(cur, 0);
    fto(j, 0, 9)
        fto(k, 0, qpp[idx])
            cur[j] += dp[idx][tr(j,k)];
    fto(i, idx+1, len){
        fto(j,0,9)
            pre[j] = cur[j];
        clr(cur, 0);
        fto(j, 0, 9)
            cur[j] += pre[tr(j, qpp[i])];
        }
    if (debugg) debuga1(cur, 0,9);
    fto(j,1,9)
        ret += cur[j];
    if (debugg) debug(ret);
    if (qpp[idx]!=9) ret += cal1(qpp, idx-1, len, num);
    return ret;
}

ll cal(ll num){ //calculate valid numbers in [1,num]
    if (debugg){
        cout<<"cal starts"<<endl;
        
    }
    //cout<<num<<endl;
    if (num==0)
        return 0;
    if (num<10){
        //cout<<solve_small(1, num)<<endl;
        return solve_small(1, num);};
    int qpp[20];
    clr(qpp,0);
    int len = 0;
    ll ret = 0;
    ll tmp = num;
    
    while (tmp > 0){
        qpp[len++] = tmp%10;
        tmp /=10;
    }
    fto(j, 1, 9)
        fto(k, 0, qpp[len-1])
            ret += dp[len-1][tr(j,k)];

    if (qpp[len-1]!=9) ret += cal1(qpp, len - 2, len, num);
    return ret;

}

ll solve_large(ll f, ll l){
    return cal(l) - cal(f-1);
}
int main(){
    ios_base::sync_with_stdio(0);
    dp[0][0] = 0;
    fto(j, 0, 9)
        dp[1][j] = 1;
    if (debugg) debuga1(dp[1], 0, 9);
    fto(i,2,19){
        fto(j,0,9)
        {
            dp[i][j] = 0;
            fto(k, 0, 9){
                dp[i][j] += dp[i-1][tr(j,k)];
            }
            //if (debugg) cout<<i<<" "<<j<<" "<<dp[i][j]<<" ";
        }
        //if (debugg) debuga1(dp[i], 0, 9);
    }

    // if (debugg) {
    //     int tmp = 1;
    //     fto(j, 1, 9)
    //         tmp += dp[6][j];
    //     debug(tmp);
    // }

    // fto (f, 82345, 88888)
    //     fto(l, f+1, f+300)
    //         if (solve_small(f,l)!=solve_large(f,l)){
    //             cout<<"ERROR!";
    //             debug(f);debug(l);
    //             cout<<solve_small(f, l)<<endl;
    //             debugg= true;
    //             cout<<solve_large(f,l)<<endl;
    //             debugg= false;
    //             return 0;
    //         }

    
    cin>>T;
    fto(it,0,T){
        cin>>f>>l; 
        ll cl, cf;
        cl = cal(l);
        cf = cal(f-1);
        ans = cl - cf;
        
        cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
            
}
