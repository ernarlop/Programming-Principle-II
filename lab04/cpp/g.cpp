#include <bits/stdc++.h>
using namespace std;

struct Node {
    int x;
    Node *l = 0, *r = 0;
};

void ins(Node*& t, int x) {
    if (!t) t = new Node{x};
    else if (x < t->x) ins(t->l, x);
    else if (x > t->x) ins(t->r, x); // равное не вставляем
}

int ans = 0;

int h(Node* t) { // высота поддерева в вершинах
    if (!t) return 0;
    int a = h(t->l), b = h(t->r);
    ans = max(ans, a + b + 1); // самый длинный путь через вершину t
    return max(a, b) + 1;
}

int main() {
    int n, x;
    cin >> n;
    Node* root = 0;
    while (n--) cin >> x, ins(root, x);
    h(root);
    cout << ans;
}
