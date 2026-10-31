n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
cols = [sorted(c, reverse=True) for c in zip(*rows)]  # каждый столбец по убыванию
for r in zip(*cols): print(*r)
