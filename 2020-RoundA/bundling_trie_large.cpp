//referenced from Heltion's Bundling submission code

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

const int maxn = 2*1e6 + 10;
int kid[maxn][26], cnt[maxn], par[maxn], dep[maxn], nn;
int newnode(){
    nn += 1;
    fill(kid[nn], kid[nn] + 26, 0);
    cnt[nn] = par[nn] = dep[nn] = 0;
    return nn;
}

int main(){
    //https://stackoverflow.com/questions/31162367/significance-of-ios-basesync-with-stdiofalse-cin-tienull
    ios::sync_with_stdio(false); //not sync c & c++ 
    cin.tie(nullptr); //untie cin & cout
    cout.tie(nullptr);
    int T;
    cin>>T;
    fto(ite,0,T){
        int n, k;
        cin>>n>>k;
        nn = 0;
        newnode();
        fto(i,0,n){
            string s;
            cin >> s;
            int p = 1;
            for(char c : s){
                if(not kid[p][c - 'A']){
                    kid[p][c - 'A'] = newnode();
                    par[kid[p][c - 'A']] = p;
                    dep[kid[p][c - 'A']] = dep[p] + 1;
                }
                p = kid[p][c - 'A'];
            }
            cnt[p] += 1; //相当于我本来的end 
        }
        int ans = 0;
        for(int i = nn; i; i -= 1){
            ans += cnt[i] / k * dep[i];
            cnt[par[i]] += cnt[i] % k;
        }
        cout << "Case #" << ite + 1 << ": " << ans << endl;
    }
    return 0;
}
