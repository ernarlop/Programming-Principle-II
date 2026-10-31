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

int tri(Node* t) { // треугольник = вершина, у которой есть оба сына
    if (!t) return 0;
    return (t->l && t->r) + tri(t->l) + tri(t->r);
}

int main() {
    int n, x;
    cin >> n;
    Node* root = 0;
    while (n--) cin >> x, ins(root, x);
    cout << tri(root);
}
