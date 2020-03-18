//referenced from https://www.programmersought.com/article/50971865916/;jsessionid=1D9B9375999162C5FBF6D6F25B01F12D
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
L lowercase words 
s1 s2 first 2 letters of string S

N length of S

N A B C D
xi = (A*Xi-1 + B*Xi-2 + C) % D

original / scrambled 
1:14开始

1:27 还剩57min 想看手机 
*/


class Word{
public:
    int s, e, l;
    //string w; 
    unsigned short key[26];
    Word(string word){
        s = word[0];
        e = word[word.size()-1];
        l = word.size();
        //sort(word.begin(), word.end());
        //w = word;
        clr(key,0);
        for (auto &c: word)
            key[c-'a']++;
    }
    /*bool operator == (const Word &b) const{
        return (s == b.s && e = b.e && w ==b.w);
    };*/
    bool operator == (const Word &w) const{
        if (s == w.s && e == w.e){
            fto(i,0,26){
                if (key[i]!=w.key[i])
                    return false;
            }
            return true;
        };
        return false;
    }

};


//没加这一段的时候会报error： implicit instantiation of undefined template 'std::__1::hash<Word>'
namespace std{
    template <>
    class hash<Word>{
    public:
        size_t operator() (const Word &w) const{ 
        //2个const 一定要加 不然会报错no matching function for call to object of type 'conststd::__1::hash<Word>'
            auto ih = hash<int>();
            auto sh = hash<unsigned short>();
            //size_t ans = hash<int>(w.s); 
            //一定要命名 不然会报错 no matching conversions from int to hash<int>
            size_t ans = ih(w.s);

            ans ^= ih(w.e);
            for (auto &c: w.key){
                ans ^= sh(c);
            }
            return ans;
        }
    };
}




const int N = 1e6 + 10; // 这样更好 防止下面弄着弄着就少了个0
int q,p1,p2,ans,T, t, n,cnt, i,j, l,r;
bool flag;
char s1, s2;
//int ord[N];
ll a,b,c,d, ord[N];
string word,ss,tmp;
set<int> lengths;
//set<Word> dic; 涉及erase之后 可能有多个key后这样就不太好
unordered_map<Word, int> dic;
/*struct Word{
    int s, e, l;
    bool flag;
    string w;
}dic[100000];*/





int main(){
    ios_base::sync_with_stdio(0);
    cin>>T;
    fto(it,0,T){

        cin>>l;
        clr(ord,0);
        dic.clear();
        lengths.clear();
        fto(i, 0, l){
            cin>>word;
            //dic.insert(Word(word));
            dic[Word(word)] ++;
            lengths.insert(word.size());
        };
        cin>>s1>>s2;
        cin>>n>>a>>b>>c>>d;
        ss = "";
        ss += s1;
        ss += s2;
        ord[0] = int(s1);
        ord[1] = int(s2);
        // a %= d;
        // b %= d;
        // c %= d;
        fto(i, 2, n){
            ord[i] = (a*ord[i-1] + b*ord[i-2] + c)%d;
            ss += char(ord[i]%26 + 97);
        }
        
        ord[0] -= 97;
        ord[1] -= 97;
        fto(i, 2, n){
            ord[i] %=26;
        }
        ans = 0;
        //debuga1(ord, 0, n);
        //debug(ss);
        //fto(i, 0, n)
        //    fto(j, 0, l){
        for (auto &l: lengths){ //一开始报错expect unqualified-id 是因为我的ll - long long 
            if (l > n)
                continue;
            i = 0;
            Word tmp = Word(ss.substr(0, l));
            auto it = dic.find(tmp);
            if (it != dic.end()){
                //ans += dic[tmp]; 
                //debug(it->second);

                ans += it->second;
                dic.erase(it); //从dic.erase(tmp) -> dic.erase(it) 后 TLE -> AC！
            }
            //在转换的时候发现直接用s sort 还是不行tmp.w = ss[0];
            tmp.key[ss[0]-'a']--;
            fto (i, 1, n-l+1){
                tmp.s = ss[i];
                tmp.e = ss[i+l-1];
                tmp.key[ss[i+l-1]-'a'] ++;
                auto it = dic.find(tmp);
                if (it != dic.end()){
                //ans += dic[tmp]; 
                   // debug(i);
                    //debug(it->second);
                    ans += it->second;
                    dic.erase(it);
            }
                tmp.key[ss[i]-'a'] --;
            }
        }
        
    cout << "Case #" << it + 1 << ": "<<ans<<endl;
    }
}
