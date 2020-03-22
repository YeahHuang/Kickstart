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

N strings 包含A..Z

捆绑strings to 尺寸为K的组

score - 最长子串

最多每个组组只有K个 

N 0..1e5

具备传递性 score(a,b) = v1, score(a,c) = v2
if v2 >= v1:
   score(b,c) >= v1 
   
small: 计算全部的score
n*n的矩阵 
从契合度最高的 直接贪心的去取 试一下 


small 最暴力的： 打擂法

*/

const int N = 1e5 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,ans,T,  n, k, cnt, common_len, i,j,jj,l,r, res;
bool flag;
string tmp,s1,s2;
vector<string> s;
//vector<vector<int>> m[26];
bool debugg = true;
bool test = true;


int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(ite,0,T){

        cin>>n>>k;
        s.clear();
        fto(i,0,n){
            cin>>tmp;
            //tmp += char(i);
            s.push_back(tmp);
            //m[s[i][0]-'A'].push_back(s[i]);
        }
        sort(s.begin(),s.end());
        //fto(i,0,26)
        //    sort(m[i].begin(), m[i].end());
        i = 0;ans = 0;
        if (debugg){
            for (auto it = s.begin(); it != s.end(); it++)
                cout<<*it<<" ";
            cout<<endl;
        }
        auto it = s.begin();
        res = n;
        while (res >= k){
           auto it1 = it;
           while (it1 != s.end() && (*it1)[0] == (*it)[0])
                it1 ++;
            it1 --;
            if (debugg){
                cout << *it << " " <<*it1<<endl;
                debug(it1-it+1);
            }
            if (it1 - it  + 1 < k){
                res -= it1 - it  + 1;
            } else{
                res -= it1 - it + 1;
                if (debugg) cout<<(it1 - it + 1)/k <<endl;
                int total_times = (it1 - it + 1)/k ;
                fto(times, 0, total_times){
                if (debugg) debug(times);
                // if (times == total_times - 1){
                //     s1 = *it;
                //     s2 = *(it + k - 1);
                //     common_len = min(s1.size(),s2.size());
                //     fto (jj, 1, min(s1.size(), s2.size()))
                //         if (s1[jj] != s2[jj]){
                //             common_len = jj ;
                //             break;
                //         };
                //     ans += common_len;
                //     continue;
                // }



                auto it2 = it;
                auto it_max = it;
                int max_com = 0;
                int bob = 0;
                while (bob<k-1){
                    if (it2>it1 || it2+k-1 > it1)
                        break;
                    s1 = *it2; s2 = *(it2+k-1);
                    if (debugg){
                        debug(bob);
                        cout<<"comparing "<<s1<< " "<<s2<<endl;
                    }
                    common_len = min(s1.size(),s2.size());
                    fto (jj, 1, min(s1.size(), s2.size()))
                        if (s1[jj] != s2[jj]){
                            common_len = jj ;
                            break;
                        };
                    if (debugg) debug(common_len);
                    if (common_len > max_com){
                        max_com = common_len;
                        it_max = it2;
                    }
                    it2 ++;
                    bob ++;
                }
                if (debugg){
                    cout<<max_com;
                    cout<<" "<<*it_max<<endl;
                }
                ans += max_com;
                if (it_max == it){
                    it += k;
                }else{
                    auto it0 = it_max;
                    fto(aha, 0, k){
                     //for (auto it0 = it_max; it0 < it_max + k; it0++){
                        //if (debugg) cout << "is erasing "<<*it0<<endl;
                        s.erase(it0);
                        it0++;
                     }
                        
                }  
                if (debugg) debug(times); 
                //if (debugg) cout<<(it1 - it + 1)/k <<endl;  
                }
                
            };
            it1 ++;
            it = it1;
            }
        cout << "Case #" << ite + 1 << ": "<<ans<<endl;
        }
        
    
        
        }
        /*
        while (i<n){
            l = i;
            r = i;
            while (r < n && s[r][0] == s[l][0])
                r++;
            if (r-l+1 < k){
                i = r + 1;
            }else {
                if (r-l+1 == k){
                    p1 = l;p2=r;
                    fto (jj, 0, min(s[p1].size(), s[p2].size()))
                        if (s[p1][jj] != s[p2][jj]){
                            common_len = jj - 1;
                            break;
                        };
                    ans += common_len;
                }

                i = r + 1;
            }*/
