#include <iostream>

using namespace std;

int get_ways_decimals(int n, int k) {
	int decimals = 1;
	double ways = 1.0;
	
	for (int i = 0; i < k; i++) {
		ways = (ways * (n-i)) / (k-i);
		while(ways >= 10) {
			ways = ways / 10;
			decimals += 1;
		}
	}
	return decimals;
}

int main() {
	int n, k;
	while (cin >> n) {
		cin >> k;
		int decimals = get_ways_decimals(n, k);
		cout << decimals << endl;
	}
}
