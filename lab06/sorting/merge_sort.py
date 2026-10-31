# Сортировка слиянием: всегда O(n log n). Делим пополам, сортируем половины, сливаем.
def merge_sort(a):
    if len(a) <= 1: return a
    L, R = merge_sort(a[:len(a) // 2]), merge_sort(a[len(a) // 2:])
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):  # берём меньший из двух "голов"
        if L[i] <= R[j]: res.append(L[i]); i += 1
        else: res.append(R[j]); j += 1
    return res + L[i:] + R[j:]

input(); print(*merge_sort(list(map(int, input().split()))))
