from bisect import bisect_right
input(); a = input().split(); k = input().strip()
i = bisect_right(a, k)  # первая буква > k (бинпоиск)
print(a[i] if i < len(a) else a[0])
