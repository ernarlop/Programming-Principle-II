#include <bits/stdc++.h>
using namespace std;

struct Node {
    int x;
    Node *l = 0, *r = 0;
};

// d — глубина; пути не длиннее 100, поэтому глубже 100 вершины не нужны
void ins(Node*& t, int x, int d) {
    if (d > 100) return;
    if (!t) t = new Node{x};
    else if (x <= t->x) ins(t->l, x, d + 1); // равные идут влево
    else ins(t->r, x, d + 1);
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m, x;
    cin >> n >> m;
    Node* root = 0;
    while (n--) cin >> x, ins(root, x, 0);
    while (m--) {
        string s;
        cin >> s;
        Node* t = root;
        for (char c : s) if (t) t = (c == 'L' ? t->l : t->r); // идём по пути
        cout << (t ? "YES" : "NO") << "\n";
    }
}
