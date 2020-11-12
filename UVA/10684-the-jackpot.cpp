#include <iostream>
#include <vector>

using namespace std;

int get_max_winnings(vector<int> bets) {
	vector<int> max_bets;
	max_bets.push_back(bets[0]);
	int max = bets[0];
	
	for(unsigned int i = 1; i < bets.size(); i++) {
		max_bets.push_back(bets[i]);
		if(max_bets[i-1] > 0) {
			 max_bets[i] += max_bets[i-1];
		}
		if(max_bets[i] > max) max = max_bets[i];
	}
	return max;
}

int main() {
	int n;
	while(true) {
		cin >> n;
		vector<int> bets;
		if(n == 0) break;
		for(int i = 0; i < n; i++) {
			int bet;
			cin >> bet;
			bets.push_back(bet);
		}
		
		int max_bet = get_max_winnings(bets);
		if(max_bet > 0) {
			cout << "The maximum winning streak is " << max_bet << "." << endl;
		}
		else {
			cout << "Losing streak." << endl;
		}
	}
}
