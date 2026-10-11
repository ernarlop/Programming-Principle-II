import sys
d = list(map(int, sys.stdin.read().split()))  # строки могут отсутствовать, читаем всё сразу
n, m = d[0], d[1]
a, b = sorted(d[2:2 + n]), sorted(d[2 + n:2 + n + m])
i = j = 0; res = []
while i < n and j < m:  # два указателя, как слияние в merge sort
    if a[i] < b[j]: i += 1
    elif a[i] > b[j]: j += 1
    else: res.append(a[i]); i += 1; j += 1
print(*res)
