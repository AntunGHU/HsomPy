# 4'35

numbers = [7, 3, 8, 2, 4, 3, 5]
numbers.sort()
print(numbers)  # [2, 3, 3, 4, 5, 7, 8]

numbers = [7, 3, 8, 2, 4, 3, 5]
numbers.sort(reverse=True)
print(numbers)  # [8, 7, 5, 4, 3, 3, 2]

# dok "sort()" modificira orginal, "sorted()" ne i moze sortirati bilo koji iterable
numbers = [7, 3, 8, 2, 4, 3, 5]
a = sorted(numbers)
print(a)        # [2, 3, 3, 4, 5, 7, 8]
print(numbers)  # [7, 3, 8, 2, 4, 3, 5]

# reversanje radi i ovdje
numbers = [7, 3, 8, 2, 4, 3, 5]
a = sorted(numbers, reverse=True)
print(a)        # [8, 7, 5, 4, 3, 3, 2]
print(numbers)  # [7, 3, 8, 2, 4, 3, 5]

# sortiranje malo kompleksnijih lista - lista tuplova
items = [
    ("pr1", 10),
    ("pr2", 9),
    ("pr3", 8)
]
# obicni pokusaj sorta nece uspjeti!
items.sort()
print(items)        # [('pr1', 10), ('pr2', 9), ('pr3', 8)] jer py ne zna!
# u ovakvim slucajevima defamo funkcije za sortanje!


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)        # [('pr3', 8), ('pr2', 9), ('pr1', 10)]


# moja provjera direktnog upisa key-a - neuspjesno!
items = [
    ("pr1", 10),
    ("pr2", 9),
    ("pr3", 8)
]
items.sort(key=items[1])    # TypeError: 'tuple' object is not callable
