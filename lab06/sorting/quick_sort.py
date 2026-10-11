# Быстрая сортировка: O(n log n) в среднем. Делим по опорному p: слева <= p, справа >= p.
def quick_sort(a, l, r):
    p, i, j = a[(l + r) // 2], l, r
    while i <= j:
        while a[i] < p: i += 1
        while a[j] > p: j -= 1
        if i <= j: a[i], a[j] = a[j], a[i]; i += 1; j -= 1
    if l < j: quick_sort(a, l, j)
    if i < r: quick_sort(a, i, r)

n = int(input()); a = list(map(int, input().split()))
if n: quick_sort(a, 0, n - 1)
print(*a)
