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

vector<long long> sum; // sum[d] — сумма на уровне d

void go(Node* t, int d) {
    if (!t) return;
    if (d == (int)sum.size()) sum.push_back(0); // новый уровень
    sum[d] += t->x;
    go(t->l, d + 1);
    go(t->r, d + 1);
}

int main() {
    int n, x;
    cin >> n;
    Node* root = 0;
    while (n--) cin >> x, ins(root, x);
    go(root, 0);
    cout << sum.size() << "\n";
    for (auto s : sum) cout << s << " ";
}
