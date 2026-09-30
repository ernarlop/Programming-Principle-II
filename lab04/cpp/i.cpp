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

int leaves(Node* t) {
    if (!t) return 0;
    if (!t->l && !t->r) return 1; // нет сыновей — лист
    return leaves(t->l) + leaves(t->r);
}

int main() {
    int n, x;
    cin >> n;
    Node* root = 0;
    while (n--) cin >> x, ins(root, x);
    cout << leaves(root);
}
