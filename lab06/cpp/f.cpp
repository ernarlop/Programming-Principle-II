#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    map<string, double> g = {{"A+", 4}, {"A", 3.75}, {"B+", 3.5}, {"B", 3}, {"C+", 2.5}, {"C", 2}, {"D+", 1.5}, {"D", 1}, {"F", 0}};
    int n, m, c; string last, first, mark; cin >> n;
    vector<tuple<double, string, string>> v; // GPA, фамилия, имя — в таком порядке и сортируем
    while (n--) {
        cin >> last >> first >> m;
        double s = 0, cr = 0;
        while (m--) cin >> mark >> c, s += g[mark] * c, cr += c;
        v.push_back({s / cr, last, first});
    }
    sort(v.begin(), v.end());
    cout << fixed << setprecision(3);
    for (auto& [gpa, l, f] : v) cout << l << " " << f << " " << gpa << "\n";
}
