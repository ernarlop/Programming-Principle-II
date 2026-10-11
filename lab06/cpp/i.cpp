#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin >> s;
    int c[26] = {};
    for (char ch : s) c[ch - 'a']++; // сортировка подсчётом: считаем каждую букву
    for (int i = 0; i < 26; i++) cout << string(c[i], 'a' + i); // и выписываем по порядку
}
