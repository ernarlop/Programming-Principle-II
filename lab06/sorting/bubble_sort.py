# Пузырёк: O(n^2). Соседей меняем местами, большие "всплывают" в конец.
n = int(input()); a = list(map(int, input().split()))
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if a[j] > a[j + 1]: a[j], a[j + 1] = a[j + 1], a[j]; swapped = True
    if not swapped: break  # уже отсортировано
print(*a)
