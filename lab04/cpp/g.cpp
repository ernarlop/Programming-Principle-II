#include <bits/stdc++.h>
using namespace std;
struct Node { int x; Node *l = 0, *r = 0; };
// равное не вставляем
void ins(Node*& t, int x) { if (!t) t = new Node{x}; else if (x < t->x) ins(t->l, x); else if (x > t->x) ins(t->r, x); }
int ans = 0;
int h(Node* t) { // высота в вершинах; путь через t = левая высота + правая + 1
    if (!t) return 0;
    int a = h(t->l), b = h(t->r);
    ans = max(ans, a + b + 1);
    return max(a, b) + 1;
}
int main() {
    int n, x; Node* root = 0;
    cin >> n;
    while (n--) cin >> x, ins(root, x);
    h(root);
    cout << ans;
}
