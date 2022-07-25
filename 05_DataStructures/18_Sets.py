# 4'03

# kolekcije bez duplikata

import numbers


numbers = [1, 1, 2, 2, 3, 3, 4]
uniques = set(numbers)
print(uniques)  # {1, 2, 3, 4}

second = {4, 5, 6}
# second.add(remove itd) # metodi
len(second)

# posebno sjaje u set-operacijama & | - ^

print(uniques | second)  # {1, 2, 3, 4, 5, 6}
print(uniques & second)  # {4}
print(uniques - second)  # {1, 2, 3}
print(uniques ^ second)  # {1, 2, 3, 5, 6}

# nisu ordered pa pokusaji trazenja indeksa daju error!

if 1 in uniques:
    print("yes")
