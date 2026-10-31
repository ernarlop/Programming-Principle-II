#include <bits/stdc++.h>
using namespace std;
struct Node { int x; Node *l = 0, *r = 0; };
void ins(Node*& t, int x) { if (!t) t = new Node{x}; else if (x < t->x) ins(t->l, x); else ins(t->r, x); }
int tri(Node* t) { return t ? (t->l && t->r) + tri(t->l) + tri(t->r) : 0; } // оба сына — треугольник
int main() {
    int n, x; Node* root = 0;
    cin >> n;
    while (n--) cin >> x, ins(root, x);
    cout << tri(root);
}
