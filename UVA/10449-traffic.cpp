#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cmath>

#define inf 1000000000
#define pair_ii pair<int, int>

using namespace std;

int latency[20010];
int n, m;
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
	int q, t;
	int teste = 0;
    while(cin >> n) {
		teste += 1;
		int busyness[n+1];
		for(int i = 0; i < n; i++) {
			cin >> busyness[i];
			vector<pair_ii> vec;
			adj.push_back(vec);
		} 
		cin >> m;
		for(int i = 0; i < m; i++) {
			int x, y;
			cin >> x >> y;
			adj[x-1].push_back(pair_ii(y-1, pow(busyness[y-1]-busyness[x-1], 3)));
		}
		cin >> q;
		dijkstra(0);
		cout << "Set #" << teste << endl;
		for(int i = 0; i < q; i++) {
			cin >> t;
			if (latency[t-1] < 3) {
				cout << "?" << endl;
			}
			else {
				cout << latency[t-1] << endl;
			}
		}
	}
}
