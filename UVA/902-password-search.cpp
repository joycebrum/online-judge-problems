#include <iostream>
#include <map>

using namespace std;

string find_max(map<string, int> count){
	string max_key = "";
	int max_value = -1;
	for (auto const& x : count)
	{
		if (x.second > max_value){
			max_value = x.second;
			max_key = x.first;
		}
	}
	return max_key;
}

string find_password(int n, string msg) {
	map<string, int> count;
	for (unsigned int i = 0; i < msg.length(); i++) {
		if (i + n > msg.length())
			break;
		string substr = msg.substr (i,n);
		if (!count[substr]){
			count[substr] = 0;
		}
		count[substr] += 1;
	}
	return find_max(count);
}
int main(){
	string msg;
	int n;
	while (cin >> n)
	{
		cin >> msg;
		string pass = find_password(n, msg);
		cout << pass << endl;
	}
}
