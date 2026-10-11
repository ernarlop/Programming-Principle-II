#include <bits/stdc++.h>
using namespace std;
string key(const string& s) { return s.substr(6, 4) + s.substr(3, 2) + s.substr(0, 2); } // ГГГГММДД
int main() {
    int n; cin >> n;
    vector<string> v(n);
    for (auto& s : v) cin >> s;
    sort(v.begin(), v.end(), [](auto& a, auto& b) { return key(a) < key(b); });
    for (auto& s : v) cout << s << "\n";
}
