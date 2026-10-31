#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; char k; cin >> n;
    vector<char> a(n);
    for (char& c : a) cin >> c;
    cin >> k;
    auto it = upper_bound(a.begin(), a.end(), k); // первая буква > k (бинпоиск)
    cout << (it == a.end() ? a[0] : *it);
}
