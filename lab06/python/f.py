import sys
g = {"A+": 4, "A": 3.75, "B+": 3.5, "B": 3, "C+": 2.5, "C": 2, "D+": 1.5, "D": 1, "F": 0}
v = []
for line in sys.stdin.read().splitlines()[1:]:
    w = line.split()
    if not w: continue
    marks, cr = w[3::2], list(map(int, w[4::2]))
    v.append((sum(g[x] * c for x, c in zip(marks, cr)) / sum(cr), w[0], w[1]))
v.sort()  # GPA, фамилия, имя
print("\n".join(f"{l} {f} {gpa:.3f}" for gpa, l, f in v))
