#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m; cin >> n >> m;
    vector<int> a(n), b(m);
    for (int& x : a) cin >> x;
    for (int& x : b) cin >> x;
    sort(a.begin(), a.end()); sort(b.begin(), b.end());
    for (int i = 0, j = 0; i < n && j < m;) // два указателя, как слияние в merge sort
        if (a[i] < b[j]) i++;
        else if (a[i] > b[j]) j++;
        else cout << a[i] << " ", i++, j++;
    cout << "\n";
}
