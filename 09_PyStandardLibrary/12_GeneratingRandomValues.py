# 4'09
import random
import string

print(random.random())  # 0.4903964984014487
print(random.randint(1, 10))  # 7
print(random.choice([1, 2, 3, 4, 5]))  # 1
print(random.choices([1, 2, 3, 4, 5], k=3))  # [1, 3, 2]
print(random.choices("abcdefghijklmnoprsstuvzxy", k=4))  # ['a', 'i', 'i', 'e']

# kako bi generirali password trebamo kombinirati gornje metode i formirati string. Naravno, ja bih jos dodao:
print(random.choice("ABCDEFGHIJKLMNOPRSTUVZXY"))
print(random.choice(".,!?"))

# i sad imam sve potrebne uvjete za moje passove
print("".join(random.choices("abcdefghij", k=4)))

# ali poslije kaze za join da je tidious i da ima better way: a to je koristenje metoda
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ; abcdefghijklmnopqrstuvwxyz; ABCDEFGHIJKLMNOPQRSTUVWXYZ; 0123456789

# i konacno rjesenje koje zadovoljava posao i koje je Athovo u osnovi s tim sto sam ja dodao jos jedan join u konkatinaciju!!
print("".join(random.choices(string.ascii_letters+string.digits, k=15)) +
      "".join(random.choice(".,!?")))
# aDj2UkOlZ9jCDt7!; KZmf5sE3IPi1xzy,; AdgoN3X9xyKDCxI,

# za kraj Ath jos o "shuffle"
numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)  # in place
print(numbers)  # [4, 3, 6, 1, 5, 2]; [1, 6, 4, 3, 5, 2]
