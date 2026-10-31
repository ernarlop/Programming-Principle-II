#include <bits/stdc++.h>
using namespace std;

struct Node {
    int x;
    Node *l = 0, *r = 0;
};

void ins(Node*& t, int x) {
    if (!t) t = new Node{x};
    else if (x < t->x) ins(t->l, x);
    else ins(t->r, x);
}

int s = 0;

void go(Node* t) { // обход наоборот: правое, вершина, левое — от большего к меньшему
    if (!t) return;
    go(t->r);
    s += t->x; // сумма всех ключей >= текущего
    cout << s << " ";
    go(t->l);
}

int main() {
    int n, x;
    cin >> n;
    Node* root = 0;
    while (n--) cin >> x, ins(root, x);
    go(root);
}
