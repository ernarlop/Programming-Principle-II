#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int &v : a) cin >> v;
    // in-order обход BST выдаёт числа по возрастанию — то же самое даёт sort
    sort(a.begin(), a.end());
    cout << (k > n ? -1 : a[k - 1]);
}
