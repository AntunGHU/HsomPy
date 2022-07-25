# 3'51

numbers = [0, 1, 2]
first = numbers[0]
second = numbers[1]
third = numbers[2]
print(first)
print(second)
print(third)

# isto to moze i ovako pod uvjetom da je broj verijabli koje deklariramo jednak broju elemenata u listi inace greska
# ? ValueError: too many values to unpack (expected 2)
# Metod se zove unpacking of lists
numbers = [0, 1, 2]
first, second, third = numbers
print(first, second, third)

# obrnuto, ako imamo vise elemenata u listi od varijabli tada ostatak sa *
numbers2 = [0, 1, 2, 3, 4, 5, ]
first, second, *others = numbers2
print(first, second, *others)  # 0 1 2 3 4 5
print(first)  # 0
print(second)  # 1
print(*others)  # 2 3 4 5

# jos jedna varijacija
numbers3 = [0, 1, 2, 3, 4, 5, ]
first, *others, last = numbers3
print(first, *others, last)  # 0 1 2 3 4 5
print(first)  # 0
print(*others)  # 1 2 3 4
print(last)  # 5
