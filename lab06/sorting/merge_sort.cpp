#include <bits/stdc++.h>
using namespace std;
// Сортировка слиянием: всегда O(n log n). Делим пополам, сортируем половины, сливаем.
vector<int> a, t;
void merge_sort(int l, int r) { // сортирует a[l..r]
    if (l >= r) return;
    int m = (l + r) / 2;
    merge_sort(l, m);
    merge_sort(m + 1, r);
    int i = l, j = m + 1, k = l;
    while (i <= m || j <= r) // берём меньший из двух "голов"
        t[k++] = (j > r || (i <= m && a[i] <= a[j])) ? a[i++] : a[j++];
    for (k = l; k <= r; k++) a[k] = t[k];
}
int main() {
    int n; cin >> n;
    a.resize(n); t.resize(n);
    for (int& x : a) cin >> x;
    merge_sort(0, n - 1);
    for (int x : a) cout << x << " ";
}
