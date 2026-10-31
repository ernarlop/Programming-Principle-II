#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int q, k, x; string c; cin >> q >> k;
    priority_queue<int, vector<int>, greater<>> h; // k самых больших, сверху — меньшее из них
    long long s = 0;
    while (q--) {
        cin >> c;
        if (c == "print") { cout << s << "\n"; continue; }
        cin >> x; h.push(x); s += x;
        if ((int)h.size() > k) s -= h.top(), h.pop(); // лишнее выкидываем
    }
}
