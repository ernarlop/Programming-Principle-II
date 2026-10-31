#include <bits/stdc++.h>
using namespace std;
// Пузырёк: O(n^2). Соседей меняем местами, большие "всплывают" в конец.
int main() {
    int n; cin >> n;
    vector<int> a(n);
    for (int& x : a) cin >> x;
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++)
            if (a[j] > a[j + 1]) swap(a[j], a[j + 1]), swapped = true;
        if (!swapped) break; // уже отсортировано
    }
    for (int x : a) cout << x << " ";
}
