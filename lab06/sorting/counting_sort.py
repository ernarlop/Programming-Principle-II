# Подсчёт: O(n + MAX). Только для небольших чисел (здесь 0..10^6).
input(); c = [0] * 1000001
for x in map(int, input().split()): c[x] += 1  # сколько раз встретилось x
print(*[v for v in range(len(c)) for _ in range(c[v])])
