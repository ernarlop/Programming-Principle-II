#include <bits/stdc++.h>
using namespace std;
struct Node { int x; Node *l = 0, *r = 0; };
// пути не длиннее 100, поэтому глубже 100 не вставляем (иначе цепочка из 10^5 — TL)
void ins(Node*& t, int x, int d = 0) {
    if (d > 100) return;
    if (!t) t = new Node{x};
    else if (x <= t->x) ins(t->l, x, d + 1); // равные — влево
    else ins(t->r, x, d + 1);
}
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m, x; string s; Node* root = 0;
    cin >> n >> m;
    while (n--) cin >> x, ins(root, x);
    while (m--) {
        cin >> s;
        Node* t = root;
        for (char c : s) if (t) t = c == 'L' ? t->l : t->r;
        cout << (t ? "YES\n" : "NO\n");
    }
}
