s = input()
# сортировка подсчётом: считаем каждую букву и выписываем по порядку
print("".join(ch * s.count(ch) for ch in "abcdefghijklmnopqrstuvwxyz"))
