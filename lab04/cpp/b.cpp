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

int size(Node* t) { // сколько вершин в поддереве t
    return t ? 1 + size(t->l) + size(t->r) : 0;
}

int main() {
    int n, x;
    cin >> n;
    Node* root = 0;
    while (n--) cin >> x, ins(root, x);
    cin >> x;
    Node* t = root;
    while (t->x != x) t = (x < t->x ? t->l : t->r); // ищем вершину x
    cout << size(t);
}
