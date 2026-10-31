#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; string a, b; cin >> n;
    map<string, string> orig; // текущий ник -> исходный
    while (n--) {
        cin >> a >> b;
        string o = orig.count(a) ? orig[a] : a;
        orig.erase(a);
        orig[b] = o;
    }
    map<string, string> res; // исходный -> текущий, map сам сортирует
    for (auto& [cur, o] : orig) res[o] = cur;
    cout << res.size() << "\n";
    for (auto& [o, cur] : res) cout << o << " " << cur << "\n";
}
