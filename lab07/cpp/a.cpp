#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t;
    cin >> t;
    string line;
    getline(cin, line); // finish the first line

    while (t--) {
        getline(cin, line);
        stringstream ss(line);
        vector<string> w;
        string s;
        while (ss >> s) w.push_back(s);

        // min-heap of (length, position):
        // shorter words come out first; equal length -> the one that was earlier (stable)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (int i = 0; i < (int)w.size(); i++) pq.push({(int)w[i].size(), i});

        bool first = true;
        while (!pq.empty()) {
            if (!first) cout << " ";
            cout << w[pq.top().second];
            pq.pop();
            first = false;
        }
        cout << "\n";
    }
}
