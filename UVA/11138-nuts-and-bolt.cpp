#include<algorithm>
#include<iostream>
#include<cmath>
#include<vector>
#include<cstring>
using namespace std;
const int maxn=550;
 
vector<int>possible_nuts[maxn];
int bolt_with_nut[maxn],used[maxn];
int ans;
int bolts, nuts,flag;
void initial()
{
    for(int i=0;i<maxn;++i){
        bolt_with_nut[i]=-1;
        possible_nuts[i].clear();
    }
    ans=0;
}
 
void readcase()
{
    cin >> bolts >> nuts;
    for(int i=1;i<=bolts;++i){
        for(int j=1;j<=nuts;++j){
            cin >> flag;
            if(flag) possible_nuts[i].push_back(j);
        }
    }
}
 
bool solve(int x)
{
    for(unsigned int i=0; i < possible_nuts[x].size(); ++i){
        int nut = possible_nuts[x][i];
        if(!used[nut]){
            used[nut]=1;
            if(bolt_with_nut[nut]==-1||solve(bolt_with_nut[nut])){
                bolt_with_nut[nut]=x;
                return true;
            }
        }
    }
    return false;
}
 
void computing()
{
    for(int i=1;i<=bolts;++i)
    {
        memset(used,0,sizeof(used));
        if(solve(i))
            ans++;
    }
    cout << "a maximum of " << ans << " nuts and bolts can be fitted together" << endl;
}
 
int main()
{
    int t;
    cin >> t;
    for(int i =1;i<=t; i++){
        initial();
        readcase();
        cout << "Case "<< i << ": ";
        computing();
    }
    return 0;
}
