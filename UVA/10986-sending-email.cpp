#include <bits/stdc++.h>
#include <iostream>

#define inf 1000000000
#define pair_ii pair<int, int>

using namespace std;

int latency[20010];
int n, m, s, t;
vector< vector<pair_ii> > adj;

void dijkstra(int s)
{
    for(int i = 0; i < n; i++) latency[i] = inf;
    latency[s] = 0;
    priority_queue<pair_ii, vector<pair_ii>, greater<pair_ii> > not_processed;
    not_processed.push( pair_ii(latency[s], s) );
    while(!not_processed.empty()){
		pair_ii p;
		int t, u;
        p = not_processed.top();
        not_processed.pop();
        t = p.first; u = p.second;
        
        if(t > latency[u] ) continue;
        for(unsigned int i = 0; i < adj[u].size(); i++){
            if(latency[adj[u][i].first] > latency[u] + adj[u][i].second){
                latency[adj[u][i].first] = latency[u] + adj[u][i].second;
                not_processed.push( pair_ii(latency[adj[u][i].first], adj[u][i].first) );
            }
        }
    }
}


int main()
{
    int testes;
    cin >> testes;
    
    for(int k = 1; k <= testes; k++){
		cin >> n >> m >> s >> t;
        adj.assign(n, vector<pair_ii>(0));
        int x, y, w;
        for(int i = 0; i < m; i++){
            cin >> x >> y >> w;
            adj[x].push_back( pair_ii(y, w) );
            adj[y].push_back( pair_ii(x, w) );
        }

        dijkstra(s);
        cout << "Case #" << k << ": ";
        if(latency[t] != inf) cout << latency[t] << endl;
        else cout << "unreachable" << endl;
    }
}
