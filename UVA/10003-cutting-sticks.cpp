#include <iostream>
#include <vector>

#define MAX 2147483647

using namespace std;

int min_cuts(int C[52][52], int cuts[52], int n) {
	for(int a = 2; a <= n; a++) {
		for(int b = 0, c = a + b; c <=n; b++, c++) {
			int min = MAX;
			for(int d = b + 1; d < c; d++) {
				int cost = C[b][d] + C[d][c] + cuts[c] - cuts[b];
				if(min > cost) min = cost;
			}
			C[b][c] = min;
		}
	}
	return C[0][n];
}

int main() {
	int n, l, cuts[52] = {0};
	
	while(cin >> l and l > 0) {
		cin >> n;
		int C[52][52] = {};
		
		for(int i = 1; i <= n; i++) {
			cin >> cuts[i];
		}
		cuts[++n] = l;
		
		int min_cut = min_cuts(C, cuts, n);
		cout << "The minimum cutting is " << min_cut << "." << endl; 
	}
}
