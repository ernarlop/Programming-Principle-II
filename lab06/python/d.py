v = [input() for _ in range(int(input()))]
v.sort(key=lambda s: (s[6:], s[3:5], s[:2]))  # год, месяц, день
print("\n".join(v))
