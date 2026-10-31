#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m, x; cin >> n >> m;
    vector<vector<int>> c(m); // c[j] — j-й столбец
    for (int i = 0; i < n * m; i++) cin >> x, c[i % m].push_back(x);
    for (auto& col : c) sort(col.rbegin(), col.rend()); // по убыванию
    for (int i = 0; i < n; i++, cout << "\n")
        for (int j = 0; j < m; j++) cout << c[j][i] << " ";
}
