#include <bits/stdc++.h>
using namespace std;
// Подсчёт: O(n + MAX). Только для небольших чисел (здесь 0..10^6).
int c[1000001];
int main() {
    int n, x; cin >> n;
    for (int i = 0; i < n; i++) cin >> x, c[x]++; // сколько раз встретилось x
    for (int v = 0; v <= 1000000; v++)
        for (int j = 0; j < c[v]; j++) cout << v << " ";
}
