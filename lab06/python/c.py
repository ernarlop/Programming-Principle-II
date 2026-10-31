input(); a = sorted(map(int, input().split()))
d = min(a[i] - a[i - 1] for i in range(1, len(a)))  # минимальная разница соседей
print(*[x for i in range(1, len(a)) if a[i] - a[i - 1] == d for x in (a[i - 1], a[i])])
