# 1'28

letters = ["a", "b", "c", "d", "e", 1, 2]
print(letters.index(1))  # 5

# ? print(letters.index(3))  # ValueError: 3 is not in list
# ovo ponasanje je drugacije od npr C++ ili JS koji ako objekta nema vracaju idex -1
# kako bi to sprijecili obicno potragu za indeksom smjestamo u "if"

if 3 in letters:
    print(letters.index(3))     # i nema nista, pa ni greske!

# tome moze posluziti i metod "count"

print(letters.count(3))     # 0
