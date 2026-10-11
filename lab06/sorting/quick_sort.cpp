#include <bits/stdc++.h>
using namespace std;
// Быстрая сортировка: O(n log n) в среднем. Делим по опорному p: слева <= p, справа >= p.
vector<int> a;
void quick_sort(int l, int r) {
    int p = a[(l + r) / 2], i = l, j = r;
    while (i <= j) {
        while (a[i] < p) i++;
        while (a[j] > p) j--;
        if (i <= j) swap(a[i++], a[j--]);
    }
    if (l < j) quick_sort(l, j);
    if (i < r) quick_sort(i, r);
}
int main() {
    int n; cin >> n;
    a.resize(n);
    for (int& x : a) cin >> x;
    if (n) quick_sort(0, n - 1);
    for (int x : a) cout << x << " ";
}
