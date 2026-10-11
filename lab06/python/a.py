input(); s = input()
# сортировка подсчётом: для каждой буквы алфавита Альберта выписываем её столько раз, сколько встретилась
print("".join(ch * s.count(ch) for ch in "aeioubcdfghjklmnpqrstvwxyz"))
