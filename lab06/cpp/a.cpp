#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, c[26] = {}; string s; cin >> n >> s;
    for (char ch : s) c[ch - 'a']++; // сортировка подсчётом
    for (char ch : string("aeioubcdfghjklmnpqrstvwxyz")) cout << string(c[ch - 'a'], ch); // алфавит Альберта
}
