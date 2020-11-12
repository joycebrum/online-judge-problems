#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cmath>

#define inf 1000000000
#define pair_ii pair<int, int>

using namespace std;

long long latency[20010];
long long n, m;
vector< vector<pair_ii> > adj;

void bellman_ford(int s) {
	for(int vertice = 0; vertice < n; vertice++) {
		latency[vertice] = inf;
	}

    latency[s] = 0;
    
    for (int j = 0; j < n; j++) {
		for(int u = 0; u < n; u++) { //para todos os vertices
			if (latency[u] == inf) {
				continue;
			} 
			for(unsigned int i = 0; i < adj[u].size(); i++){ //para cada aresta
				int v = adj[u][i].first;
				int w = adj[u][i].second;
				if(latency[v] > latency[u] + w) { //relaxamento
					latency[v] = latency[u] + w;
				}
			}
		}
	}
	
	//check for negative cycles	
	for (int j = 0; j < n; j++) {
		bool update = false;
		for(int u = 0; u < n; u++) {
			if(latency[u] == inf) {
				continue;
			}
			for(unsigned int i = 0; i < adj[u].size(); i++) { 
				int v = adj[u][i].first;
				int w = adj[u][i].second;
				if(latency[v] > latency[u] + w) {
					latency[v] = -inf;
					update = true;
				}
			}
		}
		if(not update) break;
	}
}

int main()
{
	long long q, t;
	long long teste = 0;
    while(cin >> n) {
		teste += 1;
		int busyness[n+1];
		adj.clear();
		for(int i = 0; i < n; i++) {
			cin >> busyness[i];
			vector<pair_ii> vec;
			adj.push_back(vec);
		} 
		cin >> m;
		for(int i = 0; i < m; i++) {
			int from, to;
			cin >> from >> to;
			adj[from-1].push_back(pair_ii(to-1, pow(busyness[to-1]-busyness[from-1], 3)));
		}
		cin >> q;
		
		bellman_ford(0);
		cout << "Set #" << teste << endl;
		for(int i = 0; i < q; i++) {
			cin >> t;
			if (latency[t-1] < 3 || latency[t-1] >= inf) {
				cout << "?" << endl;
			}
			else {
				cout << latency[t-1] << endl;
			}
		}
	}
}
