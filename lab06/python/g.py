orig = {}  # текущий ник -> исходный
for _ in range(int(input())):
    a, b = input().split()
    orig[b] = orig.pop(a, a)
print(len(orig))
for o, cur in sorted((o, cur) for cur, o in orig.items()): print(o, cur)
