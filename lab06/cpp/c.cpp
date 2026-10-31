#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    vector<int> a(n);
    for (int& x : a) cin >> x;
    sort(a.begin(), a.end());
    int d = INT_MAX;
    for (int i = 1; i < n; i++) d = min(d, a[i] - a[i - 1]); // минимальная разница соседей
    for (int i = 1; i < n; i++) if (a[i] - a[i - 1] == d) cout << a[i - 1] << " " << a[i] << " ";
}
